#!/usr/bin/env python3
"""Make index.html committee section mirror committee.html exactly.

Per user: index page must be consistent with committee page -- no
"See the Committee page" link approach. So index.html gets the full
Organizing Committee (9) + Student Committee (Weilun Chen) +
Program Committee name bar, same as committee.html.

Changes:
1. intro: "team of ten researchers" -> "nine"; "Five of the ten" -> "nine"
2. intro: remove "See the Committee page for the full list..." sentence
3. remove Weilun Chen Row 4 from Organizing Committee (back to 9)
4. insert Student Committee section + Program Committee bar after
   Organizing Committee content-section close

index.html uses LF line endings (normalized by prior edits).
Committee section sits one tab deeper than committee.html:
content-section at 6 tabs, rows at 7, cards at 8/9/10/11.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
p = ROOT / "index.html"
with open(p, "r", encoding="utf-8", newline="") as f:
    idx = f.read()

T = "\t"
NL = "\n"

# --- 1. intro count fixes ---
before = idx
idx = idx.replace("team of ten researchers", "team of nine researchers")
idx = idx.replace("Five of the ten organizers", "Five of the nine organizers")
print("intro ten->nine:", "changed" if idx != before else "NO CHANGE")

# --- 2. remove "See the Committee page" sentence (whitespace-flexible) ---
pat = re.compile(
    r'in vision and logistics\.\s*See the\s*'
    r'<a href="committee\.html"[^>]*>Committee</a>\s*'
    r'page for the full list with photos and affiliations\.'
)
idx2, n = pat.subn('in vision and logistics.', idx)
print("remove 'See the Committee page' sentence:", n, "replacement(s)")
idx = idx2

# --- 3+4. Row 4 removal + Student Committee + PC bar insertion ---
PC = ("Tarun Raheja, Jingyuan Huang, Xiaonan Song, Yunfan Wu, Aarush Sinha, "
      "Baruch Epstein, Erica Coppolillo, Rajarshee Dhar, Bodhisatta Maiti, "
      "Jiacheng Lin, Yasuhiro Yoshida, Huizhong Guo, Xiao Lin, Xue Li, "
      "Manoj Yadav, Sushant Mehta, Mingming Li")

old = (
    f'{T*7}</div>{NL}'
    f'{NL}'
    f'{T*7}<!-- Row 4: 1 member (centered) -->{NL}'
    f'{T*7}<div class="row">{NL}'
    f'{T*8}<div class="col-md-4 col-md-offset-4">{NL}'
    f'{T*9}<div class="committee-member">{NL}'
    f'{T*10}<a href="https://ch3nweilun.github.io/" target="_blank">{NL}'
    f'{T*11}<img src="weilunchen.jpg" alt="Weilun Chen" class="committee-photo" onerror="this.src=\'img/avatar.png\'">{NL}'
    f'{T*11}<div class="committee-name">Weilun Chen</div>{NL}'
    f'{T*11}<div class="committee-affiliation">Institute of Computing Technology, CAS, China</div>{NL}'
    f'{T*10}</a>{NL}'
    f'{T*9}</div>{NL}'
    f'{T*8}</div>{NL}'
    f'{T*7}</div>{NL}'
    f'{T*6}</div>{NL}'
)

new = (
    f'{T*7}</div>{NL}'
    f'{T*6}</div>{NL}'
    f'{NL}'
    f'{T*6}<!-- Student Committee -->{NL}'
    f'{T*6}<div class="content-section content-section--wide" style="margin-bottom: 40px;">{NL}'
    f'{T*7}<h2 style="color: #2d4a6b; font-weight: 700; margin-bottom: 20px;">Student Committee</h2>{NL}'
    f'{NL}'
    f'{T*7}<div class="row">{NL}'
    f'{T*8}<div class="col-md-4 col-md-offset-4">{NL}'
    f'{T*9}<div class="committee-member">{NL}'
    f'{T*10}<a href="https://ch3nweilun.github.io/" target="_blank">{NL}'
    f'{T*11}<img src="weilunchen.jpg" alt="Weilun Chen" class="committee-photo" onerror="this.src=\'img/avatar.png\'">{NL}'
    f'{T*11}<div class="committee-name">Weilun Chen</div>{NL}'
    f'{T*11}<div class="committee-affiliation">Institute of Computing Technology, CAS, China</div>{NL}'
    f'{T*10}</a>{NL}'
    f'{T*9}</div>{NL}'
    f'{T*8}</div>{NL}'
    f'{T*7}</div>{NL}'
    f'{T*6}</div>{NL}'
    f'{NL}'
    f'{T*6}<!-- Program Committee (name list only; affiliations not yet collected) -->{NL}'
    f'{T*6}<div class="content-section" style="margin-bottom: 30px; padding: 18px 22px; background: #fafbfc; border-left: 4px solid #2d4a6b; border-radius: 4px;">{NL}'
    f'{T*7}<strong style="color: #2d4a6b; font-size: 16px;">Program Committee:</strong>{NL}'
    f'{T*7}<span style="color: #555; line-height: 1.9;">{PC}</span>{NL}'
    f'{T*6}</div>{NL}'
)

cnt = idx.count(old)
print("Row4 block occurrences:", cnt)
if cnt != 1:
    print("ERROR: expected exactly 1 occurrence, aborting without write")
    # Debug: show what's around Row 4
    i = idx.find("Row 4: 1 member")
    print(repr(idx[i-40:i+500]))
    raise SystemExit(1)

idx = idx.replace(old, new)
with open(p, "w", encoding="utf-8", newline="") as f:
    f.write(idx)
print("index.html written OK")
