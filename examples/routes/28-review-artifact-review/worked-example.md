# Worked example: Artifact Review

## User request

Review this manual against its profile, sources, and completion test; repair only actionable defects.

## Fixture and source boundary

- The complete artifact below is a reproducible evaluation fixture supplied to this example.
- Its factual content is treated as fixture input, not as independently verified or current information.
- No browsing, private memory, external action, or real-user data is claimed.

## Runtime selection

| Field | Selection |
|---|---|
| Capability | `review` |
| Route | `review/artifact-review` |
| Profile | `technical_manual` |
| Form Lock | `adaptive` |
| Related playbooks | Route-native example |

## Route conformance illustration

**Outcome:** contract conformance is illustrated with a synthetic fixture; this is not proof of a model run or external action.

**Route contract applied:** Identify the output profile, source of truth, and requested review depth. Evaluate structure, truth, evidence, semantic finish, voice, accessibility, and readiness. Return the smallest actionable repair plan.

**Source handling:** the fixture is the complete supplied record. Any request requiring live discovery, currency, verification, publication, filing, or synchronization stops at the tool handoff below.

## Active context

- Boot: three files
- Route packet: `runtime/packets/routes/review--artifact-review.md` (4038 bytes)
- Profile packet: `runtime/packets/profiles/technical_manual.md` (883 bytes)
- Total active files: five

## Draft artifact

# Design a Clear Settings Screen

A settings screen should help people understand what they can change, what each change affects, and whether the change took effect. Keep the screen focused. Remove controls that belong in the main task flow or that most people never need.

## Organize by purpose

Group settings according to the outcome people expect, not the subsystem that implements them. Use familiar labels and keep the same term everywhere it appears.

- Put the most commonly changed settings first.
- Separate account, notification, privacy, and appearance controls when they serve different goals.
- Avoid a miscellaneous group. It usually hides an unresolved information structure.
- Keep destructive actions visually and spatially separate from routine preferences.

## Write direct labels

Use short labels that name the setting or the action. Supporting text should explain consequences that are not obvious from the label.

Prefer:

- “Download over Wi-Fi”
- “Share activity status”
- “Delete account”

Avoid labels such as “Advanced options,” “Proceed,” or “Enable functionality.” They make people translate the interface before they can use it.

## Show the result

When a setting changes immediately, preserve the person’s place and provide quiet confirmation through the updated control or nearby content. When a change requires another step, explain that requirement before the person commits.

For a setting that cannot be changed, state why and identify the action that can resolve it. Do not present an inactive control without an explanation.

## Check accessibility and localization

Before release:

1. Increase text size and confirm that labels remain readable without truncating essential meaning.
2. Navigate with assistive technology and verify that each control has a useful name, value, and state.
3. Test translated strings that are substantially longer than the source language.
4. Confirm that color is not the only signal for selection, warning, or status.
5. Review terminology for jargon, idioms, and culture-specific assumptions.

A successful settings screen feels predictable. People can scan it, understand it, make a change, and return to their original task without having to learn how the product is built.

## Gate report

**Structural preflight: Pass**

- Profile structure: required fields and form are present.
- Evidence: factual content remains explicitly classified as supplied fixture material; no independent verification is implied.
- Semantic finish: each section adds a fact, decision, mechanism, or reader capability.
- Form Lock: `adaptive` is preserved.

## Revision request

Clarify that this is the revised visible version without changing its evidence, structure, or approved terminology.

## Revised draft

# Revised: Design a Clear Settings Screen

A settings screen should help people understand what they can change, what each change affects, and whether the change took effect. Keep the screen focused. Remove controls that belong in the main task flow or that most people never need.

## Organize by purpose

Group settings according to the outcome people expect, not the subsystem that implements them. Use familiar labels and keep the same term everywhere it appears.

- Put the most commonly changed settings first.
- Separate account, notification, privacy, and appearance controls when they serve different goals.
- Avoid a miscellaneous group. It usually hides an unresolved information structure.
- Keep destructive actions visually and spatially separate from routine preferences.

## Write direct labels

Use short labels that name the setting or the action. Supporting text should explain consequences that are not obvious from the label.

Prefer:

- “Download over Wi-Fi”
- “Share activity status”
- “Delete account”

Avoid labels such as “Advanced options,” “Proceed,” or “Enable functionality.” They make people translate the interface before they can use it.

## Show the result

When a setting changes immediately, preserve the person’s place and provide quiet confirmation through the updated control or nearby content. When a change requires another step, explain that requirement before the person commits.

For a setting that cannot be changed, state why and identify the action that can resolve it. Do not present an inactive control without an explanation.

## Check accessibility and localization

Before release:

1. Increase text size and confirm that labels remain readable without truncating essential meaning.
2. Navigate with assistive technology and verify that each control has a useful name, value, and state.
3. Test translated strings that are substantially longer than the source language.
4. Confirm that color is not the only signal for selection, warning, or status.
5. Review terminology for jargon, idioms, and culture-specific assumptions.

A successful settings screen feels predictable. People can scan it, understand it, make a change, and return to their original task without having to learn how the product is built.

## Lifecycle state

```yaml
artifact_id: 28-review-artifact-review
route: review/artifact-review
profile: technical_manual
status: revised_draft
approval_record: null
human_approval_required: true
source_scope: evaluation_fixture
material_revision_requires_reapproval: true
```

## Tool handoff

The review is complete. Deployment, publication, or filing remains a human-approved external action.
