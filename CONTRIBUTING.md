# Contributing

> 中文版: `CONTRIBUTING.zh-CN.md`

Thanks for helping improve this repository.

## What this repo is for

This repository exists to convert RefoundAI “Lenny skills” into **agent-executable skill packs** (Agent Skills common subset), compatible with **Codex** and **Claude Code**.

## Ground rules

- Do not commit secrets (API keys, tokens, credentials).
- Do not commit bulk-downloaded Refound content; keep it under `sources/refound/raw/` (ignored by git).
- Prefer small, reviewable diffs (convert 1 skill or a small batch at a time).
- Keep generated skill pack content in **English**.
- Do not paste upstream content verbatim; see `docs/ATTRIBUTION_AND_IP.md`.

## Converting a skill (recommended)

1) Fetch sources
   - `python3 skills/lenny-skillpack-creator/scripts/fetch_refound_skills.py --out sources/refound/raw`
2) Convert
   - Run Codex and invoke `$lenny-skillpack-creator`
   - Write the result to `skills/<skill-slug>/`
3) Validate
   - `python3 skills/lenny-skillpack-creator/scripts/lint_skillpack.py skills/<skill-slug>`
4) Generate local mirrors (recommended for tool auto-discovery)
   - `python3 scripts/mirror_skills.py --overwrite`

## CI expectations

- CI validates Python scripts (syntax) and lints skill packs under `skills/`.
- `.codex/` and `.claude/` are generated local mirrors (ignored by git), so CI does not require them to be present.

## GitHub workflow policy

Use **GitHub CLI** (`gh`) for GitHub operations (issues, PRs, releases).
