# NeuBrut

A collection of VS Code themes inspired by neo-brutalism, with bold accents and comfortable light and dark palettes.

## License

Copyright © 2026 Vijay Krishna Ankit. NeuBrut is licensed under the [GNU General Public License, version 3](LICENSE).

## Pick your palette

- **Concrete** — dark gray, safety yellow, hot pink, and mint.
- **Hearth** — Gruvbox-inspired charcoal, warm gold, coral, and olive.
- **Verdigris** — deep charcoal with muted teal, gold, and cyan.
- **Paper** — warm cream, muted dark grey, soft rose, and teal.
- **Mint** — cool mint, deep blue, violet, and forest green.
- **Lavender** — lilac paper, purple, berry, and teal; inspired by Catppuccin Latte.
- **Blossom** — warm blush, raspberry, violet, and teal; inspired by Rosé Pine Dawn.
- **Daybreak** — sunlit ivory, deep cyan, violet, and green; inspired by Solarized Light.
- **Midnight** — inky blue, electric blue, pink, and mint; inspired by Tokyo Night.
- **Fjord** — deep slate blue, glacier blue, soft gold, and moss; inspired by Nord.

## Try it locally

1. Open this folder in VS Code.
2. Press **F5** to launch an Extension Development Host.
3. Open the Command Palette and choose **Preferences: Color Theme**, then select a NeuBrut palette.

To build an installable VSIX, run `npm install` once, then run `npm run build`. Use **Extensions: Install from VSIX** in VS Code and select the generated file in `dist/`.

## GitHub builds and prereleases

GitHub Actions builds a VSIX on pushes to `main`, pull requests, and manual runs. Download it from the run's **Artifacts** section. Actions must be enabled in the repository settings.

To publish a GitHub prerelease:

1. Set the extension version in `package.json` and `package-lock.json` together, for example with `npm version 0.1.1 --no-git-tag-version`, and commit the changes along with the workflows. Push the commit to GitHub.
2. Create and push a matching release-candidate tag (increment the `rc` number for another candidate of the same version):

   ```sh
   git tag v0.1.1-rc.1
   git push origin v0.1.1-rc.1
   ```

3. Check the **Actions** tab. The prerelease workflow builds a prerelease VSIX and attaches it to a GitHub release marked **Pre-release**. Download it from **Releases** and install it using **Extensions: Install from VSIX**.

The tag's version must match `package.json`; the `-rc.N` suffix belongs only in the Git tag. If the workflow fails, inspect its Actions log. The workflow uses GitHub's automatically supplied token with `contents: write`; repository or organization Actions policies must allow that permission. A retry after a release has already been created requires deleting that release or using a new candidate tag.

This publishes to GitHub Releases, not the VS Code Marketplace. VSIX installations do not automatically update by default. Marketplace publishing requires a separate publisher setup and authentication.

VS Code themes control colors and syntax highlighting; the editor controls the shape and thickness of UI elements.

### Pill-shaped editor tabs

In VS Code 1.141 or later, open **Preferences: Open User Settings (JSON)** and add:

```json
"workbench.experimental.modernUI": true,
"workbench.experimental.modernUIEditorTabStyle": "pill"
```

These settings are experimental and may change. The theme cannot enable the tab shape on its own.

## Sidebar icons

Choose **Preferences: Product Icon Theme** from the Command Palette, then select **NeuBrut Icons**. The geometric icons follow the active color theme. They cover VS Code’s built-in Explorer, Search, Source Control, Run and Debug, Extensions, Testing, Accounts, and Settings icons; extension-provided icons retain their own artwork.

To rebuild the icon font after editing `scripts/build-product-icons.py`, install Python `fonttools` and run `python scripts/build-product-icons.py`.
