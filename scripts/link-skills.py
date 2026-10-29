#!/usr/bin/env python3
"""Link catalog skills and agents into a project, as listed in its .claude/catalog.json.

catalog.json: {"skills": [...], "agents": [...], "local_files": ["AGENTS.md", ...]}
Names are the catalog's adapter names (index.json `adapter_name`). Each becomes a
relative symlink in <project>/.claude/skills/<name> or .claude/agents/<name>.md that
points at the catalog source, so upstream syncs reach the project without copying.
Symlinks into this catalog that are no longer listed are removed; other files are
never touched. catalog.json, the links and `local_files` are listed in a managed block
of the project's .git/info/exclude, so they stay local to this clone.
"""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("adapters", ROOT / "scripts/build-adapters.py")
adapters = importlib.util.module_from_spec(spec)
spec.loader.exec_module(adapters)


def catalog(root=ROOT):
    found = {}
    for kind, items in (("skills", adapters.collect_skills(root)), ("agents", adapters.collect_agents(root))):
        adapters.assign_adapter_names(items)
        found[kind] = {item["adapter_name"]: root / item["path"] for item in items}
    return found


def desired(project, available):
    wanted = json.loads((project / ".claude/catalog.json").read_text())
    links, missing = {}, []
    for kind in ("skills", "agents"):
        for name in wanted.get(kind, []):
            source = available[kind].get(name)
            if source is None:
                missing.append(f"{kind}/{name}")
                continue
            link = project / ".claude" / kind / (name if kind == "skills" else f"{name}.md")
            links[link] = source
    return links, missing


EXCLUDE_BEGIN = "# BEGIN skills-and-agents (managed by link-skills.py)"
EXCLUDE_END = "# END skills-and-agents"


def exclude_block(project, links):
    wanted = json.loads((project / ".claude/catalog.json").read_text())
    paths = [".claude/catalog.json", *wanted.get("local_files", []),
             *sorted(link.relative_to(project).as_posix() for link in links)]
    return "\n".join([EXCLUDE_BEGIN, *("/" + p for p in paths), EXCLUDE_END]) + "\n"


def update_exclude(project, links, check=False):
    """Rewrite the managed block in .git/info/exclude; return True if it changed."""
    exclude = project / ".git/info/exclude"
    if not (project / ".git").is_dir():
        return False
    current = exclude.read_text() if exclude.exists() else ""
    if EXCLUDE_BEGIN in current:
        head, rest = current.split(EXCLUDE_BEGIN, 1)
        tail = rest.split(EXCLUDE_END, 1)[1].lstrip("\n") if EXCLUDE_END in rest else ""
    else:
        head, tail = current, ""
    if head and not head.endswith("\n"):
        head += "\n"
    updated = head + exclude_block(project, links) + tail
    if updated == current:
        return False
    if not check:
        exclude.parent.mkdir(parents=True, exist_ok=True)
        exclude.write_text(updated)
    return True


def ours(path, root=ROOT):
    return path.is_symlink() and (path.parent / os.readlink(path)).resolve().is_relative_to(root)


def link_project(project, available, check=False, root=ROOT):
    """Create, update and prune links; return (linked, changes, problems)."""
    links, missing = desired(project, available)
    problems = [f"unknown catalog name: {name}" for name in missing]
    stale = [p for kind in ("skills", "agents") if (project / ".claude" / kind).is_dir()
             for p in (project / ".claude" / kind).iterdir() if ours(p, root) and p not in links]
    changes = len(stale)
    for link, source in links.items():
        target = os.path.relpath(source, link.parent)
        if link.is_symlink() and os.readlink(link) == target:
            continue
        if link.exists() and not link.is_symlink():
            problems.append(f"{link.relative_to(project)} exists and is not a link; skipped")
            continue
        changes += 1
        if not check:
            link.parent.mkdir(parents=True, exist_ok=True)
            if link.is_symlink():
                link.unlink()
            link.symlink_to(target)
    if not check:
        for path in stale:
            path.unlink()
    changes += update_exclude(project, links, check)
    return len(links), changes, problems


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("projects", nargs="+", type=Path)
    parser.add_argument("--check", action="store_true", help="report drift without writing")
    args = parser.parse_args()
    available, status = catalog(), 0
    for project in (p.resolve() for p in args.projects):
        linked, changes, problems = link_project(project, available, args.check)
        for problem in problems:
            print(f"{project.name}: {problem}")
        print(f"{project.name}: {linked} linked, {changes} {'to change' if args.check else 'changed'}")
        if problems or (args.check and changes):
            status = 1
    sys.exit(status)


if __name__ == "__main__":
    main()
