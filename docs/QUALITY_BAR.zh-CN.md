# 生成 skills 的质量标准（Quality bar for generated skills）

> English version: `QUALITY_BAR.md`

一个生成的 skill pack 只有在“Agent 在不确定条件下也能执行”时，才算“好”。

必须满足：
- 边界清晰（什么时候用 / 什么时候不该用）
- 明确输入契约 + 缺失信息处理
- 明确输出契约（交付物）
- 5–9 步流程，每一步都包含：
  - Inputs
  - Actions
  - Outputs
  - Checks / “definition of done”
- 渐进式展开（progressive disclosure）：
  - `SKILL.md` 保持短小，导航到 references
- 至少包含：
  - 2 个正例（good prompts）
  - 1 个反例/边界例（when NOT to use）

加分项：
- intake 的问题库
- 有 pass/fail 阈值的 rubric
- 能直接生成文件的模板（PRD、邮件、实验计划等）
- 简单的 lint/校验脚本

危险信号：
- 模糊建议（“consider”“think about”“it depends”）且没有工件
- 没有明确交付物
- 没有质量门槛
- `SKILL.md` 一整堵长文

