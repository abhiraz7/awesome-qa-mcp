#!/usr/bin/env python3
"""Validate the structure and result-log coverage of QA evaluation matrices."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SKILLS_DIR = Path(".claude") / "skills"
CASE_ID_PREFIX_RE = re.compile(r"^[A-Z][A-Z0-9]*-")
CASE_HEADING_RE = re.compile(
    r"^###\s+(?P<case_id>[A-Z][A-Z0-9]*-\d{2,3})\s+—\s+.+$"
)
RESULT_ROW_RE = re.compile(
    r"^\|\s*(?P<case_id>[A-Z][A-Z0-9]*-\d{2,3})\s*\|\s*"
    r"(?P<outcome>[^|]+?)\s*\|"
)
VALID_OUTCOMES = {"PASS", "PARTIAL", "FAIL", "NOT EVALUATED"}
REQUIRED_CASE_MARKERS = (
    "**Prompt**",
    "**Mandatory observations**",
    "**Hard failure:**",
)


def extract_section(lines: list[str], title: str) -> list[str] | None:
    """Return the contents of a level-two Markdown section, excluding its heading."""
    heading = f"## {title}"
    try:
        start = lines.index(heading) + 1
    except ValueError:
        return None

    end = next(
        (index for index in range(start, len(lines)) if lines[index].startswith("## ")),
        len(lines),
    )
    return lines[start:end]


def validate_evaluation_matrix(
    matrix_path: Path, repository_root: Path
) -> list[str]:
    """Check case structure, unique IDs, and one valid result-log row per case."""
    repository_root = repository_root.resolve()
    matrix_path = matrix_path.resolve()
    try:
        source = matrix_path.relative_to(repository_root)
    except ValueError:
        source = matrix_path

    try:
        lines = matrix_path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeError) as exc:
        return [f"{source}: cannot read evaluation matrix: {exc}"]

    errors: list[str] = []
    regression_lines = extract_section(lines, "Regression cases")
    result_lines = extract_section(lines, "Result log")

    if regression_lines is None:
        errors.append(f"{source}: missing '## Regression cases' section")
    if result_lines is None:
        errors.append(f"{source}: missing '## Result log' section")
    if regression_lines is None or result_lines is None:
        return errors

    case_ids: list[str] = []
    case_blocks: list[tuple[str, list[str]]] = []
    current_id: str | None = None
    current_block: list[str] = []

    for line in regression_lines:
        if line.startswith("### "):
            if current_id is not None:
                case_blocks.append((current_id, current_block))
            match = CASE_HEADING_RE.fullmatch(line)
            if not match:
                errors.append(f"{source}: invalid regression case heading: '{line}'")
                current_id = None
                current_block = []
                continue
            current_id = match.group("case_id")
            case_ids.append(current_id)
            current_block = [line]
        elif current_id is not None:
            current_block.append(line)

    if current_id is not None:
        case_blocks.append((current_id, current_block))

    if not case_ids:
        errors.append(f"{source}: no regression cases found under '## Regression cases'")

    seen_cases: set[str] = set()
    for case_id, block in case_blocks:
        if case_id in seen_cases:
            errors.append(f"{source}: duplicate regression case ID '{case_id}'")
        seen_cases.add(case_id)
        block_text = "\n".join(block)
        for marker in REQUIRED_CASE_MARKERS:
            if marker not in block_text:
                errors.append(
                    f"{source}: case {case_id} is missing required section '{marker}'"
                )

    result_ids: list[str] = []
    for line_number, line in enumerate(result_lines, start=1):
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue

        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if not cells or not CASE_ID_PREFIX_RE.match(cells[0]):
            continue

        match = RESULT_ROW_RE.fullmatch(stripped)
        if not match:
            errors.append(
                f"{source}: malformed result-log row at section line {line_number}: '{stripped}'"
            )
            continue

        case_id = match.group("case_id")
        outcome = match.group("outcome").strip().upper()
        result_ids.append(case_id)

        if outcome not in VALID_OUTCOMES:
            errors.append(
                f"{source}: case {case_id} has invalid evaluation outcome '{outcome}'"
            )

    if not result_ids:
        errors.append(f"{source}: result log contains no case rows")

    seen_results: set[str] = set()
    for case_id in result_ids:
        if case_id in seen_results:
            errors.append(f"{source}: duplicate result-log row for case '{case_id}'")
        seen_results.add(case_id)

    for case_id in sorted(seen_cases - seen_results):
        errors.append(f"{source}: case {case_id} is missing from the result log")
    for case_id in sorted(seen_results - seen_cases):
        errors.append(f"{source}: result log contains unknown case ID '{case_id}'")

    return errors


def validate_repository(repository_root: Path) -> tuple[list[str], int]:
    """Validate every evaluation matrix stored under the repository's skill folders."""
    repository_root = repository_root.resolve()
    skills_root = repository_root / SKILLS_DIR
    if not skills_root.is_dir():
        return [f"skills directory not found: {SKILLS_DIR}"], 0

    matrices = sorted(skills_root.rglob("*evaluation-matrix.md"))
    errors: list[str] = []
    for matrix in matrices:
        errors.extend(validate_evaluation_matrix(matrix, repository_root))
    return errors, len(matrices)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check QA evaluation-matrix case structure and result-log coverage."
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="repository root (defaults to the parent of the scripts directory)",
    )
    args = parser.parse_args(argv)

    errors, matrix_count = validate_repository(args.root)
    if errors:
        print("Evaluation-matrix validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        print(f"Checked {matrix_count} evaluation matrix file(s).", file=sys.stderr)
        return 1

    if matrix_count == 0:
        print("No evaluation matrices found; nothing to validate.")
    else:
        print(
            f"Evaluation-matrix validation passed: {matrix_count} file(s); "
            "case IDs, required sections, and result-log coverage are consistent."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
