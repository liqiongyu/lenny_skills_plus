# Lenny Skills Plus

> 中文版: [README.zh-CN.md](README.zh-CN.md)

[![CI](https://github.com/liqiongyu/lenny_skills_plus/actions/workflows/ci.yml/badge.svg)](https://github.com/liqiongyu/lenny_skills_plus/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Skills: 87](https://img.shields.io/badge/Skills-87-green.svg)](docs/SKILLS_CATALOG.md)

A curated library of **87 agent-executable skill packs** (86 converted from RefoundAI's "Lenny skills" + 1 meta-skill) that follow the open **Agent Skills** format. Works with both **OpenAI Codex** and **Claude Code**.

Each skill pack defines scope, required inputs, concrete deliverables, a step-by-step workflow, and quality gates — so agents produce reviewable artifacts instead of generic advice.

## Skills at a Glance

| Category | Count | Good Starting Points |
|---|---:|---|
| Product Management | 22 | [problem-definition](skills/problem-definition/), [writing-prds](skills/writing-prds/), [shipping-products](skills/shipping-products/) |
| Leadership | 14 | [managing-up](skills/managing-up/), [delegating-work](skills/delegating-work/), [having-difficult-conversations](skills/having-difficult-conversations/) |
| Career | 7 | [negotiating-offers](skills/negotiating-offers/), [career-transitions](skills/career-transitions/), [building-a-promotion-case](skills/building-a-promotion-case/) |
| Sales & GTM | 7 | [founder-sales](skills/founder-sales/), [enterprise-sales](skills/enterprise-sales/), [sales-qualification](skills/sales-qualification/) |
| Hiring & Teams | 6 | [writing-job-descriptions](skills/writing-job-descriptions/), [conducting-interviews](skills/conducting-interviews/), [onboarding-new-hires](skills/onboarding-new-hires/) |
| AI & Technology | 6 | [building-with-llms](skills/building-with-llms/), [ai-evals](skills/ai-evals/), [vibe-coding](skills/vibe-coding/) |
| Growth | 6 | [retention-engagement](skills/retention-engagement/), [user-onboarding](skills/user-onboarding/), [marketplace-liquidity](skills/marketplace-liquidity/) |
| Marketing | 6 | [positioning-messaging](skills/positioning-messaging/), [launch-marketing](skills/launch-marketing/), [content-marketing](skills/content-marketing/) |
| Communication | 5 | [written-communication](skills/written-communication/), [giving-presentations](skills/giving-presentations/), [running-effective-meetings](skills/running-effective-meetings/) |
| Engineering | 5 | [engineering-culture](skills/engineering-culture/), [platform-infrastructure](skills/platform-infrastructure/), [managing-tech-debt](skills/managing-tech-debt/) |
| Design | 2 | [design-systems](skills/design-systems/), [design-engineering](skills/design-engineering/) |

Full list: [docs/SKILLS_CATALOG.md](docs/SKILLS_CATALOG.md) | Curated bundles: [docs/PLAYBOOKS.md](docs/PLAYBOOKS.md)

## Quick Usage

In **Codex**, type `$` and pick a skill:

```text
$writing-prds
Turn these notes into a decision-ready PRD. Ask up to 5 questions first.
```

In **Claude Code**, invoke with `/`:

```text
/writing-prds
Turn these notes into a decision-ready PRD. Ask up to 5 questions first.
```

## Install

### Option A: From GitHub Release (recommended)

Download `skills-all.zip` from the [latest release](https://github.com/liqiongyu/lenny_skills_plus/releases) and unzip:

```bash
# For Codex (global)
mkdir -p ~/.codex/skills && unzip -o skills-all.zip -d ~/.codex/skills

# For Claude Code (global)
mkdir -p ~/.claude/skills && unzip -o skills-all.zip -d ~/.claude/skills
```

For **project-local** install, unzip into `.codex/skills/` or `.claude/skills/` in your repo instead.

<details>
<summary><b>Option B: Clone + copy</b></summary>

```bash
git clone https://github.com/liqiongyu/lenny_skills_plus.git
cd lenny_skills_plus

# Global install
mkdir -p ~/.codex/skills ~/.claude/skills
rsync -a skills/ ~/.codex/skills/
rsync -a skills/ ~/.claude/skills/
```

Or copy into `.codex/skills/` / `.claude/skills/` in your target repo for project-local install.

</details>

<details>
<summary><b>Option C: Install individual skills via Codex <code>$skill-installer</code></b></summary>

Best when you only need 1-5 skills:

```text
$skill-installer
Install `writing-prds` from `liqiongyu/lenny_skills_plus` at `skills/writing-prds`.
```

Restart Codex after installing.

</details>

<details>
<summary><b>Option D: Clone + mirror (for contributors)</b></summary>

```bash
git clone https://github.com/liqiongyu/lenny_skills_plus.git
cd lenny_skills_plus
python3 scripts/mirror_skills.py --overwrite
```

This mirrors canonical `skills/` into `.codex/skills/` and `.claude/skills/` for auto-discovery (git-ignored).

</details>

See also: [docs/USING_WITH_CODEX.md](docs/USING_WITH_CODEX.md) | [docs/USING_WITH_CLAUDE.md](docs/USING_WITH_CLAUDE.md)

## Why This Exists

High-level advice is hard for agents to execute reliably. This repo turns skills into execution contracts: inputs → deliverables → workflow → quality gate. See: [docs/WHY_THIS_PROJECT.md](docs/WHY_THIS_PROJECT.md).

## Repo Layout

```
skills/              Canonical skill packs (tracked in git)
scripts/             Python utilities for CI, mirroring, and generation
sources/refound/     Upstream manifest + URL lists
docs/                Documentation
.codex/skills/       Generated mirror for Codex (git-ignored)
.claude/skills/      Generated mirror for Claude Code (git-ignored)
```

## Quality + CI

```bash
# Lint all skill packs
python3 scripts/ci_check_skillpacks.py --skip-mirror-check

# Also validate mirrors (after running mirror_skills.py)
python3 scripts/ci_check_skillpacks.py
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [docs/WORKFLOW.md](docs/WORKFLOW.md).

## Attribution & IP

These skill packs are derived from RefoundAI's "Lenny skills" database. This project is not affiliated with RefoundAI. Upstream credit and takedown policy: [docs/ATTRIBUTION_AND_IP.md](docs/ATTRIBUTION_AND_IP.md).

## License

Apache-2.0 — see [LICENSE](LICENSE).
