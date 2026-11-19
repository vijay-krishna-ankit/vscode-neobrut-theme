# NeuBrut

A collection of VS Code themes inspired by the bold colors of neo-brutalism. NeuBrut brings those colors into light and dark palettes designed to be comfortable to look at during long coding sessions.

Color and screen comfort are personal, so try the palettes with your usual code, screen brightness, and lighting to find what works for you.

## Get started

1. Install **NeuBrut** from the VS Code Extensions view.
2. Open the Command Palette and choose **Preferences: Color Theme**.
3. Select a NeuBrut palette and try it with your usual files and lighting.
4. For matching geometric icons, choose **Preferences: Product Icon Theme** and select **NeuBrut Icons**.

## Share your experience

I'd welcome feedback on how the palettes feel during your usual work. Are any colors, contrasts, or highlights uncomfortable over time? Which palette, screen brightness, and lighting were you using?

Please [open an issue](https://github.com/vijay-krishna-ankit/vscode-neobrut-theme/issues) to share what worked or suggest improvements.

## Pick your palette

### Concrete

Dark gray, safety yellow, hot pink, and mint.

![VS Code with the NeuBrut Concrete dark theme](screenshots/Dark-Concrete.png)

### Hearth

Gruvbox-inspired charcoal, warm gold, coral, and olive.

![VS Code with the NeuBrut Hearth dark theme](screenshots/Dark-Hearth.png)

### Verdigris

Deep charcoal with muted teal, gold, and cyan.

![VS Code with the NeuBrut Verdigris dark theme](screenshots/Dark-Verdigris.png)

### Midnight

Inky blue, electric blue, pink, and mint; inspired by Tokyo Night.

![VS Code with the NeuBrut Midnight dark theme](screenshots/Dark-Midnight.png)

### Fjord

Deep slate blue, glacier blue, soft gold, and moss; inspired by Nord.

![VS Code with the NeuBrut Fjord dark theme](screenshots/Dark-Fjord.png)

### Paper

Warm cream, muted dark grey, soft rose, and teal.

![VS Code with the NeuBrut Paper light theme](screenshots/Light-Paper.png)

### Mint

Cool mint, deep blue, violet, and forest green.

![VS Code with the NeuBrut Mint light theme](screenshots/Light-Mint.png)

### Lavender

Lilac paper, purple, berry, and teal; inspired by Catppuccin Latte.

![VS Code with the NeuBrut Lavender light theme](screenshots/Light-Lavender.png)

### Blossom

Warm blush, raspberry, violet, and teal; inspired by Rosé Pine Dawn.

![VS Code with the NeuBrut Blossom light theme](screenshots/Light-Blossom.png)

### Daybreak

Sunlit ivory, deep cyan, violet, and green; inspired by Solarized Light.

![VS Code with the NeuBrut Daybreak light theme](screenshots/Light-Daybreak.png)

## Sidebar icons

NeuBrut Icons follows the active color theme and covers VS Code's built-in Explorer, Search, Source Control, Run and Debug, Extensions, Testing, Accounts, and Settings icons. Extension-provided icons retain their own artwork.

## Syntax highlighting

Each palette colors common syntax and enables semantic highlighting for symbols such as types, methods, properties, and parameters. The exact colors visible depend on the language grammar and language extension. If code still looks mostly one color, check that VS Code has detected the correct language and that its language extension is installed and active. A user or workspace `editor.semanticHighlighting.enabled` setting can also override the theme's preference.

## Readable tab labels

VS Code can color tab labels based on Git status or problems. Those colors may be hard to read against NeuBrut's bright active tabs. To use the theme's tab text colors instead, open **Preferences: Open User Settings (JSON)** and add:

```json
"workbench.editor.decorations.colors": false
```

Git status badges can still appear on tabs, and the Explorer keeps its decoration colors.

## Pill-shaped editor tabs

VS Code themes control colors and syntax highlighting; the editor controls the shape and thickness of UI elements. In VS Code 1.141 or later, open **Preferences: Open User Settings (JSON)** and add:

```json
"workbench.experimental.modernUI": true,
"workbench.experimental.modernUIEditorTabStyle": "pill"
```

These settings are experimental and may change. The theme cannot enable the tab shape on its own.

For development and release instructions, see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Copyright © 2026 Vijay Krishna Ankit. NeuBrut is licensed under the [GNU General Public License, version 3](LICENSE).
