# QA and CI

> 中文版: [QA_AND_CI.zh-CN.md](QA_AND_CI.zh-CN.md)

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
  - Codex-compatible constraints: `name` ≤ 100 chars, `description` ≤ 500 chars, both single-line
- YAML frontmatter must parse (valid YAML mapping)
- `name` must match the folder slug
- Required files: `SKILL.md`, `README.md`, and the `references/` core set:
  - `INTAKE.md`, `WORKFLOW.md`, `TEMPLATES.md`, `CHECKLISTS.md`, `RUBRIC.md`, `SOURCE_SUMMARY.md`, `EXAMPLES.md`
