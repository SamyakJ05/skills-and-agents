---
name: maintain-agent-catalog
description: Audit or extend this repository's vendored skill and agent catalog, including source classification, adapter naming, supporting resources, and generated-file drift. Use for catalog maintenance, not ordinary application code review.
---

# Maintain the agent catalog

Work from the repository root containing `scripts/build-adapters.py` and `index.json`.
If invoked from a copied skill in another project, locate this catalog before making
changes; do not assume the current project's agent configuration has this layout.

## Review before adding

Inspect `git status --short`, `README.md`, the builder, and the relevant entries in
`index.json`. Search both `skills/**/SKILL.md` and
`agents/coding/**/skills/**/SKILL.md` before declaring a capability missing.
Read candidate instructions and supporting files, not just their descriptions.
Distinguish a missing capability from an existing capability hidden by bad adapters.

Keep upstream content in its existing source tree. A `SKILL.md` is a skill even
inside an agent repository; plugin commands, templates, references, and examples
are not subagents. Copy the whole skill directory so relative references survive.
References outside that directory need separate inspection: a flattened adapter
does not recreate a complete plugin or install its runtime dependencies.

For a new local workflow, create a narrowly triggered skill under
`skills/coding/<name>/SKILL.md` with valid YAML `name` and `description`. Add only
instructions that supply missing repository knowledge. Avoid duplicating an
existing specialist or applying a task-specific workflow to every request.
For a requested upstream addition, record its source and revision and preserve its
license; follow this repository's policy for sources with unclear licensing.

## Adapter invariants

Edit `scripts/build-adapters.py` for discovery and rendering changes, never the
generated `.claude/`, `AGENTS.md`, or `index.json` directly. Preserve source names;
use the manifest's `adapter_name` and `adapter_path` for exported invocations.
Duplicate names need deterministic disambiguation in both filenames and
frontmatter, with collisions rejected before outputs are replaced.

Use a YAML parser for frontmatter. Report malformed entrypoints with their paths;
do not silently drop them or interpret nested metadata as top-level fields.
Keep agent tool/model declarations as upstream metadata, not permission grants.
Do not install hooks or external integrations merely because a vendored skill
mentions them.

## Verification

Run these from the catalog root (Python dependencies are in
`scripts/requirements.txt`):

```bash
python3 -m unittest discover -s tests -v
python3 scripts/build-adapters.py
python3 scripts/build-adapters.py --check
```

For builder changes, test observable invariants with temporary repositories:
classification, resource preservation, collision handling, and read-only drift
detection. Inspect the generated diff and source-to-adapter counts. Verify that
unrelated source bodies remain unchanged. Report concrete findings, changes,
checks, and any untested runtime dependencies without claiming every vendored
workflow has been executed.
