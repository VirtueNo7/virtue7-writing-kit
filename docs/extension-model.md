# Extension model

Virtue7 v0.5.0 defines a public compatibility boundary in [`schemas/extension-manifest.schema.json`](../schemas/extension-manifest.schema.json). An extension declares its namespace, identifier, semantic version, required Virtue7 version, registered components, and requested tool, data-scope, and external-action permissions.

## Rules

1. Use a reverse-domain-style namespace that the extension owner controls.
2. Register capability, route, profile, gate, and template identifiers without shadowing core identifiers.
3. Set `replaces_core_components: false`. Replacement is prohibited by the v0.5 contract.
4. Declare the narrowest tool, data-scope, and external-action permissions. A declaration describes need; the host and human still authorize use.
5. Preserve canonical artifact states, evidence classes, approval binding, and tool receipts at extension boundaries.
6. Pass compact records across boundaries rather than private runtime context.

The starter record is [`templates/extension-manifest.yaml`](../templates/extension-manifest.yaml), and the release suite validates [`tests/contracts/extension-manifest.json`](../tests/contracts/extension-manifest.json). The schema establishes compatibility shape; it is not a plugin loader, sandbox, signature system, or security certification.

Private applications may implement orchestration behind this contract. Their code, datasets, briefs, customer records, and business rules are outside the public foundation and must not be copied into an extension manifest or public example.

