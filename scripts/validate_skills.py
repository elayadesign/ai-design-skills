#!/usr/bin/env python3
"""Validate every skills/<name>/SKILL.md against the Agent Skills spec.

Checks the frontmatter rules from https://agentskills.io/specification:
  - the file starts with a YAML frontmatter block delimited by ---
  - name: required, 1-64 chars, lowercase letters, digits and single
    hyphens, no leading or trailing hyphen, equal to the folder name
  - description: required, non-empty, at most 1024 chars
  - compatibility: optional, 1-500 chars when present

Usage:
    python scripts/validate_skills.py [skills_dir]

Exits with status 1 if any skill is invalid, 0 otherwise.
"""

import os
import re
import sys
from pathlib import Path

import yaml

NAME_MAX = 64
DESCRIPTION_MAX = 1024
COMPATIBILITY_MAX = 500
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def read_frontmatter(text):
    """Return (frontmatter_dict, error). Exactly one of them is None."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "file must start with a '---' frontmatter line"

    for end, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            break
    else:
        return None, "frontmatter is missing its closing '---' line"

    try:
        data = yaml.safe_load("\n".join(lines[1:end]))
    except yaml.YAMLError as exc:
        return None, f"frontmatter is not valid YAML: {exc}"

    if not isinstance(data, dict):
        return None, "frontmatter must be a set of 'key: value' fields"
    return data, None


def check_text_field(data, field, max_len, required):
    """Return a list of problems for a string field."""
    if field not in data:
        return [f"'{field}' is required"] if required else []

    value = data[field]
    if not isinstance(value, str):
        return [f"'{field}' must be text"]
    if not value.strip():
        return [f"'{field}' must not be empty"]
    if len(value) > max_len:
        return [f"'{field}' is {len(value)} characters, the limit is {max_len}"]
    return []


def validate_skill(skill_dir):
    """Return a list of problems found in one skill folder."""
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return ["SKILL.md is missing"]

    data, error = read_frontmatter(skill_file.read_text(encoding="utf-8"))
    if error:
        return [error]

    problems = check_text_field(data, "name", NAME_MAX, required=True)
    name = data.get("name")
    if not problems:
        if not NAME_PATTERN.match(name):
            problems.append(
                f"'name' is '{name}', use only lowercase letters, digits and "
                "single hyphens, not at the start or end"
            )
        if name != skill_dir.name:
            problems.append(
                f"'name' is '{name}' but the folder is '{skill_dir.name}', "
                "they must match"
            )

    problems += check_text_field(data, "description", DESCRIPTION_MAX, required=True)
    problems += check_text_field(data, "compatibility", COMPATIBILITY_MAX, required=False)
    return problems


def report(path, problem):
    """Print a problem, as a GitHub annotation when running in Actions."""
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print(f"::error file={path}::{problem}")
    else:
        print(f"{path}: {problem}")


def main(argv):
    skills_root = Path(argv[1]) if len(argv) > 1 else Path("skills")
    if not skills_root.is_dir():
        print(f"{skills_root}: folder not found")
        return 1

    skill_dirs = sorted(p for p in skills_root.iterdir() if p.is_dir())
    if not skill_dirs:
        print(f"{skills_root}: no skills found")
        return 1

    failed = 0
    for skill_dir in skill_dirs:
        problems = validate_skill(skill_dir)
        for problem in problems:
            report(skill_dir / "SKILL.md", problem)
        if problems:
            failed += 1

    print(f"Checked {len(skill_dirs)} skill(s), {failed} with problems.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
