# 常见问题 / 排查（FAQ / troubleshooting）

> English version: `FAQ.md`

## Codex 看不到我的 skills

- 确认 skills 已镜像到 `.codex/skills/`（或安装到 `~/.codex/skills/`）。
- 如果你是从 `skills-all.zip` 安装：确认你解压到了“skills 目录”（例如 `~/.codex/skills/`），使得 zip 顶层文件夹落到 `~/.codex/skills/<skill-name>/`。
- 安装新 skills 后重启 Codex。
- 确保 `SKILL.md` 以 YAML frontmatter 开头，并包含 `name` 与 `description`。

## Claude Code 看不到我的 skills

- 确认 skills 已镜像到 `.claude/skills/`（或安装到 `~/.claude/skills/`）。
- 如果你是从 `skills-all.zip` 安装：确认你解压到了“skills 目录”（例如 `~/.claude/skills/`），使得 zip 顶层文件夹落到 `~/.claude/skills/<skill-name>/`。
- 确保目录结构为 `.../skills/<skill-name>/SKILL.md`（不是 `.../skills/<skill-name>.md`）。
- 确认 frontmatter 的 `name` 与文件夹名一致。

## Skill 触发过于频繁 / 触发不到

- 调整 `SKILL.md` 中的 `description` 字段（更窄或更宽）。
- 在 `SKILL.md` 增加更明确的 “When to use” 语言。
- 尽量保持 skill 边界窄；重叠技能会让自动选择更混乱。

## 我想要更严格的安全控制

- 使用项目级镜像（`.codex/skills` / `.claude/skills`）限制作用域。
- 优先使用沙盒执行（Codex），除非你需要确定性，否则避免运行脚本。

