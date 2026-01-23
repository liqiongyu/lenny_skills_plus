# Project memory

This repository is a **Skillpack Factory**: it converts RefoundAI “Lenny skills” into **agent-executable skill packs** using the **Agent Skills** common subset, compatible with **OpenAI Codex** and **Claude Code**.

## Core goals

- Generate **high-density, testable** skill packs (not essays).
- Keep **SKILL.md short** and operational; put long content in `references/`.
- All generated skill pack content must be **English** (maximum tool compatibility).

## Canonical structure

- Canonical generated skills: `skills/<skill-slug>/`
- Local mirrors for auto-discovery (generated, ignored by git):
  - `.codex/skills/<skill-slug>/` (Codex)
  - `.claude/skills/<skill-slug>/` (Claude Code)
- Source materials (downloaded from Refound):
  - `sources/refound/raw/<slug>/SKILL.md` if available
  - otherwise `sources/refound/raw/<slug>/page.html` (HTML fallback)

## Key workflows

1) Fetch sources (bulk)
   - `python3 skills/lenny-skillpack-creator/scripts/fetch_refound_skills.py --out sources/refound/raw`
2) Convert one skill (interactive)
   - Run Codex and invoke `$lenny-skillpack-creator`
3) Validate structure
   - `python3 skills/lenny-skillpack-creator/scripts/lint_skillpack.py skills/<skill-slug>`
4) Generate local mirrors
   - `python3 scripts/mirror_skills.py --overwrite`

## GitHub policy

All GitHub operations for this project should be done via **GitHub CLI** (`gh`), including:

- Authentication checks: `gh auth status`
- Repo management: `gh repo create`, `gh repo view`, `gh repo set-default`
- Issues/PRs: `gh issue create`, `gh pr create`, `gh pr status`, `gh pr merge`
- Releases: `gh release create`, `gh release list`

Use `git` for local VCS operations; use `gh` when it becomes “a GitHub thing”.
