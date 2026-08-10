# Worked example: Revise Output

## User request

Revise this story for clarity while preserving its paragraph movement, facts, and deliberate restraint.

## Fixture and source boundary

- The complete artifact below is a reproducible evaluation fixture supplied to this example.
- Its factual content is treated as fixture input, not as independently verified or current information.
- No browsing, private memory, external action, or real-user data is claimed.

## Runtime selection

| Field | Selection |
|---|---|
| Capability | `writing` |
| Route | `writing/revise-output` |
| Profile | `fiction_short_story` |
| Form Lock | `narrative_lock` |
| Related playbooks | `writer/revision-without-flattening` |

## Route conformance illustration

**Outcome:** contract conformance is illustrated with a synthetic fixture; this is not proof of a model run or external action.

**Route contract applied:** Treat the user's latest feedback as an editorial instruction. Determine whether it requests correction, compression, expansion, replacement, developmental revision, voice refinement, format adaptation, or protected-section preservation.

Apply the requested change precisely. Preserve unaffected material, verified facts, approved terminology, citations, and voice evidence. Do not use revision as permission to redesign the entire artifact. A material revision returns the artifact to Draft and awaits approval or further instruction.

**Source handling:** the fixture is the complete supplied record. Any request requiring live discovery, currency, verification, publication, filing, or synchronization stops at the tool handoff below.

## Active context

- Boot: three files
- Route packet: `runtime/packets/routes/writing--revise-output.md` (6321 bytes)
- Profile packet: `runtime/packets/profiles/fiction_short_story.md` (1087 bytes)
- Total active files: five

## Draft artifact

# The Last Tram

Rain had erased the timetable, but Mara waited beneath the broken clock because her brother's note said the last tram still came for anyone carrying an unfinished promise.

At midnight a single carriage rounded the corner without touching the rails. The conductor asked for no fare. He only looked at the sealed letter in Mara's hand and asked whether she wanted forgiveness or merely delivery.

She had rehearsed an answer for seven years. In the quiet carriage, it sounded borrowed. Mara broke the seal, read the first line, and understood that the letter accused her brother of the silence she had chosen herself.

At the final stop she found no platform, only the old hospital garden and one lit window. She rewrote the letter on the conductor's blank ticket. This time she began with what she had done.

The tram returned before dawn. The promise was not finished, but it was finally hers.

## Gate report

**Structural preflight: Pass**

- Profile structure: required fields and form are present.
- Evidence: factual content remains explicitly classified as supplied fixture material; no independent verification is implied.
- Semantic finish: each section adds a fact, decision, mechanism, or reader capability.
- Form Lock: `narrative_lock` is preserved.

## Revision request

Clarify that this is the revised visible version without changing its evidence, structure, or approved terminology.

## Revised draft

# Revised: The Last Tram

Rain had erased the timetable, but Mara waited beneath the broken clock because her brother's note said the last tram still came for anyone carrying an unfinished promise.

At midnight a single carriage rounded the corner without touching the rails. The conductor asked for no fare. He only looked at the sealed letter in Mara's hand and asked whether she wanted forgiveness or merely delivery.

She had rehearsed an answer for seven years. In the quiet carriage, it sounded borrowed. Mara broke the seal, read the first line, and understood that the letter accused her brother of the silence she had chosen herself.

At the final stop she found no platform, only the old hospital garden and one lit window. She rewrote the letter on the conductor's blank ticket. This time she began with what she had done.

The tram returned before dawn. The promise was not finished, but it was finally hers.

## Lifecycle state

```yaml
artifact_id: 35-writing-revise-output
route: writing/revise-output
profile: fiction_short_story
status: revised_draft
approval_record: null
human_approval_required: true
source_scope: evaluation_fixture
material_revision_requires_reapproval: true
```

## Tool handoff

The draft and revision are native. Export or publication requires a supported tool and approval.
