#!/usr/bin/env python3
"""Refresh vendored sources from the upstream revisions listed in upstreams.json.

Each mapping copies an upstream path over a local path. Directory mappings delete
local files that upstream removed, except paths matched by `keep`. A single `*`
segment in `from` expands against the upstream checkout and fills `*` in `to`.
`quote_descriptions` quotes plain frontmatter descriptions that are invalid YAML.
Locked skills in skills-sh.lock.json are re-hashed when their source is synced.
"""
import argparse
from datetime import date
import fnmatch
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

import yaml

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "upstreams.json"
LOCK = ROOT / "skills-sh.lock.json"
# Files carrying recorded local modifications (skills-sh.lock.json) are never overwritten.
PROTECTED = set()
ALWAYS_EXCLUDE = (".git/*", "*/.git/*", ".DS_Store", "*/.DS_Store", "*/__pycache__/*", "__pycache__/*", "*.pyc")


def matches(rel, patterns):
    return any(fnmatch.fnmatch(rel, p) for p in patterns)


def tree(base, patterns):
    return {
        p.relative_to(base).as_posix(): p
        for p in sorted(base.rglob("*"))
        if p.is_file() and not p.is_symlink() and not matches(p.relative_to(base).as_posix(), patterns)
    }


def expand(checkout, mapping):
    src, dst = mapping["from"], mapping["to"]
    if "*" not in src:
        return [(checkout / src, ROOT / dst)]
    head, tail = src.split("*", 1)
    pairs = []
    for match in sorted((checkout / head).glob("*" + tail)):
        name = match.relative_to(checkout / head).parts[0]
        if match.is_dir() and not matches(name, mapping.get("skip", [])):
            pairs.append((match, ROOT / dst.replace("*", name, 1)))
    return pairs


def quote_description(data):
    """Quote a plain frontmatter description that YAML would misread; keep its text."""
    text = data.decode("utf-8")
    match = re.match(r"(---[ \t]*\n(?:.*\n)*?)(description:[ \t]*)([^\n]*)\n", text)
    if not match or match.group(3)[:1] in ("'", '"', ">", "|", ""):
        return data
    try:
        yaml.safe_load(match.group(3))
        return data
    except yaml.YAMLError:
        pass
    quoted = match.group(2) + json.dumps(match.group(3), ensure_ascii=False) + "\n"
    return (text[:match.start(2)] + quoted + text[match.end():]).encode("utf-8")


def sync_pair(src, dst, mapping, dry_run):
    if not src.exists():
        raise FileNotFoundError(f"upstream path missing: {src}")
    stats = {"added": 0, "changed": 0, "removed": 0}
    if src.is_file():
        files, local = {"": src}, {}
    else:
        files = tree(src, list(ALWAYS_EXCLUDE) + mapping.get("exclude", []))
        local = tree(dst, list(ALWAYS_EXCLUDE) + mapping.get("keep", [])) if dst.exists() else {}
    for rel, path in files.items():
        target = dst / rel if rel else dst
        if (mapping.get("existing_only") and not target.exists()) or target in PROTECTED:
            continue
        data = path.read_bytes()
        if mapping.get("quote_descriptions") and path.suffix == ".md":
            data = quote_description(data)
        if target.exists() and target.read_bytes() == data:
            continue
        stats["changed" if target.exists() else "added"] += 1
        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
    if src.is_dir() and mapping.get("delete", True) and not mapping.get("existing_only"):
        for rel, path in local.items():
            if rel not in files:
                stats["removed"] += 1
                if not dry_run:
                    path.unlink()
        if not dry_run:
            for d in sorted((p for p in dst.rglob("*") if p.is_dir()), reverse=True):
                if not any(d.iterdir()):
                    d.rmdir()
    return stats


def checkout_for(source, checkouts):
    repo = source["repository"].removeprefix("https://github.com/")
    if checkouts:
        path = Path(checkouts) / repo.replace("/", "_")
        if not path.is_dir():
            raise FileNotFoundError(f"no checkout for {repo} at {path}")
        return path
    path = Path(tempfile.mkdtemp(prefix="upstream-")) / repo.replace("/", "_")
    subprocess.run(["git", "clone", "-q", "--depth", "1", source["repository"], str(path)], check=True)
    return path


def refresh_lock(synced):
    lock = json.loads(LOCK.read_text())
    for skill in lock["skills"]:
        commit = synced.get(skill["repository"])
        if not commit:
            continue
        folder = ROOT / skill["path"]
        skill["commit"] = commit
        skill["files"] = {
            p.relative_to(folder).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(folder.rglob("*"))
            if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc"
        }
        for patch in skill["modifications"]:
            print(f"  kept local modification {skill['path']}/{patch['path']}: {patch['reason']}")
    LOCK.write_text(json.dumps(lock, indent=2) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ids", nargs="*", help="source ids to sync (default: all)")
    parser.add_argument("--checkouts", help="directory of existing clones named OWNER_REPO")
    parser.add_argument("--dry-run", action="store_true", help="report changes without writing")
    args = parser.parse_args()

    manifest = json.loads(MANIFEST.read_text())
    for skill in json.loads(LOCK.read_text())["skills"]:
        PROTECTED.update(ROOT / skill["path"] / patch["path"] for patch in skill["modifications"])
    sources = [s for s in manifest["sources"] if not args.ids or s["id"] in args.ids]
    unknown = set(args.ids) - {s["id"] for s in sources}
    if unknown:
        sys.exit(f"unknown source ids: {', '.join(sorted(unknown))}")
    synced = {}
    for source in sources:
        checkout = checkout_for(source, args.checkouts)
        commit = subprocess.run(["git", "-C", str(checkout), "rev-parse", "HEAD"],
                                check=True, capture_output=True, text=True).stdout.strip()
        totals = {"added": 0, "changed": 0, "removed": 0}
        for mapping in source["mappings"]:
            for src, dst in expand(checkout, mapping):
                for key, value in sync_pair(src, dst, mapping, args.dry_run).items():
                    totals[key] += value
        for lic in source["licenses"]:
            license_src, license_dst = checkout / lic["upstream"], ROOT / lic["file"]
            if not license_dst.exists() or license_dst.read_bytes() != license_src.read_bytes():
                print(f"  license changed: {lic['file']}")
                if not args.dry_run:
                    shutil.copyfile(license_src, license_dst)
        print(f"{source['id']} {(source.get('commit') or 'unrecorded')[:10]} -> {commit[:8]}: {totals}")
        if not args.dry_run:
            source["commit"], source["synced_on"] = commit, date.today().isoformat()
            synced[source["repository"]] = commit
    if not args.dry_run:
        MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
        refresh_lock(synced)


if __name__ == "__main__":
    main()
