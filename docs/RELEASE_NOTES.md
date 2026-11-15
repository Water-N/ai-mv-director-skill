# AI MV Director Skill v1.0.0

## Features

- Four approval-gated phases: source analysis, creative direction, storyboard/previsualization, and production/quality control.
- Song-led creative direction with a persistent creative-fingerprint archive to reduce repetition.
- Beat-aware storyboard, lyric-subtitle alignment, and visual continuity templates.
- Contact-sheet review gates and structured delivery reporting.
- Optional Codex UI metadata and portable Agent Skills folder structure.
- Local project initialization and basic package validation scripts.

## Design principles

- Reuse technical infrastructure, not creative formulas.
- No default art style, HUD, prop, plot twist, or shot count.
- Report only verified tool execution and media properties.
- Preserve original source assets.
- No built-in telemetry or automatic media uploads.

## Compatibility

Designed for Agent Skills-compatible clients. Product-specific skill discovery paths and invocation methods may differ.

The local helper scripts require Python 3.9 or later and use only the standard library. Media generation and editing require separately configured, user-selected tools; this release does not bundle models or source media.

## Download and verification

Download `ai-mv-director-skill-v1.0.0.zip` and `SHA256SUMS.txt` from this Release. Extract the ZIP and install the `ai-mv-director/` folder with `SKILL.md` directly inside it. The archive includes the full references, prompts, templates, scripts, and documentation.

Verify the ZIP's SHA-256 against `SHA256SUMS.txt`, then run `python scripts/validate_skill.py .` from the extracted folder. These checks cover package structure and helper syntax; they do not certify end-to-end generation with every media model or client.
