# enjoy-skills

Curated collection of Agent / Claude skills I built and use daily. Every skill here was extracted from a real workflow I kept coming back to.

## Skills

| Skill | What it does | When to use |
|---|---|---|
| [product-judgment](./skills/product-judgment) | Train product sense — the ability to make good calls about features, priorities, and real vs. fake needs | When you're a PM, founder, designer, or dev making a product call and want a thinking partner |

## Philosophy

A skill should:

1. **Solve a real problem I had.** If I built it, I needed it. No "skills for skills' sake."
2. **Not be a one-line prompt.** If the whole value is the prompt, it's not a skill — it's a one-liner. Skills are for workflows that need a framework, a checklist, or references.
3. **Be runnable without me.** Every skill works on a clean machine. No personal paths, no private API keys, no "ask Joy for the spreadsheet."
4. **Be opinionated.** Generic advice is useless. Each skill has a point of view.

## How to install

```bash
# Copy a skill into your skills directory
cp -r skills/product-judgment ~/.hermes/skills/
# or
cp -r skills/product-judgment ~/.claude/skills/
```

Most agents (Claude Code, Hermes Agent, etc.) auto-discover skills in the standard `skills/` directory under your home.

## How to contribute

Issues and PRs welcome. If you have a skill you've built and want to add it here:

1. Open an issue first — describe the problem the skill solves and why it should be a skill (not a prompt).
2. Keep the structure: `skills/<name>/SKILL.md` + optional `references/`, `scripts/`, `assets/`.
3. Make sure your skill works on a clean machine with no personal paths or private credentials.

## License

MIT. See [LICENSE](./LICENSE).
