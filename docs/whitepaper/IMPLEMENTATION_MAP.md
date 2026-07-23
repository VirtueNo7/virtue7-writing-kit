# Whitepaper Implementation Map

| Whitepaper concept | Repository implementation |
|---|---|
| Canonical content system `C = (K, U, E, P, Q)` | `MASTER_PROMPT.md`, `architecture/01-content-system.md` |
| Canonical kernel | `architecture/02-canonical-kernel.md`, `templates/book-kernel.md` |
| Canonical content units | `architecture/03-content-units.md`, `templates/chapter-unit.md` |
| Controlled expansion | `architecture/04-expansion-and-compression.md`, `workflows/03-expand.md` |
| Reliable compression | `architecture/04-expansion-and-compression.md`, `workflows/04-collapse.md` |
| Projection contracts | `architecture/05-projection-contracts.md` |
| Semantic invariants and round-trip test | `architecture/06-round-trip-validation.md`, `workflows/05-validate.md` |
| Human authorship and approval | `architecture/07-governance.md`, `templates/session-state.md` |
| Repository separation of kernel, units, sources, manuscript, validation, outputs, versions | Root folder structure |
| Representative prototype before scaling | `workflows/01-new-book.md`, `workflows/02-master-builder-demo.md` |
| Multi-format projection | `config/resolutions.yaml`, projection contract table |

## White-label implementation

The architecture paper contains a named reference implementation. The writing kit separates provenance from generated output:

- kit documentation may identify its publisher and source lineage;
- user books do not inherit that branding by default;
- demonstration content is isolated under `demo/`;
- validation scans for demonstration leakage;
- every user project creates its own kernel, matrix, units, sources, and projection contracts.
