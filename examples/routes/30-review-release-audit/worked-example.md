# Worked example: Release Audit

## User request

Audit this product brief for release readiness, evidence, unresolved risks, and required approval.

## Fixture and source boundary

- The complete artifact below is a reproducible evaluation fixture supplied to this example.
- Its factual content is treated as fixture input, not as independently verified or current information.
- No browsing, private memory, external action, or real-user data is claimed.

## Runtime selection

| Field | Selection |
|---|---|
| Capability | `review` |
| Route | `review/release-audit` |
| Profile | `product_brief` |
| Form Lock | `preserve_form` |
| Related playbooks | `brand/claim-audit`, `product/release-decision` |

## Route conformance illustration

**Outcome:** contract conformance is illustrated with a synthetic fixture; this is not proof of a model run or external action.

**Route contract applied:** Check versioning, names, manifests, source lineage, approvals, tests, white-label boundaries, hidden files, generated outputs, and reproducibility. Never mark Released without human approval.

**Source handling:** the fixture is the complete supplied record. Any request requiring live discovery, currency, verification, publication, filing, or synchronization stops at the tool handoff below.

## Active context

- Boot: three files
- Route packet: `runtime/packets/routes/review--release-audit.md` (4017 bytes)
- Profile packet: `runtime/packets/profiles/product_brief.md` (916 bytes)
- Total active files: five

## Draft artifact

# Guided Setup Brief

## Problem
New users cannot explain which configuration path applies to them.

## Evidence
Five observed sessions and 126 support records show repeated uncertainty at the same decision.

## Users
First-time workspace administrators.

## Proposed Value
Frame the decision before asking for configuration details.

## Requirements
- The flow must explain each path in plain language.
- Acceptance criteria: a test user shall select a path and state why it applies.

## Non-Goals
- Rebuilding advanced configuration.

## Risks
- Oversimplifying uncommon setups.

## Success Conditions
- Fewer unresolved choices during observed sessions.

## Open Questions
- Which exception requires escalation?

## Gate report

**Structural preflight: Pass**

- Profile structure: required fields and form are present.
- Evidence: factual content remains explicitly classified as supplied fixture material; no independent verification is implied.
- Semantic finish: each section adds a fact, decision, mechanism, or reader capability.
- Form Lock: `preserve_form` is preserved.

## Revision request

Clarify that this is the revised visible version without changing its evidence, structure, or approved terminology.

## Revised draft

# Revised: Guided Setup Brief

## Problem
New users cannot explain which configuration path applies to them.

## Evidence
Five observed sessions and 126 support records show repeated uncertainty at the same decision.

## Users
First-time workspace administrators.

## Proposed Value
Frame the decision before asking for configuration details.

## Requirements
- The flow must explain each path in plain language.
- Acceptance criteria: a test user shall select a path and state why it applies.

## Non-Goals
- Rebuilding advanced configuration.

## Risks
- Oversimplifying uncommon setups.

## Success Conditions
- Fewer unresolved choices during observed sessions.

## Open Questions
- Which exception requires escalation?

## Lifecycle state

```yaml
artifact_id: 30-review-release-audit
route: review/release-audit
profile: product_brief
status: revised_draft
approval_record: null
human_approval_required: true
source_scope: evaluation_fixture
material_revision_requires_reapproval: true
```

## Tool handoff

The review is complete. Deployment, publication, or filing remains a human-approved external action.
