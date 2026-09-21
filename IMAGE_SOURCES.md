# Image Sources & License Notes

All images fetched on **2026-09-21** for the HCRS@WWW 2027 workshop website.

## Organizer Photos (200×200 JPEG, circular crop via CSS)

| File | Person | Source URL | License / Notes |
|---|---|---|---|
| `tjk.png` | Jiakai Tang | Reused from 2026 site (`HCRec/HCRec.github.io`) | Original organizer photo; no change |
| `weixinchen.jpg` | Weixin Chen | https://weixinchen.com/public/personal/weixin_jp_cropped.jpg | Personal homepage of the organizer (Applied Scientist at Kuaishou). Cropped center-square, resized 200×200. |
| `yuanhaoliu.jpg` | Yuanhao Liu | https://unitdan.github.io/images/android-chrome-512x512.png | Personal homepage avatar (`class="author__avatar" alt="Yuanhao Liu"`). Resized 200×200. |
| `cq2.png` | Qi Cao | Reused from 2026 site | Original organizer photo; no change |
| `lsc.jpg` | Shuchang Liu | Reused from 2026 site | Original organizer photo; no change |
| `tunlu.jpg` | Tun Lu | https://datascience.fudan.edu.cn/_upload/article/images/48/30/b5df446d46a189173b8edee01e79/693bda2b-c10b-4f2d-bdd8-f4b156d1129a.png | Fudan University School of Data Science faculty page. Original 162×162 PNG, upscaled to 200×200 (1.23×, minor softness acceptable). |
| `renzhaochun.png` | Zhaochun Ren | Reused from 2026 site | Original organizer photo (was 2026 keynote); no change |
| `chenli.jpeg` | Li Chen | Reused from 2026 site | Original organizer photo (was 2026 keynote); no change |
| `ofey.jpg` | Fei Sun | Compressed from 2026 site's `ofey.png` (3.0 MB → 24.7 KB) | Original 1800×2520 PNG center-cropped to square, resized 400×400, JPEG q=88. |

> **Note**: Photos from personal/institutional homepages are used under the
> standard academic convention that organizers' publicly posted portraits may
> appear on the workshop site they organize. If any organizer requests removal
> or replacement, swap the file at the same path.

## Hero Image

| File | Status | Notes |
|---|---|---|
| `img/hero-dublin.jpg` | **Temporary placeholder** | Programmatically generated gradient using workshop brand colors (`#2d4a6b` → `#C6743B`), 1920×600 JPEG. Created because Wikimedia Commons was unreachable from the build machine (all `*.wikimedia.org` domains timed out). |
| `img/hero-candidate-www2027-banner.jpg` | **Candidate, not wired up** | Downloaded from https://www2027.thewebconf.org/wp-content/uploads/2026/09/WebBanner-1-scaled.jpg (official WWW 2027 conference banner, 2560×640 → resized 1920×480). Handoff §6.3 lists this as a possible source but notes copyright belongs to the conference; **confirm usage rights with WWW 2027 web chair before wiring up**. |

### TODO: Final hero image

The user chose "Wikimedia CC Dublin photo" as the hero source. When network
access to Wikimedia Commons is restored:

1. Search Commons for a CC-BY-SA or CC0 Dublin landmark photo (candidates:
   Ha'penny Bridge, Trinity College Campanile, Custom House, Dublin skyline
   from Liffey, Spire of Dublin).
2. Download at ≥1920px wide.
3. Crop/resize to 1920×600, save as `img/hero-dublin.jpg` (JPEG q≈82, ≤500 KB).
4. Add attribution line to footer or this file per CC-BY-SA requirements.
5. Delete `img/hero-candidate-www2027-banner.jpg` if not used.

Alternatively, if the WWW 2027 web chair confirms the official banner may be
used, rename `img/hero-candidate-www2027-banner.jpg` → `img/hero-dublin.jpg`
and adjust the hero container aspect ratio if needed (banner is 4:1, current
placeholder is 3.2:1).

## Other Assets

| Path | Source | Notes |
|---|---|---|
| `img/avatar.png` | Reused from 2026 site | Fallback for broken organizer photos (`onerror`) |
| `img/bg_direction_nav.png` | Reused from 2026 site | Referenced by `css/flexslider.css` |
| `css/` `js/` `fonts/` | Reused from 2026 site | Full template stack; `css/jcarousel.css` reference removed (file never existed in 2026 repo either) |
