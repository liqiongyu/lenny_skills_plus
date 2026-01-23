# Getting started

This repository contains a curated set of **agent-executable skill packs** under `skills/`.

## I just want to use the skills (recommended)

You do **not** need to clone this repo to use the prebuilt skill packs.

Install from the latest GitHub Release by downloading `skills-all.zip` and unzipping it into:
- `~/.codex/skills/` (Codex global install), and/or
- `~/.claude/skills/` (Claude Code global install)

See:
- `USING_WITH_CODEX.md`
- `USING_WITH_CLAUDE.md`

## I want to contribute / modify skills

A “skill pack” is a directory that contains:

- `SKILL.md` (required): YAML frontmatter (`name`, `description`) + operational instructions
- `README.md` (required in this repo): short usage + example prompts
- `references/` (required in this repo): templates, checklists, rubrics, deeper workflow docs

To make skills auto-discoverable in tools, mirror `skills/` into tool-specific directories:

```bash
python3 scripts/mirror_skills.py --overwrite
```

That generates:
- `.codex/skills/<skill>/` for Codex
- `.claude/skills/<skill>/` for Claude Code

If you prefer global installation instead of project-local mirrors, see `USING_WITH_CODEX.md` and `USING_WITH_CLAUDE.md`.
