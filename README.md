# Corgi Chomp 🐶

A browser game: help Hrozna the Cardigan corgi eat snacks smaller than she is (butter, cake, birthday cake, bread, mice, fish, waffles, yogurt, carrots, apples) while dodging the ones that are too big. Every snack she eats makes her bigger, so foods that were dangerous at the start become edible later.

**Play it online:** https://sanderdebleeckerr.github.io/corgi-chomp/

## How to play

- **Move:** mouse, touch, or WASD / arrow keys
- **Phone / tablet:** three ways to move. Tap the control button at the top to change:
  - 📱 **Tilt:** tilt the device. The angle you hold it at when you tap Play counts as level. A finger on the screen overrides the tilt
  - 🕹️ **Joystick:** touch anywhere and drag; the joystick appears under your thumb
  - 👆 **Finger:** Hrozna follows your finger
- Snacks **smaller** than Hrozna: eat them and grow. The game compares the size you see (a mix of visible area and length), so a flat butter and a round apple are judged the same way
- Snacks **bigger** than Hrozna: touching one costs a heart
- Hrozna grows through 15 sizes. The camera zooms out two times as she grows
- **Win:** grow until Hrozna fills half of the screen
- **P / Esc:** pause · **M:** mute

## Run locally

Open `index.html` in any browser. It has no dependencies and no build step.

## Hosting

`.github/workflows/pages.yml` publishes the game to GitHub Pages on every push to `main`.
In the repository settings, set **Pages → Build and deployment → Source** to **GitHub Actions**.
