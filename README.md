# Virtue7 Writing Kit

A portable, AI-guided method for creating a book from an initial idea, expanding it to the required depth, and collapsing it back to a reliable source of truth.

## Intended experience

1. Download the release ZIP.
2. Upload the ZIP to a file-capable AI system.
3. The AI reads `00_START_HERE.md` and presents the guided menu.
4. Choose the built-in demonstration or create a new book.

Some AI products do not inspect an archive until the user sends a message. In that case, send the single word `Begin`. If the platform still does not inspect the archive, send: `Read and run 00_START_HERE.md.` This is a platform limitation, not a new initiation ritual invented by the kit.

## What the kit does

- creates a canonical book kernel before large-scale drafting;
- represents the complete book as a compact matrix;
- expands the matrix into plans, handbook entries, chapters, and a full manuscript;
- collapses large outputs back into summaries, decision lines, and the kernel;
- separates facts, interpretations, sources, and narrative delivery;
- uses approval gates and round-trip validation to limit meaning drift;
- preserves a portable session state for continuation across AI systems;
- generates white-label books by default.

## Built-in test

The archive includes a completely fictional biography dossier about a master builder. The test requires no uploads, research, or personal information. It exists only to demonstrate the method.

## Repository and release

The GitHub repository is the development source. The downloadable ZIP is the user product. Generated books do not need to mention Virtue7 or the writing kit.

## Whitepaper

The original working whitepaper, *The Compressible Content Architecture: A System for Creating, Expanding, and Adapting Structured Knowledge*, is included in `docs/whitepaper/` as both the original PDF and an AI-readable text extraction.

## Version

`0.1.0` - initial guided release.
