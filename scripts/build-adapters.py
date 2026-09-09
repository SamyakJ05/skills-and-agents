#!/usr/bin/env python3
"""
Builds agent-agnostic adapters from the vendored skills/ and agents/coding/ trees.

Sources of truth (edit these, not the generated output):
  skills/design/**/SKILL.md   - design skills (frontmatter: name, description)
  agents/coding/**/*.md       - coding subagents (frontmatter: name, description, tools, model)

Generates:
  .claude/skills/<name>/SKILL.md   - symlink-free copy for Claude Code
  .claude/agents/<name>.md         - copy for Claude Code
  AGENTS.md                        - single-file index Codex/OpenCode/etc. read natively
  index.json                       - machine-readable manifest for any other harness

Re-run after adding/removing a vendored skill or agent:
  python3 scripts/build-adapters.py
"""
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
AGENTS_DIR = ROOT / "agents" / "coding"
CLAUDE_SKILLS = ROOT / ".claude" / "skills"
CLAUDE_AGENTS = ROOT / ".claude" / "agents"
AGENTS_MD = ROOT / "AGENTS.md"
INDEX_JSON = ROOT / "index.json"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    fm = {}
    lines = m.group(1).splitlines()
    key = None
    block_indent = None
    for line in lines:
        # continuation of a YAML block scalar (>-, |-, >, |)
        if block_indent is not None and (line.startswith(" " * block_indent) or not line.strip()):
            fm[key] = (fm.get(key, "") + " " + line.strip()).strip()
            continue
        block_indent = None
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        k = k.strip()
        v = v.strip()
        if v in (">-", "|-", ">", "|"):
            key = k
            block_indent = 1  # any indentation counts as continuation
            fm[k] = ""
            continue
        fm[k] = v.strip('"').strip("'")
    return fm


def slugify(p: Path, base: Path) -> str:
    rel = p.relative_to(base)
    parts = list(rel.parts[:-1]) if rel.parts[-1].lower() in ("skill.md",) else list(rel.parts[:-1]) + [rel.stem]
    return "/".join(parts) if parts else rel.stem


def collect_skills():
    out = []
    for skill_md in sorted(SKILLS_DIR.rglob("SKILL.md")):
        fm = parse_frontmatter(skill_md.read_text(errors="ignore"))
        skill_dir = skill_md.parent
        rel_dir = skill_dir.relative_to(SKILLS_DIR)
        out.append({
            "id": str(rel_dir).replace("\\", "/"),
            "name": fm.get("name") or skill_dir.name,
            "description": fm.get("description", ""),
            "path": str(skill_dir.relative_to(ROOT)),
            "type": "skill",
        })
    return out


def collect_agents():
    out = []
    for agent_md in sorted(AGENTS_DIR.rglob("*.md")):
        if agent_md.name.upper() in ("README.MD",):
            continue
        fm = parse_frontmatter(agent_md.read_text(errors="ignore"))
        if not fm.get("name") and not fm.get("description"):
            continue
        rel = agent_md.relative_to(AGENTS_DIR)
        out.append({
            "id": str(rel.with_suffix("")).replace("\\", "/"),
            "name": fm.get("name") or agent_md.stem,
            "description": fm.get("description", ""),
            "tools": fm.get("tools", ""),
            "model": fm.get("model", ""),
            "path": str(agent_md.relative_to(ROOT)),
            "type": "agent",
        })
    return out


