"""Tests for scripts/validate_skills.py. Run with: python -m unittest discover tests"""

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from validate_skills import main, validate_skill  # noqa: E402

VALID_DESCRIPTION = "Builds landing pages. Use when working on a marketing site."


class ValidateSkillTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def make_skill(self, folder, content):
        skill_dir = self.root / folder
        skill_dir.mkdir()
        if content is not None:
            (skill_dir / "SKILL.md").write_text(content, encoding="utf-8")
        return skill_dir

    def frontmatter(self, name="my-skill", description=VALID_DESCRIPTION, extra=""):
        return f"---\nname: {name}\ndescription: {description}\n{extra}---\n\n# Body\n"

    def test_valid_skill_has_no_problems(self):
        skill = self.make_skill("my-skill", self.frontmatter())
        self.assertEqual(validate_skill(skill), [])

    def test_multiline_description_is_accepted(self):
        content = "---\nname: my-skill\ndescription: >\n  First line\n  second line.\n---\n"
        skill = self.make_skill("my-skill", content)
        self.assertEqual(validate_skill(skill), [])

    def test_missing_skill_file(self):
        skill = self.make_skill("my-skill", None)
        self.assertEqual(validate_skill(skill), ["SKILL.md is missing"])

    def test_missing_opening_delimiter(self):
        skill = self.make_skill("my-skill", "# No frontmatter\n")
        self.assertIn("must start with", validate_skill(skill)[0])

    def test_missing_closing_delimiter(self):
        skill = self.make_skill("my-skill", "---\nname: my-skill\n")
        self.assertIn("closing", validate_skill(skill)[0])

    def test_invalid_yaml(self):
        skill = self.make_skill("my-skill", "---\nname: [unclosed\n---\n")
        self.assertIn("not valid YAML", validate_skill(skill)[0])

    def test_name_must_match_folder(self):
        skill = self.make_skill("other-folder", self.frontmatter())
        problems = validate_skill(skill)
        self.assertEqual(len(problems), 1)
        self.assertIn("must match", problems[0])

    def test_name_format_rules(self):
        for bad in ["My-Skill", "-skill", "skill-", "my--skill", "my_skill"]:
            with self.subTest(name=bad):
                skill = self.make_skill(bad, self.frontmatter(name=bad))
                problems = validate_skill(skill)
                self.assertTrue(any("lowercase" in p for p in problems), problems)

    def test_name_too_long(self):
        long_name = "a" * 65
        skill = self.make_skill(long_name, self.frontmatter(name=long_name))
        self.assertIn("limit is 64", validate_skill(skill)[0])

    def test_name_at_limit_is_accepted(self):
        name = "a" * 64
        skill = self.make_skill(name, self.frontmatter(name=name))
        self.assertEqual(validate_skill(skill), [])

    def test_missing_description(self):
        skill = self.make_skill("my-skill", "---\nname: my-skill\n---\n")
        self.assertEqual(validate_skill(skill), ["'description' is required"])

    def test_empty_description(self):
        skill = self.make_skill("my-skill", self.frontmatter(description='""'))
        self.assertEqual(validate_skill(skill), ["'description' must not be empty"])

    def test_description_length_limit(self):
        at_limit = self.make_skill("my-skill", self.frontmatter(description="x" * 1024))
        self.assertEqual(validate_skill(at_limit), [])

        over = self.make_skill("over", self.frontmatter(name="over", description="x" * 1025))
        self.assertIn("limit is 1024", validate_skill(over)[0])

    def test_compatibility_length_limit(self):
        extra = f"compatibility: {'x' * 501}\n"
        skill = self.make_skill("my-skill", self.frontmatter(extra=extra))
        self.assertIn("limit is 500", validate_skill(skill)[0])

    def test_non_text_name(self):
        skill = self.make_skill("my-skill", self.frontmatter(name="123"))
        self.assertEqual(validate_skill(skill), ["'name' must be text"])


class MainTest(unittest.TestCase):
    def test_exit_codes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            good = root / "good-skill"
            good.mkdir()
            (good / "SKILL.md").write_text(
                f"---\nname: good-skill\ndescription: {VALID_DESCRIPTION}\n---\n",
                encoding="utf-8",
            )
            self.assertEqual(main(["prog", str(root)]), 0)

            (root / "broken").mkdir()
            self.assertEqual(main(["prog", str(root)]), 1)

    def test_missing_folder_fails(self):
        self.assertEqual(main(["prog", "does-not-exist"]), 1)


if __name__ == "__main__":
    unittest.main()
