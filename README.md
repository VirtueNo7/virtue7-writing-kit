# Virtue7 Writing Kit v0.5.0

**Use AI without losing your voice, evidence, form, or control.**

Virtue7 Writing Kit is a lightweight, model-neutral writing runtime for **Chat, Content, and bounded Automation**. It combines task-first routing, selective context loading, evidence discipline, optional scoped personalization, output profiles, Form Lock, exact artifact approval, and tool-truth controls.

This public release stays focused on governed writing, research, content creation, career materials, job search, legal preparation, continuation, review, and bounded automation.

## Boot

```text
# What are we doing now?

1. **Chat**
2. **Create content**
3. **Automate a task**

Or tell me what you want to make or do.
```

A substantive request skips the menu. A request only to open, read, load, start, initialize, or boot the package is activation and shows the menu exactly. Chat stays conversational. Content ends in an artifact. Automation ends in a terminal task state.

## What v0.5.0 adds over v0.4.0

- A compact mode-first boot that separates conversation, artifact creation, and bounded automation.
- Compiled route and profile packets for minimum-sufficient loading.
- Stronger artifact lifecycle records, exact approval binding, and tool receipts.
- Canonical taxonomy and gate registries plus deterministic release validation.
- A complete worked-example library across every shipped route and every governance failure/repair case.
- A `spoken_argument` output profile for oral advocacy and presentation-ready prose.
- A prose-structure safeguard that blocks pseudo-lists: short points must become developed prose or actual list items.

## Shipped capability set

The runtime contains 9 capability modules and 35 routes: Personalization, Writing, Content Creator, Research, Resume/Career Materials, Job Search, Legal Preparation, Continuation, and Review. These capabilities sit below the three operating modes rather than appearing as a giant boot menu.

## Worked examples and validation

The generated example library covers all 35 shipped routes plus deterministic failure-and-repair cases. Profile validation covers all 24 output profiles with paired passing and blocking fixtures. Governance checks cover privacy boundaries, tool truth, form drift, pseudo-list drift, career evidence, legal context, claim status, cadence authorization, approval binding, and release lifecycle controls.

Structural automation is a guardrail, not proof of factual or semantic correctness. Independent source verification and human review remain necessary where the stakes require them.

## Collapsible, extendable, reversible

- **Collapsible:** substantial work returns to meaning, evidence, decisions, dependencies, qualifications, and unresolved questions.
- **Extendable:** approved state can generate depth, formats, audiences, briefs, and form-native projections without inventing evidence.
- **Reversible:** artifact records preserve lineage, versions, lifecycle state, and human authority. Reversibility is semantic, not necessarily word-for-word.

## Personalization and form

`Make it mine` creates visible, user-owned profiles across personal, role, organization, client, channel, and project scopes. A public handle is a discovery key, not proof of identity or permission. Form Lock supports `adaptive`, `preserve_form`, and `narrative_lock`.

For prose-led outputs, Narrative Lock also rejects **pseudo-lists**: successive short standalone paragraphs that merely enumerate points. Those ideas must be developed and connected in prose or formatted as explicit bullets or numbered items when lists are appropriate.

## Approval, tools, and truth

The lifecycle is `draft -> revision_requested -> revised_draft -> approved -> exported -> released`.

Approval is valid only when a human event records the exact artifact identifier, version, and SHA-256. A material revision requires approval again.

Reasoning over supplied material, structuring, drafting, revision, and review are native. Browsing, retrieval, OCR, transcription, editing, file generation, analytics, publishing, filing, deployment, and workflow actions require actual tools and authorization. A tool-dependent action can be called complete only with a schema-valid receipt for the exact target.

## Release package

The public source release is `virtue7-writing-kit_v0.5.0.zip` with a SHA-256 checksum.

## Validation

```bash
python -m pip install -r requirements-dev.txt
python scripts/run_release_checks.py
```

Checks cover runtime packet fidelity, schemas, profiles, adversarial and governance cases, examples, local links, file-manifest integrity, white-label hygiene, whitepaper generation, boot behavior, and deterministic archives.

## Documentation

- [Quickstart](docs/quickstart.md)
- [Product foundation](docs/product-foundation.md)
- [Architecture](docs/architecture.md)
- [Extension model](docs/extension-model.md)
- [Hardening roadmap](docs/hardening-roadmap.md)
- [Engineering case study](docs/case-study.md)
- [Whitepaper](docs/whitepaper/README.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)

## License

Virtue7 Writing Kit is released under the [MIT License](LICENSE).

**Your work. Your cadence. Your system. Human approval remains in control.**
