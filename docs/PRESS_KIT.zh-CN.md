# 宣传物料（可直接复制）

> English version: [PRESS_KIT.md](PRESS_KIT.md)

这份文件提供可直接复制粘贴的宣传文案/发布文案/社区招募文案。

上游署名与知识产权处理：见 [ATTRIBUTION_AND_IP.zh-CN.md](ATTRIBUTION_AND_IP.zh-CN.md)。

## 一句话介绍

- “把 RefoundAI 的 ‘Lenny skills’ 变成 **Agent 可执行** 的技能包，支持 Codex 和 Claude Code。”
- “86 个高密度 skill packs + 1 个转换器 meta-skill，输出具体工件而不是泛建议。”
- “每个 skill 都有：边界、输入/输出契约、可执行流程、质量门槛（checklists/rubric）。”

## 一段话介绍（短版）

Lenny Skills Plus 是一个社区驱动的仓库：把 RefoundAI 的 “Lenny skills” 从偏高层的方法论，转化为 **86 个 Agent 可执行的 skill packs**，并提供一个 meta-skill（`lenny-skillpack-creator`）用于继续转换更多 skills。每个 skill pack 都定义清晰边界、最小输入、明确交付物、步骤化流程与质量门槛，让 Agent 能稳定产出可 review 的结果（模板、清单、计划、文档），并可在 **Codex** 与 **Claude Code** 中直接使用。

## 差异点 / 卖点

- 每个 skill 是一个“执行契约”：输入 → 交付物 → 步骤 → 质量门槛
- 输出是“可交付工件”（templates / checklists / logs / rubrics）
- 同时兼容 Codex + Claude Code（common Agent Skills subset）
- 欢迎共创：用起来发现问题就提 PR（小而可 review）

## Demo 用例（示例 prompt）

- `$writing-prds` — “把这些 notes 写成可决策的 PRD，先问我最多 5 个问题。”
- `$ai-evals` — “为这个 LLM 功能设计 eval：golden set + rubric + judge plan。”
- `$managing-timelines` — “我们有一个上线日期，把它变成里程碑、范围控制和沟通节奏。”

## 推荐发布文案

### X / Twitter

“我们开源了 Lenny Skills Plus：86 个可给 Agent 执行的 skill packs（外加一个转换器），把高层建议变成可交付工件——PRD、checklists、templates、rubrics——可在 Codex + Claude Code 中使用。Repo: <link>”

### LinkedIn

“这些年我们见过很多高质量的产品/领导力方法论，但对 Agent 来说需要的是 *执行契约*，而不是长文。  
Lenny Skills Plus 把 RefoundAI 的 ‘Lenny skills’ 转成 86 个可执行的 skill packs（以及一个用于继续转换的 meta-skill）：边界、输入/输出契约、步骤化流程、质量门槛。  
欢迎在真实使用中发现问题并提 PR 共创。Repo: <link>”

### Hacker News

标题： “Show HN: Lenny Skills Plus — 86 agent-executable skill packs for Codex + Claude Code”

正文：
- What: 86 个 skill packs + 1 个转换器 meta-skill
- Why: 高层建议 → 可执行工作流（含 artifacts + quality gates）
- How: 将 `skills/` 镜像到 `.codex/skills` + `.claude/skills`，然后按名字调用
- Ask: 希望获得对格式的反馈，并欢迎基于真实使用的贡献

## Boilerplate（用于文章/长文）

Lenny Skills Plus 是一个开源仓库：把高层 “skills” 内容转换为可给 Agent 执行的 skill packs，强调以可交付工件为核心的输出、缺失信息处理策略，以及质量门槛（checklists + rubric）。项目欢迎社区在真实使用中通过小 PR 持续改进。
