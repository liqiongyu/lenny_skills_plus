# Lenny Skills Plus

一个可直接使用的 **86 个高密度、可执行（agent-executable）的 skill packs** 集合，来源于 RefoundAI 的 “Lenny skills” 数据库（本项目非官方、非隶属）。

这些 skill packs 采用开放的 **Agent Skills** 目录格式（每个 skill 是一个文件夹，包含 `SKILL.md` + supporting files），目标是让 AI agent 能稳定地产出 **具体交付物**（模板、清单、决策文档、计划、脚本等），而不是泛泛的建议。

支持：
- **OpenAI Codex（CLI / IDE）**：`.codex/skills/` 或 `~/.codex/skills/`
- **Claude Code**：`.claude/skills/` 或 `~/.claude/skills/`

> 备注：Refound 的部分页面写 “87 skills”，但当前可抓取/浏览到的清单为 **86**。

## 署名与知识产权（重要）

本项目尊重并标注上游来源（RefoundAI “Lenny skills”）。上游致谢与侵权/下架处理流程：`docs/ATTRIBUTION_AND_IP.zh-CN.md`。

## 快速开始（推荐：无需 clone）

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
- `docs/USING_WITH_CODEX.md`
- `docs/USING_WITH_CLAUDE.md`

### 方案 B：clone 本仓库（适合共创/维护者）

本仓库以 `skills/` 作为 **canonical**（git 追踪），并可生成工具自动发现用的本地镜像目录：

```bash
python3 scripts/mirror_skills.py --overwrite
```

它会生成（不进 git）：
- `.codex/skills/<skill>/`
- `.claude/skills/<skill>/`

## 如何使用

- **Codex**：启动后用 `/skills` 浏览，或输入 `$` 选择 skill
  ```text
  $writing-prds
  Turn these notes into a decision-ready PRD. Ask up to 5 questions first.
  ```

- **Claude Code**：在项目里直接调用 `/skill-name`
  ```text
  /writing-prds
  Turn these notes into a decision-ready PRD. Ask up to 5 questions first.
  ```

## Skill 列表

见：`docs/SKILLS_CATALOG.md`

## 为什么做这个项目

“高层方法论”对人类很有帮助，但对 agent 来说往往不够可执行。本项目把技能写成更像“执行合同”：输入 → 流程 → 交付物 → 质量门槛。详见：`docs/WHY_THIS_PROJECT.zh-CN.md`。

## 共创 / 贡献

欢迎大家在使用中发现问题、补充 examples、提升可执行性并提交 PR：`CONTRIBUTING.md`。

## License

Apache-2.0 — 见 `LICENSE`。
