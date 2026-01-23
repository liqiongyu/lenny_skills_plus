# Lenny Skillpack Factory (Codex-first, Claude-compatible)

这个仓库模板的目标：把 Refound AI 的 **Lenny Skills Database**（原始 skills 往往“方法论强但可执行性弱”）逐个转化为“真正可给 Agent 干活”的 **Agent Skills Skill Packs**：
- 边界清晰（When to use / When not to use）
- 明确输入/输出契约（inputs/outputs contract）
- 可复用的流程（5–9 steps）
- 具备模板/清单/质量门槛（references/ + optional scripts/）
- **产出全部用英文**（为了最大兼容性 + 可复用）

本仓库同时兼容：
- OpenAI **Codex CLI / Codex IDE**（项目内 skills 通过 `.codex/skills/` 自动发现）
- **Claude Code**（项目内 skills 通过 `.claude/skills/` 自动发现）

> 说明：Refound 的页面写“87 skills across 11 categories”，但 browse 页当前可数到 **86**（你会在 `sources/refound/refound_lenny_skills_manifest.csv` 看到 86 行）。建议始终以脚本重新抓取为准，因为站点可能随时更新。

## Repo metadata

- License: Apache-2.0 (`LICENSE`)
- Version: `VERSION` (SemVer-style)
- GitHub policy: use GitHub CLI (`gh`) for GitHub operations (issues/PRs/releases)

---

## 目录结构

- `skills/`：**canonical** skill packs（git 追踪；发布/打包以这里为准）
- `.codex/skills/`：Codex 自动发现用的**本地镜像目录**（不进 git；用脚本生成）
- `.claude/skills/`：Claude Code 自动发现用的**本地镜像目录**（不进 git；用脚本生成）
- `sources/refound/`：Refound 原始 skill 的 URL 清单与 manifest
- `sources/refound/raw/`：你下载下来的原始 SKILL.md / HTML 备份（脚本生成）
- `output/`：你最终整理好的可发布 skill packs（可选）
- `samples/`：示例（原始 Lenny skill + 我们转换后的“可执行 skill pack”）

---

## 快速开始（推荐 workflow）

1) 安装/确认 Codex CLI 可用（你已经在用的话可跳过）
- `codex` 进入交互模式
- 用 `/skills` 或输入 `$` 检查是否能看到 skills

2) 拉取 Refound 原始 skills（两种方式）
- 方式 A（推荐）：运行本仓库带的抓取脚本（会抓取 browse 页→生成 slug→尝试下载 `/skills/<slug>/SKILL.md`，失败就保存 HTML 备份）
  - `python3 skills/lenny-skillpack-creator/scripts/fetch_refound_skills.py --out sources/refound/raw`
- 方式 B：使用 `sources/refound/refound_lenny_skill_md_urls.txt` 里那批 URL 自己下载（如果 Refound 对机器人访问有限制，建议加浏览器 UA）

3) 转换单个 skill（核心）
- 启动 Codex：在仓库根目录运行 `codex`
- 在对话里显式调用 meta-skill：
  - 输入 `$lenny-skillpack-creator`
- 给它这三类信息（越具体越好）：
  1. 原始 skill 内容（本地文件路径或粘贴文本）
  2. 目标 persona（PM / Recruiter / Engineer / Founder / Marketer …）
  3. 期望输出（明确要哪些 artifacts：例如 PRD、checklist、templates、rubric、email draft …）
- 让它把生成的 skill 写到：`skills/<skill-slug>/`（canonical）
  - 然后运行 `python3 scripts/mirror_skills.py --overwrite` 生成 `.codex/skills/` 与 `.claude/skills/` 本地镜像（用于工具自动发现）

4) 质量检查
- 对生成的 skill pack 运行 lint：
  - `python3 skills/lenny-skillpack-creator/scripts/lint_skillpack.py <path-to-skill>`
- 随机用 2–3 个真实任务 prompt 试跑，看是否能产出“可交付”的 artifacts

5) 生成本地镜像（Codex/Claude 自动发现用，推荐）
- 本仓库默认只 git 追踪 `skills/`。要让 Codex/Claude 在项目内“自动发现”，运行：
  - `python3 scripts/mirror_skills.py --overwrite`

---

## 你应该怎么批量转 86 个 skills（强烈建议 “半自动”）

最稳的方式是 **一边转一边做 QA**：
- 每个 skill 都至少跑一遍 lint
- 每个 skill 至少做 1 次“真实任务 smoke test”
- 每个 category 先挑 1–2 个代表 skill 打磨模板（形成你的 house style），再批量复制 pattern

如果你想更自动化：可以用 `codex exec` 做 pipeline，但要小心权限/安全设置（尤其是写文件和网络访问）。建议先把 workspace 限制在这个 repo 内，然后再逐个跑。

---

## 示例

- `samples/writing-prds-source/`：Refound 原始 skill（信息密度较低、偏方法论）
- `samples/writing-prds-executable/`：转换后的“可执行 skill pack”（含模板/清单/质量门槛/脚本）

---

## 重要约束（建议你坚持）

- 生成的 skill pack **必须英文**
- SKILL.md 只写“可执行指令 + 导航”，长内容放 references/（保持短、可读）
- 明确输入/输出契约（否则 agent 很容易输出泛泛而谈）
- 对高风险操作（网络/写系统文件/改生产配置）要有显式确认与回滚
