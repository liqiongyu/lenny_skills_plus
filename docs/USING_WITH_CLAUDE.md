# Using with Claude Code

Claude Code supports skills that follow the Agent Skills open standard.

## Where Claude Code looks for skills

Common locations:
- Project scope: `.claude/skills/<skill-name>/SKILL.md`
- Personal scope: `~/.claude/skills/<skill-name>/SKILL.md`

This repo keeps canonical skill packs in `skills/`, and mirrors them into `.claude/skills/` for discovery.

## Project-local usage (recommended)

1) Mirror canonical skills into `.claude/skills/`:

```bash
python3 scripts/mirror_skills.py --overwrite
```

2) In Claude Code, invoke a skill directly with:

```text
/skill-name
```

Example:

```text
/writing-prds
Turn these notes into a decision-ready PRD. Ask up to 5 questions first.
```

## Global installation (optional)

To use these skills across all projects:

```bash
mkdir -p ~/.claude/skills
rsync -a skills/ ~/.claude/skills/
```

Claude Code supports automatic discovery in nested directories, so you can also place `.claude/skills/` inside subfolders of a monorepo if you want package-specific skills.
