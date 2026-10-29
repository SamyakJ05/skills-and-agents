import importlib.util
from pathlib import Path
import tempfile
import unittest

import yaml

spec = importlib.util.spec_from_file_location(
    "sync", Path(__file__).resolve().parents[1] / "scripts/sync-upstreams.py")
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.up = Path(self.temporary.name) / "up"
        self.root = Path(self.temporary.name) / "repo"
        self.root.mkdir()
        self.addCleanup(setattr, sync, "ROOT", sync.ROOT)
        sync.ROOT = self.root

    def write(self, base, path, content):
        dest = base / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content)

    def run_mapping(self, mapping, dry_run=False):
        totals = {"added": 0, "changed": 0, "removed": 0}
        for src, dst in sync.expand(self.up, mapping):
            for key, value in sync.sync_pair(src, dst, mapping, dry_run).items():
                totals[key] += value
        return totals

    def test_directory_sync_deletes_removed_files_but_keeps_local_additions(self):
        self.write(self.up, "skills/a/SKILL.md", "new")
        self.write(self.up, "skills/a/tests/t.py", "test")
        self.write(self.root, "local/a/SKILL.md", "old")
        self.write(self.root, "local/a/gone.md", "stale")
        self.write(self.root, "local/a/LICENSE.txt", "mine")
        stats = self.run_mapping({"from": "skills/a", "to": "local/a",
                                  "exclude": ["tests/*"], "keep": ["LICENSE.txt"]})
        self.assertEqual(stats, {"added": 0, "changed": 1, "removed": 1})
        self.assertEqual(sorted(p.name for p in (self.root / "local/a").iterdir()), ["LICENSE.txt", "SKILL.md"])

    def test_glob_expansion_and_existing_only(self):
        self.write(self.up, "plugins/p1/commands/run.md", "v2")
        self.write(self.up, "plugins/p1/commands/new.md", "x")
        self.write(self.up, "plugins/p2/commands/other.md", "x")
        self.write(self.root, "agents/p1/commands/run.md", "v1")
        stats = self.run_mapping({"from": "plugins/*/commands", "to": "agents/*/commands", "existing_only": True})
        self.assertEqual(stats["changed"], 1)
        self.assertEqual((self.root / "agents/p1/commands/run.md").read_text(), "v2")
        self.assertFalse((self.root / "agents/p1/commands/new.md").exists())
        self.assertFalse((self.root / "agents/p2").exists())

    def test_dry_run_writes_nothing(self):
        self.write(self.up, "s/SKILL.md", "x")
        self.assertEqual(self.run_mapping({"from": "s", "to": "d"}, dry_run=True)["added"], 1)
        self.assertFalse((self.root / "d").exists())

    def test_quote_description_repairs_invalid_yaml_only(self):
        broken = b"---\nname: a\ndescription: Use when: 'x', \"y\"\ntools: Read\n---\nBody\n"
        fixed = sync.quote_description(broken).decode()
        fm = yaml.safe_load(fixed.split("---")[1])
        self.assertEqual(fm["description"], "Use when: 'x', \"y\"")
        self.assertEqual(fm["tools"], "Read")
        valid = b"---\nname: a\ndescription: Plain text\n---\n"
        self.assertEqual(sync.quote_description(valid), valid)


if __name__ == "__main__":
    unittest.main()
