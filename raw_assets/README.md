# Raw asset archive

This directory stores original files that were removed or optimized for the website.
Jekyll explicitly excludes `raw_assets/`, so none of these files are copied to `_site`
or included in the deployed webpage.

- Source revision: `93cb983411cfa218d807db30f0f381ac5807cb34`
- Archived on: 2026-07-11
- Original files: `original-tree/`
- Integrity manifest: `SHA256SUMS`

The paths below `original-tree/` match the files' former repository paths. To verify
the archive, run this command from the repository root:

```sh
cd raw_assets/original-tree && shasum -a 256 -c ../SHA256SUMS
```
