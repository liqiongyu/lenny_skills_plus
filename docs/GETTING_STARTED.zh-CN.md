# 快速开始（Getting started）

> English version: [GETTING_STARTED.md](GETTING_STARTED.md)

本仓库在 `skills/` 下提供一组整理好的 **agent-executable skill packs**。

## 我只想直接使用这些 skills（推荐）

你 **不需要** clone 本仓库也可以使用这些已转换好的 skill packs。

从最新 GitHub Release 下载 `skills-all.zip`，然后解压到：
- `~/.codex/skills/`（Codex 全局安装），和/或
- `~/.claude/skills/`（Claude Code 全局安装）

详见：
- [USING_WITH_CODEX.zh-CN.md](USING_WITH_CODEX.zh-CN.md)
- [USING_WITH_CLAUDE.zh-CN.md](USING_WITH_CLAUDE.zh-CN.md)

其他安装方式：
- clone 本仓库后，把 `skills/` 复制到 `~/.codex/skills` 和/或 `~/.claude/skills`
- 如果你只需要少量 skills 且使用 Codex，可以通过 `$skill-installer` 从 GitHub 直接安装单个 skill

推荐：先从 playbook 开始（按角色打包的一组 skills + 建议使用顺序）：
- [PLAYBOOKS.zh-CN.md](PLAYBOOKS.zh-CN.md)

## 我想共创 / 修改 skills

一个 “skill pack” 是一个目录，包含：

- `SKILL.md`（必需）：YAML frontmatter（`name`, `description`）+ 可执行指令
- `README.md`（本仓库要求）：简要使用说明 + 示例 prompts
- `references/`（本仓库要求）：模板、清单、rubric、扩展流程等

为了让工具自动发现 skills，可以把 `skills/` 镜像到工具专用目录：

```bash
python3 scripts/mirror_skills.py --overwrite
```

它会生成：
- Codex：`.codex/skills/<skill>/`
- Claude Code：`.claude/skills/<skill>/`

如果你更偏好全局安装（而不是项目级镜像），请查看 [USING_WITH_CODEX.zh-CN.md](USING_WITH_CODEX.zh-CN.md) 和 [USING_WITH_CLAUDE.zh-CN.md](USING_WITH_CLAUDE.zh-CN.md)。
