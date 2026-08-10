# Worked example: Source Review

## User request

Classify the supplied sources and map each material claim to support, contradiction, and limitation.

## Fixture and source boundary

- The complete artifact below is a reproducible evaluation fixture supplied to this example.
- Its factual content is treated as fixture input, not as independently verified or current information.
- No browsing, private memory, external action, or real-user data is claimed.

## Runtime selection

| Field | Selection |
|---|---|
| Capability | `research` |
| Route | `research/source-review` |
| Profile | `fact_check_report` |
| Form Lock | `preserve_form` |
| Related playbooks | `research/source-map`, `research/claim-ledger` |

## Route conformance illustration

**Outcome:** contract conformance is illustrated with a synthetic fixture; this is not proof of a model run or external action.

**Route contract applied:** Collect and classify sources. Record authority, date, relevance, claim support, limitations, conflicts, rights, and verification state. Prefer claim-level mapping over bibliography theatre.

**Source handling:** the fixture is the complete supplied record. Any request requiring live discovery, currency, verification, publication, filing, or synchronization stops at the tool handoff below.

## Active context

- Boot: three files
- Route packet: `runtime/packets/routes/research--source-review.md` (4068 bytes)
- Profile packet: `runtime/packets/profiles/fact_check_report.md` (984 bytes)
- Total active files: five

## Draft artifact

# Fact Check: Did the Pilot Cut Contacts in Half?

## Question
Did the 2025 guided-setup pilot reduce repeat contacts by fifty percent?

## Methodology
Compare the dated 2025 pilot report with the 2024 baseline and the 2026 correction note.

## Findings
The verified fact is that contacts fell during the pilot. The fifty-percent figure is a credible report based on a filtered subset.

## Claim Statuses
- Verified fact: total contacts declined.
- Credible report: the filtered group declined by fifty percent.
- Interpretation: the guide caused the entire decline.
- Unknown: the effect after the pilot window.

## Contradictions
The correction note excludes two support queues included in the baseline.

## Limitations
The sources do not isolate seasonality.

## Conclusion
The broad claim is not verified; a narrower reported result is supported.

## Sources
- 2024 baseline report.
- 2025 pilot analysis.
- 2026 correction note.

## Gate report

**Structural preflight: Pass**

- Profile structure: required fields and form are present.
- Evidence: factual content remains explicitly classified as supplied fixture material; no independent verification is implied.
- Semantic finish: each section adds a fact, decision, mechanism, or reader capability.
- Form Lock: `preserve_form` is preserved.

## Revision request

Clarify that this is the revised visible version without changing its evidence, structure, or approved terminology.

## Revised draft

# Revised: Fact Check: Did the Pilot Cut Contacts in Half?

## Question
Did the 2025 guided-setup pilot reduce repeat contacts by fifty percent?

## Methodology
Compare the dated 2025 pilot report with the 2024 baseline and the 2026 correction note.

## Findings
The verified fact is that contacts fell during the pilot. The fifty-percent figure is a credible report based on a filtered subset.

## Claim Statuses
- Verified fact: total contacts declined.
- Credible report: the filtered group declined by fifty percent.
- Interpretation: the guide caused the entire decline.
- Unknown: the effect after the pilot window.

## Contradictions
The correction note excludes two support queues included in the baseline.

## Limitations
The sources do not isolate seasonality.

## Conclusion
The broad claim is not verified; a narrower reported result is supported.

## Sources
- 2024 baseline report.
- 2025 pilot analysis.
- 2026 correction note.

## Lifecycle state

```yaml
artifact_id: 24-research-source-review
route: research/source-review
profile: fact_check_report
status: revised_draft
approval_record: null
human_approval_required: true
source_scope: evaluation_fixture
material_revision_requires_reapproval: true
```

## Tool handoff

Analysis of supplied sources is complete. Discovery and current verification require live research.
