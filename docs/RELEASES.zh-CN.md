# 发布（Releases）

> English version: `RELEASES.md`

本仓库使用一个简单的发布节奏：

- `VERSION` 保存当前版本号（SemVer 风格）。
- `CHANGELOG.md` 记录重要变更。
- `CHANGELOG.zh-CN.md` 记录同一份变更日志的中文镜像（与 `CHANGELOG.md` 同步）。

建议的发布 checklist：
1) 对所有 skills 跑 lint：
   ```bash
   python3 scripts/ci_check_skillpacks.py --skip-mirror-check
   ```
2) 更新 `CHANGELOG.md`、`CHANGELOG.zh-CN.md` 与 `VERSION`。
3) 打 tag 并发布（如果使用 GitHub）：
   - 使用 `gh release create ...`（参见 `PROJECT_MEMORY.zh-CN.md`）。

打包提示：
- GitHub Releases 会发布每个 skill 的单独 zip，同时也会发布一个合集：`skills-all.zip`。
- 用户可将 skill 文件夹解压到 `.codex/skills`、`.claude/skills`、`~/.codex/skills` 或 `~/.claude/skills` 来安装使用。
