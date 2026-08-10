# Session State

```yaml
project_id: ""
project_title: ""
kit_version: "0.5.0"
capability: ""
route: ""
profile: ""
form_lock: "adaptive | preserve_form | narrative_lock"
artifact_state: "draft | revision_requested | revised_draft | approved | exported | released"
approved_artifacts: []
last_approved_artifact:
  artifact_id: ""
  version: ""
  sha256: ""
  approval_record_id: ""

canonical:
  records: []
  approved_invariants: []

scope:
  active: "personal | role | organization | client | channel | project"
  profile_file: ""
  data_classification: ""

evidence:
  source_register: ""
  claim_register: ""
  unresolved_claim_ids: []

production:
  current_artifact: ""
  current_artifact_id: ""
  current_artifact_version: ""
  current_artifact_sha256: ""
  latest_draft: ""
  latest_gate_report: ""
  latest_revision_instruction: ""
  tool_receipt_ids: []

next_action: ""
unresolved_decisions: []
files_to_load_next: []
```
