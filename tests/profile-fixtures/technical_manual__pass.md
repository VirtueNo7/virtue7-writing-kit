# Design a Clear Settings Screen

A settings screen should help people understand what they can change, what each change affects, and whether the change took effect. Keep the screen focused. Remove controls that belong in the main task flow or that most people never need.

## Organize by purpose

Group settings according to the outcome people expect, not the subsystem that implements them. Use familiar labels and keep the same term everywhere it appears.

- Put the most commonly changed settings first.
- Separate account, notification, privacy, and appearance controls when they serve different goals.
- Avoid a miscellaneous group. It usually hides an unresolved information structure.
- Keep destructive actions visually and spatially separate from routine preferences.

## Write direct labels

Use short labels that name the setting or the action. Supporting text should explain consequences that are not obvious from the label.

Prefer:

- “Download over Wi-Fi”
- “Share activity status”
- “Delete account”

Avoid labels such as “Advanced options,” “Proceed,” or “Enable functionality.” They make people translate the interface before they can use it.

## Show the result

When a setting changes immediately, preserve the person’s place and provide quiet confirmation through the updated control or nearby content. When a change requires another step, explain that requirement before the person commits.

For a setting that cannot be changed, state why and identify the action that can resolve it. Do not present an inactive control without an explanation.

## Check accessibility and localization

Before release:

1. Increase text size and confirm that labels remain readable without truncating essential meaning.
2. Navigate with assistive technology and verify that each control has a useful name, value, and state.
3. Test translated strings that are substantially longer than the source language.
4. Confirm that color is not the only signal for selection, warning, or status.
5. Review terminology for jargon, idioms, and culture-specific assumptions.

A successful settings screen feels predictable. People can scan it, understand it, make a change, and return to their original task without having to learn how the product is built.
