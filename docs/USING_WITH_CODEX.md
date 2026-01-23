# Using with OpenAI Codex (CLI / IDE)

> 中文版: `USING_WITH_CODEX.zh-CN.md`

Codex supports “Agent Skills”: each skill is a folder containing `SKILL.md` with YAML frontmatter (`name`, `description`) plus optional supporting files.

## Frontmatter constraints (important)

Codex validates skill metadata at startup. In `SKILL.md` YAML frontmatter:

- `name` must be **single-line** and **≤ 100 characters**
- `description` must be **single-line** and **≤ 500 characters**

Multi-line YAML styles like `description: >` can cause validation errors and the skill may be skipped.

## Install from a release (recommended; no cloning)

Download `skills-all.zip` from the latest GitHub Release, then install it either globally or per-repo.

If your release doesn’t include `skills-all.zip` yet, you can still download individual per-skill zip files from the release.

### Global install

```bash
mkdir -p ~/.codex/skills
unzip -o skills-all.zip -d ~/.codex/skills
```

Restart Codex after installing new skills.

### Project-local install

From the root of *your* repo:

```bash
mkdir -p .codex/skills
unzip -o skills-all.zip -d .codex/skills
```

## Where Codex looks for skills

Codex loads skills from several scopes, including:

- Repo scope: `.codex/skills/` (various repo-relative locations)
- User scope: `~/.codex/skills` (macOS/Linux default)

This repository keeps canonical skill packs in `skills/`, and can mirror them into `.codex/skills/` for discovery.

## If you cloned this repo (contributors)

1) Mirror canonical skills into `.codex/skills/`:

```bash
python3 scripts/mirror_skills.py --overwrite
```

2) Start Codex from the repo (or any folder that can see `.codex/skills/`):

```bash
codex
```

3) Invoke a skill:
- Run `/skills` to browse, or type `$` and pick a skill
- Then provide your task details

Example:

```text
$writing-prds
Turn these notes into a decision-ready PRD. Ask up to 5 questions first.
```

## Global installation from a clone (optional)

If you cloned this repo and want these skills available across all repos:

```bash
mkdir -p ~/.codex/skills
rsync -a skills/ ~/.codex/skills/
```

Restart Codex after installing new skills.

## Skill metadata constraints (important)

For maximum compatibility across tools, keep `name` and `description`:
- short and specific (avoid paragraphs)
- plain single-line YAML strings (avoid block scalars like `description: >`)

This repo’s linter enforces that the frontmatter is valid YAML and that `name` / `description` are present, single-line, and within Codex length limits.
