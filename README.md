# NeuBrut

A loud, colorful VS Code theme collection inspired by neo-brutalism: hard borders, punchy accents, and unapologetic contrast.

## Pick your palette

- **Concrete** — dark gray, safety yellow, hot pink, and mint.
- **Hearth** — Gruvbox-inspired charcoal, warm gold, coral, and olive.
- **Electric** — deep violet with pink, yellow, and cyan.
- **Paper** — warm cream, black ink, berry, and teal.
- **Mint** — cool mint, deep blue, violet, and forest green.
- **Lavender** — lilac paper, purple, berry, and teal; inspired by Catppuccin Latte.
- **Blossom** — warm blush, raspberry, violet, and teal; inspired by Rosé Pine Dawn.
- **Daybreak** — sunlit ivory, deep cyan, violet, and green; inspired by Solarized Light.
- **Midnight** — inky blue, electric blue, pink, and mint; inspired by Tokyo Night.
- **Fjord** — slate, icy teal, rose, and moss; inspired by Nord.

## Try it locally

1. Open this folder in VS Code.
2. Press **F5** to launch an Extension Development Host.
3. Open the Command Palette and choose **Preferences: Color Theme**, then select a NeuBrut palette.

To build an installable VSIX, run `npm install` once, then run `npm run build`. Use **Extensions: Install from VSIX** in VS Code and select the generated file in `dist/`.

VS Code themes control colors and syntax highlighting; the editor controls the shape and thickness of UI elements.

## Sidebar icons

Choose **Preferences: Product Icon Theme** from the Command Palette, then select **NeuBrut Icons**. The geometric icons follow the active color theme. They cover VS Code’s built-in Explorer, Search, Source Control, Run and Debug, Extensions, Testing, Accounts, and Settings icons; extension-provided icons retain their own artwork.

To rebuild the icon font after editing `scripts/build-product-icons.py`, install Python `fonttools` and run `python scripts/build-product-icons.py`.
