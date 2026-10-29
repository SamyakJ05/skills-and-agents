# skills-and-agents

Agent-agnostic collection of vendored **design, coding, 3D, and video skills**,
**coding subagents**, and **commands**, vendored from their upstream GitHub repos and made usable from
any harness — Claude Code, Codex/OpenCode (via `AGENTS.md`), or anything else that can
read a directory of Markdown files.

## Layout

```
skills/<category>/**/SKILL.md        skills (source of truth)
agents/coding/**/skills/*/SKILL.md   skills bundled with upstream agent plugins
agents/coding/<source>/**/*.md       vendored coding subagents (source of truth)
.claude/skills/<name>/SKILL.md       generated — Claude Code skill adapter
.claude/agents/<name>.md             generated — Claude Code agent adapter
.claude/commands/<name>.md           generated — Claude Code command adapter
AGENTS.md                            generated — index for Codex/OpenCode/etc.
index.json                           generated — machine-readable manifest for any other harness
LICENSES/                            upstream LICENSE file for every vendored source
scripts/build-adapters.py            regenerates all adapters and indexes
upstreams.json                       upstream repo, synced commit, and path mappings per source
scripts/sync-upstreams.py            refreshes vendored sources from upstreams.json
scripts/link-skills.py               links selected skills/agents into another project
```

**Edit skill and agent content in `skills/` and `agents/coding/`.** Edit adapter logic
in `scripts/build-adapters.py`. `.claude/skills/`, `.claude/agents/`,
`.claude/commands/`, `AGENTS.md`, and `index.json` are generated and replaced by the
builder. Other `.claude/` configuration is left alone.

Install the builder dependency once with `python3 -m pip install -r scripts/requirements.txt`.

```bash
python3 scripts/build-adapters.py
```

## What's included

### Design skills (`skills/design/`)

