# Lenny Skillpack Factory — Agent 指南（Codex）

> English version: `AGENTS.md`

你正在一个仓库里工作。这个仓库的唯一目的，是把 RefoundAI 的 “Lenny skills” 转化为 **Agent 可执行的 skill packs**。

主要目标：
1) 产出 **高密度、可测试** 的 Agent Skills skill packs（不是长篇文章）。
2) 确保输出同时兼容 **OpenAI Codex** 与 **Claude Code**（使用共同的 Agent Skills 子集）。
3) 所有生成的 skill pack 内容必须为 **英文**。

## 仓库约定

- Canonical skills 放在：
  - `skills/<skill-slug>/`（优先、工具无关、git 追踪）

- `.codex/` 和 `.claude/` 是 **本地生成的镜像目录**（用于工具自动发现），**不进 git**。
  - 通过命令生成/更新：`python3 scripts/mirror_skills.py --overwrite`
  - Codex 自动发现目录：`.codex/skills/<skill-slug>/`
  - Claude Code 自动发现目录：`.claude/skills/<skill-slug>/`

- 上游源材料（从 Refound 下载）建议存放：
  - 优先：`sources/refound/raw/<slug>/SKILL.md`
  - 兜底：`sources/refound/raw/<slug>/page.html`

## 如何转换一个 skill

每次转换建议按以下流程：
1) 找到源 skill（`sources/refound/raw/...`），或使用 `sources/refound/` 下的 URL 清单/manifest。
2) 调用 meta-skill：
   - `$lenny-skillpack-creator`
3) 生成可安装的 skill 目录：
   - `<skill-slug>/SKILL.md`
   - `<skill-slug>/README.md`
   - `<skill-slug>/references/`（intake/workflow/templates/checklists/rubric/source summary）
   - `<skill-slug>/scripts/`（可选）
4) 运行 linter：
   - `python3 skills/lenny-skillpack-creator/scripts/lint_skillpack.py <path-to-skill-folder>`
5) 做快速 smoke test：
   - 用 1–2 个真实 prompt，验证输出是具体工件（不是泛建议）。

## 质量标准（不可妥协）

- Skill 必须边界清晰：
  - When to use / When NOT to use
- 必须定义输入/输出契约：
  - 最少必需输入 + 缺失信息策略
  - 明确交付物（文件或结构化输出）
- 必须提供 5–9 步流程
- 必须包含质量门槛：
  - checklists + rubric + risks/open questions/next steps
- 保持 `SKILL.md` 简洁；长内容放在 `references/`。
- 所有内容用英文（最大兼容性）。

## 安全

- 不要请求或提交任何 secrets/凭证。
- 未明确确认前避免不可逆改动。
- 运行脚本时遵循最小权限原则。

## GitHub 操作（项目政策）

- 所有 GitHub 操作（仓库设置、issues/PRs、release、workflows）使用 GitHub CLI：`gh`
- 本地版本控制使用 `git`

