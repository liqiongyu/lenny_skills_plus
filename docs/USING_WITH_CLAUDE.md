# Using with Claude Code

> 中文版: [USING_WITH_CLAUDE.zh-CN.md](USING_WITH_CLAUDE.zh-CN.md)

Claude Code supports skills that follow the Agent Skills open standard.

## Install from a release (recommended; no cloning)

Download `skills-all.zip` from the latest GitHub Release, then install it either globally or per-repo.

If your release doesn’t include `skills-all.zip` yet, you can still download individual per-skill zip files from the release.

### Global install

```bash
mkdir -p ~/.claude/skills
unzip -o skills-all.zip -d ~/.claude/skills
```

### Project-local install

From the root of *your* repo:

```bash
mkdir -p .claude/skills
unzip -o skills-all.zip -d .claude/skills
```

## Where Claude Code looks for skills

Common locations:
- Project scope: `.claude/skills/<skill-name>/SKILL.md`
- Personal scope: `~/.claude/skills/<skill-name>/SKILL.md`

This repo keeps canonical skill packs in `skills/`, and mirrors them into `.claude/skills/` for discovery.

## If you cloned this repo (contributors)

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

## Global installation from a clone (optional)

If you cloned this repo and want to use these skills across all projects:

```bash
mkdir -p ~/.claude/skills
rsync -a skills/ ~/.claude/skills/
```

Claude Code supports automatic discovery in nested directories, so you can also place `.claude/skills/` inside subfolders of a monorepo if you want package-specific skills.
