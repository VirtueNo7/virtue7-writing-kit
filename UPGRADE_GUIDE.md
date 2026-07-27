# Upgrade Guide: v0.1.0 to v0.2.0

Version 0.2.0 is a backward-compatible architectural upgrade. Existing kernels, matrices, plans, chapters, source records, and session states remain valid.

## What changes

The project model now includes a classified reference corpus (`R`) and voice contract (`V`). Projects created entirely from scratch may leave these layers minimal. Projects built from prior writing, transcripts, interviews, notes, or archives should complete the reference and voice gates before representative drafting.

## Migrating an existing project

1. Keep all approved canonical records unchanged.
2. Inventory prior writing and source materials using `templates/reference-register.md`.
3. Classify each item using `config/reference-policy.yaml`.
4. Build a voice contract only from suitable, approved voice references.
5. Create a compact reference packet for the next unit being drafted or revised.
6. Add provenance to representative and publication-ready units.
7. Run `workflows/09-run-drift-test.md` before scaling or release.
8. Update `SESSION_STATE` with reference and voice status.

No existing prose is automatically promoted into the voice canon. Human approval is required.
