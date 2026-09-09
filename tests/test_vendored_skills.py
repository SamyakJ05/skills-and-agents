import hashlib
import json
from pathlib import Path
import re
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]


class VendoredSkillTests(unittest.TestCase):
    def test_locked_skills_match_recorded_contents_and_license_evidence(self):
        lock = json.loads((ROOT / 'skills-sh.lock.json').read_text())
        names = set()
        for skill in lock['skills']:
            with self.subTest(skill=skill['name']):
                self.assertRegex(skill['commit'], r'^[a-f0-9]{40}$')
                self.assertNotIn(skill['name'], names)
                names.add(skill['name'])
                folder = ROOT / skill['path']
                actual = {
                    p.relative_to(folder).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                    for p in folder.rglob('*') if p.is_file()
                    and '__pycache__' not in p.parts and p.suffix != '.pyc'
                }
                self.assertEqual(actual, skill['files'])
                text = (folder / 'SKILL.md').read_text()
                fm = yaml.safe_load(re.match(r'---\n(.*?)\n---', text, re.S).group(1))
                self.assertEqual(fm['name'], skill['name'])
                self.assertTrue(fm['description'])
                self.assertTrue((ROOT / skill['license_evidence_path']).is_file())
                for patch in skill['modifications']:
                    self.assertIn(patch['path'], actual)
                for added in skill['added_files']:
                    self.assertIn(added, actual)


if __name__ == '__main__':
    unittest.main()
