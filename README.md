# skills-and-agents

Agent-agnostic collection of the most popular open-source **UI/UX design skills** and
**coding subagents**, vendored from their upstream GitHub repos and made usable from
any harness — Claude Code, Codex/OpenCode (via `AGENTS.md`), or anything else that can
read a directory of Markdown files.

## Layout

```
skills/design/<skill>/SKILL.md       vendored design skills (source of truth)
agents/coding/<source>/**/*.md       vendored coding subagents (source of truth)
.claude/skills/<name>/SKILL.md       generated — Claude Code skill adapter
.claude/agents/<name>.md             generated — Claude Code agent adapter
AGENTS.md                            generated — index for Codex/OpenCode/etc.
index.json                           generated — machine-readable manifest for any other harness
LICENSES/                            upstream LICENSE file for every vendored source
scripts/build-adapters.py            regenerates the three generated targets above
```

**Edit only `skills/` and `agents/coding/`.** Everything else (`.claude/`, `AGENTS.md`,
`index.json`) is generated — running the build script overwrites it.

```bash
python3 scripts/build-adapters.py
```

## What's included

### Design skills (`skills/design/`)

| Skill | Upstream | Stars* | License |
|---|---|---|---|
| ui-ux-pro-max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 126k | MIT |
| taste-skill | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 86k | MIT |
| baoyu-design | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | 4.0k | MIT |
| nothing-design | [dominikmartn/nothing-design-skill](https://github.com/dominikmartn/nothing-design-skill) | 2.8k | MIT |
| styleseed | [bitjaru/styleseed](https://github.com/bitjaru/styleseed) | 945 | MIT |
| hue | [dominikmartn/hue](https://github.com/dominikmartn/hue) | 828 | MIT |
| superdesign | [superdesigndev/superdesign-skill](https://github.com/superdesigndev/superdesign-skill) | 527 | MIT |

*Star counts captured 2026-09-09 via the GitHub API — check upstream for current counts.

### Coding subagents (`agents/coding/`)

| Source | Upstream | Stars* | License | Agents vendored |
|---|---|---|---|---|
| wshobson | [wshobson/agents](https://github.com/wshobson/agents) | 40k | MIT | 416 |
| voltagent | [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 25k | MIT | 158 |

### Skipped — license risk (linked, not vendored)

These were in the original shortlist but were **not copied in** because their license
is missing or unclear (`NOASSERTION`). Use at your own risk directly from upstream:

| Repo | Issue |
|---|---|
| [plugin87/ux-ui-agent-skills](https://github.com/plugin87/ux-ui-agent-skills) | no LICENSE file |
| [s0xDk/refactoring-ui-skill](https://github.com/s0xDk/refactoring-ui-skill) | LICENSE present but SPDX `NOASSERTION` |
| [vercel/vercel-plugin](https://github.com/vercel/vercel-plugin) | LICENSE present but SPDX `NOASSERTION` |

## Using it

**Claude Code** — skills/agents in `.claude/skills/` and `.claude/agents/` are picked up
automatically; no setup needed.

**Codex / OpenCode / other AGENTS.md-aware tools** — point the harness at this repo;
`AGENTS.md` lists every skill and agent with a one-line description.

**Anything else** — parse `index.json`. Each entry has `id`, `name`, `description`,
`path` (relative to repo root), and `type` (`skill` or `agent`); agents also carry
`tools`/`model` from their frontmatter.

## Updating

To pull a newer version of a vendored source, re-clone it, copy the updated
`skills/design/<skill>/` or `agents/coding/<source>/` files over the existing ones,
update the LICENSE in `LICENSES/` if it changed, then re-run:

```bash
python3 scripts/build-adapters.py
```

## License

Each vendored skill/agent keeps its original upstream license — see `LICENSES/`.
This repo's own glue code (`scripts/build-adapters.py`) has no separate license
restriction beyond what's declared at the repo root, if any.
