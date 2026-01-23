# Releases

This repo follows a simple release discipline:

- `VERSION` stores the current version string (SemVer-style).
- `CHANGELOG.md` captures notable changes.

Suggested release checklist:
1) Run lint across all skills:
   ```bash
   python3 scripts/ci_check_skillpacks.py --skip-mirror-check
   ```
2) Update `CHANGELOG.md` and `VERSION`.
3) Tag and release (if using GitHub):
   - use `gh release create ...` (see `PROJECT_MEMORY.md`).

Packaging tip:
- GitHub Releases publish per-skill zip files, and also a single bundle: `skills-all.zip`.
- Users can install by unzipping skill folders into `.codex/skills`, `.claude/skills`, `~/.codex/skills`, or `~/.claude/skills`.
