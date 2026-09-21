#!/usr/bin/env python3
"""Phase 3d: add CC-BY-SA 4.0 hero image attribution to footer of all 6 pages.

Inserts a new <div class="row"> after the existing footer row closes,
before the container div closes. Indentation is detected from the
existing footer row opening tag.

Attribution required by CC BY-SA 4.0:
  Hero image: Ha'penny Bridge, Dublin by Chris Light, CC BY-SA 4.0,
  via Wikimedia Commons
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ["index.html", "cfp.html", "committee.html", "program.html", "papers.html", "keynote.html"]

ANCHOR = "A venue for discussing problems of"

ATTRIBUTION_TEMPLATE = (
    '{indent}<div class="row">\r\n'
    '{indent}\t<div class="col-lg-12">\r\n'
    '{indent}\t\t<p style="margin: 0; padding: 0 0 15px 0; font-size: 12px; '
    'color: rgba(255,255,255,0.7); text-align: center;">\r\n'
    '{indent}\t\t\tHero image: '
    '<a href="https://commons.wikimedia.org/wiki/File:Ha%27penny_bridge_00209.jpg" '
    'style="color: rgba(255,255,255,0.85); text-decoration: underline;">'
    "Ha'penny Bridge, Dublin</a> by Chris Light, "
    '<a href="https://creativecommons.org/licenses/by-sa/4.0" '
    'style="color: rgba(255,255,255,0.85); text-decoration: underline;">'
    'CC BY-SA 4.0</a>, via Wikimedia Commons\r\n'
    '{indent}\t\t</p>\r\n'
    '{indent}\t</div>\r\n'
    '{indent}</div>\r\n'
)


def process(path: Path) -> str:
    with open(path, "r", encoding="utf-8", newline="") as f:
        text = f.read()

    if "Chris Light" in text:
        return "already has attribution, skipped"

    anchor_idx = text.find(ANCHOR)
    if anchor_idx == -1:
        return "ANCHOR NOT FOUND"

    # Find the 3rd </div> after the anchor (closes: styled-div, col-lg-6, row)
    pos = anchor_idx
    for i in range(3):
        nxt = text.find("</div>", pos)
        if nxt == -1:
            return f"only found {i} </div> after anchor"
        pos = nxt + len("</div>")

    # pos is now right after the 3rd </div> (row close).
    # Detect indentation: look back for the line that opened this row.
    # Find the last '<div class="row">' or '<div class=" row">' before anchor.
    row_open_match = None
    for m in re.finditer(r'^([ \t]*)<div class=" ?row">', text[:anchor_idx], re.MULTILINE):
        row_open_match = m
    indent = row_open_match.group(1) if row_open_match else "\t\t\t"

    # Consume trailing whitespace/newline after the 3rd </div> so we insert cleanly
    while pos < len(text) and text[pos] in " \t":
        pos += 1
    if pos < len(text) and text[pos:pos+2] == "\r\n":
        insert_at = pos + 2
    elif pos < len(text) and text[pos] == "\n":
        insert_at = pos + 1
    else:
        insert_at = pos

    attribution = ATTRIBUTION_TEMPLATE.format(indent=indent)
    new_text = text[:insert_at] + attribution + text[insert_at:]

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(new_text)
    return f"inserted attribution (indent={repr(indent)})"


def main():
    for name in FILES:
        path = ROOT / name
        if not path.exists():
            print(f"{name}: MISSING")
            continue
        result = process(path)
        print(f"{name}: {result}")


if __name__ == "__main__":
    main()