| Skill | Upstream | Stars* | License |
|---|---|---|---|
| ui-ux-pro-max | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 126k | MIT |
| taste-skill | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) + [taste-skill-classics](https://github.com/Leonxlnx/taste-skill-classics) + [imagegen-skills](https://github.com/Leonxlnx/imagegen-skills) | 86k | MIT |
| baoyu-design | [JimLiu/baoyu-design](https://github.com/JimLiu/baoyu-design) | 4.0k | MIT |
| nothing-design | [dominikmartn/nothing-design-skill](https://github.com/dominikmartn/nothing-design-skill) | 2.8k | MIT |
| styleseed | [bitjaru/styleseed](https://github.com/bitjaru/styleseed) | 945 | MIT |
| hue | [dominikmartn/hue](https://github.com/dominikmartn/hue) | 828 | MIT |
| superdesign | [superdesigndev/superdesign-skill](https://github.com/superdesigndev/superdesign-skill) | 527 | MIT |
| impeccable | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 67k | Apache-2.0 |
| emilkowalski (12 skills) | [emilkowalski/skills](https://github.com/emilkowalski/skills) | 36k | MIT |
| anti-slop (6 skills) | [miqdadbadjuber/anti-slop](https://github.com/miqdadbadjuber/anti-slop) | 1.7k | MIT |
| motion-primitives (33 components) | [ibelick/motion-primitives](https://github.com/ibelick/motion-primitives) | 6.2k | MIT |
| gsap-skills (8 official GSAP skills) | [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | 17k | MIT |
| threejs-skills (13 skills, three.js r186/WebGPU) | [CloudAI-X/threejs-skills](https://github.com/CloudAI-X/threejs-skills) | 3.8k | MIT |
| mengto (6 scroll/3D storytelling skills) | [MengTo/Skills](https://github.com/MengTo/Skills) | 7.1k | MIT |
| modern-web-guidance | [GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance) | 2.6k | Apache-2.0 |
| claudedesignskills (23 skills) | [freshtechbro/claudedesignskills](https://github.com/freshtechbro/claudedesignskills) | 869 | MIT |

**Scroll-driven and 3D web motion (added 2026-10-29).** `gsap-skills` is GreenSock's
official set (ScrollTrigger pin/scrub/batch/cleanup, ScrollSmoother, `useGSAP`); it
overlaps claudedesignskills' `gsap-scrolltrigger`, and the builder disambiguates the
shared name. `mengto` vendors only the scroll subset of MengTo/Skills (Three.js scroll
worlds with a scroll "conductor", image-sequence scrubbing, Lenis + ScrollTrigger
choreography, horizontal scenes); demo HTML and prompts are kept, binary demo media is
not, so demos are references rather than runnable pages. `modern-web-guidance` covers
CSS scroll-driven animations and View Transitions with Baseline fallbacks; its search
command calls `npx modern-web-guidance@latest` (network). React View Transitions is in
`skills/coding/vercel/react-view-transitions`.

Taste-skill follows its 2.1 split: classics (`high-end-visual-design`, `minimalist-ui`,
`industrial-brutalist-ui`, `gpt-taste`, `stitch-design-taste`, `design-taste-frontend-v1`)
are opt-in upstream (`disable-model-invocation: true`); `full-output-enforcement` and
`redesign-existing-projects` were retired upstream and removed here. StyleSeed's 22
`ss-*` skills are now internal workflows of the single `styleseed` skill.

### Security and compliance skills (`skills/security/`, `agents/coding/trailofbits/`)

| Source | Upstream | Stars* | License | Selection |
|---|---|---|---|---|
| trailofbits | [trailofbits/skills](https://github.com/trailofbits/skills) | 7.9k | **CC-BY-SA-4.0** | 13 plugins: static-analysis (Semgrep, CodeQL, SARIF), Semgrep rule authoring, variant analysis, fp-check, differential review, sharp-edges, insecure-defaults, entry-point analysis, audit context, supply-chain risk, agentic GitHub Actions audit, Testing Handbook fuzzing skills |
| sentry | [getsentry/skills](https://github.com/getsentry/skills) | 1.1k | Apache-2.0 | security-review, gha-security-review, security-model, secret-serialization, skill-scanner, django-access-review |
| grcskills | [better-isms/grcskills](https://github.com/better-isms/grcskills) | 53 | MIT | 65 GRC skills: ISO 27001/SOC 2/NIST/EU AI Act/NIS2 SoA, evidence, risk register, policies, questionnaires, DPIA |
| cybersecurity-skills | [mukul975/Anthropic-Cybersecurity-Skills](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) | 35k | Apache-2.0 | 13 defensive skills only: SLSA/Sigstore/SBOM/in-toto, MCP tool-poisoning audit, LLM prompt-injection and red-teaming, Terraform/Trivy/CIS, SOC 2 Type II prep, NIST CSF |

License and runtime notes:

- **Trail of Bits content is CC-BY-SA-4.0 (share-alike).** Redistributing modified
  versions requires the same license and attribution; it is vendored unmodified.
  Sentry's `security-review` references derive from the OWASP Cheat Sheets (CC BY-SA 4.0).
- Trail of Bits skills expect `semgrep`, `codeql`, `uv`, `gh`, and fuzzers (libFuzzer,
  AFL++, cargo-fuzz) as applicable. `fp-check` ships a `hooks/hooks.json`, which this
  catalog does not install. Tests and evals were not vendored.
- grcskills offer an optional step that sends a short question to the commercial ISMS
  Copilot MCP server, only if the user connects it; the skills work without it.
- cybersecurity-skills include `scripts/agent.py` helpers that call tools such as cosign,
  syft, trivy, mcp-scan, garak and promptfoo. Use them only against systems you own or are
  authorized to assess. The upstream repo also contains offensive skills, which were not vendored.

### 3D skills (`skills/3d/`)

| Skill | Upstream | Stars* | License |
|---|---|---|---|
| blender (30 skills) | [RobLe3/cc-blender-skill](https://github.com/RobLe3/cc-blender-skill) | 56 | MIT |

Agentic Blender control: modeling, UV/texturing, materials, lighting, cameras, animation,
rendering, export, plus higher-level pipelines (text-to-blender, reference-to-3d,
wireframe-to-3d, mascot-logo-reconstruction). Complements `claudedesignskills`'
`blender-web-pipeline` (glTF export for Three.js/Babylon.js) with actual in-Blender
modeling/animation work.

### Video skills (`skills/video/`)

| Skill | Upstream | Stars* | License |
|---|---|---|---|
| video-shotcraft | [Vincentwei1021/video-shotcraft](https://github.com/Vincentwei1021/video-shotcraft) | 7.8k | Apache-2.0 |

Cinematic product videos from shot-recipe cards using Remotion, real page screenshots,
2.5D camera moves, and beat-synced timing. Vendored the skill, references, agents, and
workbench template only — the upstream repo's `demos/`, `gallery/`, and `assets/`
(36M+ of example media) were dropped as non-essential to the skill's function.

*Star counts captured 2026-09-09 (sources added 2026-10-29: on that date) via the GitHub API — check upstream for current counts.

### Coding skills

The adapter discovers 183 existing skills inside `agents/coding/wshobson/**/skills/`,
including debugging, code review, testing, API design, authentication, CI/CD,
Python, TypeScript, data engineering, and LLM workflows. Their supporting resources
are copied with them. One local skill, `maintain-agent-catalog`, supplies this
repository's classification, update, and verification workflow.

The current catalog sources contain **453 skills, 372 agents, and 18 commands** (2026-10-29).
These are entrypoint counts, not counts of unique capabilities or upstream files.

### Selected skills.sh additions

Nine additional skills were selected for this repository on 2026-09-09: Vercel
React performance, composition, and React Native; Supabase PostgreSQL; Playwright
CLI; Anthropic webapp testing and MCP building; Matt Pocock domain modeling; and
Vercel skill discovery.

See [the selection and usage notes](docs/skills-sh-additions.md) for individual
links, rationale, dependencies, and skipped candidates. `skills-sh.lock.json`
records upstream commit IDs, source paths, license evidence, local changes, and
per-file hashes for these additions. It is maintained source metadata, not a
builder output, and does not cover older vendored packages. Hashes are checked by
the test suite; update them deliberately when updating one of these skills.

### Coding subagents (`agents/coding/`)

| Source | Upstream | Stars* | License | Agent entrypoints |
|---|---|---|---|---|
| wshobson | [wshobson/agents](https://github.com/wshobson/agents) | 40k | MIT | 202 |
| trailofbits | [trailofbits/skills](https://github.com/trailofbits/skills) | 7.9k | CC-BY-SA-4.0 | 6 |
| local | this repository (`agents/coding/local/`) | — | MIT | 1 |
| voltagent | [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 25k | MIT | 158 |

### Skipped — license risk (linked, not vendored)

These were in the original shortlist but were **not copied in** because their license
is missing or unclear (`NOASSERTION`). Use at your own risk directly from upstream:

| Repo | Issue |
|---|---|
| [plugin87/ux-ui-agent-skills](https://github.com/plugin87/ux-ui-agent-skills) | no LICENSE file |
| [s0xDk/refactoring-ui-skill](https://github.com/s0xDk/refactoring-ui-skill) | LICENSE present but SPDX `NOASSERTION` |
| [vercel/vercel-plugin](https://github.com/vercel/vercel-plugin) | LICENSE present but SPDX `NOASSERTION` |

## Not vendored

| Item | Why not vendored |
|---|---|
| `npx -y add-mcp https://vgpu.sh/api/mcp -g` / [vercel-labs/vgpu](https://github.com/vercel-labs/vgpu) | MCP server + WebGPU runtime library, not a skill or subagent. Install it as an MCP server via the command above if you want the tool itself. |
| [reactbits.dev](https://reactbits.dev/) → [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) (47k stars) | License is **MIT + Commons Clause** (`NOASSERTION` on GitHub) — the Commons Clause restricts selling the software itself. Link-only per this repo's license policy; browse/copy components directly from the site or repo if needed for your own project. |
| [godly.design](https://godly.design/) | Design-inspiration gallery site with no GitHub repo behind it — nothing to vendor. |
| [manus.im](https://manus.im/) | Commercial hosted AI agent product, no GitHub repo — nothing to vendor. |
| [motion-primitives.com](https://motion-primitives.com/) | ✅ Vendored — see `skills/design/motion-primitives/` above ([ibelick/motion-primitives](https://github.com/ibelick/motion-primitives), MIT). Copied only `components/core/` (the 33 reusable primitives), not the marketing site's own UI scaffolding. |
| ["best free skills" from mcpmarket.com/tools/skills](https://mcpmarket.com/tools/skills) | The page returned HTTP 429 (rate-limited) on every fetch attempt and isn't confirmed by search to be a curated "best of" list — it appears to be a large third-party aggregator/marketplace, not a hand-picked set. Rather than guess at its contents or vendor an unverified bulk listing, this was skipped. If you can open the page and name specific skills from it, they can be vendored the same way as everything else here. |

## Using it

**Claude Code** — skills/agents in `.claude/skills/` and `.claude/agents/` are picked up
automatically; no setup needed.

**Other project repos** — list the skills and agents a project needs in
`<project>/.claude/catalog.json` (`{"skills": [...], "agents": [...]}`, using adapter
names), then run `python3 scripts/link-skills.py <project>`. It creates relative
symlinks into this catalog's sources under `<project>/.claude/skills/` and
`.claude/agents/`, removes links it created that are no longer listed, and leaves the
project's own files alone; `--check` reports drift. `catalog.json`, the links, and any `local_files` (for example the project's `AGENTS.md`) go into a managed block of the project's `.git/info/exclude`, so the setup stays local to that clone and never shows up in commits. Linked skills follow upstream syncs
without copying. Nine sites are set up this way across eight repos: techshorts (news + blog, and Circuit),
reboundq.com, reachgrid-networks.com, piccolo-mind, RetainIQ, intellifunnel,
summitvertex.com and intellifunnellabs, each with a local routing table in its `AGENTS.md`
(or `CLAUDE.local.md` where `AGENTS.md` is already tracked).

**Codex / OpenCode / other AGENTS.md-aware tools** — point the harness at this repo;
`AGENTS.md` lists every skill and agent with a one-line description.

**Anything else** — parse `index.json`, which separates `skills`, `agents`, and
`commands`. Each entry has `id`, `name`, `description`, `path` (relative to repo
root), `type`, `adapter_name`, and `adapter_path`; agents also carry `tools`/`model`
from their frontmatter. Duplicate names receive source-derived adapter names;
use `adapter_name` for invocation. Generated frontmatter matches those names.
Existing numeric aliases such as `code-reviewer-2` are replaced by these names.

Choose skills for the current task; avoid loading multiple competing design
systems at once. The catalog does not install MCP servers, hooks, plugin runtimes,
or application dependencies. Upstream model/tool fields are metadata and may need
translation to the harness in use. References outside a skill directory require
checking against the original source tree.

The [catalog review](docs/catalog-review.md) records findings and remaining limits.

## Updating

`upstreams.json` records, for each vendored source, its repository, license, the last
synced commit, and which upstream paths map to which local paths (with excludes and
locally added files to keep). To pull the latest upstream revisions:

```bash
python3 scripts/sync-upstreams.py --dry-run          # report what would change
python3 scripts/sync-upstreams.py                    # all sources (shallow-clones each repo)
python3 scripts/sync-upstreams.py wshobson-agents    # or selected source ids
python3 scripts/build-adapters.py
```

Directory mappings delete files that upstream removed. Files listed as `modifications`
in `skills-sh.lock.json` are never overwritten, and that lock's hashes and commits are
refreshed automatically. Review the diff before committing: upstreams rename and retire
skills (taste-skill and StyleSeed both did in October 2026), and a removed upstream path
needs a manifest edit. Sources vendored before 2026-10-29 show `null` as their previous
commit because earlier revisions were not recorded. The finance toolkits under
`skills/coding/finance-tools/` pair authored `SKILL.md` files with upstream package
source; after syncing them, check the `SKILL.md` API references against the new code.

## Validation

```bash
python3 -m unittest discover -s tests -v
python3 scripts/build-adapters.py --check
```

`--check` renders into a temporary directory and exits nonzero if generated files
are missing, changed, or stale. It does not modify the repository. Builds parse
YAML and validate names before replacing outputs; malformed entrypoints fail with
their source path. Adapter tests cover classification, support files, duplicate
names, nested YAML, drift detection, and failure before output replacement.

## License

Each vendored skill/agent keeps its original upstream license — see `LICENSES/`.
This repo's own glue code (`scripts/build-adapters.py`) has no separate license
restriction beyond what's declared at the repo root, if any.
