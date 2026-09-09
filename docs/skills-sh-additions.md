# Selected skills.sh additions

Reviewed on 2026-09-09 against the [skills.sh directory](https://www.skills.sh/)
and downloaded upstream source trees. Selection favors specific capabilities
missing from this repository, maintained upstream sources, useful supporting
resources, and explicit licensing. Popularity was a discovery signal, not a
quality guarantee. Nine skills were added; no global installation was made.

| Skill | Why it adds value | Source |
|---|---|---|
| `vercel-react-best-practices` | Prioritized React/Next.js performance rules covering data fetching, bundles, server rendering, and re-renders. | [skills.sh](https://skills.sh/vercel-labs/agent-skills/vercel-react-best-practices) |
| `vercel-composition-patterns` | Component APIs, compound components, context, and explicit variants. | [skills.sh](https://skills.sh/vercel-labs/agent-skills/vercel-composition-patterns) |
| `vercel-react-native-skills` | Expo/React Native list, image, animation, navigation, and native-module performance. | [skills.sh](https://skills.sh/vercel-labs/agent-skills/vercel-react-native-skills) |
| `supabase-postgres-best-practices` | PostgreSQL queries, pooling, RLS, indexes, locks, and diagnostics beyond the existing table-design skill. | [skills.sh](https://skills.sh/supabase/agent-skills/supabase-postgres-best-practices) |
| `webapp-testing` | Python Playwright examples and a helper for starting local app servers around a test command. | [skills.sh](https://skills.sh/anthropics/skills/webapp-testing) |
| `playwright-cli` | Interactive browser automation, sessions, storage, tracing, mocking, and test generation through a CLI. | [skills.sh](https://skills.sh/microsoft/playwright-cli/playwright-cli) |
| `mcp-builder` | MCP server design and implementation with Python/TypeScript references and an evaluation harness. | [skills.sh](https://skills.sh/anthropics/skills/mcp-builder) |
| `domain-modeling` | A concrete domain glossary and ADR workflow, including reusable formats and code/terminology consistency checks. | [skills.sh](https://skills.sh/mattpocock/skills/domain-modeling) |
| `find-skills` | Discover additional skills by task through the skills ecosystem. | [skills.sh](https://skills.sh/vercel-labs/skills/find-skills) |

## Packaging and provenance

Full skill directories are vendored under `skills/coding/`, including rule files,
references, examples, scripts, and skill UI metadata. All are exported by the
existing builder into `.claude/skills/`, `AGENTS.md`, and `index.json`.

[skills-sh.lock.json](../skills-sh.lock.json) records exact downloaded revisions,
source and destination paths, per-file SHA-256 hashes, and local changes. Three
broken links in Vercel's compiled React guide were corrected to point into its
existing `rules/` directory; that patch is recorded in the lock. Other upstream
instruction content is unchanged.

Supabase, Matt Pocock, and Vercel's skill-discovery repository supply MIT license
files. Anthropic's two selected skills carry their own Apache-2.0 license files;
Microsoft's Playwright CLI repository also supplies Apache-2.0. License evidence
is retained centrally in `LICENSES/` and inside standalone skill exports.

Vercel's `agent-skills` snapshot declares MIT in its README and the three selected
skills' frontmatter, but has no standalone LICENSE file. The original README is
preserved as license-declaration evidence rather than inventing a copyright
notice or pretending it supplied a full license file.

## Choosing between related skills

Use `webapp-testing` for a scripted test of a local application and server
lifecycle management. Use `playwright-cli` when the task calls for interactive
CLI browser automation. Both complement the existing E2E testing-pattern skill.

Use React performance guidance for measured or likely rendering/data-fetching
costs, composition guidance for component interface design, and React Native
guidance for mobile projects. Check the project's React version before applying
React 19-specific patterns.

These are instructions and supporting resources. Browser binaries, Playwright
CLI, MCP dependencies, API keys, and hosted services are not installed or
configured by vendoring them. The MCP evaluation helper uses Anthropic's SDK and
requires its runtime dependencies and credentials. Current harness tool access
and the user's task scope still determine what can be executed.

## Candidates not added

- Existing taste-skill, UI/UX Pro Max, impeccable, and Wshobson skills already
  cover many popular directory entries; no duplicate copies were added.
- `next-best-practices` from `vercel-labs/next-skills` returned an unavailable
  listing during review; the current catalog already has Next.js App Router
  patterns.
- [Remotion skills](https://skills.sh/remotion-dev/skills/remotion-best-practices)
  remain link-only: the inspected source revision has no license file or license
  declaration, and its current entrypoint routes to a larger sibling skill set.
- Matt Pocock's merge-conflict workflow mandates staging everything and
  committing. Its TDD workflow requires seam confirmation and additional skill
  dependencies. These were not selected for this general-purpose addition.
- Vercel's web-design-guidelines entrypoint fetches an external rule document at
  runtime and overlaps existing UI audit coverage; the self-contained React
  rules provide more additional value here.

## Verification

The adapter and provenance tests pass; every new entrypoint parses as YAML and
has a unique skill name. The builder's read-only freshness check passes. The
webapp server helper's `--help` command runs. Bundled Python scripts are syntax
checked without installing their dependencies or invoking remote APIs. Browser
and MCP workflows have not been run end to end as part of this catalog update.
