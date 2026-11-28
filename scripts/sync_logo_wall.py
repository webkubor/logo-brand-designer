#!/usr/bin/env python3
"""Refresh the README and website logo walls from free-imgbed's published manifests."""
import argparse
from html import escape
import json
from pathlib import Path
import subprocess
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- logo-wall:start -->"
END = "<!-- logo-wall:end -->"
FEATURED = ("nativecrew", "xianling-music", "chat-mood-gen", "wallpaper-generator")


def git(checkout, *args):
    return subprocess.check_output(["git", "-C", str(checkout), *args], text=True).strip()


def load_marks(checkout):
    revision = git(checkout, "rev-parse", "origin/main")
    files = set(git(checkout, "ls-tree", "-r", "--name-only", revision).splitlines())
    records = [
        json.loads(git(checkout, "show", f"{revision}:{name}"))
        for name in sorted(files)
        if name.startswith("brand/") and name.endswith(".json")
    ]
    records.sort(key=lambda row: FEATURED.index(row["id"]) if row["id"] in FEATURED else len(FEATURED))
    marks = {}
    for record in records:
        if record["status"] != "ready":
            continue
        asset = record["asset"]
        if asset not in files:
            raise ValueError(f"Missing published logo: {asset}")
        marks.setdefault(asset, record)
    if not marks:
        raise ValueError("No ready logos found")
    return list(marks.values()), revision


def tile(mark, revision, website):
    name = escape(mark["name"], quote=True)
    url = "https://github.com/" + quote(mark["sourceRepo"])
    base = f"https://cdn.jsdelivr.net/gh/webkubor/free-imgbed@{revision}/"
    asset = base + quote(mark["asset"])
    if website:
        tone = " logo-tile--dark" if mark["id"] == "wallpaper-generator" else ""
        return (
            f'    <a class="logo-tile{tone}" href="{url}" title="{name}" data-case="{name}">'
            f'<img src="{asset}" width="120" height="120" loading="lazy" alt="{name}"></a>'
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