def build_claude_layout(skills, agents):
    if CLAUDE_SKILLS.exists():
        shutil.rmtree(CLAUDE_SKILLS)
    if CLAUDE_AGENTS.exists():
        shutil.rmtree(CLAUDE_AGENTS)
    CLAUDE_SKILLS.mkdir(parents=True)
    CLAUDE_AGENTS.mkdir(parents=True)

    for s in skills:
        src_dir = ROOT / s["path"]
        dest_name = s["name"] if s["name"] else Path(s["id"]).name
        dest_name = re.sub(r"[^a-zA-Z0-9_-]", "-", dest_name)
        dest = CLAUDE_SKILLS / dest_name
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(src_dir, dest)

    for a in agents:
        src = ROOT / a["path"]
        dest_name = re.sub(r"[^a-zA-Z0-9_-]", "-", a["name"] or Path(a["id"]).name) + ".md"
        dest = CLAUDE_AGENTS / dest_name
        if dest.exists():
            i = 2
            stem = dest.stem
            while dest.exists():
                dest = CLAUDE_AGENTS / f"{stem}-{i}.md"
                i += 1
        shutil.copy2(src, dest)


def build_agents_md(skills, agents):
    lines = []
    lines.append("# AGENTS.md\n")
    lines.append(
        "Agent-agnostic index of vendored skills and subagents in this repo. "
        "Codex, OpenCode, and other AGENTS.md-aware harnesses should read this file "
        "to discover available skills/agents. Claude Code users: see `.claude/skills/` "
        "and `.claude/agents/` (generated from the same sources — do not edit directly).\n"
    )
    lines.append("Regenerate after changes: `python3 scripts/build-adapters.py`\n")

    lines.append("\n## Design skills\n")
    for s in skills:
        if s["path"].startswith("skills/design"):
            desc = s["description"].split("\n")[0][:160]
            lines.append(f"- **{s['name']}** (`{s['path']}`) — {desc}")

    lines.append("\n## Coding skills\n")
    any_coding_skill = False
    for s in skills:
        if s["path"].startswith("skills/coding"):
            any_coding_skill = True
            desc = s["description"].split("\n")[0][:160]
            lines.append(f"- **{s['name']}** (`{s['path']}`) — {desc}")
    if not any_coding_skill:
        lines.append("_(none yet — coding assistance here is via subagents below)_")

    lines.append("\n## 3D skills\n")
    for s in skills:
        if s["path"].startswith("skills/3d"):
            desc = s["description"].split("\n")[0][:160]
            lines.append(f"- **{s['name']}** (`{s['path']}`) — {desc}")

    lines.append("\n## Video skills\n")
    for s in skills:
        if s["path"].startswith("skills/video"):
            desc = s["description"].split("\n")[0][:160]
            lines.append(f"- **{s['name']}** (`{s['path']}`) — {desc}")

    other_cats = {"skills/design", "skills/coding", "skills/3d", "skills/video"}
    other = [s for s in skills if not any(s["path"].startswith(c) for c in other_cats)]
    if other:
        lines.append("\n## Other skills\n")
        for s in other:
            desc = s["description"].split("\n")[0][:160]
            lines.append(f"- **{s['name']}** (`{s['path']}`) — {desc}")

    lines.append("\n## Coding subagents\n")
    lines.append("| Name | Source | Tools | Model | Description |")
    lines.append("|---|---|---|---|---|")
    for a in agents:
        source = a["path"].split("/")[2] if a["path"].startswith("agents/coding/") else ""
        desc = a["description"].replace("|", "\\|").split("\n")[0][:140]
        lines.append(f"| `{a['name']}` | {source} | {a['tools']} | {a['model']} | {desc} |")

    AGENTS_MD.write_text("\n".join(lines) + "\n")


def build_index_json(skills, agents):
    INDEX_JSON.write_text(json.dumps({
        "generated_by": "scripts/build-adapters.py",
        "skills": skills,
        "agents": agents,
    }, indent=2) + "\n")


def main():
    skills = collect_skills()
    agents = collect_agents()
    build_claude_layout(skills, agents)
    build_agents_md(skills, agents)
    build_index_json(skills, agents)
    print(f"skills: {len(skills)}  agents: {len(agents)}")
    print(f"wrote .claude/skills/*, .claude/agents/*, AGENTS.md, index.json")


if __name__ == "__main__":
    main()
