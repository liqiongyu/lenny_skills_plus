# Lenny Skills Plus

> English version: [README.md](README.md)

[![CI](https://github.com/liqiongyu/lenny_skills_plus/actions/workflows/ci.yml/badge.svg)](https://github.com/liqiongyu/lenny_skills_plus/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Skills: 87](https://img.shields.io/badge/Skills-87-green.svg)](docs/SKILLS_CATALOG.zh-CN.md)

一个可直接使用的 **87 个高密度、可执行（agent-executable）的 skill packs** 集合（86 个转化自 RefoundAI 的 "Lenny skills" + 1 个 meta-skill），采用开放的 **Agent Skills** 格式，兼容 **OpenAI Codex** 与 **Claude Code**。

每个 skill pack 定义了作用域、所需输入、具体交付物、分步工作流和质量门槛——让 agent 产出可评审的制品，而非泛泛的建议。

## Skills 一览

| 类别 | 数量 | 推荐起点 |
|---|---:|---|
| Product Management（产品管理） | 22 | [problem-definition](skills/problem-definition/), [writing-prds](skills/writing-prds/), [shipping-products](skills/shipping-products/) |
| Leadership（领导力） | 14 | [managing-up](skills/managing-up/), [delegating-work](skills/delegating-work/), [having-difficult-conversations](skills/having-difficult-conversations/) |
| Career（职业发展） | 7 | [negotiating-offers](skills/negotiating-offers/), [career-transitions](skills/career-transitions/), [building-a-promotion-case](skills/building-a-promotion-case/) |
| Sales & GTM（销售与 GTM） | 7 | [founder-sales](skills/founder-sales/), [enterprise-sales](skills/enterprise-sales/), [sales-qualification](skills/sales-qualification/) |
| Hiring & Teams（招聘与团队） | 6 | [writing-job-descriptions](skills/writing-job-descriptions/), [conducting-interviews](skills/conducting-interviews/), [onboarding-new-hires](skills/onboarding-new-hires/) |
| AI & Technology（AI 与技术） | 6 | [building-with-llms](skills/building-with-llms/), [ai-evals](skills/ai-evals/), [vibe-coding](skills/vibe-coding/) |
| Growth（增长） | 6 | [retention-engagement](skills/retention-engagement/), [user-onboarding](skills/user-onboarding/), [marketplace-liquidity](skills/marketplace-liquidity/) |
| Marketing（市场营销） | 6 | [positioning-messaging](skills/positioning-messaging/), [launch-marketing](skills/launch-marketing/), [content-marketing](skills/content-marketing/) |
| Communication（沟通） | 5 | [written-communication](skills/written-communication/), [giving-presentations](skills/giving-presentations/), [running-effective-meetings](skills/running-effective-meetings/) |
| Engineering（工程） | 5 | [engineering-culture](skills/engineering-culture/), [platform-infrastructure](skills/platform-infrastructure/), [managing-tech-debt](skills/managing-tech-debt/) |
| Design（设计） | 2 | [design-systems](skills/design-systems/), [design-engineering](skills/design-engineering/) |

完整列表：[docs/SKILLS_CATALOG.zh-CN.md](docs/SKILLS_CATALOG.zh-CN.md) | 推荐组合：[docs/PLAYBOOKS.zh-CN.md](docs/PLAYBOOKS.zh-CN.md)

## 快速使用

在 **Codex** 中，输入 `$` 并选择 skill：

```text
$writing-prds
Turn these notes into a decision-ready PRD. Ask up to 5 questions first.
```

在 **Claude Code** 中，用 `/` 调用：

```text
/writing-prds
Turn these notes into a decision-ready PRD. Ask up to 5 questions first.
```

## 安装

### 方案 A：从 GitHub Release 安装（推荐）

从[最新 Release](https://github.com/liqiongyu/lenny_skills_plus/releases) 下载 `skills-all.zip` 并解压：

```bash
# Codex（全局）
mkdir -p ~/.codex/skills && unzip -o skills-all.zip -d ~/.codex/skills

# Claude Code（全局）
mkdir -p ~/.claude/skills && unzip -o skills-all.zip -d ~/.claude/skills
```

如需 **项目级** 安装，解压到你项目的 `.codex/skills/` 或 `.claude/skills/` 中即可。

<details>
<summary><b>方案 B：clone + 复制</b></summary>

```bash
git clone https://github.com/liqiongyu/lenny_skills_plus.git
cd lenny_skills_plus

# 全局安装
mkdir -p ~/.codex/skills ~/.claude/skills
rsync -a skills/ ~/.codex/skills/
rsync -a skills/ ~/.claude/skills/
```

也可复制到目标项目的 `.codex/skills/` / `.claude/skills/` 作为项目级安装。

</details>

<details>
<summary><b>方案 C：通过 Codex <code>$skill-installer</code> 安装个别 skill</b></summary>

适合只需 1-5 个 skill 的场景：

```text
$skill-installer
Install `writing-prds` from `liqiongyu/lenny_skills_plus` at `skills/writing-prds`.
```

安装后重启 Codex。

</details>

<details>
<summary><b>方案 D：clone + mirror（适合贡献者）</b></summary>

```bash
git clone https://github.com/liqiongyu/lenny_skills_plus.git
cd lenny_skills_plus
python3 scripts/mirror_skills.py --overwrite
```

将 canonical `skills/` 镜像到 `.codex/skills/` 和 `.claude/skills/`，供工具自动发现（git-ignored）。

</details>

更多说明：[docs/USING_WITH_CODEX.zh-CN.md](docs/USING_WITH_CODEX.zh-CN.md) | [docs/USING_WITH_CLAUDE.zh-CN.md](docs/USING_WITH_CLAUDE.zh-CN.md)

## 为什么做这个项目

"高层方法论"对人类有帮助，但对 agent 来说不够可执行。本项目把技能写成执行合同：输入 → 交付物 → 工作流 → 质量门槛。详见：[docs/WHY_THIS_PROJECT.zh-CN.md](docs/WHY_THIS_PROJECT.zh-CN.md)。

## 仓库结构

```
skills/              Canonical skill packs（git 追踪）
scripts/             CI、镜像、生成等 Python 工具
sources/refound/     上游 manifest + URL 清单
docs/                项目文档
.codex/skills/       Codex 自动发现用的镜像（git-ignored）
.claude/skills/      Claude Code 自动发现用的镜像（git-ignored）
```

## 质量与 CI

```bash
# 校验所有 skill packs
python3 scripts/ci_check_skillpacks.py --skip-mirror-check

# 也校验镜像一致性（运行 mirror_skills.py 之后）
python3 scripts/ci_check_skillpacks.py
```

## 贡献

见 [CONTRIBUTING.zh-CN.md](CONTRIBUTING.zh-CN.md) 和 [docs/WORKFLOW.zh-CN.md](docs/WORKFLOW.zh-CN.md)。

## 署名与知识产权

本项目转化自 RefoundAI 的 "Lenny skills" 数据库，与 RefoundAI 无隶属关系。上游致谢与下架处理：[docs/ATTRIBUTION_AND_IP.zh-CN.md](docs/ATTRIBUTION_AND_IP.zh-CN.md)。

## License

Apache-2.0 — 见 [LICENSE](LICENSE)。
