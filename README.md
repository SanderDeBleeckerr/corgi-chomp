# Corgi Chomp 🐶

A browser game: help Hrozna the Cardigan corgi eat snacks smaller than she is (hand-drawn grass, sausages, mice, carrots and birthday cakes) while dodging the ones that are too big. Every snack she eats makes her bigger, so foods that were dangerous at the start become edible later.

**Play it online:** https://sanderdebleeckerr.github.io/corgi-chomp/

## How to play

- **Move:** mouse, touch, or WASD / arrow keys
- **Phone / tablet:** three ways to move. Tap the control button at the top to change:
  - 📱 **Tilt:** tilt the device. The angle you hold it at when you tap Play counts as level. A finger on the screen overrides the tilt
  - 🕹️ **Joystick:** touch anywhere and drag; the joystick appears under your thumb
  - 👆 **Finger:** Hrozna follows your finger
- Snacks **smaller** than Hrozna: eat them and grow. The game compares the size you see (a mix of visible area and length), so a flat butter and a round apple are judged the same way
- Snacks **bigger** than Hrozna: touching one costs a heart
- Every kind of snack has its own fixed size, from small to big: grass, sausages, mouse, carrot, birthday cake
- Hrozna grows through 22 ranks. The camera zooms out two times as she grows
- **Top Dog:** when she is bigger than the birthday cake, nothing can hurt her any more, and she grows faster
- **Screen Filler:** she grows until she fills the whole screen, and then 2 ranks more (Galaxy Gobbler, Legendary Hrozna) until she is bigger than the screen. Then every snack gives double points. The game has no end: keep eating for a high score
- **P / Esc:** pause · **M:** mute

## Art

- `sprites/hrozna_walk_1-3.webp`: Hrozna's walk cycle, cut from photos (transparent WebP, 1100 x 648 px, same crop for all frames). 1 size unit = 310 px; the middle of her torso is at pixel (550, 390).
- `sounds/bark1-8.mp3`: Hrozna's real barks.

### Add or change a snack drawing

1. Put the drawing in `art/foods/` as a PNG or WebP with a transparent background (for example `art/foods/apple.png`).
2. Run `python3 tools/build_foods.py`. It makes `sprites/food_apple.webp` and measures the visible shape (for size and collisions) into `sprites/foods.js`.
3. Add a line to the `FOODS` list in `index.html` with its id, fixed size and movement.

## Run locally

Open `index.html` in any browser. It has no dependencies and no build step.

## Hosting

`.github/workflows/pages.yml` publishes the game to GitHub Pages on every push to `main`.
In the repository settings, set **Pages → Build and deployment → Source** to **GitHub Actions**.
