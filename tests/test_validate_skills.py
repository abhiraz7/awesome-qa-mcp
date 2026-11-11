from pathlib import Path
import tempfile
import unittest

from scripts.validate_skills import (
    iter_markdown_links,
    parse_frontmatter,
    validate_repository,
)


class ParseFrontmatterTests(unittest.TestCase):
    def test_accepts_required_fields(self):
        content = "---\nname: sample-skill\ndescription: A sample QA skill.\n---\n\n# Sample\n"
        name, errors = parse_frontmatter(content, "sample-skill")
        self.assertEqual(name, "sample-skill")
        self.assertEqual(errors, [])

    def test_accepts_quoted_fields(self):
        content = '---\nname: "sample-skill"\ndescription: "A sample QA skill."\n---\n'
        name, errors = parse_frontmatter(content, "sample-skill")
        self.assertEqual(name, "sample-skill")
        self.assertEqual(errors, [])

    def test_rejects_missing_opening_delimiter(self):
        _, errors = parse_frontmatter("name: sample-skill\n---\n", "sample-skill")
        self.assertTrue(any("opening YAML frontmatter delimiter" in error for error in errors))

    def test_rejects_missing_description(self):
        content = "---\nname: sample-skill\n---\n"
        _, errors = parse_frontmatter(content, "sample-skill")
        self.assertTrue(any("description" in error for error in errors))

    def test_rejects_duplicate_required_field(self):
        content = (
            "---\nname: sample-skill\nname: another-name\n"
            "description: A sample.\n---\n"
        )
        _, errors = parse_frontmatter(content, "sample-skill")
        self.assertTrue(any("duplicate 'name'" in error for error in errors))

    def test_rejects_directory_name_mismatch(self):
        content = "---\nname: other-skill\ndescription: A sample.\n---\n"
        _, errors = parse_frontmatter(content, "sample-skill")
        self.assertTrue(any("does not match skill directory" in error for error in errors))

    def test_rejects_invalid_skill_name(self):
        content = "---\nname: Sample_Skill\ndescription: A sample.\n---\n"
        _, errors = parse_frontmatter(content, "Sample_Skill")
        self.assertTrue(any("lowercase letters" in error for error in errors))


class MarkdownLinkTests(unittest.TestCase):
    def test_finds_links_but_ignores_code_examples(self):
        inline_code = chr(96) + "[inline](missing-inline.md)" + chr(96)
        content = (
            "[external](https://example.com) [section](#heading)\n"
            + inline_code
            + "\n~~~markdown\n[example](missing-fenced.md)\n~~~\n"
            + "[local](templates/guide.md)\n"
        )
        links = list(iter_markdown_links(content))
        self.assertEqual(
            links,
            [
                (1, "https://example.com"),
                (1, "#heading"),
                (6, "templates/guide.md"),
            ],
        )

    def test_checks_existing_relative_file_and_ignores_external_links(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            skill_dir = root / ".claude" / "skills" / "sample-skill"
            (skill_dir / "templates").mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                "---\nname: sample-skill\ndescription: A sample.\n---\n"
                "[Guide](templates/guide.md) [external](https://example.com) [section](#heading)\n",
                encoding="utf-8",
            )
            (skill_dir / "templates" / "guide.md").write_text("# Guide\n", encoding="utf-8")
            errors, skills, markdown_files = validate_repository(root)
            self.assertEqual(errors, [])
            self.assertEqual(skills, 1)
            self.assertEqual(markdown_files, 2)

    def test_reports_broken_relative_file(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            skill_dir = root / ".claude" / "skills" / "sample-skill"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                "---\nname: sample-skill\ndescription: A sample.\n---\n"
                "[Missing](templates/missing.md)\n",
                encoding="utf-8",
            )
            errors, _, _ = validate_repository(root)
            self.assertTrue(any("broken relative link" in error for error in errors))

    def test_rejects_links_that_escape_repository(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory) / "repo"
            skill_dir = root / ".claude" / "skills" / "sample-skill"
            skill_dir.mkdir(parents=True)
            (skill_dir / "SKILL.md").write_text(
                "---\nname: sample-skill\ndescription: A sample.\n---\n"
                "[Outside](../../../../outside.md)\n",
                encoding="utf-8",
            )
            errors, _, _ = validate_repository(root)
            self.assertTrue(any("escapes the repository" in error for error in errors))

    def test_rejects_duplicate_skill_names(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            for directory in ("sample-skill", "another-folder"):
                skill_dir = root / ".claude" / "skills" / directory
                skill_dir.mkdir(parents=True)
                (skill_dir / "SKILL.md").write_text(
                    "---\nname: sample-skill\ndescription: A sample.\n---\n",
                    encoding="utf-8",
                )
            errors, skills, _ = validate_repository(root)
            self.assertEqual(skills, 2)
            self.assertTrue(any("duplicate skill name" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
