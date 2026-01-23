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
- For distribution, you can zip the `skills/` directory or a selected subset.
- Users can install by copying directories into `.codex/skills`, `.claude/skills`, `~/.codex/skills`, or `~/.claude/skills`.
