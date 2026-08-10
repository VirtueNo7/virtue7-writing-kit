# Worked example: Evidence Brief

## User request

Produce a decision-ready evidence brief that does not exceed the supplied record.

## Fixture and source boundary

- The complete artifact below is a reproducible evaluation fixture supplied to this example.
- Its factual content is treated as fixture input, not as independently verified or current information.
- No browsing, private memory, external action, or real-user data is claimed.

## Runtime selection

| Field | Selection |
|---|---|
| Capability | `research` |
| Route | `research/evidence-brief` |
| Profile | `business_report` |
| Form Lock | `adaptive` |
| Related playbooks | `creator/topic-radar`, `research/timeline-reconstruction`, `research/decision-brief`, `product/feedback-synthesis`, `company_admin/incident-record` |

## Route conformance illustration

**Outcome:** contract conformance is illustrated with a synthetic fixture; this is not proof of a model run or external action.

**Route contract applied:** Synthesize the evidence with clear sections for question, method, evidence, interpretation, limitations, conclusion, and sources. Do not exceed what the source record supports.

**Source handling:** the fixture is the complete supplied record. Any request requiring live discovery, currency, verification, publication, filing, or synchronization stops at the tool handoff below.

## Active context

- Boot: three files
- Route packet: `runtime/packets/routes/research--evidence-brief.md` (4057 bytes)
- Profile packet: `runtime/packets/profiles/business_report.md` (789 bytes)
- Total active files: five

## Draft artifact

# Service Intake Review

## Executive Summary

Support data and interview evidence show that configuration questions create avoidable repeat contacts. The decision is whether to improve onboarding before adding more support capacity.

## Findings

The source data records 126 repeat contacts in the quarter. Interviews identify unclear ownership and inconsistent setup language as the common causes.

## Implications

Additional staffing would absorb demand without removing its source. A guided setup check could reduce demand while preserving an escalation path for complex cases.

## Recommendation

Recommend a four-week pilot for the guided check. The next step is to approve an owner, baseline the repeat-contact rate, and review the result before wider release.

## Gate report

**Structural preflight: Pass**

- Profile structure: required fields and form are present.
- Evidence: factual content remains explicitly classified as supplied fixture material; no independent verification is implied.
- Semantic finish: each section adds a fact, decision, mechanism, or reader capability.
- Form Lock: `adaptive` is preserved.

## Revision request

Clarify that this is the revised visible version without changing its evidence, structure, or approved terminology.

## Revised draft

# Revised: Service Intake Review

## Executive Summary

Support data and interview evidence show that configuration questions create avoidable repeat contacts. The decision is whether to improve onboarding before adding more support capacity.

## Findings

The source data records 126 repeat contacts in the quarter. Interviews identify unclear ownership and inconsistent setup language as the common causes.

## Implications

Additional staffing would absorb demand without removing its source. A guided setup check could reduce demand while preserving an escalation path for complex cases.

## Recommendation

Recommend a four-week pilot for the guided check. The next step is to approve an owner, baseline the repeat-contact rate, and review the result before wider release.

## Lifecycle state

```yaml
artifact_id: 22-research-evidence-brief
route: research/evidence-brief
profile: business_report
status: revised_draft
approval_record: null
human_approval_required: true
source_scope: evaluation_fixture
material_revision_requires_reapproval: true
```

## Tool handoff

Analysis of supplied sources is complete. Discovery and current verification require live research.
