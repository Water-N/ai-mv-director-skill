#!/usr/bin/env python3
"""Lightweight standard-library validation for this Agent Skill package."""
from pathlib import Path
import ast
import re
import sys

def fail(message):
    print(f"[FAIL] {message}")
    return False

def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    skill_file = root / "SKILL.md"
    if not skill_file.is_file():
        return 1 if fail(f"SKILL.md not found in {root}") else 0

    content = skill_file.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        return 1 if fail("SKILL.md must start with YAML frontmatter") else 0

    parts = content.split("---", 2)
    if len(parts) < 3:
        return 1 if fail("YAML frontmatter closing delimiter not found") else 0

    frontmatter = parts[1]
    name_match = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", frontmatter)
    desc_match = re.search(r"(?m)^description:\s*(.+)$", frontmatter)
    if not name_match:
        return 1 if fail("Missing or invalid name field") else 0
    if not desc_match:
        return 1 if fail("Missing description field") else 0

    name = name_match.group(1)
    if len(name) > 64 or name.startswith("-") or name.endswith("-") or "--" in name:
        return 1 if fail("Skill name violates naming constraints") else 0

    if not desc_match.group(1).strip().strip("'\""):
        return 1 if fail("Description is empty") else 0

    if root.name != name:
        print(f"[WARN] Folder name '{root.name}' differs from Skill name '{name}'.")
        print("       Install the folder as the name above, e.g. ~/.agents/skills/" + name)

    required = [
        "README.md",
        "LICENSE",
        "CHANGELOG.md",
        "docs/PRIVACY.md",
        "docs/RELEASE_NOTES.md",
        "agents/openai.yaml",
        "references/01-music-analysis.md",
        "references/02-creative-direction.md",
        "references/03-storyboard-and-visuals.md",
        "references/04-production-and-qc.md",
        "templates/storyboard.csv",
        "templates/creative-fingerprint.yaml",
        "scripts/init_project.py",
        "scripts/package_release.py",
        "prompts/00-project-start.md",
        "prompts/01-source-analysis.md",
        "prompts/02-creative-direction.md",
        "prompts/03-storyboard.md",
        "prompts/04-production.md",
        "prompts/05-quality-check.md",
        "prompts/06-archive.md",
        "templates/project-brief.md",
        "templates/analysis-report.md",
        "templates/creative-proposals.md",
        "templates/visual-bible.md",
        "templates/contact-sheet-report.md",
        "templates/delivery-report.md",
    ]
    missing = [p for p in required if not (root / p).is_file()]
    if missing:
        return 1 if fail("Missing required support files: " + ", ".join(missing)) else 0

    for ref in re.findall(r"`((?:references|prompts|templates)/[^`]+\.(?:md|yaml|csv))`", content):
        if not (root / ref).is_file():
            fail("Broken Skill reference: " + ref)
            return 1
    for script in (root / "scripts").glob("*.py"):
        try:
            ast.parse(script.read_text(encoding="utf-8"))
        except SyntaxError:
            fail("Python syntax error: scripts/" + script.name)
            return 1

    print(f"[OK] Skill metadata found: {name}")
    print(f"[OK] Required support files found: {len(required)}")
    print("[OK] Basic validation passed. This is not a full YAML/spec validator.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
