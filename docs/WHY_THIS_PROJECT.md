# Why this project exists

> 中文版: `WHY_THIS_PROJECT.zh-CN.md`

RefoundAI’s “Lenny skills” are full of high-quality product/leadership patterns, but many entries are **too high-level** for reliable agent execution.

Modern agents (Codex, Claude Code, etc.) work best when the “skill” is an **execution contract**: clear inputs, explicit deliverables, a step-by-step workflow, and quality gates.

This repo converts the upstream skills into **agent-executable skill packs** that:

- Define a tight scope (when to use / when not to use)
- Require minimum inputs + a missing-info strategy (ask a few targeted questions)
- Produce concrete deliverables (templates, checklists, memos, plans, logs)
- Include quality gates (checklists + rubric) so results are reviewable
- Are compatible with both **Codex** and **Claude Code** (common Agent Skills subset)

Upstream credit & IP policy: see `ATTRIBUTION_AND_IP.md`.

## How to use (quick)

1) Mirror skills for tool auto-discovery:
   - `python3 scripts/mirror_skills.py --overwrite`
2) In Codex:
   - start `codex`, then use `$<skill-slug>` (e.g., `$writing-prds`)
3) In Claude Code:
   - invoke `/skill-slug` (e.g., `/writing-prds`)

## How to contribute (practical)

The fastest way to improve this library is “use → find gaps → PR”.

Good contributions:
- Make outputs more concrete (add templates/checklists/quality gates)
- Tighten scope to reduce false triggering
- Add better examples (good prompts + boundary prompt) in `references/EXAMPLES.md`
- Fix missing-info questions so the skill can start from imperfect input

Before opening a PR:
- Run: `python3 scripts/ci_check_skillpacks.py --skip-mirror-check`
- Keep skill content in **English**
- Prefer small diffs (1 skill or a small batch)
