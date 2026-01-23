# Lenny Skills Plus — Agent Instructions

You are working in a repository that serves two purposes:
1) A **curated library** of agent-executable skill packs under `skills/` (installable from GitHub Releases).
2) A **skillpack factory**: tooling + workflows to convert RefoundAI “Lenny skills” into reliable, portable skill packs.

Primary goals:
1) Produce **high-density, testable** Agent Skills skill packs (not essays).
2) Ensure outputs are **compatible with both OpenAI Codex and Claude Code** (use the common Agent Skills subset).
3) All generated skill pack content must be written in **English**.

Start here (repo docs):
- [README.md](README.md) (overview + install)
- [docs/README.md](docs/README.md) (documentation index)
- [docs/WORKFLOW.md](docs/WORKFLOW.md) (conversion workflow)
- [docs/SKILL_PACK_FORMAT.md](docs/SKILL_PACK_FORMAT.md) (house style)
- [docs/QUALITY_BAR.md](docs/QUALITY_BAR.md) (quality gates)

## Repo conventions

### Canonical skill packs (tracked)

- Canonical skills live under `skills/<skill-slug>/` (tool-agnostic, tracked in git).
- Each skill pack must include:
  - `skillpack.json` (metadata used by this repo’s tooling + releases)
  - `SKILL.md` (Agent Skills entrypoint; YAML frontmatter with `name`, `description`)
  - `README.md` (human-friendly overview + example prompts)
  - `references/` core set:
    - `INTAKE.md`, `WORKFLOW.md`, `TEMPLATES.md`, `CHECKLISTS.md`, `RUBRIC.md`, `SOURCE_SUMMARY.md`, `EXAMPLES.md`
  - `scripts/` (optional; only when it materially improves determinism)

### Tool mirrors (generated, not tracked)

- `.codex/skills/<skill-slug>/` and `.claude/skills/<skill-slug>/` are **generated mirrors** for tool auto-discovery and are **ignored by git**.
- Generate/update via: `python3 scripts/mirror_skills.py --overwrite`.

### Upstream sources (usually local-only)

- Keep bulk-downloaded Refound sources out of git by default.
- Store sources under:
  - `sources/refound/raw/<slug>/SKILL.md` (preferred), or
  - `sources/refound/raw/<slug>/page.html` (fallback).
- (Optional) Fetch sources in bulk: `python3 skills/lenny-skillpack-creator/scripts/fetch_refound_skills.py --out sources/refound/raw`

## How to convert one skill (repeatable)

1) Locate/collect the upstream source (`sources/refound/raw/...`) or confirm the slug + URLs from `sources/refound/`.
2) Invoke the meta-skill: `$lenny-skillpack-creator`.
3) Write/update the canonical folder: `skills/<skill-slug>/` (including `skillpack.json` + `references/EXAMPLES.md`).
4) Run the linter:
   - `python3 skills/lenny-skillpack-creator/scripts/lint_skillpack.py skills/<skill-slug>`
5) Smoke test:
   - Use 1–2 realistic prompts and verify the output is concrete artifacts (templates/checklists/memos), not generic advice.
6) (Recommended) Mirror for local discovery:
   - `python3 scripts/mirror_skills.py --overwrite`

## Documentation rules (navigation + bilingual)

- Prefer **clickable relative links** when referencing other repo docs (don’t leave doc references only as inline code).
  - Example: `[docs/WORKFLOW.md](docs/WORKFLOW.md)`
- Root + `docs/` documentation is bilingual (EN + `*.zh-CN.md`). Keep the top-of-file language switch marker present and correct.
  - Check pairing/alignment: `python3 scripts/check_bilingual_docs.py`
- Generated docs should be regenerated, not hand-edited:
  - Skills catalog: `python3 scripts/generate_skills_catalog.py`
  - Audit report: `python3 scripts/generate_audit_report.py`

## Quality bar (non-negotiable)

- Clear boundary: When to use / When NOT to use.
- Explicit input contract + missing-info strategy.
- Explicit output contract (deliverables/artifacts).
- 5–9 step workflow with checks / definition of done.
- Quality gates: checklists + rubric + always include “Risks / Open questions / Next steps”.
- Keep `SKILL.md` concise; put depth in `references/`.
- Keep skill pack content in **English** (tool compatibility).

## Safety

- Do not request secrets or credentials.
- Avoid irreversible changes without explicit confirmation.
- Prefer least privilege when deciding to run scripts or modify files.

## GitHub operations (project policy)

- For GitHub operations (issues/PRs/releases/workflows), use GitHub CLI (`gh`).
- Use `git` for local version control; use `gh` when it’s “a GitHub thing”.
