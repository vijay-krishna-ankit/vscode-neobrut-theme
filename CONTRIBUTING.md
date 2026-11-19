# Contributing to NeuBrut

## Development

1. Open this folder in VS Code.
2. Press **F5** to launch an Extension Development Host.
3. Open the Command Palette and choose **Preferences: Color Theme**, then select a NeuBrut palette.

To build an installable VSIX, run `npm install` once, then run `npm run build`. Use **Extensions: Install from VSIX** in VS Code and select the generated file in `dist/`. To rebuild the icon font after editing `scripts/build-product-icons.py`, install Python `fonttools` and run `python scripts/build-product-icons.py`.

## GitHub builds and releases

GitHub Actions builds a VSIX on pushes to `main`, pull requests, and manual runs. Download it from the run's **Artifacts** section. Actions must be enabled in the repository settings.

To create a stable GitHub release, update the version in `package.json` and `package-lock.json`, commit and push the changes, then create and push a matching tag:

```sh
git tag -a v0.1.3 -m "Release 0.1.3"
git push origin v0.1.3
```

The release workflow builds a stable VSIX and attaches it to the GitHub release. Download the VSIX from **Releases** to upload it to the VS Code Marketplace. For an existing tag, run **GitHub release** from the Actions tab and enter the tag name. The tag must match the version in the tagged commit.

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

