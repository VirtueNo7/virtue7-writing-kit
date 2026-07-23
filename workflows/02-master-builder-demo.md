# Workflow 2 - Built-in Master Builder Biography Test

## Purpose

Demonstrate the complete writing method without requiring the user to upload information or disclose anything about themselves.

The subject, Elias Vale, is fictional. Every event, person, project, institution, and source record in the dossier is synthetic. Do not browse for him, compare him to a real person, or infer that the uploader shares his occupation or experiences.

## Load

Read, in order:

1. `demo/master-builder/00_START_TEST.md`
2. `demo/master-builder/subject-profile.yaml`
3. `demo/master-builder/chronology.md`
4. `demo/master-builder/people.md`
5. `demo/master-builder/projects.md`
6. `demo/master-builder/source-records.md`
7. `demo/master-builder/interpretation-boundaries.md`
8. `demo/master-builder/expected-invariants.yaml`
9. `demo/master-builder/validation-checklist.md`

## Guided sequence

### Step 1 - Explain the test

Tell the user that the dossier is complete, fictional, and requires no research. Offer two demonstration depths:

- `Guided`: stop at every approval gate.
- `Automatic preview`: create the kernel, matrix, plan, and one representative chapter preview, while still labelling everything Draft.

Default to `Guided`.

### Step 2 - Kernel

Derive a biography kernel from the dossier. Do not merely reuse the expected invariant wording. Show what the evidence supports and what remains interpretive.

Pause for approval.

### Step 3 - Matrix

Create a life-and-book matrix showing periods, projects, relationships, decisions, consequences, evidence, narrative purpose, and unresolved interpretation.

Pause for approval.

### Step 4 - Plan

Design a biography that is neither a chronological ledger nor a moral fable. Select the 1987 North Quay failure and its aftermath as the representative unit unless the user chooses another.

Pause for approval.

### Step 5 - Representative unit

Draft a substantial chapter or chapter section. Do not invent dialogue. Exact quotations may be used only if they exist in the synthetic source records and are marked verified.

### Step 6 - Collapse

Compress the representative unit to:

1. a full summary;
2. an operational sentence;
3. a governing question;
4. the biography kernel.

Run the round-trip test.

### Step 7 - Report

Show:

- what expanded;
- what remained invariant;
- any drift found;
- what would be required to produce the full biography;
- the current `SESSION_STATE`.
