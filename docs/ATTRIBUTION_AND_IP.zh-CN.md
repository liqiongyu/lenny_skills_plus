# 署名与知识产权（Refound/Lenny）

这个项目的目标：在**尊重原创**与**明确署名来源**的前提下，把 RefoundAI 的 “Lenny skills” 从“高层方法论”转化为“Agent 可执行”的技能包（能产出具体工件、模板、清单、质量门槛）。

## 原始来源 / 致谢

- 原始来源：RefoundAI “Lenny skills” 数据库：`https://refoundai.com/lenny-skills/`
- 本仓库与 RefoundAI、以及 Lenny / Lenny’s Podcast **没有官方关联**。
- 如果你希望把本仓库作为公开/共创项目长期运营，建议主动请求明确授权：`REQUESTING_UPSTREAM_PERMISSION.zh-CN.md`。

## 本仓库包含什么（以及刻意避免什么）

- ✅ `skills/`：按 Agent Skills 开放格式整理的“可执行 skill packs”。
- ✅ `sources/refound/`：用于溯源的 manifest 与 URL 列表（便于署名与追踪）。
- ❌ 本仓库不会把大量上游页面/原文内容提交进 git。你本地抓取到的副本应放在 `sources/refound/raw/`（已 gitignore）。

## 我们为什么做这件事

我们认为上游 “Lenny skills” 很有价值，但很多内容对 Agent 来说**过于 high-level**，难以稳定产出结果。我们把它们转为：

- 清晰边界（什么时候用 / 什么时候不该用）
- 明确的输入/输出契约
- 5–9 步的可执行流程
- 必选质量门槛（checklists + rubric）

## 知识产权与下架处理（非法律建议，偏流程）

我们尊重所有知识产权来源，并会快速处理相关诉求。

如果你是权利人（或授权代理）并认为仓库内的某些内容需要删除或修改：

1) 请在 GitHub 提 Issue，并提供：
   - skill 的 slug（例如 `writing-prds`）
   - 对应的上游链接
   - 具体问题与期望动作（删除 / 修改 / 更正署名等）
2) 我们会跟进并做出必要的处理（包括删除）。

如需更正式的渠道，GitHub 也提供 DMCA 下架流程。

## 共创者约定（保证溯源与安全）

- 不要把上游内容逐字粘贴进仓库。
- skill pack 内容保持**英文**（最大化工具兼容性）。
- 尽量小 PR（一次改 1 个或少量 skills），便于 review。
- 修改 skill 时请同步更新 `references/EXAMPLES.md`，让他人可复现/验证。
