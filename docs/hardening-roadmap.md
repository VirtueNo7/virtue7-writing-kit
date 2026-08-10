# Hardening roadmap

This roadmap separates shipped evidence from future targets.

## Shipped in v0.5.0

- Exact-version human approval records bound to artifact SHA-256.
- Universal tool-receipt schema for tool-dependent completion claims.
- Explicit lifecycle transition registry and negative governance cases.
- Evidence attestations required for release-grade profile checks on evidence-sensitive forms.
- Canonical gate text and source hashes compiled into route packets.
- Deterministic ZIP metadata and cross-directory reproducibility testing.
- Namespaced extension manifest and channel-scoped personalization record.
- Generated examples left at `revised_draft`, never self-approved.

## Next targets

1. Make complete-book orchestration a first-class contract: book kernel, canon register, chapter dependency graph, continuity checks, batch approval, and publication package.
2. Run blinded semantic evaluation across multiple model families, with adjudication by reviewers who did not author the fixtures.
3. Replace lexical legal-context hints with structured jurisdiction and authority resolution plus live currency checks where tools are authorized.
4. Add cryptographic signatures or trusted attestations for approval actors and tool receipts. v0.5 binds hashes but does not authenticate identities.
5. Publish a fully hashed dependency lock strategy for every supported platform.

Exit criteria belong in tests and results, not release prose. A target becomes shipped only after its artifact exists, negative controls fail safely, positive controls pass, and the release report points to the generated evidence.

