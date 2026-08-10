# Whitepaper Implementation Map - v0.5.0

| Whitepaper concept | Repository implementation |
|---|---|
| Three operating modes | `00_START_HERE.md`, `MASTER_PROMPT.md`, `RUNTIME_MANIFEST.yaml` |
| Chat and Content stay light | three-file boot; compiled route/profile packets |
| Automation is bounded work | `runtime/packets/modes/automation.md`; bounded-task rules in the master prompt |
| Mode is separate from capability | `RUNTIME_MANIFEST.yaml`, capability/route registry |
| Minimum-sufficient loading | boot loading rules, compact handoffs, compiled packets |
| Canonical content `C = (K, U, E, P, Q)` | architecture and canonical-content templates |
| Evidence, cadence, and Form Lock | `config/gates.yaml`, `config/form-lock.yaml`, quality gates and templates |
| Pseudo-list protection | `quality/FORM_LOCK_GATE.md`, narrative profile gate, writing contract tests |
| Tool truth and receipts | `schemas/tool-receipt.schema.json`, runtime tool-truth rules |
| Human artifact approval | artifact lifecycle and `schemas/approval-record.schema.json` |
| Controlled improvement | whitepaper plus deterministic release/evaluation suite |
| Lean boot budget | `scripts/validate_runtime.py`, `scripts/benchmark_runtime.py` |
| PDF projection | `scripts/build_whitepaper.py`, `scripts/validate_whitepaper.py` |

The paper explains the architecture. Runtime behavior is controlled by the three-file boot, the selected route/profile/tool packets, compact state, and the user's latest explicit instruction.
