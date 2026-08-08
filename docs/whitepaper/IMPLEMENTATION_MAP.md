# Whitepaper Implementation Map — v0.4

| Whitepaper concept | Repository implementation |
|---|---|
| Lean boot and direct routing | `00_START_HERE.md`, `RUNTIME_MANIFEST.yaml`, `MASTER_PROMPT.md` |
| Canonical system `C = (K, U, E, P, Q)` | `architecture/`, `templates/canonical-kernel.md`, `templates/content-kernel.md` |
| Personal work layer `W = (I, V, R, O, S)` | `capabilities/personalization/`, personal and scoped profile templates |
| Optional identity and discovery keys | `templates/personal-work-profile.md`, personalization initialization route |
| Evidence-backed cadence | `templates/cadence-profile.md`, `templates/voice-contract.md`, `quality/CADENCE_FIDELITY_GATE.md` |
| Adaptive, Preserve Form, and Narrative Form Lock | `config/form-lock.yaml`, `templates/form-lock-record.md`, `quality/FORM_LOCK_GATE.md` |
| Role, organization, client, and project isolation | scoped templates, `quality/PRIVACY_BOUNDARY_GATE.md`, runtime precedence |
| Playbooks and custom commands | `library/`, `templates/custom-command.md`, create-command route |
| Evidence and claim states | source, source-register, claim-record, timeline, and publication-risk templates |
| Output profiles | `config/output-profiles.yaml`, `profiles/` |
| Project state and controlled continuation | `templates/project-state.md`, `templates/session-state.md`, continuation capability |
| Expansion, compression, and projection | `architecture/04-expansion-and-compression.md`, `architecture/05-projection-contracts.md` |
| Round-trip validation | `architecture/06-round-trip-validation.md`, review capability, test fixtures |
| Tool contracts | runtime tool-truth rules, playbook `tool_contract` fields, README boundaries |
| Human approval | artifact lifecycle, approval matrix, publication-risk and universal gates |
| White-label operation | `config/kit.yaml`, bundle validation, isolated demo content |
| Executable release validation | `scripts/run_release_checks.py`, playbook, runtime, bundle, profile, and PDF validators |

The paper is an architectural explanation. Runtime behavior is controlled by the boot files, selected manifests, scoped records, and the user's latest explicit instruction.
