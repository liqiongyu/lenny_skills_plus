# 在 OpenAI Codex 中使用（CLI / IDE）

> English version: [USING_WITH_CODEX.md](USING_WITH_CODEX.md)

Codex 支持 “Agent Skills”：每个 skill 是一个文件夹，包含带 YAML frontmatter（`name`, `description`）的 `SKILL.md`，以及可选的 supporting files。

## Frontmatter 限制（重要）

Codex 会在启动时校验 skill 的元数据。在 `SKILL.md` 的 YAML frontmatter 中：

- `name` 必须是 **单行** 且 **≤ 100 个字符**
- `description` 必须是 **单行** 且 **≤ 500 个字符**

像 `description: >` 这种多行 YAML 写法可能导致校验错误，skill 会被跳过加载。

## 从 Release 安装（推荐；无需 clone）

从最新 GitHub Release 下载 `skills-all.zip`，然后选择全局或项目级安装。

如果某个 Release 暂时没有 `skills-all.zip`，也可以从 Release 下载每个 skill 单独的 zip 文件。

### 全局安装

```bash
mkdir -p ~/.codex/skills
unzip -o skills-all.zip -d ~/.codex/skills
```

安装新 skills 后请重启 Codex。

### 项目级安装

在你的项目根目录执行：

```bash
mkdir -p .codex/skills
unzip -o skills-all.zip -d .codex/skills
```

## Codex 会从哪里加载 skills

Codex 会从多个 scope 加载 skills，包括：

- Repo scope：`.codex/skills/`（各种 repo 相对路径）
- User scope：`~/.codex/skills`（macOS/Linux 默认）

本仓库将 canonical skill packs 放在 `skills/`，并可镜像到 `.codex/skills/` 以便自动发现。

## 如果你 clone 了本仓库（贡献者）

1) 将 canonical skills 镜像到 `.codex/skills/`：

```bash
python3 scripts/mirror_skills.py --overwrite
```

2) 在仓库内启动 Codex（或任何能看到 `.codex/skills/` 的目录）：

```bash
codex
```

3) 调用 skill：
- 用 `/skills` 浏览，或输入 `$` 选择 skill
- 然后提供任务细节

示例：

```text
$writing-prds
Turn these notes into a decision-ready PRD. Ask up to 5 questions first.
```

## 从 clone 仓库全局安装（可选）

如果你 clone 了本仓库，并希望在所有仓库中可用：

```bash
mkdir -p ~/.codex/skills
rsync -a skills/ ~/.codex/skills/
```

安装新 skills 后请重启 Codex。

## Skill 元数据约束（重要）

为了最大化跨工具兼容性，建议 `name` 与 `description`：
- 短、具体（避免长段落）
- 使用普通的单行 YAML 字符串（避免使用 `description: >` 等 block scalars）

本仓库 linter 会确保 frontmatter 是有效 YAML，且 `name` / `description` 存在、为单行，并满足 Codex 的长度限制。
