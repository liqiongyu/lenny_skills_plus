# Lenny Skills Plus

A curated library of **86 high-density, agent-executable skill packs** converted from RefoundAI’s “Lenny skills” database, plus a meta-skill (`lenny-skillpack-creator`) for converting additional skills.

These skill packs follow the **open Agent Skills** format (a folder with `SKILL.md` + supporting files) and are designed to work in both:

- **OpenAI Codex (CLI + IDE)** via `.codex/skills/` or `~/.codex/skills/`
- **Claude Code** via `.claude/skills/` or `~/.claude/skills/`

If you just want to **use the skills**, you do *not* need to clone this repo or run any conversion scripts — you can install the prebuilt skill packs from a GitHub Release.

> Note: Some upstream pages mention “87 skills”, but the current Refound browse/manifest contains **86** skills.

## Attribution & IP

These skill packs are derived from RefoundAI’s “Lenny skills” database. Upstream credit and takedown policy: `docs/ATTRIBUTION_AND_IP.md`.

## Quickstart

### Option A (recommended): Install from a release (no cloning)

1) Download `skills-all.zip` from the latest GitHub Release.
   - If your release doesn’t include `skills-all.zip` yet, you can still download individual per-skill zip files from the release.

2) Install for **Codex** (global):

```bash
mkdir -p ~/.codex/skills
unzip -o skills-all.zip -d ~/.codex/skills
```

3) Install for **Claude Code** (global):

```bash
mkdir -p ~/.claude/skills
unzip -o skills-all.zip -d ~/.claude/skills
```

If you prefer **project-local** skills, unzip into your repo at:
- `.codex/skills/` (Codex)
- `.claude/skills/` (Claude Code)

See:
- `docs/USING_WITH_CODEX.md`
- `docs/USING_WITH_CLAUDE.md`

### Option B: Clone + mirror (for contributors)

This repo keeps **canonical** skill packs under `skills/` (tracked in git) and provides scripts to mirror them into tool-specific directories for auto-discovery:

```bash
python3 scripts/mirror_skills.py --overwrite
```

This creates:
- `.codex/skills/<skill>/` for Codex
- `.claude/skills/<skill>/` for Claude Code

These mirror folders are ignored by git.

## Use in Codex

- Start Codex (either globally-installed skills, or any folder that can see `.codex/skills/`):
  ```bash
  codex
  ```
- Browse skills with `/skills` or type `$` to mention a skill.
- Example:
  ```text
  $writing-prds
  Turn these notes into a decision-ready PRD. Ask up to 5 questions first.
  ```

## Use in Claude Code

- Open your project in Claude Code (either globally-installed skills, or a repo with `.claude/skills/`).
- Invoke a skill directly with `/skill-name`.
- Example:
  ```text
  /writing-prds
  Turn these notes into a decision-ready PRD. Ask up to 5 questions first.
  ```

## Skill catalog

See: `docs/SKILLS_CATALOG.md`

## Why this exists

High-level advice is hard for agents to execute reliably. This repo turns skills into execution contracts (inputs → deliverables → workflow → quality gate). See: `docs/WHY_THIS_PROJECT.md`.

## Contributing / regeneration

If you want to help improve skill quality, add examples, or regenerate skill packs, start with:
- `CONTRIBUTING.md`
- `docs/WORKFLOW.md`

## Quality + CI

Run structure checks on all skill packs:

```bash
python3 scripts/ci_check_skillpacks.py --skip-mirror-check
```

If you mirrored to `.codex/skills` and `.claude/skills`, you can also validate mirrors:

```bash
python3 scripts/ci_check_skillpacks.py
```

## Repo layout

- `skills/` — canonical skill packs (tracked in git)
- `.codex/skills/` — generated mirror for Codex auto-discovery (ignored by git)
- `.claude/skills/` — generated mirror for Claude Code auto-discovery (ignored by git)
- `sources/refound/` — upstream manifest + URL lists
- `sources/refound/raw/` — optional downloaded upstream sources (ignored by git)
- `docs/` — documentation

## Contributing

See `CONTRIBUTING.md`.

## License

Apache-2.0 — see `LICENSE`.
