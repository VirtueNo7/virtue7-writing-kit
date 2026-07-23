# Workflow 6 - Resume and Export

## Resume

1. Read the latest `SESSION_STATE`.
2. Read every artifact listed under `approved_artifacts`.
3. Confirm the current kernel version and invariant set.
4. Identify the last approved gate.
5. List unresolved decisions and source gaps.
6. Continue from the next action. Do not restart the project unless the user requests it.

When chat memory conflicts with the files, the approved files control.

## Export state

Produce an updated file using `templates/session-state.md` after each approval gate.

## Export project

When the AI system can create files, prepare:

```text
project/
├── README.md
├── canonical/
│   ├── book-kernel.md
│   ├── book-matrix.md
│   └── invariant-set.yaml
├── planning/
│   └── book-plan.md
├── units/
├── sources/
├── manuscript/
├── validation/
├── outputs/
└── SESSION_STATE.md
```

When file creation is unavailable, output each changed file in a separate fenced block with its exact relative path as the heading. Do not merge the canonical source and manuscript into one enormous document simply because the interface has a text box.
