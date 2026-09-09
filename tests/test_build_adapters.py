import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location(
    "adapters", Path(__file__).resolve().parents[1] / "scripts/build-adapters.py")
adapters = importlib.util.module_from_spec(spec)
spec.loader.exec_module(adapters)


class AdapterTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def write(self, path, content):
        dest = self.root / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content)
        return dest

    def source(self, path, name="example", extra=""):
        return self.write(path, f"---\nname: {name}\ndescription: Useful workflow\n{extra}---\n\nBody.\n")

    def test_classification_and_supporting_resources(self):
        self.source("skills/design/example/SKILL.md", "design-example")
        self.source("agents/coding/vendor/plugin/skills/example/SKILL.md")
        self.write("agents/coding/vendor/plugin/skills/example/references/guide.md", "Guide")
        self.source("agents/coding/vendor/plugin/skills/example/references/sample.md", "sample")
        self.source("agents/coding/vendor/plugin/agents/worker.md", "worker")
        self.write("agents/coding/vendor/plugin/commands/run.md", "# Run workflow\n\n$ARGUMENTS\n")
        self.source("agents/coding/vendor/plugin/templates/example.md", "template")
        self.assertEqual(adapters.build(self.root), 0)
        manifest = json.loads((self.root / "index.json").read_text())
        self.assertEqual([a["name"] for a in manifest["agents"]], ["worker"])
        self.assertEqual(len(manifest["skills"]), 2)
        self.assertEqual(len(manifest["commands"]), 1)
        self.assertEqual((self.root / ".claude/skills/example/references/guide.md").read_text(), "Guide")
        self.assertIn("$ARGUMENTS", (self.root / ".claude/commands/run.md").read_text())

    def test_duplicate_names_agree_with_frontmatter(self):
        for vendor in ("alpha", "beta"):
            self.source(f"agents/coding/{vendor}/agents/reviewer.md", "reviewer")
            self.source(f"skills/design/{vendor}/SKILL.md", "shared-skill")
        adapters.build(self.root)
        manifest = json.loads((self.root / "index.json").read_text())
        for kind in ("agents", "skills"):
            names = [a["adapter_name"] for a in manifest[kind]]
            self.assertEqual(len(names), len(set(names)))
            for item in manifest[kind]:
                fm = adapters.parse_frontmatter((self.root / item["adapter_path"]).read_text())
                self.assertEqual(fm["name"], item["adapter_name"])
        self.assertEqual(adapters.build(self.root, check=True), 0)

    def test_yaml_nested_metadata_and_multiline(self):
        metadata = adapters.parse_frontmatter(
            '---\nname: example\ndescription: >-\n  First line:\n  second line\n'
            'tools: [Read, Edit]\nmetadata:\n  name: nested\n---\n')
        self.assertEqual(metadata["name"], "example")
        self.assertEqual(metadata["description"], "First line: second line")
        self.assertEqual(metadata["tools"], ["Read", "Edit"])

    def test_check_is_read_only_and_detects_stale_extra_missing_files(self):
        self.source("skills/coding/example/SKILL.md")
        adapters.build(self.root)
        output = self.root / ".claude/skills/example/SKILL.md"
        output.write_text("stale")
        self.assertEqual(adapters.build(self.root, check=True), 1)
        self.assertEqual(output.read_text(), "stale")
        adapters.build(self.root)
        extra = self.write(".claude/agents/stale.md", "obsolete")
        self.assertEqual(adapters.build(self.root, check=True), 1)
        self.assertTrue(extra.exists())
        adapters.build(self.root)
        self.assertFalse(extra.exists())
        output.unlink()
        self.assertEqual(adapters.build(self.root, check=True), 1)
        self.assertFalse(output.exists())

    def test_malformed_source_does_not_replace_existing_outputs(self):
        self.source("skills/coding/example/SKILL.md")
        adapters.build(self.root)
        before = (self.root / "index.json").read_bytes()
        self.write("skills/coding/broken/SKILL.md", "---\nname: broken\ndescription: invalid: yaml\n---\n")
        with self.assertRaisesRegex(ValueError, "broken/SKILL.md"):
            adapters.build(self.root)
        self.assertEqual((self.root / "index.json").read_bytes(), before)

    def test_sanitized_collision_fails_before_writes(self):
        self.source("skills/design/a_b/SKILL.md", "duplicate")
        self.source("skills/design/a-b/SKILL.md", "duplicate")
        with self.assertRaisesRegex(ValueError, "collision"):
            adapters.build(self.root)
        self.assertFalse((self.root / "index.json").exists())


if __name__ == "__main__":
    unittest.main()
