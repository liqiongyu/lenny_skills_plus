# 为什么做这个项目

> English version: [WHY_THIS_PROJECT.md](WHY_THIS_PROJECT.md)

RefoundAI 的 “Lenny skills” 有很多高质量的产品/领导力经验，但不少条目对 Agent 来说**太 high-level**：缺少明确输入、明确交付物、可执行步骤与质量门槛，导致 Agent 很容易输出“泛泛而谈”的建议。

而现代 Agent（Codex、Claude Code 等）最擅长的，其实是执行**契约式工作流**：

- 边界清晰（什么时候用 / 什么时候不该用）
- 输入最小集 + 缺失信息策略（先问少量关键问题）
- 明确交付物（模板、清单、文档、计划、记录）
- 质量门槛（checklists + rubric）保证结果可 review
- 兼容 Codex 与 Claude Code（common Agent Skills subset）

关于上游来源与知识产权处理：见 [ATTRIBUTION_AND_IP.zh-CN.md](ATTRIBUTION_AND_IP.zh-CN.md)。

## 快速使用

1) 生成工具自动发现用的镜像目录：
   - `python3 scripts/mirror_skills.py --overwrite`
2) Codex 中使用：
   - 启动 `codex`，然后输入 `$<skill-slug>`（例如 `$writing-prds`）
3) Claude Code 中使用：
   - 输入 `/skill-slug`（例如 `/writing-prds`）

## 共创方式（实用）

最有效的共创路径是：**用起来 → 发现问题 → 提 PR**。

欢迎的贡献类型：
- 让输出更“可交付”（补模板/清单/质量门槛）
- 缩小边界，减少误触发
- 强化 `references/EXAMPLES.md`（好用例 + 边界用例）
- 改进缺失信息提问，让 skill 能从不完整输入启动

提交前建议：
- 运行：`python3 scripts/ci_check_skillpacks.py --skip-mirror-check`
- skill 内容保持**英文**
- 尽量小 PR（一次改 1 个或少量 skills）
