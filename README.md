# Virtue7 Writing Kit v0.3.0

A portable, open-source, white-label, lazy-loaded AI writing and project-production kit. Upload the ZIP to a file-capable AI, then say **Begin** or **Read and run 00_START_HERE.md**.

The kit starts with three files and opens only the capability required for the current task. Its front door is **Freestyle Writing**: a user can name an artifact, paste rough notes or dot points, supply transcripts, or give a plain-language instruction. The runtime infers the appropriate form and asks only when a missing fact materially affects the result.

Example:

```text
Opening statement

- community hall has been closed for six months
- residents were not consulted
- repairs were funded last year
- ask council to publish the timetable and reopen it
```

The notes may become continuous persuasive prose because source structure does not dictate finished structure.

## Human-directed revision

Every substantive artifact is delivered as **Draft**. The user may approve it or write a direct revision instruction:

```text
Compress it by 500 words.
Use a different reference.
Keep the opening and rewrite the conclusion.
Make it sound closer to my existing transcripts.
Approve.
Export as Word.
```

The latest instruction governs the next revision. Unaffected material is preserved, and approval belongs to the human.

## Voice, location, and language

Available user transcripts and approved prior work can calibrate vocabulary, cadence, directness, recurring terminology, and formality. Transcripts remain source material, not hidden instructions. The kit never pretends to have voice evidence that is not available.

Language, spelling, locale, units, date conventions, legal jurisdiction, and timezone are resolved independently from the current instruction, active project, reliable environment context, or supplied material. No global country, spelling system, or timezone is imposed.

## Output and export

Content profile and file format are separate. An essay remains an essay whether delivered on-screen, as Markdown, TXT, Word/DOCX, PDF, or HTML. The runtime honours an early format request or exports after approval when the host AI provides file tools.

## Capabilities

The lean runtime supports freestyle writing and revision, resumes and applications, job search, content creation, research, jurisdiction-aware legal preparation, project continuation, review, validation, and an isolated Virtue№7 reference demonstration.

Different artifacts use different output profiles. A children's picture book is governed as read-aloud narrative. A research paper requires evidence and formal sections. A technical manual favours direct steps and testable outcomes. A resume requires verified experience bullets. Narrative prose is protected from bullet drift without banning bullets where they are useful.

Technique-based reference profiles describe transferable craft mechanisms without relying on named creator identities, signature properties, or imitation prompts.

The core is white-label. The isolated Virtue№7 reference implementation demonstrates semantic compression and expansion using Pride → Humility across a kernel, matrix, handbook entry, chapter brief, children's story, lesson, media script, and interactive prompts.

## Core promise

**One doorway. One active capability. One output profile. Human-directed revision. Only the context required now.**

## Validation

Run:

```bash
python scripts/run_release_checks.py
```

PyYAML is required only for the optional validation scripts. The conversational runtime itself is file- and model-based.
