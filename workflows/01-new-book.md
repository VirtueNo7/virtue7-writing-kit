# Workflow 1 - Create a New Book From Scratch

## Stage 0 - Welcome

Explain that the method will build the book in layers and that no manuscript will be generated until the foundation is inspectable.

Ask:

> What kind of book are you hoping to create, even if the idea is still rough?

Do not ask for title, audience, length, genre, and tone in the same message. Extract what is already present and ask only for the next missing decision.

## Stage 1 - Intent interview

Gather, one primary question per turn:

1. **Subject or central idea:** What is the book about?
2. **Reader change:** What should the reader understand, recognise, feel, decide, or do differently?
3. **Audience:** Who is it for, and what can they reasonably be expected to know?
4. **Governing relation:** Is the book organised by chronology, transformation, problem-solution, question-discovery, principle-application, cause-consequence, method, comparison, or another stable relation?
5. **Evidence and material:** Will it rely on lived experience, supplied documents, external research, interviews, fictional invention, technical evidence, or a mixture?
6. **Boundaries:** What should the book never claim, reveal, diagnose, imitate, or become?
7. **Reading experience:** Select useful qualities such as clear, intimate, analytical, narrative, practical, reflective, concise, or richly detailed.
8. **First target resolution:** concept, matrix, plan, short handbook, representative chapter, or full book.

Use defaults only when they are low-risk and reversible. Label them `Proposed default`.

## Stage 2 - Kernel gate

Create `templates/book-kernel.md` and show the complete kernel. Include unresolved questions. Run the kernel test from `architecture/02-canonical-kernel.md`.

Ask for approval or revision.

Do not proceed until the user approves the kernel or explicitly authorises provisional continuation.

## Stage 3 - Matrix gate

Create `templates/book-matrix.md`.

The matrix must:

- cover the complete reader promise;
- assign one clear responsibility to each unit;
- reveal sequence and relationships;
- identify evidence needs;
- identify likely duplication or gaps;
- remain readable at a glance.

Ask for approval or revision.

## Stage 4 - Plan gate

Create `templates/book-plan.md`.

Select one representative unit that best tests the book's hardest requirements. For a biography, this is usually a decisive period containing context, action, consequence, interpretation, and connection to the whole life.

Ask for approval or revision.

## Stage 5 - Representative unit

Research only under the agreed evidence policy. Create source and claim records before presenting factual prose as established.

Draft one complete unit at the intended publication quality. Validate:

- knowledge;
- narrative;
- mechanism or governing relation;
- evidence;
- reader value;
- voice;
- compression;
- read-aloud quality where relevant.

Record improvements before scaling.

## Stage 6 - Full production

Draft in controlled batches. At the end of each batch:

- update unit states;
- run consistency checks;
- update the source register;
- compress each completed unit;
- compare against the matrix;
- update `SESSION_STATE`.

## Stage 7 - Release

Run the complete validation workflow. Produce the publication package and unresolved-risk report.
