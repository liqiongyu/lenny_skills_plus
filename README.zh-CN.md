# Lenny Skills Plus

> English version: `README.md`

一个可直接使用的 **86 个高密度、可执行（agent-executable）的 skill packs** 集合，来源于 RefoundAI 的 “Lenny skills” 数据库（本项目非官方、非隶属）。

这些 skill packs 采用开放的 **Agent Skills** 目录格式（每个 skill 是一个文件夹，包含 `SKILL.md` + supporting files），目标是让 AI agent 能稳定地产出 **具体交付物**（模板、清单、决策文档、计划、脚本等），而不是泛泛的建议。

支持：
- **OpenAI Codex（CLI / IDE）**：`.codex/skills/` 或 `~/.codex/skills/`
- **Claude Code**：`.claude/skills/` 或 `~/.claude/skills/`

> 备注：Refound 的部分页面写 “87 skills”，但当前可抓取/浏览到的清单为 **86**。

## 署名与知识产权（重要）

本项目尊重并标注上游来源（RefoundAI “Lenny skills”）。上游致谢与侵权/下架处理流程：`docs/ATTRIBUTION_AND_IP.zh-CN.md`。

## 快速开始（Quickstart）

### 方案 A：从 Release 安装（不需要拉仓库）

1) 从 GitHub Releases 下载 `skills-all.zip`
   - 如果该 Release 里暂时没有 `skills-all.zip`，也可以按需下载每个 skill 单独的 zip 文件。

2) 安装到 Codex（全局）：

```bash
mkdir -p ~/.codex/skills
unzip -o skills-all.zip -d ~/.codex/skills
```

3) 安装到 Claude Code（全局）：

```bash
mkdir -p ~/.claude/skills
unzip -o skills-all.zip -d ~/.claude/skills
```

如果你更偏好 **项目级** skills，把 zip 解压到你的项目里：
- Codex：`.codex/skills/`
- Claude Code：`.claude/skills/`

更详细的使用说明：
- `docs/USING_WITH_CODEX.zh-CN.md`
- `docs/USING_WITH_CLAUDE.zh-CN.md`

### 方案 B：clone 本仓库（适合共创/维护者）

本仓库以 `skills/` 作为 **canonical**（git 追踪），并可生成工具自动发现用的本地镜像目录：

```bash
python3 scripts/mirror_skills.py --overwrite
```

它会生成（不进 git）：
- `.codex/skills/<skill>/`
- `.claude/skills/<skill>/`

## 在 Codex 中使用

启动 Codex（无论你是全局安装，还是项目内放了 `.codex/skills/`）：

```bash
codex
```

然后用 `/skills` 浏览，或输入 `$` 选择 skill。示例：

```text
$writing-prds
Turn these notes into a decision-ready PRD. Ask up to 5 questions first.
```

## 在 Claude Code 中使用

在 Claude Code 中打开你的项目（无论你是全局安装，还是项目内放了 `.claude/skills/`），然后直接调用：

```text
/skill-name
```

示例：

```text
/writing-prds
Turn these notes into a decision-ready PRD. Ask up to 5 questions first.
```

## Skill 目录

见：`docs/SKILLS_CATALOG.zh-CN.md`

## 为什么做这个项目

“高层方法论”对人类很有帮助，但对 agent 来说往往不够可执行。本项目把技能写成更像“执行合同”：输入 → 流程 → 交付物 → 质量门槛。详见：`docs/WHY_THIS_PROJECT.zh-CN.md`。

## 共创 / 再生成

如果你希望参与打磨这些技能、补充 examples、或再生成 skill packs：
- 贡献指南：`CONTRIBUTING.zh-CN.md`
- 转换流程：`docs/WORKFLOW.zh-CN.md`

## 质量与 CI

对所有 skills 做结构校验：

```bash
python3 scripts/ci_check_skillpacks.py --skip-mirror-check
```

如果你已经镜像到 `.codex/skills` 与 `.claude/skills`，也可以校验镜像一致性：

```bash
python3 scripts/ci_check_skillpacks.py
```

## 仓库结构

- `skills/` — canonical skill packs（git 追踪）
- `.codex/skills/` — Codex 自动发现用的本地镜像目录（忽略 git）
- `.claude/skills/` — Claude Code 自动发现用的本地镜像目录（忽略 git）
- `sources/refound/` — 上游 manifest + URL 清单
- `sources/refound/raw/` — 可选：本地抓取的上游源材料（忽略 git）
- `docs/` — 项目文档

## 贡献

见 `CONTRIBUTING.zh-CN.md`。

## License

Apache-2.0 — 见 `LICENSE`。
