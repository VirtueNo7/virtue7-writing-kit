# Worked example: Cover Letter

## User request

Write a specific cover letter using two verified evidence matches and no invented familiarity.

## Fixture and source boundary

- The complete artifact below is a reproducible evaluation fixture supplied to this example.
- Its factual content is treated as fixture input, not as independently verified or current information.
- No browsing, private memory, external action, or real-user data is claimed.

## Runtime selection

| Field | Selection |
|---|---|
| Capability | `resume` |
| Route | `resume/cover-letter` |
| Profile | `cover_letter` |
| Form Lock | `adaptive` |
| Related playbooks | Route-native example |

## Route conformance illustration

**Outcome:** contract conformance is illustrated with a synthetic fixture; this is not proof of a model run or external action.

**Route contract applied:** Use the verified resume source and target job packet. Select two or three strongest evidence matches. Write a specific professional letter without repeating the resume or claiming unsupported enthusiasm or familiarity.

**Source handling:** the fixture is the complete supplied record. Any request requiring live discovery, currency, verification, publication, filing, or synchronization stops at the tool handoff below.

## Active context

- Boot: three files
- Route packet: `runtime/packets/routes/resume--cover-letter.md` (4106 bytes)
- Profile packet: `runtime/packets/profiles/cover_letter.md` (740 bytes)
- Total active files: five

## Draft artifact

Dear Hiring Team,

I am applying for the Operations Coordinator role because it combines service delivery, records, and cross-team follow-through. My experience includes coordinating a high-volume intake process and supporting a team through changing priorities.

In my current position, I built a shared tracking routine that reduced unresolved handoffs and gave managers a reliable weekly view. I also supported the rollout of a revised customer process, documenting exceptions and helping colleagues adopt the change.

The role's emphasis on accurate communication and dependable execution matches the work I have delivered. I would welcome the opportunity to discuss how that evidence could support your team.

Sincerely,
Jordan Lee

## Gate report

**Structural preflight: Pass**

- Profile structure: required fields and form are present.
- Evidence: factual content remains explicitly classified as supplied fixture material; no independent verification is implied.
- Semantic finish: each section adds a fact, decision, mechanism, or reader capability.
- Form Lock: `adaptive` is preserved.

## Revision request

Clarify that this is the revised visible version without changing its evidence, structure, or approved terminology.

## Revised draft

Dear Hiring Team,

I am applying for the Operations Coordinator role because it combines service delivery, records, and cross-team follow-through. My experience includes coordinating a high-volume intake process and supporting a team through changing priorities.

In my current position, I built a shared tracking routine that reduced unresolved handoffs and gave managers a reliable weekly view. I also supported the rollout of a revised customer process, documenting exceptions and helping colleagues adopt the change.

The role's emphasis on accurate communication and dependable execution matches the work I have delivered. I would welcome the opportunity to discuss how that evidence could support your team.

Sincerely,
Jordan Lee

## Lifecycle state

```yaml
artifact_id: 26-resume-cover-letter
route: resume/cover-letter
profile: cover_letter
status: revised_draft
approval_record: null
human_approval_required: true
source_scope: evaluation_fixture
material_revision_requires_reapproval: true
```

## Tool handoff

The document is complete from supplied evidence. Listing verification and submission require external tools.
