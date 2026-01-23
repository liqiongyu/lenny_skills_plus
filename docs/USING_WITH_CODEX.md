# Using with OpenAI Codex (CLI / IDE)

Codex supports “Agent Skills”: each skill is a folder containing `SKILL.md` with YAML frontmatter (`name`, `description`) plus optional supporting files.

## Where Codex looks for skills

Codex loads skills from several scopes, including:

- Repo scope: `.codex/skills/` (various repo-relative locations)
- User scope: `~/.codex/skills` (macOS/Linux default)

This repo keeps canonical skill packs in `skills/`, and mirrors them into `.codex/skills/` for discovery.

## Project-local usage (recommended)

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

## Global installation (optional)

If you want these skills available across all repos:

```bash
mkdir -p ~/.codex/skills
rsync -a skills/ ~/.codex/skills/
```

Restart Codex after installing new skills.

## Skill metadata constraints (important)

For maximum compatibility, keep `name` and `description`:
- single-line scalars (no YAML block scalars like `description: >`)
- within typical size limits (name <= 100 chars, description <= 500 chars)

This repo’s linter enforces these constraints.
