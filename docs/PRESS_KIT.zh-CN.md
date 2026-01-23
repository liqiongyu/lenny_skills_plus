# 宣传物料（可直接复制）

这份文件提供可直接复制粘贴的宣传文案/发布文案/社区招募文案。

上游署名与知识产权处理：见 `ATTRIBUTION_AND_IP.zh-CN.md`。

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

### 朋友圈 / 社群（短）

“开源了一个 skill packs 仓库：把 RefoundAI 的 ‘Lenny skills’ 变成 Agent 可执行的工作流（86 个 skills + 转换器）。每个 skill 都能产出模板/清单/计划/文档，支持 Codex + Claude Code。欢迎来用、来提 PR 共创：<link>”

### 长文 / 公众号（结构）

- 背景：好内容太 high-level，Agent 难以执行
- 方法：把技能写成执行契约（输入/输出/流程/质量门槛）
- 结果：86 个 skills + 转换器 meta-skill
- 号召：欢迎用起来提 PR，共创把每个 skill 打磨到“真能用”

