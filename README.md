# Corgi Chomp 🐶

A browser game: help Biscuit the Cardigan corgi eat snacks smaller than she is (butter, cake, birthday cake, bread, mice, fish, waffles, yogurt, carrots, apples) while dodging the ones that are too big. Every snack she eats makes her bigger, so foods that were dangerous at the start become edible later.

**Play it online:** https://sanderdebleeckerr.github.io/corgi-chomp/

## How to play

- **Move:** mouse, touch, or WASD / arrow keys
- Snacks **smaller** than Biscuit: eat them and grow
- Snacks **bigger** than Biscuit: touching one costs a heart
- Biscuit grows through 15 sizes. The camera zooms out two times as she grows
- **Win:** grow until Biscuit fills half of the screen
- **P / Esc:** pause · **M:** mute

## Run locally

Open `index.html` in any browser. It has no dependencies and no build step.

## Hosting

`.github/workflows/pages.yml` publishes the game to GitHub Pages on every push to `main`.
In the repository settings, set **Pages → Build and deployment → Source** to **GitHub Actions**.
