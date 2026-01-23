# Lenny Skillpack Creator

This is a meta-skill that converts “insight-heavy” Refound/Lenny skills into **agent-executable skill packs** (clear boundaries, explicit input/output contracts, templates, checklists, and quality gates).

The resulting skill packs are written to the **Agent Skills** format so they can be used by both **OpenAI Codex** and **Claude Code**.

## Install

### Option A: Project-local (recommended)

Canonical source lives at:

- `skills/lenny-skillpack-creator/`

To enable project-local auto-discovery, generate local mirrors:

- `python3 scripts/mirror_skills.py --overwrite`

That populates one (or both) of these locations inside your repo:

- **Codex**: `.codex/skills/lenny-skillpack-creator/`
- **Claude Code**: `.claude/skills/lenny-skillpack-creator/`

Note: `.codex/` and `.claude/` are generated local directories and are typically ignored by git.

The [SKILL.md](SKILL.md) ends up at:

- `.codex/skills/lenny-skillpack-creator/SKILL.md`
- `.claude/skills/lenny-skillpack-creator/SKILL.md`

### Option B: User/global install

- **Codex (macOS/Linux default)**: `~/.codex/skills/lenny-skillpack-creator/`
- **Claude Code**: `~/.claude/skills/lenny-skillpack-creator/`

## Use

1) Provide the source Refound/Lenny skill content (either the original [SKILL.md](SKILL.md) or copied guide text).
2) Tell the agent:
   - the intended agent persona (PM, recruiter, founder, etc.)
   - the desired deliverables (artifacts)

### In Codex

Start typing `$` and select `lenny-skillpack-creator`, or run `/skills` and select it, then paste your request.

### In Claude Code

Run `/lenny-skillpack-creator` (or describe what you want and explicitly reference the skill).

## Output format (generated skill packs)

Each converted skill becomes a folder like:

- `<skill-slug>/SKILL.md`
- `<skill-slug>/README.md`
- `<skill-slug>/references/*` (templates, checklists, rubrics, source notes)
- `<skill-slug>/scripts/*` (optional helpers)

See [references/SKILL_PACK_SPEC.md](references/SKILL_PACK_SPEC.md) for the exact structure used by this generator.

## Scripts

This meta-skill includes helper scripts under `scripts/`:

- `init_skillpack.py` — scaffold a new skill pack folder
- `lint_skillpack.py` — validate structure + required files
- `package_skillpack.py` — zip a skill pack for distribution
- `fetch_refound_skills.py` — download Refound SKILL.md sources (given URL list or manifest)
- `extract_lenny_skill.py` — extract a Refound skill into a normalized source bundle
- `batch_init_skillpacks.py` — create skeletons for many skills at once
