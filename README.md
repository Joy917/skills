# Skills

[简体中文](README.zh-CN.md)

A curated set of skills I personally use in the AI era. Most are mine; some are adapted from others. All are battle-tested in my daily workflow.

These are not one-line prompts. Each skill is a workflow I keep coming back to — extracted, packaged, and shipped so others can adopt them without rebuilding from scratch.

---

## Why these skills?

Most skill collections are mirrors of upstream. This one is different:

- **Filtered by use, not by fame.** A skill only makes it here after I have used it on real work for at least a month. If it sits in my skills folder unused, it doesn't ship.
- **Honest about provenance.** Most skills in this repo are mine — built from workflows I kept coming back to. A few are inspired by or adapted from open-source work by others; when that's the case, the `SKILL.md` credits the original. Nothing is rebranded as "all original" when it isn't.
- **Runnable without me.** No personal paths, no private API keys, no "ask Joy for the spreadsheet." Every skill works on a clean machine.
- **Opinionated.** Generic advice is useless. Each skill has a point of view and tells you when to override it.
- **Privacy-first**: personal paths, API keys, tokens, and identifying info are stripped before publication. If you find anything sensitive, open an issue.

> **AI is a force multiplier, not a substitute for thinking.** These skills are designed to sharpen your judgment, not replace it. The best output still comes from a person who knows what they want and why.

---

## Skills

| Skill | What it does | When to use |
|---|---|---|
| [product-judgment](./skills/product-judgment) | Build product sense — the ability to decide which features matter, which buttons users actually need, and whether a request is a real need or a "nice to have" | When you're a PM, founder, designer, or dev making a product call and want a thinking partner |

More skills are in the pipeline. They ship here only after they've earned a place in my daily workflow.

---

## Quick install

**Prerequisites**

- An agent that supports the skills standard: Claude Code, Hermes Agent, or any compatible runtime.
- A `~/.claude/skills/` or `~/.hermes/skills/` directory. Most agents create this on first run.

**Install a single skill**

```bash
# Clone the whole repo
git clone https://github.com/Joy917/skills.git
cd skills

# Copy the skill you want
cp -r skills/product-judgment ~/.hermes/skills/
# or
cp -r skills/product-judgment ~/.claude/skills/
```

**Install all skills**

```bash
cp -r skills/* ~/.hermes/skills/
```

Most agents auto-discover skills in the standard `skills/` directory under your home. Restart the agent to pick up new skills.

---

## Philosophy

A skill makes the cut only if it passes all four of these:

1. **Solves a real problem I had.** If I built it, I needed it. No "skills for skills' sake."
2. **Not a one-line prompt.** If the whole value is the prompt, it's not a skill — it's a one-liner. Skills are for workflows that need a framework, a checklist, or references.
3. **Runnable without me.** Every skill works on a clean machine. No personal paths, no private API keys, no "ask Joy for the spreadsheet."
4. **Be opinionated.** Generic advice is useless. Each skill has a point of view.

If a skill fails any of these, it stays in my local skills folder. It doesn't ship.

---

## How to contribute

Issues and PRs are welcome. If you have a skill you've built and want to add it here:

1. **Open an issue first** — describe the problem the skill solves and why it should be a skill (not a prompt).
2. **Keep the structure** — `skills/<name>/SKILL.md` plus optional `references/`, `scripts/`, `assets/`.
3. **Make sure your skill works on a clean machine** with no personal paths or private credentials.

> This is a personal curation, not a marketplace. I'll review every submission and may decline ones that don't match the philosophy above. That's not a rejection of you — it's a refusal to dilute the signal.

---

## License

MIT. See [LICENSE](./LICENSE).

Use it, fork it, learn from it. If you ship something inspired by these skills, I'd love to hear about it.
