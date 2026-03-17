# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A curated library of 87 agent-executable skill packs (`skills/`) converted from RefoundAI's "Lenny skills," plus the tooling to produce more. Skills are portable across OpenAI Codex and Claude Code. All generated skill pack content must be in **English**.

## Common Commands

```bash
# Lint a single skill pack
python3 skills/lenny-skillpack-creator/scripts/lint_skillpack.py skills/<skill-slug>

# Lint all skill packs (CI-style, skip mirror check for local dev)
python3 scripts/ci_check_skillpacks.py --skip-mirror-check

# Mirror canonical skills to .codex/ and .claude/ for local auto-discovery
python3 scripts/mirror_skills.py --overwrite

# Check bilingual doc pairing (EN + zh-CN)
python3 scripts/check_bilingual_docs.py

# Python syntax validation
python -m compileall scripts skills

# Scaffold a new skill pack
python3 skills/lenny-skillpack-creator/scripts/init_skillpack.py skills/<skill-slug>

# Regenerate skills catalog / audit report
python3 scripts/generate_skills_catalog.py
python3 scripts/generate_audit_report.py
```

## Architecture

### Directory Layout

- **`skills/<skill-slug>/`** — Canonical skill packs (tracked in git). Each contains `SKILL.md`, `skillpack.json`, `README.md`, and `references/` with 7 standard files (INTAKE, WORKFLOW, TEMPLATES, CHECKLISTS, RUBRIC, SOURCE_SUMMARY, EXAMPLES).
- **`.codex/skills/`**, **`.claude/skills/`** — Generated mirrors for tool auto-discovery (git-ignored). Regenerate with `mirror_skills.py`.
- **`scripts/`** — Python utilities for CI validation, mirroring, doc generation, and normalization.
- **`skills/lenny-skillpack-creator/`** — The meta-skill that converts Refound sources into skill packs. Also contains the linter and scaffolding scripts under its `scripts/` subdirectory.
- **`sources/refound/`** — Upstream manifest; `raw/` subdirectory for downloaded sources (git-ignored).
- **`docs/`** — Bilingual documentation (EN + `*.zh-CN.md`).

### Skill Conversion Workflow

1. Locate upstream source in `sources/refound/raw/<slug>/`
2. Invoke the `$lenny-skillpack-creator` meta-skill
3. Write canonical skill to `skills/<slug>/`
4. Lint: `python3 skills/lenny-skillpack-creator/scripts/lint_skillpack.py skills/<slug>`
5. Smoke test with 1–2 realistic prompts
6. Mirror: `python3 scripts/mirror_skills.py --overwrite`

### CI/CD

- **ci.yml**: Runs on push/PR. Tests Python 3.9 & 3.11 — syntax check, bilingual docs, skill pack linting.
- **release.yml**: Triggered by `v*` tags. Validates all skills, packages individual zips + `skills-all.zip` bundle, generates SHA256 checksums, creates GitHub Release.

## Key Conventions

- **Progressive disclosure**: `SKILL.md` stays compact; depth goes in `references/`.
- **Artifact-driven**: Skills must produce concrete deliverables (templates, checklists, memos), not generic advice.
- **Boundary clarity**: Every skill explicitly defines when NOT to use it.
- **Quality gates**: Clear input/output contracts, 5–9 step workflow with checks, rubric with pass/fail thresholds.
- **Description limit**: SKILL.md frontmatter `description` must be under 500 characters. Adding NOT-for clauses requires concise wording.
- **YAML quotes**: Always use ASCII double quotes (`"`) in SKILL.md frontmatter. Unicode smart quotes (curly quotes) break YAML parsing.
- **Bilingual docs**: Root and `docs/` files need EN + `*.zh-CN.md` pairs with language switch markers.
- **Bilingual doc markers**: Use `> 中文版: [FILE.zh-CN.md](FILE.zh-CN.md)` in EN files and `> English version: [FILE.md](FILE.md)` in zh-CN files. Other formats will fail `check_bilingual_docs.py`.
- **GitHub operations**: Use `gh` CLI for anything GitHub-related (PRs, issues, releases).
- **Indentation**: 4 spaces for Python, 2 spaces for YAML. UTF-8, LF line endings.

## Key Documentation

- [AGENTS.md](AGENTS.md) — Full agent instructions (conventions, workflow, quality bar)
- [docs/SKILL_PACK_FORMAT.md](docs/SKILL_PACK_FORMAT.md) — House style for skill pack structure
- [docs/QUALITY_BAR.md](docs/QUALITY_BAR.md) — Non-negotiable quality standards
- [docs/WORKFLOW.md](docs/WORKFLOW.md) — Step-by-step conversion workflow
- [docs/SKILL_OPTIMIZATION_WORKFLOW.md](docs/SKILL_OPTIMIZATION_WORKFLOW.md) — Standard 6-step workflow for optimizing existing skill packs
- [CONTRIBUTING.md](CONTRIBUTING.md) — Contribution rules (small diffs, no secrets, no bulk upstream content)
