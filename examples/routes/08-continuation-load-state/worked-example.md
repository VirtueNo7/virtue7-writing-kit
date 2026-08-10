# Worked example: Load Project State

## User request

Load the approved novel state and continue only from the next authorized scene decision.

## Fixture and source boundary

- The complete artifact below is a reproducible evaluation fixture supplied to this example.
- Its factual content is treated as fixture input, not as independently verified or current information.
- No browsing, private memory, external action, or real-user data is claimed.

## Runtime selection

| Field | Selection |
|---|---|
| Capability | `continuation` |
| Route | `continuation/load-state` |
| Profile | `novel_chapter` |
| Form Lock | `narrative_lock` |
| Related playbooks | Route-native example |

## Route conformance illustration

**Outcome:** contract conformance is illustrated with a synthetic fixture; this is not proof of a model run or external action.

**Route contract applied:** Locate the active project-state file and approved canonical records. Summarize current gate, decisions, open questions, dependencies, and next approved action. Never continue from a blank template.

**Source handling:** the fixture is the complete supplied record. Any request requiring live discovery, currency, verification, publication, filing, or synchronization stops at the tool handoff below.

## Active context

- Boot: three files
- Route packet: `runtime/packets/routes/continuation--load-state.md` (4001 bytes)
- Profile packet: `runtime/packets/profiles/novel_chapter.md` (1084 bytes)
- Total active files: five

## Draft artifact

# Chapter Seven

The signal returned just after midnight, too faint for the station to classify and too regular for weather. Mara listened through three complete cycles before touching the recorder. Each pulse arrived with the patience of a clock in another room, followed by a wash of static that seemed to erase its own arrival.

She carried the printout down the east corridor. The building had been designed to make every journey feel official, but at this hour the locked offices and dark glass reduced it to a tunnel. At the archive door she stopped. The last sealed report had described the same interval, although the author had called it equipment fatigue and closed the file.

Inside, she laid both traces beneath the green lamp. The peaks aligned. What had looked like noise in the older record was not noise at all; it was the beginning of the second sequence. She wrote the finding in the margin, then crossed it out. If the signal had already been heard, the first question was no longer what it meant. The first question was who had decided it should be forgotten.

## Gate report

**Structural preflight: Pass**

- Profile structure: required fields and form are present.
- Evidence: factual content remains explicitly classified as supplied fixture material; no independent verification is implied.
- Semantic finish: each section adds a fact, decision, mechanism, or reader capability.
- Form Lock: `narrative_lock` is preserved.

## Revision request

Clarify that this is the revised visible version without changing its evidence, structure, or approved terminology.

## Revised draft

# Revised: Chapter Seven

The signal returned just after midnight, too faint for the station to classify and too regular for weather. Mara listened through three complete cycles before touching the recorder. Each pulse arrived with the patience of a clock in another room, followed by a wash of static that seemed to erase its own arrival.

She carried the printout down the east corridor. The building had been designed to make every journey feel official, but at this hour the locked offices and dark glass reduced it to a tunnel. At the archive door she stopped. The last sealed report had described the same interval, although the author had called it equipment fatigue and closed the file.

Inside, she laid both traces beneath the green lamp. The peaks aligned. What had looked like noise in the older record was not noise at all; it was the beginning of the second sequence. She wrote the finding in the margin, then crossed it out. If the signal had already been heard, the first question was no longer what it meant. The first question was who had decided it should be forgotten.

## Lifecycle state

```yaml
artifact_id: 08-continuation-load-state
route: continuation/load-state
profile: novel_chapter
status: revised_draft
approval_record: null
human_approval_required: true
source_scope: evaluation_fixture
material_revision_requires_reapproval: true
```

## Tool handoff

State handling is complete. External synchronization or task updates require an authorized host tool.
