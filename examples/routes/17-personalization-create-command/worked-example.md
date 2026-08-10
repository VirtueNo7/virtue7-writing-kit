# Worked example: Create a Custom Command

## User request

Turn this recurring operating process into a transparent custom command with inputs, gates, and a completion test.

## Fixture and source boundary

- The complete artifact below is a reproducible evaluation fixture supplied to this example.
- Its factual content is treated as fixture input, not as independently verified or current information.
- No browsing, private memory, external action, or real-user data is claimed.

## Runtime selection

| Field | Selection |
|---|---|
| Capability | `personalization` |
| Route | `personalization/create-command` |
| Profile | `standard_operating_procedure` |
| Form Lock | `preserve_form` |
| Related playbooks | Route-native example |

## Route conformance illustration

**Outcome:** contract conformance is illustrated with a synthetic fixture; this is not proof of a model run or external action.

**Route contract applied:** Ask for the command name, outcome, required inputs, closest existing playbook, required content, prohibited outcomes, tools, risk, and completion test. Create a transparent command record that routes through the existing runtime. A custom command cannot bypass evidence, privacy, professional-scope, approval, or release gates.

**Source handling:** the fixture is the complete supplied record. Any request requiring live discovery, currency, verification, publication, filing, or synchronization stops at the tool handoff below.

## Active context

- Boot: three files
- Route packet: `runtime/packets/routes/personalization--create-command.md` (4716 bytes)
- Profile packet: `runtime/packets/profiles/standard_operating_procedure.md` (972 bytes)
- Total active files: five

## Draft artifact

# Equipment Return Procedure

## Purpose

Return issued equipment securely and create an auditable completion record.

## Scope

This procedure applies to all issued devices returned after replacement or role change.

## Prerequisites

- Approved return request
- Device identifier
- Secure intake location

## Roles

- The requester delivers the device.
- The intake owner verifies identity and condition.
- The system administrator confirms data handling.

## Procedure

1. The intake owner confirms the request and matches the device identifier.
2. Record physical condition before changing the device.
3. Place the device in the controlled intake area.
4. The system administrator verifies backup or approved data destruction.
5. Update the asset register and close the return request.
6. Send the requester the completion record.

## Decision Points

If the identifier does not match, stop and escalate before accepting custody.

## Exceptions

Damaged or inaccessible devices follow the incident process before normal intake continues.

## Controls

Two-person verification is required when the device contains restricted data.

## Records

The closed request and updated asset register are the evidence of completion.

## Escalation

The intake owner escalates mismatches to the operations manager and system owner.

## Review

The procedure owner reviews the process every six months and after any control failure.

## Gate report

**Structural preflight: Pass**

- Profile structure: required fields and form are present.
- Evidence: factual content remains explicitly classified as supplied fixture material; no independent verification is implied.
- Semantic finish: each section adds a fact, decision, mechanism, or reader capability.
- Form Lock: `preserve_form` is preserved.

## Revision request

Clarify that this is the revised visible version without changing its evidence, structure, or approved terminology.

## Revised draft

# Revised: Equipment Return Procedure

## Purpose

Return issued equipment securely and create an auditable completion record.

## Scope

This procedure applies to all issued devices returned after replacement or role change.

## Prerequisites

- Approved return request
- Device identifier
- Secure intake location

## Roles

- The requester delivers the device.
- The intake owner verifies identity and condition.
- The system administrator confirms data handling.

## Procedure

1. The intake owner confirms the request and matches the device identifier.
2. Record physical condition before changing the device.
3. Place the device in the controlled intake area.
4. The system administrator verifies backup or approved data destruction.
5. Update the asset register and close the return request.
6. Send the requester the completion record.

## Decision Points

If the identifier does not match, stop and escalate before accepting custody.

## Exceptions

Damaged or inaccessible devices follow the incident process before normal intake continues.

## Controls

Two-person verification is required when the device contains restricted data.

## Records

The closed request and updated asset register are the evidence of completion.

## Escalation

The intake owner escalates mismatches to the operations manager and system owner.

## Review

The procedure owner reviews the process every six months and after any control failure.

## Lifecycle state

```yaml
artifact_id: 17-personalization-create-command
route: personalization/create-command
profile: standard_operating_procedure
status: revised_draft
approval_record: null
human_approval_required: true
source_scope: evaluation_fixture
material_revision_requires_reapproval: true
```

## Tool handoff

The scoped record is complete. Public-source retrieval requires permission and a live research tool.
