# arabic-editorial-infographic

A [Claude](https://claude.com/claude-code) skill that turns copy into vertical **RTL Arabic
editorial infographic** posters and carousels, in the style of a curated Saudi/Gulf design
reference (national, economic, tourism, religious, and human-interest posters).

It **preserves your copy verbatim** (no rewrite/translation unless you ask), organizes it
into an editorial layout, and emits **three outputs per panel**:

- **(a) Copy organization** — your text mapped to slots, verbatim.
- **(b) Scene-only background prompt** — a text-free background plate (recommended: typeset
  the Arabic afterward in a real RTL editor).
- **(c) Combined prompt** — scene + exact Arabic text in one image-gen prompt (preview; long
  Arabic often garbles in image models).

## Files
- [`SKILL.md`](SKILL.md) — the workflow, modes, guardrails.
- [`references/design-system.md`](references/design-system.md) — archetypes, palettes, layout
  grid, deterministic decision table, typography, RTL/numeral rules.
- [`references/prompt-template.md`](references/prompt-template.md) — prompt skeletons
  (combined, scene-only, cover) + worked examples.

## Install
Copy this folder into your Claude skills directory:

```bash
git clone https://github.com/elmarakpy/arabic-editorial-infographic.git \
  ~/.claude/skills/arabic-editorial-infographic
```

Then invoke it with `/arabic-editorial-infographic` or by asking Claude to turn copy into an
Arabic infographic.
