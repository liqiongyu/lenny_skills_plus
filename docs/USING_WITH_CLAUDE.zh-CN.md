# 在 Claude Code 中使用

> English version: [USING_WITH_CLAUDE.md](USING_WITH_CLAUDE.md)

Claude Code 支持遵循 Agent Skills open standard 的 skills。

## 从 Release 安装（推荐；无需 clone）

从最新 GitHub Release 下载 `skills-all.zip`，然后选择全局或项目级安装。

如果某个 Release 暂时没有 `skills-all.zip`，也可以从 Release 下载每个 skill 单独的 zip 文件。

### 全局安装

```bash
mkdir -p ~/.claude/skills
unzip -o skills-all.zip -d ~/.claude/skills
```

### 项目级安装

在你的项目根目录执行：

```bash
mkdir -p .claude/skills
unzip -o skills-all.zip -d .claude/skills
```

## Claude Code 会从哪里加载 skills

常见位置：
- Project scope：`.claude/skills/<skill-name>/SKILL.md`
- Personal scope：`~/.claude/skills/<skill-name>/SKILL.md`

本仓库将 canonical skill packs 放在 `skills/`，并可镜像到 `.claude/skills/` 以便自动发现。

## 如果你 clone 了本仓库（贡献者）

1) 将 canonical skills 镜像到 `.claude/skills/`：

```bash
python3 scripts/mirror_skills.py --overwrite
```

2) 在 Claude Code 中直接用以下方式调用 skill：

```text
/skill-name
```

示例：

```text
/writing-prds
Turn these notes into a decision-ready PRD. Ask up to 5 questions first.
```

## 从 clone 仓库全局安装（可选）

如果你 clone 了本仓库，并希望在所有项目中可用：

```bash
mkdir -p ~/.claude/skills
rsync -a skills/ ~/.claude/skills/
```

Claude Code 支持在嵌套目录自动发现 skills，因此在 monorepo 中也可以把 `.claude/skills/` 放到子目录下，作为包级 skills 使用。

