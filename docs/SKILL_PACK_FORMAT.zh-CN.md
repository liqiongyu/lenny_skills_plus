# Skill pack 格式（仓库规范 / house style）

> English version: `SKILL_PACK_FORMAT.md`

本仓库对每个 skill pack 做了统一结构规范，以最大化 Agent 执行可靠性，并保证 Codex + Claude Code 的可移植性。

## Canonical 结构

每个 skill 位于：

- `skills/<skill-slug>/`

必需文件：

- `skillpack.json`
  - 类似 package 的元数据（每个 skill 的 `version`、`authors`/贡献者、origin + 上游链接）
  - 本仓库工具链与发布打包会用到；Codex / Claude Code 会忽略该文件
- `SKILL.md`
  - YAML frontmatter：`name`、`description`（YAML-safe 且工具友好；更偏好单行字符串或引号）
  - 简短、可执行的操作指令：
    - Scope（覆盖范围 / 什么时候用 / 什么时候不该用）
    - Inputs（最少必需输入 + 缺失信息策略）
    - Outputs（交付物 / 工件）
    - Workflow（5–9 步）
    - 指向 `references/` 的细节导航
- `README.md`
  - 面向人类的概览
  - 用于触发 skill 的示例 prompts
- `references/`
  - `INTAKE.md`：问题库 + 缺失信息策略
  - `WORKFLOW.md`：扩展的步骤说明
  - `TEMPLATES.md`：可复制的模板
  - `CHECKLISTS.md`：DoD checklists
  - `RUBRIC.md`：评分 / 质量阈值
  - `SOURCE_SUMMARY.md`：上游内容压缩 + 关键洞察
  - `EXAMPLES.md`：更多 prompts + 边界例

## 设计原则

- Progressive disclosure：`SKILL.md` 保持紧凑；深度内容放 `references/`
- Artifact-driven outputs：必须产出具体交付物，而不是泛建议
- Boundary clarity：明确“什么时候不该用”
- Safe-by-default：默认无外网、风险操作先询问、避免敏感信息
