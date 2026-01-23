# 贡献指南（Contributing）

> English version: `CONTRIBUTING.md`

感谢你帮助改进这个仓库。

## 这个仓库的目标

本仓库用于把 RefoundAI 的 “Lenny skills” 转化为 **Agent 可执行的 skill packs**（Agent Skills common subset），并兼容 **Codex** 与 **Claude Code**。

## 基本规则

- 不要提交任何 secrets（API keys、tokens、凭证等）。
- 不要把批量下载的 Refound 原始内容提交进 git；本地副本应放在 `sources/refound/raw/`（已 gitignore）。
- 尽量小而可 review 的改动（一次转换 1 个 skill 或少量 skills）。
- skill pack 内容保持 **英文**。
- 不要逐字粘贴上游内容；详见 `docs/ATTRIBUTION_AND_IP.zh-CN.md`。

## 转换一个 skill（推荐流程）

1) 拉取上游源材料
   - `python3 skills/lenny-skillpack-creator/scripts/fetch_refound_skills.py --out sources/refound/raw`
2) 转换
   - 运行 Codex 并调用 `$lenny-skillpack-creator`
   - 将结果写入 `skills/<skill-slug>/`
3) 校验
   - `python3 skills/lenny-skillpack-creator/scripts/lint_skillpack.py skills/<skill-slug>`
4) 生成本地镜像（推荐，用于工具自动发现）
   - `python3 scripts/mirror_skills.py --overwrite`

## CI 预期

- CI 会做 Python 脚本语法检查，并对 `skills/` 下的 skill packs 做 lint。
- `.codex/` 与 `.claude/` 是本地生成的镜像目录（不进 git），CI 不要求它们存在。

## GitHub 工作流政策

GitHub 相关操作（issues、PRs、releases）使用 **GitHub CLI**（`gh`）。
