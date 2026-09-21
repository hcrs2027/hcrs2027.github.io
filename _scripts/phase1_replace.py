#!/usr/bin/env python3
"""Phase 1: batch replacements per HCRS_2027_website_handoff.md section 1.

Runs on all 6 HTML files. Preserves UTF-8 encoding and CRLF line endings.
Every replacement is idempotent-safe (running twice won't break anything).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ["index.html", "cfp.html", "committee.html", "program.html", "papers.html", "keynote.html"]

# ---------------------------------------------------------------------------
# Simple string replacements (order matters: more specific first)
# ---------------------------------------------------------------------------
REPLACEMENTS = [
    # Brand / navbar / footer / meta author
    ("HCRS@TheWebConf 2026", "HCRS@WWW 2027"),
    ("HCRS@TheWebConf 2025", "HCRS@WWW 2025"),
    ("@TheWebConf 2026", "@The Web Conference 2027"),
    # Full workshop name
    ("The 2nd Workshop on Human-Centered Recommender Systems",
     "The 3rd Workshop on Human-Centered Recommender Systems"),
    ("2nd Workshop", "3rd Workshop"),
    # Session shape
    ("half-day session", "full-day session"),
    ("half-day", "full-day"),
    # Location / modality
    ("held online", "held in person"),
    ("meeting link to be announced", ""),
    # Dates
    ("Tuesday, June 30, 2026, 10:00\u201313:30",
     "Date and time TBA (during May 3\u20137, 2027)"),
    ("June 30, 2026", "TBA (during May 3\u20137, 2027)"),
    ("January 14, 2026", "February 1, 2027"),
    ("February 2, 2026", "February 16, 2027"),
    ("January 4, 2026", "January 4, 2027"),
    # Timezone
    ("GST (UTC+4)", "IST (Irish Standard Time, UTC+1)"),
    ("(GST, UTC+4)", "(IST, UTC+1)"),
    ("Gulf Standard Time", "Irish Standard Time"),
    ("(GST)", "(IST)"),
    # Template / structure
    ("ACM WWW 2026 template", "ACM Web Conference 2027 template"),
    ("Two 30-minute keynote talks", "Four 30-minute keynote talks"),
    # OpenReview 2026 group -> TBA
    ("https://openreview.net/group?id=ACM.org/TheWebConf/2026/Workshop/HCRS",
     "#TBA-openreview-2027"),
    # Hero image
    ("https://www2026.thewebconf.org/images/Large-DubaiSkyline_BurjKhalifa_DET.jpg",
     "img/hero-dublin.jpg"),
    # Fix 2026 typo in footer container div
    ('<div class="container" ">', '<div class="container">'),
]

# ---------------------------------------------------------------------------
# Regex removals (multi-line blocks)
# ---------------------------------------------------------------------------
def remove_blocks(text: str) -> str:
    # google-site-verification (whole line with leading whitespace)
    text = re.sub(
        r'^[ \t]*<meta name="google-site-verification"[^>]*>\r?\n',
        '',
        text,
        flags=re.MULTILINE,
    )
    # html5shim IE conditional block (3-4 lines, may include comment header)
    text = re.sub(
        r'[ \t]*<!-- HTML5 shim[^>]*-->\r?\n'
        r'[ \t]*<!--\[if lt IE 9\]>\s*\r?\n'
        r'[ \t]*<script src="http://html5shim[^"]*"></script>\s*\r?\n'
        r'[ \t]*<!\[endif\]-->\r?\n',
        '',
        text,
    )
    # Fallback: bare IE conditional without the HTML5 shim comment header
    text = re.sub(
        r'[ \t]*<!--\[if lt IE 9\]>\s*\r?\n'
        r'[ \t]*<script src="http://html5shim[^"]*"></script>\s*\r?\n'
        r'[ \t]*<!\[endif\]-->\r?\n',
        '',
        text,
    )
    # jcarousel.css dead-link reference
    text = re.sub(
        r'^[ \t]*<link href="css/jcarousel\.css"[^>]*>\r?\n',
        '',
        text,
        flags=re.MULTILINE,
    )
    return text


# ---------------------------------------------------------------------------
# Additions
# ---------------------------------------------------------------------------
def add_robots_noindex(text: str) -> str:
    """Insert <meta name="robots" ...> right after the viewport meta, if absent."""
    if 'name="robots"' in text:
        return text
    return re.sub(
        r'(<meta name="viewport"[^>]*/>)',
        r'\1\r\n\t<meta name="robots" content="noindex, nofollow" />',
        text,
        count=1,
    )


def add_previous_2026_entry(text: str) -> str:
    """Insert 2nd HCRS@WWW 2026 entry above 1st HCRS@WWW 2025 in Previous dropdown."""
    if "2nd HCRS@WWW 2026" in text or "hcrec.github.io" in text:
        return text
    # Match the opening of the dropdown-menu <ul> and inject a new <li> before the 1st entry
    pattern = re.compile(
        r'(<ul class="dropdown-menu">\s*\r?\n)(\s*)(<li><a href="https://human-centeredrec\.github\.io/")',
    )
    def repl(m):
        ul_open, indent, first_li_start = m.group(1), m.group(2), m.group(3)
        new_li = (f'{indent}<li><a href="https://hcrec.github.io/" '
                  f'target="_blank">2nd HCRS@WWW 2026</a></li>\r\n')
        return f'{ul_open}{new_li}{indent}{first_li_start}'
    return pattern.sub(repl, text, count=1)


# ---------------------------------------------------------------------------
# Per-page <title> fix (each page has its own title)
# ---------------------------------------------------------------------------
TITLES = {
    "index.html":     "HCRS@WWW 2027 - The 3rd Workshop on Human-Centered Recommender Systems",
    "cfp.html":       "Call for Papers - HCRS@WWW 2027",
    "committee.html": "Committee - HCRS@WWW 2027",
    "program.html":   "Program - HCRS@WWW 2027",
    "papers.html":    "Accepted Papers - HCRS@WWW 2027",
    "keynote.html":   "Keynote - HCRS@WWW 2027",
}

def fix_title(text: str, filename: str) -> str:
    new_title = TITLES[filename]
    return re.sub(
        r'<title>[^<]*</title>',
        f'<title>{new_title}</title>',
        text,
        count=1,
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def process(path: Path) -> dict:
    with open(path, "r", encoding="utf-8", newline="") as f:
        original = f.read()
    text = original
    stats = {}

    for old, new in REPLACEMENTS:
        n = text.count(old)
        if n:
            text = text.replace(old, new)
            stats[old[:40]] = n

    before = text
    text = remove_blocks(text)
    if text != before:
        stats["remove_blocks"] = "yes"

    before = text
    text = add_robots_noindex(text)
    if text != before:
        stats["add_robots"] = "yes"

    before = text
    text = add_previous_2026_entry(text)
    if text != before:
        stats["add_prev_2026"] = "yes"

    before = text
    text = fix_title(text, path.name)
    if text != before:
        stats["fix_title"] = "yes"

    if text != original:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(text)
    return stats


def main():
    total = 0
    for name in FILES:
        path = ROOT / name
        if not path.exists():
            print(f"MISSING: {name}")
            continue
        stats = process(path)
        total += sum(v for v in stats.values() if isinstance(v, int))
        print(f"\n[{name}]")
        for k, v in stats.items():
            print(f"  {v:>4}  {k}")
    print(f"\nTotal numeric replacements: {total}")


if __name__ == "__main__":
    main()
