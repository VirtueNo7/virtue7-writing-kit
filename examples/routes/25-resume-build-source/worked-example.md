# Worked example: Build Resume Source

## User request

Build a verified career source from these records without polishing unknowns into achievements.

## Fixture and source boundary

- The complete artifact below is a reproducible evaluation fixture supplied to this example.
- Its factual content is treated as fixture input, not as independently verified or current information.
- No browsing, private memory, external action, or real-user data is claimed.

## Runtime selection

| Field | Selection |
|---|---|
| Capability | `resume` |
| Route | `resume/build-source` |
| Profile | `resume` |
| Form Lock | `adaptive` |
| Related playbooks | `career/evidence-inventory` |

## Route conformance illustration

**Outcome:** contract conformance is illustrated with a synthetic fixture; this is not proof of a model run or external action.

**Route contract applied:** Request or locate the base resume. Convert it into a verified source record containing chronology, roles, duties, achievements, qualifications, skills, and unresolved fields. Do not polish unknowns into facts.

**Source handling:** the fixture is the complete supplied record. Any request requiring live discovery, currency, verification, publication, filing, or synchronization stops at the tool handoff below.

## Active context

- Boot: three files
- Route packet: `runtime/packets/routes/resume--build-source.md` (4104 bytes)
- Profile packet: `runtime/packets/profiles/resume.md` (819 bytes)
- Total active files: five

## Draft artifact

# Jordan Lee

Seattle, WA | jordan.lee@example.com | 555-010-2400

## Professional Summary

Operations coordinator with five years of experience improving scheduling, customer communication, vendor coordination, and process documentation in fast-moving service environments. Known for turning incomplete information into clear work plans and maintaining reliable follow-through across teams.

## Core Skills

- Workflow coordination
- Customer communication
- Calendar and schedule management
- Vendor and contractor liaison
- Process documentation
- Spreadsheet reporting
- Issue triage
- Quality control

## Professional Experience

### Operations Coordinator | Northline Services | 2022–Present

- Coordinate daily schedules for 18 field employees across residential and commercial service appointments.
- Reworked the dispatch checklist, reducing avoidable return visits by 17 percent over six months.
- Maintain customer updates from booking through completion and document unresolved issues for management review.
- Prepare weekly reports covering workload, cancellations, delays, and service-recovery actions.
- Train new coordinators on scheduling standards, escalation rules, and customer-record accuracy.

### Administrative Assistant | Harbor Works | 2019–2022

- Managed calendars, purchase records, supplier communication, and job-file documentation for a small construction office.
- Introduced a shared status tracker that replaced separate email chains and improved visibility across active jobs.
- Verified invoices against purchase orders and raised discrepancies before payment.
- Prepared client handover folders containing warranties, permits, and completion records.

## Education

Certificate in Business Administration | Cascadia College | 2019

## Gate report

**Structural preflight: Pass**

- Profile structure: required fields and form are present.
- Evidence: factual content remains explicitly classified as supplied fixture material; no independent verification is implied.
- Semantic finish: each section adds a fact, decision, mechanism, or reader capability.
- Form Lock: `adaptive` is preserved.

## Revision request

Clarify that this is the revised visible version without changing its evidence, structure, or approved terminology.

## Revised draft

# Revised: Jordan Lee

Seattle, WA | jordan.lee@example.com | 555-010-2400

## Professional Summary

Operations coordinator with five years of experience improving scheduling, customer communication, vendor coordination, and process documentation in fast-moving service environments. Known for turning incomplete information into clear work plans and maintaining reliable follow-through across teams.

## Core Skills

- Workflow coordination
- Customer communication
- Calendar and schedule management
- Vendor and contractor liaison
- Process documentation
- Spreadsheet reporting
- Issue triage
- Quality control

## Professional Experience

### Operations Coordinator | Northline Services | 2022–Present

- Coordinate daily schedules for 18 field employees across residential and commercial service appointments.
- Reworked the dispatch checklist, reducing avoidable return visits by 17 percent over six months.
- Maintain customer updates from booking through completion and document unresolved issues for management review.
- Prepare weekly reports covering workload, cancellations, delays, and service-recovery actions.
- Train new coordinators on scheduling standards, escalation rules, and customer-record accuracy.

### Administrative Assistant | Harbor Works | 2019–2022

- Managed calendars, purchase records, supplier communication, and job-file documentation for a small construction office.
- Introduced a shared status tracker that replaced separate email chains and improved visibility across active jobs.
- Verified invoices against purchase orders and raised discrepancies before payment.
- Prepared client handover folders containing warranties, permits, and completion records.

## Education

Certificate in Business Administration | Cascadia College | 2019

## Lifecycle state

```yaml
artifact_id: 25-resume-build-source
route: resume/build-source
profile: resume
status: revised_draft
approval_record: null
human_approval_required: true
source_scope: evaluation_fixture
material_revision_requires_reapproval: true
```

## Tool handoff

The document is complete from supplied evidence. Listing verification and submission require external tools.
