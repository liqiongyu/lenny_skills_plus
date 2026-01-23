# 项目记忆（Project memory）

> English version: [PROJECT_MEMORY.md](PROJECT_MEMORY.md)

本仓库是一个 **Skillpack Factory**：把 RefoundAI 的 “Lenny skills” 转化为 **agent-executable skill packs**，使用 **Agent Skills** common subset，并兼容 **OpenAI Codex** 与 **Claude Code**。

## 核心目标

- 产出 **高密度、可测试** 的 skill packs（不是长篇文章）。
- `SKILL.md` 保持短小、可执行；长内容放入 `references/`。
- 所有生成的 skill pack 内容必须为 **英文**（最大化工具兼容性）。

## Canonical 结构

- Canonical skills：`skills/<skill-slug>/`
- 本地镜像（生成、忽略 git，用于自动发现）：
  - Codex：`.codex/skills/<skill-slug>/`
  - Claude Code：`.claude/skills/<skill-slug>/`
- 上游源材料（从 Refound 下载）：
  - 优先：`sources/refound/raw/<slug>/SKILL.md`
  - 兜底：`sources/refound/raw/<slug>/page.html`（HTML fallback）

## 关键流程

1) 批量抓取源材料
   - `python3 skills/lenny-skillpack-creator/scripts/fetch_refound_skills.py --out sources/refound/raw`
2) 转换单个 skill（交互式）
   - 运行 Codex 并调用 `$lenny-skillpack-creator`
3) 校验结构
   - `python3 skills/lenny-skillpack-creator/scripts/lint_skillpack.py skills/<skill-slug>`
4) 生成本地镜像
   - `python3 scripts/mirror_skills.py --overwrite`

## GitHub 政策

本项目所有 GitHub 操作请使用 **GitHub CLI**（`gh`），包括：

- 鉴权检查：`gh auth status`
- 仓库管理：`gh repo create`、`gh repo view`、`gh repo set-default`
- Issues/PRs：`gh issue create`、`gh pr create`、`gh pr status`、`gh pr merge`
- Releases：`gh release create`、`gh release list`

本地版本控制用 `git`；涉及 GitHub 平台功能时用 `gh`。

