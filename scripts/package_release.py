#!/usr/bin/env python3
"""Build a reproducible, source-only release ZIP and its SHA-256 checksum."""
import argparse
import hashlib
from pathlib import Path
import subprocess
import sys
import zipfile

VERSION = '1.0.0'
ROOT_FILES = {'.gitignore', 'README.md', 'SKILL.md', 'LICENSE', 'CHANGELOG.md', 'CONTRIBUTING.md'}
SOURCE_DIRS = {'.github', 'agents', 'docs', 'examples', 'prompts', 'references', 'scripts', 'templates'}
TEXT_SUFFIXES = {'.md', '.py', '.yaml', '.yml', '.csv'}


def source_files(root):
    files = []
    for p in sorted(root.rglob('*')):
        rel = p.relative_to(root)
        if any(part in {'.git', '__pycache__', 'node_modules', 'dist'} for part in rel.parts):
            continue
        if p.is_symlink():
            raise ValueError('Symlinks are not release sources')
        if not p.is_file():
            continue
        if len(rel.parts) == 1 and rel.name in ROOT_FILES:
            files.append(p)
        elif rel.parts[0] in SOURCE_DIRS and p.suffix in TEXT_SUFFIXES:
            p.read_text(encoding='utf-8')
            files.append(p)
        else:
            raise ValueError('Unexpected release source: ' + rel.as_posix())
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output-dir', type=Path, default=Path('dist'))
    args = parser.parse_args()
    root = args.root.resolve()
    subprocess.run([sys.executable, str(root / 'scripts' / 'validate_skill.py'), str(root)], check=True)
    files = source_files(root)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    archive = args.output_dir / ('ai-mv-director-skill-v' + VERSION + '.zip')
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in files:
            info = zipfile.ZipInfo('ai-mv-director/' + p.relative_to(root).as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            z.writestr(info, p.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    (args.output_dir / 'SHA256SUMS.txt').write_text(digest + '  ' + archive.name + '\n', encoding='utf-8')
    print('[OK] Packaged ' + str(len(files)) + ' source files as ' + archive.name)
    print('[OK] SHA-256: ' + digest)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
