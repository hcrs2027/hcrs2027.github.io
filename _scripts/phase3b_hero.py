#!/usr/bin/env python3
"""Phase 3b: create hero image.

Wikimedia Commons is unreachable from this machine (all *.wikimedia.org
domains time out), so the user-chosen "Wikimedia CC Dublin photo" cannot
be fetched right now.

Fallback strategy:
1. Generate a branded gradient placeholder (2026 site colors #2d4a6b ->
   #C6743B) at img/hero-dublin.jpg so the site renders correctly.
2. Save the downloaded WWW 2027 official banner as
   img/hero-candidate-www2027-banner.jpg for user review. The handoff
   section 6.3 lists this banner as a possible source, but the user
   chose Wikimedia CC instead, so it is NOT wired up automatically.
3. Document both in IMAGE_SOURCES.md.

When the user confirms a final hero image (Wikimedia CC Dublin photo,
the official banner, or something else), replace img/hero-dublin.jpg
with the chosen file at 1920x600 JPEG quality ~82.
"""
from PIL import Image, ImageDraw
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "img"
TMP = Path(r"C:\Users\fetter\AppData\Local\Temp\hcrs_photos")

W, H = 1920, 600
# Brand colors from 2026 site
C_TOP = (45, 74, 107)      # #2d4a6b deep blue
C_BOT = (198, 116, 59)     # #C6743B orange


def make_gradient() -> Image.Image:
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)
    for y in range(H):
        t = y / (H - 1)
        r = int(C_TOP[0] + (C_BOT[0] - C_TOP[0]) * t)
        g = int(C_TOP[1] + (C_BOT[1] - C_TOP[1]) * t)
        b = int(C_TOP[2] + (C_BOT[2] - C_TOP[2]) * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b))
    return img


def main():
    IMG.mkdir(exist_ok=True)

    # 1. Gradient placeholder -> img/hero-dublin.jpg
    grad = make_gradient()
    out = IMG / "hero-dublin.jpg"
    grad.save(out, "JPEG", quality=82, optimize=True, progressive=True)
    print(f"placeholder: {out} {grad.size} {out.stat().st_size/1024:.1f} KB")

    # 2. Copy downloaded WWW 2027 banner as candidate (not wired up)
    src_banner = TMP / "www2027_banner.jpg"
    if src_banner.exists():
        dst_banner = IMG / "hero-candidate-www2027-banner.jpg"
        # Resize to 1920 wide for consistency, keep aspect
        bimg = Image.open(src_banner)
        ratio = W / bimg.width
        new_h = int(bimg.height * ratio)
        bimg = bimg.resize((W, new_h), Image.LANCZOS)
        bimg.save(dst_banner, "JPEG", quality=85, optimize=True, progressive=True)
        print(f"candidate:   {dst_banner} {bimg.size} {dst_banner.stat().st_size/1024:.1f} KB")
    else:
        print("candidate:   WWW 2027 banner not found in temp dir")


if __name__ == "__main__":
    main()
