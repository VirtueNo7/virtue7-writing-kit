# Worked example: Search Jobs

## User request

Create a current, verifiable job-search brief for operations roles matching the supplied constraints.

## Fixture and source boundary

- The complete artifact below is a reproducible evaluation fixture supplied to this example.
- Its factual content is treated as fixture input, not as independently verified or current information.
- No browsing, private memory, external action, or real-user data is claimed.

## Runtime selection

| Field | Selection |
|---|---|
| Capability | `job-search` |
| Route | `job-search/search` |
| Profile | `job_search_brief` |
| Form Lock | `adaptive` |
| Related playbooks | `career/opportunity-search` |

## Route conformance illustration

**Outcome:** contract conformance is illustrated with a synthetic fixture; this is not proof of a model run or external action.

**Route contract applied:** Resolve location and role constraints. Retrieve current postings from approved sources. Record title, employer, location, work arrangement, employment type, compensation when supplied, date, source, and application URL.

**Source handling:** the fixture is the complete supplied record. Any request requiring live discovery, currency, verification, publication, filing, or synchronization stops at the tool handoff below.

## Active context

- Boot: three files
- Route packet: `runtime/packets/routes/job-search--search.md` (4157 bytes)
- Profile packet: `runtime/packets/profiles/job_search_brief.md` (884 bytes)
- Total active files: five

## Draft artifact

# Qualified Job Search Brief

Search target: Remote or Seattle-area operations coordination roles requiring scheduling, customer communication, process documentation, and cross-team follow-through.

## Strong Match

### Operations Coordinator — Example Facilities Group

- Work arrangement: Hybrid, Seattle
- Employment type: Full time
- Match rationale: Strong overlap with dispatch, vendor coordination, reporting, and customer updates.
- Verification needed: Confirm salary range and weekend rotation before applying.
- Recommended action: Tailor the résumé around scheduling scale, return-visit reduction, and service-recovery experience.

### Customer Operations Specialist — Example Software Company

- Work arrangement: Remote within the United States
- Employment type: Full time
- Match rationale: Transferable experience in issue triage, customer communication, records, and workflow ownership.
- Verification needed: Determine whether direct software-support experience is mandatory or preferred.
- Recommended action: Emphasize process learning, documentation accuracy, and cross-functional escalation.

## Possible Match

### Project Administrator — Example Construction Services

- Work arrangement: On-site, Bellevue
- Employment type: Contract
- Match rationale: Relevant construction-office administration, supplier communication, invoice checks, and handover documentation.
- Constraint: Commute and contract status may reduce suitability.
- Recommended action: Apply only if compensation and contract duration justify the travel.

## Next Step

Select one role for a deeper qualification check. The selected posting should be converted into a compact job evidence packet before the résumé capability loads.

## Gate report

**Structural preflight: Pass**

- Profile structure: required fields and form are present.
- Evidence: factual content remains explicitly classified as supplied fixture material; no independent verification is implied.
- Semantic finish: each section adds a fact, decision, mechanism, or reader capability.
- Form Lock: `adaptive` is preserved.

## Revision request

Clarify that this is the revised visible version without changing its evidence, structure, or approved terminology.

## Revised draft

# Revised: Qualified Job Search Brief

Search target: Remote or Seattle-area operations coordination roles requiring scheduling, customer communication, process documentation, and cross-team follow-through.

## Strong Match

### Operations Coordinator — Example Facilities Group

- Work arrangement: Hybrid, Seattle
- Employment type: Full time
- Match rationale: Strong overlap with dispatch, vendor coordination, reporting, and customer updates.
- Verification needed: Confirm salary range and weekend rotation before applying.
- Recommended action: Tailor the résumé around scheduling scale, return-visit reduction, and service-recovery experience.

### Customer Operations Specialist — Example Software Company

- Work arrangement: Remote within the United States
- Employment type: Full time
- Match rationale: Transferable experience in issue triage, customer communication, records, and workflow ownership.
- Verification needed: Determine whether direct software-support experience is mandatory or preferred.
- Recommended action: Emphasize process learning, documentation accuracy, and cross-functional escalation.

## Possible Match

### Project Administrator — Example Construction Services

- Work arrangement: On-site, Bellevue
- Employment type: Contract
- Match rationale: Relevant construction-office administration, supplier communication, invoice checks, and handover documentation.
- Constraint: Commute and contract status may reduce suitability.
- Recommended action: Apply only if compensation and contract duration justify the travel.

## Next Step

Select one role for a deeper qualification check. The selected posting should be converted into a compact job evidence packet before the résumé capability loads.

## Lifecycle state

```yaml
artifact_id: 12-job-search-search
route: job-search/search
profile: job_search_brief
status: revised_draft
approval_record: null
human_approval_required: true
source_scope: evaluation_fixture
material_revision_requires_reapproval: true
```

## Tool handoff

The structure is complete. Current listing discovery and verification require live browsing.
