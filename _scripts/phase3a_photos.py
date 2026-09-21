#!/usr/bin/env python3
"""Phase 3a: process 3 organizer photos to 200x200 JPEG for the website.

Sources (fetched 2026-09-21):
- Weixin Chen:  https://weixinchen.com/public/personal/weixin_jp_cropped.jpg
- Yuanhao Liu:  https://unitdan.github.io/images/android-chrome-512x512.png
- Tun Lu:       https://datascience.fudan.edu.cn/_upload/article/images/48/30/b5df446d46a189173b8edee01e79/693bda2b-c10b-4f2d-bdd8-f4b156d1129a.png
"""
from PIL import Image
from pathlib import Path
import sys

SRC = Path(r"C:\Users\fetter\AppData\Local\Temp\hcrs_photos")
DST = Path(__file__).resolve().parent.parent
TARGET = 200
QUALITY = 88
MAX_BYTES = 200 * 1024

JOBS = [
    ("weixinchen.jpg",  "weixinchen.jpg"),
    ("yuanhaoliu.png",  "yuanhaoliu.jpg"),
    ("tunlu_ds.png",    "tunlu.jpg"),
]


def center_crop_square(img: Image.Image) -> Image.Image:
    w, h = img.size
    s = min(w, h)
    left = (w - s) // 2
    top = (h - s) // 2
    return img.crop((left, top, left + s, top + s))


def process(src_name: str, dst_name: str) -> None:
    src = SRC / src_name
    dst = DST / dst_name
    if not src.exists():
        print(f"MISSING source: {src}")
        return

    img = Image.open(src)
    # Flatten alpha to white background (PNG with transparency)
    if img.mode in ("RGBA", "LA", "P"):
        bg = Image.new("RGB", img.size, (255, 255, 255))
        if img.mode == "P":
            img = img.convert("RGBA")
        bg.paste(img, mask=img.split()[-1] if img.mode in ("RGBA", "LA") else None)
        img = bg
    elif img.mode != "RGB":
        img = img.convert("RGB")

    img = center_crop_square(img)
    img = img.resize((TARGET, TARGET), Image.LANCZOS)

    # Try quality levels until under MAX_BYTES
    for q in (QUALITY, 82, 75, 68, 60):
        img.save(dst, "JPEG", quality=q, optimize=True, progressive=True)
        size = dst.stat().st_size
        if size <= MAX_BYTES:
            print(f"{dst_name}: {TARGET}x{TARGET} JPEG q={q} {size/1024:.1f} KB  (from {src_name} {Image.open(src).size})")
            return
    print(f"{dst_name}: WARNING still {size/1024:.1f} KB at q=60")


def main():
    for src_name, dst_name in JOBS:
        process(src_name, dst_name)


if __name__ == "__main__":
    main()
