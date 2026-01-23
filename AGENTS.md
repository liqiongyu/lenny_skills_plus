# Lenny Skillpack Factory — Agent Instructions (Codex)

You are working in a repository whose sole purpose is to convert RefoundAI “Lenny skills” into **agent-executable skill packs**.

Primary goals:
1) Produce **high-density, testable** Agent Skills skill packs (not essays).
2) Ensure outputs are **compatible with both OpenAI Codex and Claude Code** (use the common Agent Skills subset).
3) All generated skill packs must be written in **English**.

## Repo conventions

- Canonical generated skills live under:
  - `skills/<skill-slug>/` (preferred, tool-agnostic, tracked in git)

- `.codex/` and `.claude/` are **generated local mirrors** for tool auto-discovery and are **not tracked in git**.
  - Generate/update them via: `python3 scripts/mirror_skills.py --overwrite`
  - Codex discovers project skills from `.codex/skills/<skill-slug>/`
  - Claude Code discovers project skills from `.claude/skills/<skill-slug>/`

- Source materials (downloaded from Refound) should be stored under:
  - `sources/refound/raw/<slug>/SKILL.md` if available
  - otherwise `sources/refound/raw/<slug>/page.html` as a fallback

## How to convert one skill

For each conversion task:
1) Locate the source skill (`sources/refound/raw/...`) or use the URL list/manifest under `sources/refound/`.
2) Invoke the meta-skill:
   - `$lenny-skillpack-creator`
3) Generate an installable skill folder:
   - `<skill-slug>/SKILL.md`
   - `<skill-slug>/README.md`
   - `<skill-slug>/references/` (intake/workflow/templates/checklists/rubric/source summary)
   - `<skill-slug>/scripts/` (optional)
4) Run the linter:
   - `python3 skills/lenny-skillpack-creator/scripts/lint_skillpack.py <path-to-skill-folder>`
5) Do a quick smoke test:
   - Use 1–2 realistic user prompts and verify the outputs are concrete artifacts (not generic advice).

## Quality bar (non-negotiable)

- Skills must have a clear boundary:
  - When to use / When NOT to use
- Must define an input/output contract:
  - minimum required inputs + missing-info strategy
  - explicit deliverables (files or structured outputs)
- Must provide a step-by-step workflow (5–9 steps)
- Must include quality gates:
  - checklists + rubric + “risks/open questions/next steps”
- Keep SKILL.md concise; put long content in `references/`.
- Keep everything in English.

## Safety

- Do not request secrets or credentials.
- Avoid irreversible changes without explicit confirmation.
- Prefer least privilege when deciding to run scripts or modify files.

## GitHub operations (project policy)

- For all GitHub operations (repo setup, issues/PRs, releases, workflows), use GitHub CLI (`gh`).
- Use `git` for local version control (commit/branch/rebase); use `gh` for GitHub-specific actions.
