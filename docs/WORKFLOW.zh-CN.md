# 转换流程（推荐）（Conversion workflow）

> English version: `WORKFLOW.md`

这是把一个 Refound/Lenny skill 转成“可执行 skill pack”的可重复流程。

1. 获取源材料
   - 优先下载 `/skills/<slug>/SKILL.md`（Agent Skills 格式）。
   - 如果被限制，保存 HTML 页面（`/lenny-skills/s/<slug>/`）并从 HTML 转换。

2. 确定目标 slug
   - 使用小写 + 连字符（符合 Agent Skills 命名约束）。
   - slug 尽量保持稳定（它会成为 skill 的命令名）。

3. 调用 `$lenny-skillpack-creator`
   提供：
   - 源内容路径（SKILL.md 或 page.html）
   - 目标 persona
   - 期望交付物

4. 确保生成的 skill pack 包含：
   - SKILL.md（短小、可执行）
   - references/INTAKE.md
   - references/WORKFLOW.md
   - references/TEMPLATES.md
   - references/CHECKLISTS.md
   - references/RUBRIC.md
   - references/SOURCE_SUMMARY.md
   - README.md（安装 + 调用 + examples）

5. 运行 linter
   - `python3 skills/lenny-skillpack-creator/scripts/lint_skillpack.py <skill-dir>`

6. Smoke test
   - 跑 1–2 个真实任务，检查输出是否符合 “Output contract”。

7. 生成本地镜像（推荐）
   - 运行 `python3 scripts/mirror_skills.py --overwrite`，生成 `.codex/skills/` 与 `.claude/skills/` 供工具自动发现。

8. 提交
   - 每个 skill 或少量 skills 提交一次，保持 diff 可 review。

