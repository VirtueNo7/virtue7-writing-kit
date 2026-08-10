# Worked example: Controlled Update

## User request

Convert these meeting notes into an approval-tracked decision update without changing unrelated state.

## Fixture and source boundary

- The complete artifact below is a reproducible evaluation fixture supplied to this example.
- Its factual content is treated as fixture input, not as independently verified or current information.
- No browsing, private memory, external action, or real-user data is claimed.

## Runtime selection

| Field | Selection |
|---|---|
| Capability | `continuation` |
| Route | `continuation/controlled-update` |
| Profile | `meeting_decision_record` |
| Form Lock | `preserve_form` |
| Related playbooks | `company_admin/meeting-to-decisions` |

## Route conformance illustration

**Outcome:** contract conformance is illustrated with a synthetic fixture; this is not proof of a model run or external action.

**Route contract applied:** Register the proposed change, rationale, affected canonical fields, affected outputs, unaffected outputs, migration action, validation, and approval state before propagation.

**Source handling:** the fixture is the complete supplied record. Any request requiring live discovery, currency, verification, publication, filing, or synchronization stops at the tool handoff below.

## Active context

- Boot: three files
- Route packet: `runtime/packets/routes/continuation--controlled-update.md` (3984 bytes)
- Profile packet: `runtime/packets/profiles/meeting_decision_record.md` (1207 bytes)
- Total active files: five

## Draft artifact

# Setup Pilot Decision

## Context
- Repeat configuration contacts increased during the quarter.

## Decisions
- Run a four-week guided-setup pilot.

## Rationale
- Observation and support evidence identify the same decision point.

## Actions
- Build the prototype.
- Recruit five test users.

## Owners
- Prototype: Sam.
- Research: Ari.

## Due Dates
- Prototype due 2026-09-01.

## Dependencies
- Approved test environment.

## Unresolved Questions
- Which exception path needs specialist review?

## Gate report

**Structural preflight: Pass**

- Profile structure: required fields and form are present.
- Evidence: factual content remains explicitly classified as supplied fixture material; no independent verification is implied.
- Semantic finish: each section adds a fact, decision, mechanism, or reader capability.
- Form Lock: `preserve_form` is preserved.

## Revision request

Clarify that this is the revised visible version without changing its evidence, structure, or approved terminology.

## Revised draft

# Revised: Setup Pilot Decision

## Context
- Repeat configuration contacts increased during the quarter.

## Decisions
- Run a four-week guided-setup pilot.

## Rationale
- Observation and support evidence identify the same decision point.

## Actions
- Build the prototype.
- Recruit five test users.

## Owners
- Prototype: Sam.
- Research: Ari.

## Due Dates
- Prototype due 2026-09-01.

## Dependencies
- Approved test environment.

## Unresolved Questions
- Which exception path needs specialist review?

## Lifecycle state

```yaml
artifact_id: 07-continuation-controlled-update
route: continuation/controlled-update
profile: meeting_decision_record
status: revised_draft
approval_record: null
human_approval_required: true
source_scope: evaluation_fixture
material_revision_requires_reapproval: true
```

## Tool handoff

State handling is complete. External synchronization or task updates require an authorized host tool.
