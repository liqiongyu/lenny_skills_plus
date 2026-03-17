# 技能优化工作流

> English version: [SKILL_OPTIMIZATION_WORKFLOW.md](SKILL_OPTIMIZATION_WORKFLOW.md)

使用 `/skill-creator` 评估循环优化现有技能包的标准工作流。

## 前提条件

- 技能已存在于 `skills/<slug>/`，包含 SKILL.md + references/
- 原始 Refound 源文件位于 `sources/refound/raw/<slug>/SKILL.md`（如有）
- 已创建优化工作分支

## 工作流（6 步）

### 第 1 步：快照基线

```bash
mkdir -p <slug>-workspace/skill-snapshot
cp -r skills/<slug>/* <slug>-workspace/skill-snapshot/
```

保留旧版本用于 A/B 对比。

### 第 2 步：差距分析

阅读两个版本（原始 Refound 源 + 当前技能包）并分析：

1. **当前版本的优势** — 结构、工作流完整性、安全覆盖、洞察转化率
2. **缺失或薄弱之处** — 与邻域技能的消歧、缺失的交付物、模板可操作性、评分标准校准、示例覆盖
3. **边界清晰度** — description 是否能正确触发范围内的提示词，同时不触发邻域技能？

通过检查技能的类别和相关主题来识别邻域/易混淆的技能。

### 第 3 步：起草改进

对以下文件进行改进：

**SKILL.md**（主要变更）：
- **Description**：添加 `NOT for` 子句引用特定邻域技能
- **Scope**：扩展 "When NOT to use" 并添加明确的技能重定向
- **交付物**：添加缺失的交付物（如终止标准、快速模式）
- **工作流**：强化检查点、添加失败模式感知、引用源洞察
- **示例**：添加展示正确重定向的边界示例 + 反模式示例
- **反模式**：添加 3-5 个常见失败模式（如适用）

**references/RUBRIC.md**：
- 为每个评分维度添加具体的 0/1/2 边界定义
- 每个级别应足够具体，使两个评审者能达成一致

**references/TEMPLATES.md**：
- 为新增交付物添加模板
- 考虑添加"快速模式"子集（如适用）

**编辑后执行 lint：**
```bash
python3 skills/lenny-skillpack-creator/scripts/lint_skillpack.py skills/<slug>
```

### 第 4 步：设计测试提示词（3 个用例）

创建 3 个覆盖不同场景的测试提示词：

| # | 类型 | 目的 |
|---|------|------|
| 1 | **完整执行** | 真实、详细的提示词，执行完整工作流 |
| 2 | **变体/边界用例** | 不同场景（快速模式、不同行业、部分信息） |
| 3 | **边界重定向** | 应被拒绝并重定向到邻域技能的提示词 |

保存至 `<slug>-workspace/evals.json`。

### 第 5 步：运行评估（6 个子代理并行）

对每个测试提示词同时启动 2 个子代理：

- **with_skill**：使用改进版 `skills/<slug>/`
- **old_skill**：使用快照 `<slug>-workspace/skill-snapshot/`

每个子代理：
1. 读取 SKILL.md 和所有 references/
2. 按工作流生成输出
3. 保存至 `<slug>-workspace/iteration-1/<eval-name>/<variant>/outputs/`

子代理运行期间，为每个评估起草断言（章节存在性、质量检查、边界行为）。

子代理完成后：
1. 保存 `timing.json`
2. 用断言评分（优先使用脚本）
3. 创建 `benchmark.json`（通过率、token 数、耗时）
4. 生成评估查看器：`generate_review.py --static`

### 第 6 步：审查 + 提交

向用户展示结果。关键指标：

| 评估 | 改进版 | 基线 | 关键差异 |
|------|--------|------|---------|
| 完整执行 | X/Y | X/Y | 新增内容 |
| 变体 | X/Y | X/Y | 差异点 |
| 边界 | X/Y | X/Y | 重定向准确性 |

用户批准后：
1. 最终 lint 检查
2. 提交变更（仅技能文件，不含 workspace）
3. 推送 + 创建 PR

## 改进模式（跨技能复用）

### 适用于大多数技能的通用改进：

1. **NOT-for 消歧** — 每个技能应在 description 中明确命名 2-4 个邻域技能
2. **终止标准/退出条件** — 策略和规划类技能受益于"何时停止"的交付物
3. **快速模式** — 交付物超过 6 个的技能可提供精简子集
4. **反模式** — 3-5 个特定领域的常见失败模式
5. **评分标准校准** — 用具体的 0/1/2 边界替代一行描述
6. **边界示例** — 展示不匹配的提示词到达时的处理方式

### 取决于技能类型的改进：

| 技能类型 | 可能的改进 |
|----------|----------|
| 策略/规划 | 终止标准、快速模式、反模式 |
| 执行/流程 | 清单强化、失败模式示例 |
| 沟通 | 语调/受众感知、格式选项 |
| 职业/个人 | 敏感性护栏、个性化 |
| 销售/GTM | 阶段适配指导、指标示例 |

## 文件结构

```
<slug>-workspace/
├── evals.json                          # 测试提示词
├── skill-snapshot/                     # 旧版本（基线）
│   ├── SKILL.md
│   └── references/
├── grade_all.py                        # 评分脚本
└── iteration-1/
    ├── <eval-name>/
    │   ├── eval_metadata.json          # 提示词 + 断言
    │   ├── with_skill/
    │   │   ├── outputs/strategy-pack.md
    │   │   ├── timing.json
    │   │   └── grading.json
    │   └── old_skill/
    │       ├── outputs/strategy-pack.md
    │       ├── timing.json
    │       └── grading.json
    ├── benchmark.json
    └── review.html                     # 评估查看器
```
