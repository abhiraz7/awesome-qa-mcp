#!/usr/bin/env python3
"""Validate Claude skill frontmatter and local Markdown links."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

SKILLS_DIR = Path(".claude") / "skills"
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FENCE_RE = re.compile(r"^\s{0,3}(\x60{3,}|~{3,})(.*)$")
INLINE_CODE_RE = re.compile(r"(?<!\x60)\x60+.*?\x60+(?!\x60)")
MARKDOWN_LINK_RE = re.compile(
    r"!?\\[[^\\]]*\\]\\((?P<target><[^>]*>|[^)\\s]+)(?:\\s+[^)]*)?\\)"
)


def _frontmatter_scalar(value: str, field: str, errors: list[str]) -> str:
    value = value.strip()
    if value.startswith(("'", '"')):
        quote = value[0]
        if len(value) < 2 or value[-1] != quote:
            errors.append(f"frontmatter field '{field}' has an unterminated quoted value")
            return ""
        value = value[1:-1]
    return value.strip()


def parse_frontmatter(content: str, expected_directory: str) -> tuple[str | None, list[str]]:
    """Read required simple YAML frontmatter fields without third-party packages.

    This validates the fields used by this repository; it is not a full YAML parser.
    Skill files should keep name and description as scalar fields.
    """
    errors: list[str] = []
    lines = content.splitlines()

    if not lines or lines[0].strip() != "---":
        return None, ["missing opening YAML frontmatter delimiter ('---')"]

    closing_index = next(
        (index for index in range(1, len(lines)) if lines[index].strip() == "---"),
        None,
    )
    if closing_index is None:
        return None, ["missing closing YAML frontmatter delimiter ('---')"]

    fields: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:closing_index], start=2):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        key, separator, raw_value = line.partition(":")
        if not separator:
            continue
        key = key.strip()
        if key not in {"name", "description"}:
            continue
        if key in fields:
            errors.append(f"frontmatter line {line_number}: duplicate '{key}' field")
            continue
        fields[key] = _frontmatter_scalar(raw_value, key, errors)

    name = fields.get("name", "").strip()
    description = fields.get("description", "").strip()

    if not name:
        errors.append("frontmatter is missing a non-empty 'name' field")
    else:
        if not SKILL_NAME_RE.fullmatch(name):
            errors.append(
                "frontmatter 'name' must use lowercase letters, numbers, and single hyphens"
            )
        if name != expected_directory:
            errors.append(
                f"frontmatter name '{name}' does not match skill directory '{expected_directory}'"
            )

    if not description:
        errors.append("frontmatter is missing a non-empty 'description' field")

    return name or None, errors


def iter_markdown_links(content: str):
    """Yield (line_number, destination) for inline Markdown links outside code blocks."""
    in_fence: tuple[str, int] | None = None

    for line_number, line in enumerate(content.splitlines(), start=1):
        fence_match = FENCE_RE.match(line)
        if in_fence is not None:
            if fence_match:
                marker, remainder = fence_match.groups()
                if (
                    marker[0] == in_fence[0]
                    and len(marker) >= in_fence[1]
                    and not remainder.strip()
                ):
                    in_fence = None
            continue

        if fence_match:
            marker, _ = fence_match.groups()
            in_fence = (marker[0], len(marker))
            continue

        searchable_line = INLINE_CODE_RE.sub("", line)
        for match in MARKDOWN_LINK_RE.finditer(searchable_line):
            destination = match.group("target").strip()
            if destination.startswith("<") and destination.endswith(">"):
                destination = destination[1:-1]
            if destination:
                yield line_number, destination


def validate_markdown_links(markdown_path: Path, repository_root: Path) -> list[str]:
    errors: list[str] = []
    relative_source = markdown_path.relative_to(repository_root)

    try:
        content = markdown_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return [f"{relative_source}: cannot read Markdown file: {exc}"]

    for line_number, destination in iter_markdown_links(content):
        try:
            parsed = urlsplit(destination)
        except ValueError as exc:
            errors.append(
                f"{relative_source}:{line_number}: invalid Markdown link '{destination}': {exc}"
            )
            continue

        # External links and fragment-only links are outside this local-file check.
        if parsed.scheme or parsed.netloc or not parsed.path or parsed.path.startswith("/"):
            continue

        target = (markdown_path.parent / unquote(parsed.path)).resolve()
        try:
            target.relative_to(repository_root)
        except ValueError:
            errors.append(
                f"{relative_source}:{line_number}: link escapes the repository: '{destination}'"
            )
            continue

        if not target.exists():
            errors.append(
                f"{relative_source}:{line_number}: broken relative link '{destination}'"
            )

    return errors


def validate_repository(repository_root: Path) -> tuple[list[str], int, int]:
    repository_root = repository_root.resolve()
    skills_root = repository_root / SKILLS_DIR
    errors: list[str] = []

    if not skills_root.is_dir():
        return [f"skills directory not found: {SKILLS_DIR}"], 0, 0

    skill_files = sorted(skills_root.rglob("SKILL.md"))
    if not skill_files:
        errors.append(f"no SKILL.md files found under {SKILLS_DIR}")

    seen_names: dict[str, Path] = {}
    for skill_file in skill_files:
        try:
            content = skill_file.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{skill_file.relative_to(repository_root)}: cannot read skill: {exc}")
            continue

        name, frontmatter_errors = parse_frontmatter(content, skill_file.parent.name)
        source = skill_file.relative_to(repository_root)
        errors.extend(f"{source}: {message}" for message in frontmatter_errors)

        if name:
            previous = seen_names.get(name)
            if previous is not None:
                errors.append(
                    f"{source}: duplicate skill name '{name}' also used by "
                    f"'{previous.relative_to(repository_root)}'"
                )
            else:
                seen_names[name] = skill_file

    markdown_files = sorted(skills_root.rglob("*.md"))
    for markdown_file in markdown_files:
        errors.extend(validate_markdown_links(markdown_file, repository_root))

    return errors, len(skill_files), len(markdown_files)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check Claude skill frontmatter and relative Markdown links."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (defaults to the parent of the scripts directory)",
    )
    args = parser.parse_args(argv)

    errors, skill_count, markdown_count = validate_repository(args.root)
    if errors:
        print("Skill validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        print(
            f"Checked {skill_count} skill file(s) and {markdown_count} Markdown file(s).",
            file=sys.stderr,
        )
        return 1

    print(
        f"Skill validation passed: {skill_count} skill file(s), "
        f"{markdown_count} Markdown file(s); no broken relative links found."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
