#!/usr/bin/env python3
"""Build adapters from skills/ and agents/coding/; use --check to detect drift."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile

import yaml

ROOT = Path(__file__).resolve().parent.parent
FRONTMATTER_RE = re.compile(r"\A---[ \t]*\n(.*?)\n---[ \t]*(?:\n|$)", re.DOTALL)
GENERATED = (".claude/skills", ".claude/agents", ".claude/commands", "AGENTS.md", "index.json")


def parse_frontmatter(text: str) -> dict:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a mapping")
    return data


def read_metadata(path):
    try:
        return parse_frontmatter(path.read_text())
    except (ValueError, yaml.YAMLError) as exc:
        raise ValueError(f"{path}: {exc}") from exc


def entry(path, base, kind, root):
    fm = read_metadata(path)
    if kind != "command":
        for key in ("name", "description"):
            if not isinstance(fm.get(key), str) or not fm[key].strip():
                raise ValueError(f"{path}: missing or invalid {key}")
    source_path = path.parent if kind == "skill" else path
    identity = source_path.relative_to(base)
    if kind != "skill":
        identity = identity.with_suffix("")
    result = {
        "id": identity.as_posix(),
        "name": fm.get("name") or path.stem,
        "description": fm.get("description", ""),
        "path": source_path.relative_to(root).as_posix(),
        "type": kind,
    }
    if kind == "command" and not result["description"]:
        heading = re.search(r"^#\s+(.+)$", path.read_text(), re.MULTILINE)
        result["description"] = heading.group(1) if heading else path.stem
    if kind == "agent":
        result.update(tools=fm.get("tools", ""), model=fm.get("model", ""))
    return result


def collect_skills(root=ROOT):
    out = [entry(p, root / "skills", "skill", root)
           for p in sorted((root / "skills").rglob("SKILL.md"))]
    for p in sorted((root / "agents/coding").rglob("SKILL.md")):
        item = entry(p, root / "agents/coding", "skill", root)
        item["id"] = "coding/" + item["id"]
        out.append(item)
    return out


def collect_agents(root=ROOT):
    out = []
    base = root / "agents/coding"
    for p in sorted(base.rglob("*.md")):
        parts = p.relative_to(base).parts
        # Plugin skills, commands, templates and references are not subagents.
        if p.name.upper() == "README.MD" or any(
            part in {"skills", "commands", "templates", "references"} for part in parts[:-1]
        ):
            continue
        fm = read_metadata(p)
        if fm.get("name") or fm.get("description"):
            out.append(entry(p, base, "agent", root))
    return out


def collect_commands(root=ROOT):
    base = root / "agents/coding"
    return [entry(p, base, "command", root) for p in sorted(base.rglob("commands/*.md"))]


def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def assign_adapter_names(entries):
    counts = Counter(slug(item["name"]) for item in entries)
    used = set()
    for item in entries:
        short = slug(item["name"])
        name = short if counts[short] == 1 else slug(item["id"])
        if len(name) > 64:
            name = name[:51].rstrip("-") + "-" + hashlib.sha256(item["id"].encode()).hexdigest()[:12]
        if not name or name in used:
            raise ValueError(f"Adapter name collision or empty name: {item['path']} ({name})")
        used.add(name)
        item["adapter_name"] = name
        suffix = "/SKILL.md" if item["type"] == "skill" else ".md"
        item["adapter_path"] = f".claude/{item['type']}s/{name}{suffix}"


def adapter_text(text, name):
    match = FRONTMATTER_RE.match(text)
    if not match:
        return text
    # Preserve upstream formatting, metadata and body; change only invocation name.
    front = re.sub(r"^name:.*$", f"name: {name}", match.group(1), count=1, flags=re.MULTILINE)
    return text[:match.start(1)] + front + text[match.end(1):]


def build_claude_layout(skills, agents, commands, root, output):
    for kind in ("skills", "agents", "commands"):
        (output / ".claude" / kind).mkdir(parents=True, exist_ok=True)
    for item in skills + agents + commands:
        src = root / item["path"]
        dest = output / item["adapter_path"]
        if item["type"] == "skill":
            shutil.copytree(src, dest.parent, ignore=shutil.ignore_patterns(
                "__pycache__", "*.pyc", ".DS_Store", "node_modules", ".git"))
            src = src / "SKILL.md"
        dest.write_text(adapter_text(src.read_text(), item["adapter_name"]))


def cell(value):
    if isinstance(value, list):
        value = ", ".join(map(str, value))
    return " ".join(str(value).split()).replace("|", "\\|")


def build_agents_md(skills, agents, commands, output):
    lines = ["# AGENTS.md\n",
        "Agent-agnostic index of vendored skills and subagents. Edit sources, not this generated file.\n",
        "Regenerate: `python3 scripts/build-adapters.py`. Validate: `python3 scripts/build-adapters.py --check`.\n",
        "Read only the skill or agent relevant to the current task. Choose one primary design direction; "
        "do not combine competing style systems by default. Agent tools/model fields describe upstream "
        "preferences, not capabilities or permissions granted by the current harness. "
        "Full descriptions and adapter paths are in `index.json`.\n"]
    groups = {}
    for item in skills:
        category = item["id"].split("/")[0]
        groups.setdefault(category, []).append(item)
    titles = {"design": "Design", "coding": "Coding", "3d": "3D", "video": "Video"}
    for category, items in sorted(groups.items()):
        lines.append(f"\n## {titles.get(category, category.title())} skills\n")
        for item in items:
            lines.append(f"- **{item['name']}** (`{item['path']}`) — {cell(item['description'])[:160].rstrip()}")
    lines.extend(["\n## Coding subagents\n", "| Name / source file | Adapter | Tools | Model | Description |",
                  "|---|---|---|---|---|"])
    for item in agents:
        lines.append(f"| [{item['name']}]({item['path']}) | `{item['adapter_name']}` | "
                     f"{cell(item['tools'])} | {cell(item['model'])} | {cell(item['description'])[:140]} |")
    lines.append("\n## Commands\n")
    for item in commands:
        lines.append(f"- `{item['adapter_name']}` (`{item['path']}`) — {cell(item['description'])[:160].rstrip()}")
    (output / "AGENTS.md").write_text("\n".join(lines) + "\n")


def snapshot(path):
    if path.is_file():
        return {"": path.read_bytes()}
    if path.is_dir():
        return {p.relative_to(path).as_posix(): p.read_bytes()
                for p in path.rglob("*") if p.is_file()}
    return None


def build(root=ROOT, check=False):
    skills, agents, commands = collect_skills(root), collect_agents(root), collect_commands(root)
    for items in (skills, agents, commands):
        assign_adapter_names(items)
    # Render everything before replacing any generated files.
    with tempfile.TemporaryDirectory(prefix="skill-adapters-") as temporary:
        output = Path(temporary)
        build_claude_layout(skills, agents, commands, root, output)
        build_agents_md(skills, agents, commands, output)
        (output / "index.json").write_text(json.dumps({
            "generated_by": "scripts/build-adapters.py", "skills": skills,
            "agents": agents, "commands": commands,
        }, indent=2) + "\n")
        drift = [name for name in GENERATED if snapshot(root / name) != snapshot(output / name)]
        if check:
            if drift:
                print("Out of date: " + ", ".join(drift))
                return 1
            print("Generated adapters are current.")
        else:
            for name in drift:
                src, dest = output / name, root / name
                if src.is_dir():
                    if dest.exists():
                        shutil.rmtree(dest)
                    shutil.copytree(src, dest)
                else:
                    dest.write_bytes(src.read_bytes())
        print(f"skills: {len(skills)}  agents: {len(agents)}  commands: {len(commands)}")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="detect stale adapters without writing")
    args = parser.parse_args()
    try:
        return build(check=args.check)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"{exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
