"""核验候选变更与跨阶段选择是否保留正确的审核证据。"""

import json
import base64
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from review_workbench import Review


class WorkbenchTests(unittest.TestCase):
    def setUp(self):
        scratch = tempfile.TemporaryDirectory()
        self.addCleanup(scratch.cleanup)
        self.root = Path(scratch.name)
        self.storage = self.root / "review.json"
        self.shape = self.manifest("shape", ["01", "02"])
        self.color = self.manifest("color", ["mauve"])
        self.review = Review(self.storage, self.shape, self.color, "测试")

    def manifest(self, stage, ids):
        candidates = []
        for ident in ids:
            image = self.root / f"{stage}-{ident}.svg"
            image.write_text(
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" role="img" aria-label="Mark">'
                '<title>Mark</title><path d="M2 8 H28 V24 H2 Z" fill="#111111"/></svg>'
            )
            candidates.append({
                "id": ident, "name": ident, "asset": image.name,
                "tokens": dict(primary="#111", accent="#333", onLight="#111", onDark="#fff", background="transparent"),
            })
        manifest = self.root / f"{stage}.json"
        manifest.write_text(json.dumps({"projects": candidates}))
        return manifest

    def choose(self, stage, ident, revision=None):
        options, _ = self.review.candidates()
        selected = next(item for item in options["color" if stage == "final" else stage] if item["id"] == ident)
        self.review.record({
            "stage": stage, "candidate": ident, "sha": selected["sha"],
            "revision": self.review.state["revision"] if revision is None else revision,
        }, True)

    def test_order_and_reselect(self):
        with self.assertRaisesRegex(ValueError, "先确认"):
            self.choose("color", "mauve")
        self.choose("shape", "01")
        self.choose("color", "mauve")
        self.choose("final", "mauve")
        restarted = Review(self.storage, self.shape, self.color, "测试")
        self.assertEqual(restarted.state["decisions"]["final"]["id"], "mauve")
        self.choose("shape", "02")
        self.assertEqual(list(self.review.state["decisions"]), ["shape"])

    def test_changed_revision_or_source_rejects_finalization(self):
        self.choose("shape", "01")
        self.choose("color", "mauve")
        with self.assertRaisesRegex(ValueError, "进度已变化"):
            self.choose("final", "mauve", 1)
        source = self.root / "color-mauve.svg"
        source.write_text(source.read_text().replace("#111111", "#4422aa"))
        with self.assertRaisesRegex(ValueError, "候选素材已更新"):
            self.choose("final", "mauve")
        self.assertNotIn("final", self.review.state["decisions"])

    def test_raster_candidate_can_be_reviewed_but_requires_svg_for_delivery(self):
        pixel = base64.b64decode(
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADElEQVR4nGNg+M/wHwAEAQH/4YN+3QAAAABJRU5ErkJggg=="
        )
        (self.root / "raster.png").write_bytes(pixel)
        manifest = json.loads(self.color.read_text())
        manifest["projects"][0]["asset"] = "raster.png"
        self.color.write_text(json.dumps(manifest))
        self.choose("shape", "01")
        self.choose("color", "mauve")
        with self.assertRaisesRegex(ValueError, "SVG"):
            self.choose("final", "mauve")


if __name__ == "__main__":
    unittest.main()
