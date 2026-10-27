"""Exercise the public CLI with real temporary manifests and assets."""

import base64
import hashlib
import html
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
SCRIPT = PROJECT / "scripts" / "build_review.py"


def svg(body='<circle cx="128" cy="128" r="80" fill="#0F766E"/>'):
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" '
            'role="img" aria-labelledby="name"><title id="name">测试标识</title>'
            + body + '</svg>')


class ReviewCliTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix=".test-", dir=PROJECT)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.delivery = self.root / "delivery"
        self.delivery.mkdir()
        self.asset = self.delivery / "mark.svg"
        self.asset.write_text(svg(), encoding="utf-8")
        self.manifest = self.delivery / "manifest.json"
        self.output = self.delivery / "review.html"
        self.project = {
            "id": "demo",
            "name": "测试品牌",
            "tokens": {
                "primary": "#0F766E", "accent": "#F59E0B",
                "onLight": "#0F766E", "onDark": "#FFFDF7",
                "background": "transparent",
            },
            "asset": "mark.svg",
        }

    def generate(self, output=None):
        self.manifest.write_text(json.dumps({"projects": [self.project]}), encoding="utf-8")
        # The working directory differs from both the skill and manifest directories.
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--manifest", str(self.manifest),
             "--out", str(output or self.output)],
            cwd=self.root, capture_output=True, text=True, encoding="utf-8", timeout=20,
        )

    def bundle(self):
        page = self.output.read_text(encoding="utf-8")
        script = re.search(r"<script>(.*?)</script>", page, re.S).group(1)
        data = json.JSONDecoder().raw_decode(script.split("const DATA = ", 1)[1])[0]
        return page, script, data

    def test_first_design_without_old_or_dark_assets(self):
        self.project.update({
            "rationale": ["本次建议：以圆形表达聚合。"],
            "userDecisions": ["保留品牌绿"],
            "recommendations": ["评估更大的留白"],
        })
        for explicit_null in (False, True):
            with self.subTest(explicit_null=explicit_null):
                if explicit_null:
                    self.project.update(oldAsset=None, darkAsset=None)
                result = self.generate()
                self.assertEqual(result.returncode, 0, result.stderr)
                page, _, data = self.bundle()
                record = data["projects"][0]
                asset = record["assets"]["asset"]
                self.assertIsNone(record["assets"]["oldAsset"])
                self.assertIsNone(record["assets"]["darkAsset"])
                self.assertEqual(asset["svg"], self.asset.read_text(encoding="utf-8"))
                self.assertEqual(base64.b64decode(asset["dataUri"].split(",", 1)[1]),
                                 self.asset.read_bytes())
                self.assertEqual(asset["sha256"], hashlib.sha256(self.asset.read_bytes()).hexdigest())
                self.assertEqual(record["userDecisions"], ["保留品牌绿"])
                self.assertEqual(record["recommendations"], ["评估更大的留白"])
                self.assertIn("未核验", record["tokenSources"]["primary"])
                self.assertIn("未解码/渲染像素", data["limitation"])
                self.assertIn("首次设计 / 未提供旧图", page)

    def test_distinct_dark_and_old_assets_with_local_sources(self):
        dark = svg('<path fill="#FFFDF7" d="M48 48h160v160H48z"/>')
        old = svg('<circle cx="128" cy="128" r="64" fill="#334155"/>')
        (self.delivery / "dark.svg").write_text(dark, encoding="utf-8")
        (self.delivery / "old.svg").write_text(old, encoding="utf-8")
        (self.delivery / "theme.css").write_text(":root {--brand: #0F766E}", encoding="utf-8")
        self.project.update({
            "darkAsset": "dark.svg", "oldAsset": "old.svg",
            "sourceFiles": [{"path": "theme.css", "label": "生产主题"}],
            "sources": ["https://example.org/brand"],
            "tokenSources": {"primary": "项目既有：theme.css:1"},
        })
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stderr)
        _, _, data = self.bundle()
        record = data["projects"][0]
        self.assertEqual(record["assets"]["darkAsset"]["svg"], dark)
        self.assertEqual(record["assets"]["oldAsset"]["svg"], old)
        self.assertNotEqual(record["assets"]["asset"]["dataUri"], record["assets"]["darkAsset"]["dataUri"])
        self.assertEqual(record["sources"][0]["value"], "theme.css")
        self.assertIsNone(record["sources"][0]["url"])
        self.assertEqual(record["sources"][1]["url"], "https://example.org/brand")
        self.assertEqual(record["tokenSources"]["primary"], "项目既有：theme.css:1")

    def test_safe_gradient_and_internal_use(self):
        self.asset.write_text(svg(
            '<defs><linearGradient id="ink"><stop offset="0" stop-color="#0F766E"/>'
            '<stop offset="1" stop-color="#F59E0B"/></linearGradient>'
            '<path id="mark" d="M48 48h160v160H48z" fill="url(#ink)"/></defs>'
            '<use href="#mark"/>'), encoding="utf-8")
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(self.output.is_file())

    def test_script_breakout_is_escaped_and_csp_matches(self):
        attack = '</script><script>alert("injected")</script>'
        self.project["name"] = attack
        result = self.generate()
        self.assertEqual(result.returncode, 0, result.stderr)
        page, script, data = self.bundle()
        self.assertEqual(data["projects"][0]["name"], attack)
        self.assertNotIn(attack, page)
        self.assertEqual(page.count("<script>"), 1)
        digest = base64.b64encode(hashlib.sha256(script.encode("utf-8")).digest()).decode("ascii")
        self.assertIn("script-src 'sha256-" + digest + "'", html.unescape(page))

    def test_dangerous_svg_rejected_without_replacing_output(self):
        cases = {
            "script": svg('<script>alert(1)</script>'),
            "event": svg('<path d="M0 0h10v10z" onload="alert(1)"/>'),
            "external-use": svg('<use href="https://example.org/mark.svg#x"/>'),
            "external-paint": svg('<path d="M0 0h10v10z" fill="url(https://example.org/x)"/>'),
            "bitmap": svg('<image href="data:image/png;base64,AA=="/>'),
            "foreign-object": svg('<foreignObject/>'),
            "style": svg('<path style="fill:red" d="M0 0h10v10z"/>'),
            "entity": '<!DOCTYPE svg [<!ENTITY x "bad">]>' + svg(),
            "missing-reference": svg('<use href="#missing"/>'),
            "recursive-use": svg('<g id="loop"><use href="#loop"/></g>'),
        }
        for name, content in cases.items():
            with self.subTest(name=name):
                self.asset.write_text(content, encoding="utf-8")
                self.output.write_text("previous review", encoding="utf-8")
                result = self.generate()
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertIn("ERROR:", result.stderr)
                self.assertEqual(self.output.read_text(encoding="utf-8"), "previous review")

    def test_svg_geometry_and_accessibility_contract(self):
        valid = svg()
        for content in (
            valid.replace('viewBox="0 0 256 256"', 'viewBox="0 0 256 128"'),
            valid.replace('<title id="name">测试标识</title>', ''),
            valid.replace('role="img"', ''),
            valid.replace('aria-labelledby="name"', 'aria-labelledby="missing"'),
        ):
            with self.subTest(svg=content):
                self.asset.write_text(content, encoding="utf-8")
                result = self.generate()
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertFalse(self.output.exists())

    def test_local_paths_cannot_escape_manifest_directory(self):
        outside = self.root / "outside.svg"
        outside.write_text(svg(), encoding="utf-8")
        (self.delivery / "linked.svg").symlink_to(outside)
        unsafe = ("../outside.svg", str(outside), r"C:\outside.svg",
                  "https://example.org/outside.svg", "linked.svg")
        for field in ("asset", "darkAsset", "oldAsset", "sourceFiles", "sources"):
            for value in unsafe:
                with self.subTest(field=field, value=value):
                    original = self.project.copy()
                    self.project[field] = [value] if field in ("sourceFiles", "sources") else value
                    # HTTP(S) is allowed for source citations, never for assets.
                    if field in ("sourceFiles", "sources") and value.startswith("https:"):
                        self.project = original
                        continue
                    result = self.generate()
                    self.project = original
                    self.assertEqual(result.returncode, 1, result.stderr)
                    self.assertFalse(self.output.exists())
        self.assertEqual(outside.read_text(encoding="utf-8"), svg())

    def test_output_cannot_overwrite_source_or_follow_symlink(self):
        source = self.delivery / "source.html"
        source.write_text("production source", encoding="utf-8")
        self.project["sources"] = ["source.html"]
        result = self.generate(output=source)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertEqual(source.read_text(encoding="utf-8"), "production source")
        self.output.symlink_to(source)
        result = self.generate()
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertTrue(self.output.is_symlink())
        self.assertEqual(source.read_text(encoding="utf-8"), "production source")


if __name__ == "__main__":
    unittest.main()
