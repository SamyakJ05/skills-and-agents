import importlib.util
import json
import os
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location(
    "link", Path(__file__).resolve().parents[1] / "scripts/link-skills.py")
link = importlib.util.module_from_spec(spec)
spec.loader.exec_module(link)


class LinkTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        base = Path(self.temporary.name).resolve()
        self.root, self.project = base / "catalog", base / "site"
        self.write(self.root / "skills/design/gsap/SKILL.md", "---\nname: gsap\ndescription: d\n---\n")
        self.write(self.root / "agents/coding/v/agents/rev.md", "---\nname: rev\ndescription: d\n---\n")
        self.write(self.project / ".claude/skills/own/SKILL.md", "mine")

    def write(self, path, text):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def run_link(self, wanted, check=False):
        self.write(self.project / ".claude/catalog.json", json.dumps(wanted))
        return link.link_project(self.project, link.catalog(self.root), check, self.root)

    def test_links_relative_and_prunes_only_catalog_links(self):
        self.assertEqual(self.run_link({"skills": ["gsap"], "agents": ["rev"]})[:2], (2, 2))
        skill = self.project / ".claude/skills/gsap"
        self.assertFalse(os.path.isabs(os.readlink(skill)))
        self.assertTrue((skill / "SKILL.md").is_file())
        self.assertTrue((self.project / ".claude/agents/rev.md").is_file())
        self.assertEqual(self.run_link({"skills": ["gsap"], "agents": ["rev"]}, check=True)[1], 0)
        self.assertEqual(self.run_link({"skills": []})[1], 2)
        self.assertFalse(skill.is_symlink())
        self.assertTrue((self.project / ".claude/skills/own/SKILL.md").is_file())

    def test_local_exclude_block_is_managed(self):
        (self.project / ".git/info").mkdir(parents=True)
        (self.project / ".git/info/exclude").write_text("# user rule\n*.log\n")
        self.write(self.project / ".claude/catalog.json",
                   json.dumps({"skills": ["gsap"], "agents": ["rev"], "local_files": ["AGENTS.md"]}))
        link.link_project(self.project, link.catalog(self.root), False, self.root)
        text = (self.project / ".git/info/exclude").read_text()
        self.assertTrue(text.startswith("# user rule\n*.log\n"))
        for path in ("/.claude/catalog.json", "/AGENTS.md", "/.claude/skills/gsap", "/.claude/agents/rev.md"):
            self.assertIn(path + "\n", text)
        self.assertEqual(self.run_link({"skills": ["gsap"], "agents": [], "local_files": ["AGENTS.md"]})[1], 2)
        text = (self.project / ".git/info/exclude").read_text()
        self.assertNotIn("/.claude/agents/rev.md", text)
        self.assertEqual(text.count(link.EXCLUDE_BEGIN), 1)

    def test_unknown_names_and_real_dirs_are_reported(self):
        _, _, problems = self.run_link({"skills": ["missing", "own"]})
        self.assertIn("unknown catalog name: skills/missing", problems)
        self.write(self.root / "skills/design/own/SKILL.md", "---\nname: own\ndescription: d\n---\n")
        _, _, problems = self.run_link({"skills": ["own"]})
        self.assertTrue(any("not a link" in p for p in problems))


if __name__ == "__main__":
    unittest.main()
