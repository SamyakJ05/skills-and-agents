# Catalog review — 2026-09-09

The principal gap was adapter correctness. The source tree already includes broad
coding coverage, but the builder presented many skills as agents. This review
checked entrypoint classification and metadata across the catalog, inspected
representative instructions, and tested adapter behavior. It did not execute all
vendored workflows or re-audit upstream licensing and current library guidance.

## Findings and changes

| Priority | Finding | Change |
|---|---|---|
| High | 183 `SKILL.md` files under `agents/coding/wshobson` were emitted as agents. The index said there were no coding skills, and skill resources were not copied. | Discover both skill source trees, export whole skill directories, and list them as coding skills. This restores 16 supporting files. |
| High | Four command files with frontmatter were classified as agents; ten commands without frontmatter were omitted. | Classify all 14 commands separately and export `.claude/commands/`. |
| High | Duplicate agent filenames used numeric suffixes while retaining identical frontmatter names. Skill name collisions would silently overwrite a previous skill. | Generate source-derived names for duplicates, synchronize exported frontmatter, expose adapter paths in the manifest, and reject residual collisions before writing. |
| Medium | The handwritten YAML parser flattened nested fields, mishandled list values, and accepted malformed descriptions. Eight VoltAgent descriptions contained unquoted `: ` sequences. | Use PyYAML, preserve structured metadata, and quote those eight source descriptions without changing their text. |
| Medium | No regression suite or read-only generated-file check existed. | Add six temporary-repository tests and `--check`; render before replacing outputs. |
| Low | README counts mixed skills, agents, and other Markdown files. Agent rows lacked source-file links. | Document entrypoint counts and add source links and adapter names. |

The resulting catalog contains **305 skills, 360 agents, and 14 commands**. Of the
skills, 304 already existed and one is new: `maintain-agent-catalog`. Agent sources
contain 202 Wshobson and 158 VoltAgent entrypoints. No specialist agent was added:
the collection already covers the common development roles inspected here.

## Instruction quality and packaging limits

- **Overlapping design directions:** antislop, taste-skill, StyleSeed, impeccable,
  and other systems have different triggers and constraints. The generated entry
  file now advises choosing one primary direction and reading only relevant
  instructions. Their upstream bodies remain intact.
- **Environment assumptions:** for example, VoltAgent's `code-reviewer` asks for
  a context manager and imposes fixed coverage/complexity targets. Those are
  upstream workflow assumptions, not evidence that this harness supplies the
  dependency or that a project adopted those targets.
- **Incomplete plugin packaging:** `review-agent-setup` references a sibling
  agent using `../agents/review-policy-author.md`, which does not resolve from
  its vendored skill directory. It also expects a separately installed plugin
  runtime. Exporting its skill does not install that runtime or repair every
  cross-plugin reference. Consult the source tree and task-specific dependencies
  before using such workflows.
- **Catalog size:** `AGENTS.md` still embeds the full inventory, so loading it has
  a substantial context cost. A future selective installer or split catalog would
  be useful when a harness needs only one domain; this change preserves the
  repository's existing full-index convention.
- **Update provenance:** upstream URLs and licenses exist, but a uniform pinned
  revision manifest does not. Record revisions on future upstream updates; this
  review does not invent historical commit hashes.

## Validation

- Six adapter regression tests pass.
- The new maintenance skill passes the skill-creator frontmatter validator.
- A complete build succeeds, followed by a passing read-only freshness check.
- Generated entries are checked against their source type and exported names;
  supporting files stay with their skill directories.

The generated diff is large because it moves 183 entries from agents to skills
and replaces ambiguous agent aliases. Upstream instruction bodies were preserved.
