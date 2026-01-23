# FAQ / troubleshooting

## Codex doesn’t see my skills

- Confirm skills are mirrored into `.codex/skills/` (or installed in `~/.codex/skills/`).
- Restart Codex after installing new skills.
- Ensure `SKILL.md` starts with YAML frontmatter and includes `name` and `description`.

## Claude Code doesn’t see my skills

- Confirm skills are mirrored into `.claude/skills/` (or installed in `~/.claude/skills/`).
- Ensure the directory is `.../skills/<skill-name>/SKILL.md` (not `.../skills/<skill-name>.md`).
- Verify `name` matches the folder name.

## A skill triggers too often / not often enough

- Tighten or broaden the `description` field in `SKILL.md`.
- Add more explicit “When to use” language in `SKILL.md`.
- Keep skills narrow; overlapping skills confuse automatic selection.

## I want stricter safety controls

- Keep mirrors project-local (`.codex/skills`, `.claude/skills`) so scope is limited.
- Prefer sandboxed execution (Codex) and avoid scripts unless you need determinism.
