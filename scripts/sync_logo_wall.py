#!/usr/bin/env python3
"""Refresh the README and website logo walls from free-imgbed's published manifests."""
import argparse
from html import escape
import json
from pathlib import Path
import subprocess
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- logo-wall:start -->"
END = "<!-- logo-wall:end -->"
PROJECTS = ROOT / "references/current-logo-projects.json"


def git(checkout, *args):
    return subprocess.check_output(["git", "-C", str(checkout), *args], text=True).strip()


def load_marks(checkout):
    revision = git(checkout, "rev-parse", "origin/main")
    files = set(git(checkout, "ls-tree", "-r", "--name-only", revision).splitlines())
    projects = json.loads(PROJECTS.read_text(encoding="utf-8"))
    marks = []
    urls = set()
    for project_id, project in projects.items():
        manifest_path = f"brand/{project_id}.json"
        details = json.loads(git(checkout, "show", f"{revision}:{manifest_path}"))
        if details["status"] != "ready":
            raise ValueError(f"{project_id}: no longer marked ready in free-imgbed")
        asset = project["asset"]
        if asset not in files:
            raise ValueError(f"Missing published logo: {asset}")
        url = urlsplit(project["url"])
        if url.scheme != "https" or not url.hostname or url.username or url.password:
            raise ValueError(f"{project_id}: expected a public HTTPS project URL")
        if project["url"].rstrip("/") in urls:
            raise ValueError(f"{project_id}: duplicate project URL")
        urls.add(project["url"].rstrip("/"))
        marks.append({"id": project_id, "name": project.get("name", details["name"]),
                      "asset": asset, "url": project["url"]})
    if not marks:
        raise ValueError("No verified projects found")
    return marks, revision


def tile(mark, revision, website):
    name = escape(mark["name"], quote=True)
    url = escape(mark["url"], quote=True)
    base = f"https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@{revision}/"
    asset = base + quote(mark["asset"])
    if website:
        tone = " logo-tile--dark" if mark["id"] == "wallpaper-generator" else ""
        return (
            f'    <a class="logo-tile{tone}" href="{url}" title="{name}" data-case="{name}">'
            f'<span class="logo-tile-mark"><img src="{asset}" width="120" height="120" loading="lazy" alt=""></span>'
            f'<span class="logo-tile-name">{name}</span></a>'
        )
    image = f'<img src="{asset}" width="80" height="80" alt="{name}">'
    return f'<td align="center"><a href="{url}">{image}</a></td>'


def block(marks, revision, website):
    tiles = [tile(mark, revision, website) for mark in marks]
    if website:
        return '<div class="logo-wall">\n' + "\n".join(tiles) + "\n</div>"
    rows = ["  <tr>" + "".join(tiles[i:i + 5]) + "</tr>" for i in range(0, len(tiles), 5)]
    return "<table>\n" + "\n".join(rows) + "\n</table>"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("imgbed", type=Path, help="free-imgbed checkout with current origin/main")
    args = parser.parse_args()
    marks, revision = load_marks(args.imgbed)
    paths = ("README.md", "README.en.md", "docs/index.html", "docs/en/index.html")
    contents = {}
    for name in paths:
        path = ROOT / name
        before, middle = path.read_text(encoding="utf-8").split(START)
        _, after = middle.split(END)
        contents[path] = before + START + "\n" + block(marks, revision, name.endswith(".html")) + "\n" + END + after
    for path, content in contents.items():
        path.write_text(content, encoding="utf-8")
    print(f"{len(marks)} logos from free-imgbed {revision}")


if __name__ == "__main__":
    main()
