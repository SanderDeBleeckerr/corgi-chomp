#!/usr/bin/env python3
"""Turn the hand-drawn snacks in art/foods/ into game sprites.

For every drawing (PNG or WebP with a transparent background) this script:
  1. crops it to the visible pixels and puts it in the middle of a square
     512 x 512 canvas (4 % empty border), so turning it looks right;
  2. saves it as sprites/food_<name>.webp;
  3. measures its visible shape, the same way the game measures Hrozna:
     - area:  part of the square that is visible
     - ext:   longest side of the visible box (part of the square)
     - cx,cy: middle of the visible pixels (the snack turns around this point)
     - pts:   an 18 x 18 grid of points on the visible pixels, used for collisions
  4. writes all of it to sprites/foods.js (loaded by index.html).

Run it again after you add or change a drawing:  python3 tools/build_foods.py
"""
import json, pathlib
import numpy as np
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / 'art' / 'foods', ROOT / 'sprites'
S, PAD, G = 512, 0.04, 18

meta = {}
for f in sorted(list(SRC.glob('*.png')) + list(SRC.glob('*.webp'))):
    im = Image.open(f).convert('RGBA')
    box = im.getchannel('A').point(lambda v: 255 if v > 8 else 0).getbbox()
    im = im.crop(box)
    fit = S * (1 - 2 * PAD) / max(im.size)
    im = im.resize((max(1, round(im.width * fit)), max(1, round(im.height * fit))), Image.LANCZOS)
    sq = Image.new('RGBA', (S, S), (0, 0, 0, 0))
    sq.alpha_composite(im, ((S - im.width) // 2, (S - im.height) // 2))
    sq.save(OUT / f'food_{f.stem}.webp', 'WEBP', quality=88, method=6)

    a = np.array(sq.getchannel('A')) > 128
    ys, xs = np.nonzero(a)
    cx, cy = xs.mean() / S, ys.mean() / S
    pts = []
    for j in range(G):
        for i in range(G):
            x, y = int((i + 0.5) / G * S), int((j + 0.5) / G * S)
            if a[y, x]:
                pts.append([round(x / S - cx, 4), round(y / S - cy, 4)])
    meta[f.stem] = {
        'src': f'sprites/food_{f.stem}.webp',
        'area': round(float(a.mean()), 4),
        'ext': round(max(xs.max() - xs.min(), ys.max() - ys.min()) / S, 4),
        'cx': round(float(cx), 4), 'cy': round(float(cy), 4),
        'pts': pts,
    }
    print(f'{f.stem:10s} area {meta[f.stem]["area"]:.3f}  ext {meta[f.stem]["ext"]:.3f}  points {len(pts)}  '
          f'{(OUT / f"food_{f.stem}.webp").stat().st_size // 1024} KB')

(OUT / 'foods.js').write_text('// Made by tools/build_foods.py from the drawings in art/foods/. Do not edit by hand.\n'
                              'window.FOOD_META = ' + json.dumps(meta, separators=(',', ':')) + ';\n')
