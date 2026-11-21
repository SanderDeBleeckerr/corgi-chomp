# Corgi Chomp 🐶

A browser game: help Hrozna the Cardigan corgi eat snacks smaller than she is (butter, cake, birthday cake, bread, mice, fish, waffles, yogurt, carrots, apples) while dodging the ones that are too big. Every snack she eats makes her bigger, so foods that were dangerous at the start become edible later.

**Play it online:** https://sanderdebleeckerr.github.io/corgi-chomp/

## How to play

- **Move:** mouse, touch, or WASD / arrow keys
- **Phone / tablet:** tilt the device to move. The angle you hold it at when you tap Play counts as level. A finger on the screen overrides the tilt; the 📱 button turns tilt on or off
- Snacks **smaller** than Hrozna: eat them and grow
- Snacks **bigger** than Hrozna: touching one costs a heart
- Hrozna grows through 15 sizes. The camera zooms out two times as she grows
- **Win:** grow until Hrozna fills half of the screen
- **P / Esc:** pause · **M:** mute

## Run locally

Open `index.html` in any browser. It has no dependencies and no build step.

## Hosting

`.github/workflows/pages.yml` publishes the game to GitHub Pages on every push to `main`.
In the repository settings, set **Pages → Build and deployment → Source** to **GitHub Actions**.
