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
| `weilunchen.jpg` | Weilun Chen | https://ch3nweilun.github.io/profile.jpg | Personal homepage of the organizer (M.S. student, ICT CAS). Original 295×413 portrait, cropped square with slight upward bias (face-centered), resized 200×200, JPEG q=88 (7.7 KB). Added 2026-09-22 per user request — **note: deviates from handoff §2 item 9 / §3.3 item 3, which said 2027 has no Student Organizers category; user opted to add Weilun Chen directly to Organizing Committee instead of creating a separate section.** |

**Update 2026-09-22**: Weilun Chen was removed from the Organizing Committee sections of `index.html` / `committee.html` at the user's request; the site now credits him in the page footers ("Website by Weilun Chen") instead. `weilunchen.jpg` was deleted from the repo on 2026-09-23 (unreferenced; still retrievable from git history if ever needed).

> **Note**: Photos from personal/institutional homepages are used under the
> standard academic convention that organizers' publicly posted portraits may
> appear on the workshop site they organize. If any organizer requests removal
> or replacement, swap the file at the same path.

## Hero Image

| File | Status | Notes |
|---|---|---|
| `img/hero-beckett-bridge.jpg` | **Final** | Samuel Beckett Bridge, Dublin. Original: `Samuel_Beckett_Bridge_20160818.jpg` (1920×1280, 362.7 KB) provided by user from Wikimedia Commons on 2026-09-23. Processed: vertical crop to 1920×600 (3.2:1, 40% position bias), JPEG q=88 progressive (163.7 KB). Replaces `hero-dublin.jpg` per user request. |

### License & Attribution

- **Author**: Suicasmo
- **License**: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0)
- **Source**: via Wikimedia Commons — file page: https://commons.wikimedia.org/wiki/File:Samuel_Beckett_Bridge_20160818.jpg
- **Attribution placement**: footer of all 6 HTML pages (small centered text with links to file page and license)
- **CC BY-SA obligations met**: ✅ author credited, ✅ license named + linked, ✅ source indicated. Share-alike applies to adaptations — the crop/resize is a trivial mechanical transformation, not a creative derivative, so SA does not impose additional licensing on the website itself. If this interpretation is ever questioned, the safest fallback is to also license the hero crop under CC BY-SA 4.0 (does not affect the rest of the site).

> ⚠️ **Verify file page URL**: constructed from the filename pattern the user provided
> (`Samuel_Beckett_Bridge_20160818.jpg`). Confirm it resolves to the exact image
> used before the site goes public.

### Removed candidates

- `img/hero-dublin.jpg` — replaced by `img/hero-beckett-bridge.jpg` on 2026-09-23 (user requested the Samuel Beckett Bridge photo); old file deleted from the repo.
- `img/hero-candidate-www2027-banner.jpg` — deleted (user provided a properly
  licensed Wikimedia image instead; no need to pursue conference banner rights).

## Other Assets

| Path | Source | Notes |
|---|---|---|
| `img/avatar.png` | Reused from 2026 site | Fallback for broken organizer photos (`onerror`) |
| `img/bg_direction_nav.png` | Reused from 2026 site | Referenced by `css/flexslider.css` |
| `css/` `js/` `fonts/` | Reused from 2026 site | Full template stack; `css/jcarousel.css` reference removed (file never existed in 2026 repo either) |
