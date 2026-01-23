# Press kit (copy & paste)

> 中文版: `PRESS_KIT.zh-CN.md`

This file contains ready-to-use copy for announcements, posts, and community outreach.

Upstream attribution & IP policy: see `ATTRIBUTION_AND_IP.md`.

## One-liners

- “Turn RefoundAI’s ‘Lenny skills’ into **agent-executable** skill packs for Codex and Claude Code.”
- “A community library of **86** high-density skill packs + a converter meta-skill.”
- “Skills that don’t just explain *what*—they produce *artifacts* (templates, checklists, plans).”

## Short description (1 paragraph)

Lenny Skills Plus is a curated library of **86 agent-executable skill packs** converted from RefoundAI’s “Lenny skills” database, plus a meta-skill (`lenny-skillpack-creator`) for converting more. Each skill pack defines scope, required inputs, concrete deliverables, a step-by-step workflow, and quality gates—so AI agents can reliably produce reviewable outputs instead of generic advice. Works with **OpenAI Codex** and **Claude Code** via project-local mirrors.

## What makes it different

- **Execution contract** per skill: inputs → deliverables → workflow → quality gate
- **Artifact-first** outputs (templates, logs, checklists, rubrics)
- **Cross-tool** compatible (Codex + Claude Code)
- **Community-friendly**: improve skills via small PRs as you use them

## Example prompts (for demos)

- `$writing-prds` — “Turn these notes into a decision-ready PRD. Ask up to 5 questions first.”
- `$ai-evals` — “Design evals for this LLM feature and produce a golden set + rubric + judge plan.”
- `$managing-timelines` — “We have a launch date. Convert it into milestones, scope control, and comms.”

## Suggested announcement posts

### X / Twitter

“We open-sourced Lenny Skills Plus: 86 agent-executable skill packs (plus a converter) that turn high-level advice into concrete artifacts—PRDs, checklists, templates, rubrics—usable in Codex + Claude Code. Repo: <link>”

### LinkedIn

“We’ve been collecting great product/leadership patterns for years, but agents need *execution contracts*, not essays.  
Lenny Skills Plus converts RefoundAI’s ‘Lenny skills’ into 86 agent-executable skill packs (plus a meta-skill to convert more): scope boundaries, input/output contracts, workflows, and quality gates.  
If you use a skill and find gaps, PRs are welcome. Repo: <link>”

### Hacker News

Title: “Show HN: Lenny Skills Plus — 86 agent-executable skill packs for Codex + Claude Code”

Body:
- What: 86 skill packs + a converter meta-skill
- Why: high-level advice → agent-executable workflows with artifacts + quality gates
- How: mirror `skills/` into `.codex/skills` + `.claude/skills` and invoke by name
- Ask: feedback on the format + contributions from real-world use

## Boilerplate (for articles)

Lenny Skills Plus is an open-source repository that turns high-level “skills” content into agent-executable skill packs. It focuses on artifact-driven outputs, missing-info strategies, and quality gates. The project is community-driven and welcomes improvements via small pull requests based on real usage.
