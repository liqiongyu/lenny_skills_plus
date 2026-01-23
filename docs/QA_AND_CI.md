# QA and CI

## 1) Lint a single skill pack

```bash
python3 skills/lenny-skillpack-creator/scripts/lint_skillpack.py skills/<skill-slug>
```

## 2) Lint all skills

```bash
python3 scripts/ci_check_skillpacks.py --skip-mirror-check
```

## 3) Validate mirrors (optional)

If you generated `.codex/skills/` and `.claude/skills/` mirrors, validate that mirrors are byte-identical:

```bash
python3 scripts/ci_check_skillpacks.py
```

## What the linter enforces

- Required frontmatter fields: `name`, `description`
- Strict, cross-tool metadata constraints:
  - single-line scalars for `name` and `description`
  - typical size limits (name <= 100 chars, description <= 500 chars)
- Required files: `SKILL.md`, `README.md`, and the `references/` core set
