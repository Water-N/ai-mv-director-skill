#!/usr/bin/env python3
"""Create a non-destructive AI MV project folder and copy starter templates."""
from pathlib import Path
import argparse
import shutil

DIRS = [
    "01_资料分析", "02_创意方案", "03_分镜脚本", "04_视觉素材",
    "05_工程", "06_联系表", "07_阶段导出", "08_最终成片", "09_归档",
]
TEMPLATES = [
    "project-brief.md", "analysis-report.md", "creative-proposals.md",
    "visual-bible.md", "storyboard.csv", "contact-sheet-report.md",
    "delivery-report.md", "creative-fingerprint.yaml",
]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("destination", help="Destination folder, e.g. /path/to/song/制作")
    parser.add_argument("--skill-root", default=str(Path(__file__).resolve().parents[1]))
    args = parser.parse_args()

    dest = Path(args.destination).expanduser().resolve()
    skill_root = Path(args.skill_root).expanduser().resolve()
    dest.mkdir(parents=True, exist_ok=True)

    created = []
    for folder in DIRS:
        p = dest / folder
        if not p.exists():
            p.mkdir(parents=True)
            created.append(str(p))

    template_dir = dest / "03_分镜脚本" / "模板"
    template_dir.mkdir(parents=True, exist_ok=True)
    for filename in TEMPLATES:
        src = skill_root / "templates" / filename
        target = template_dir / filename
        if src.is_file() and not target.exists():
            shutil.copy2(src, target)
            created.append(str(target))

    print(f"[OK] Project folder: {dest}")
    print(f"[OK] Created {len(created)} new directories/files.")
    print("[INFO] Existing files were not overwritten.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
