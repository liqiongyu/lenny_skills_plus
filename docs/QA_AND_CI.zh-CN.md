# QA 与 CI（QA and CI）

> English version: `QA_AND_CI.md`

## 1) lint 单个 skill pack

```bash
python3 skills/lenny-skillpack-creator/scripts/lint_skillpack.py skills/<skill-slug>
```

## 2) lint 全部 skills

```bash
python3 scripts/ci_check_skillpacks.py --skip-mirror-check
```

## 3) 校验镜像目录（可选）

如果你生成了 `.codex/skills/` 与 `.claude/skills/` 镜像目录，可以校验镜像是否逐字节一致：

```bash
python3 scripts/ci_check_skillpacks.py
```

## linter 会检查什么

- 必需 frontmatter 字段：`name`、`description`
  - Codex 兼容约束：`name` ≤ 100 字符，`description` ≤ 500 字符，且二者必须是单行
- YAML frontmatter 必须可解析（有效 YAML mapping）
- `name` 必须与文件夹 slug 一致
- 必需文件：`SKILL.md`、`README.md`，以及 `references/` 的核心文件集：
  - `INTAKE.md`、`WORKFLOW.md`、`TEMPLATES.md`、`CHECKLISTS.md`、`RUBRIC.md`、`SOURCE_SUMMARY.md`、`EXAMPLES.md`
