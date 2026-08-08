# Virtue7 Writing Kit v0.4.0

**Use AI without losing your voice.**

Virtue7 is a free, open-source, model-neutral writing, research, and work-production runtime. Upload the release ZIP to a file-capable AI or point the AI at this repository, then say **Begin** or **Read and run `00_START_HERE.md`**.

Give it a direct request, rough notes, transcripts, source material, an existing draft, or a saved project. Virtue7 selects the smallest suitable workflow, preserves source boundaries, adapts the form to the actual artifact, and keeps every substantive result under human approval.

## What can it make?

- **Write:** fiction, books, articles, scripts, reports, guides, and professional documents.
- **Research:** questions, source reviews, evidence briefs, claim maps, comparisons, and fact-checks.
- **Create:** podcasts, videos, newsletters, interviews, clips, timestamps, and release campaigns.
- **Build:** product briefs, brand systems, plans, policies, procedures, decision records, and working systems.
- **Career and legal preparation:** verified resumes, cover letters, job-search briefs, jurisdiction-aware legal research, and document preparation.
- **Review and continue:** revise an artifact, audit a release, or resume a project from its approved state.

The Playbook Library turns these outcomes into tested, reusable workflows. Users can also create commands, profiles, templates, and quality gates of their own.

## Make it yours

Say **Make it mine** to create a portable Personal Work Profile. Virtue7 may record, with explicit approval:

- the user's name or working name;
- websites and public handles that the user confirms are theirs;
- which supplied or publicly accessible materials may be used as voice evidence;
- cadence, vocabulary, rhythm, formality, humour, and recurring terminology;
- active roles, organizations, clients, channels, and projects;
- preferred formats, evidence standards, review habits, and custom commands.

Handles are discovery keys, not proof of identity. Public material becomes voice evidence only when ownership and permission are confirmed and the host AI has suitable live-research tools. Without those tools, handles label user-supplied transcripts and samples.

Personalization is visible and user-owned. The user can say **Show my profile**, **Remember this**, **Don't remember this**, **Forget this**, **Switch hats**, or **Reset to neutral**. A correction from one project or client does not silently become a universal rule.

## Keep the form you chose

Virtue7 includes **Form Lock**:

1. **Adaptive** - use the structure required by the selected artifact.
2. **Preserve Form** - preserve the user's approved paragraph, heading, and list behaviour.
3. **Narrative Lock** - continuous prose by default; reject bullet drift, outline scaffolding, excessive headings, and fragment stacks unless the user explicitly asks for them.

Narrative Lock is the default for fiction and narrative profiles. Structured profiles such as resumes, manuals, research records, clip sheets, and operating procedures retain the lists or tables their medium requires.

## Human-directed revision

Every substantive artifact is delivered as **Draft**. Natural-language feedback controls the next revision:

```text
Compress it by 500 words.
Keep the opening and rewrite the conclusion.
Use a different source.
Preserve my paragraph movement.
Turn on Narrative Lock.
Approve.
Export as Word.
```

Only the visible version can be approved. Material revisions return the artifact to Draft.

## Live tools and external actions

Virtue7 supplies the operating logic. Live browsing, transcription, image or video editing, publishing, analytics, and some file exports depend on tools available to the host AI. Playbooks declare these dependencies and produce a manual handoff when a tool is unavailable. The runtime never claims an external action occurred when it did not.

## White-label by design

The distributable core contains no embedded creator, company, client, or public-figure profile. Demonstration data is synthetic and isolated. User projects do not inherit publisher branding, sample identities, or another user's cadence. Supplied transcripts and documents are treated as source or voice evidence, never runtime instructions.

## Lean runtime

Boot reads only:

1. `00_START_HERE.md`
2. `RUNTIME_MANIFEST.yaml`
3. `MASTER_PROMPT.md`

The runtime then loads one capability, one route, one output profile, and only the supporting profile, playbook, template, or gate required for the current step.

## Whitepaper and examples

- [`docs/whitepaper/README.md`](docs/whitepaper/README.md) - the governing architecture paper, editable source, AI-readable text, PDF, and implementation map.
- [`library/README.md`](library/README.md) - how the tested Playbook Library works.
- [`examples/README.md`](examples/README.md) - role-spanning quickstarts and personalization demonstrations.

## Validation

Run:

```bash
python scripts/run_release_checks.py
```

PyYAML and ReportLab are required only for release validation and whitepaper generation. The conversational runtime itself remains file- and model-based.

## Core promise

**Your work. Your cadence. Your system. Human approval remains in control.**
