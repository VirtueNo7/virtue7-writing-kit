# GitHub Release Checklist

Before publishing:

- [ ] Replace `[RIGHTS HOLDER]` in `LICENSE.md`.
- [ ] Select an open-source, source-available, or proprietary licence deliberately.
- [ ] Confirm repository name and description.
- [ ] Confirm the whitepaper may be distributed with the release.
- [ ] Run `python scripts/validate_bundle.py`.
- [ ] Confirm no personal or recipient-specific information appears anywhere.
- [ ] Confirm the Master Builder is clearly fictional.
- [ ] Confirm generated-output branding remains disabled by default.
- [ ] Create a GitHub release tagged `v0.1.0`.
- [ ] Attach the ZIP file as the release asset.
- [ ] Test the release ZIP in at least two file-capable AI systems.
- [ ] Record differences in archive handling or file-reading behaviour.
