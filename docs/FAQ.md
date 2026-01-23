# FAQ / troubleshooting

> 中文版: [FAQ.zh-CN.md](FAQ.zh-CN.md)

## Codex doesn’t see my skills

- Confirm skills are mirrored into `.codex/skills/` (or installed in `~/.codex/skills/`).
- If you installed from `skills-all.zip`, confirm you unzipped into the *skills directory* (e.g., `~/.codex/skills/`) so the zip’s top-level folders become `~/.codex/skills/<skill-name>/`.
- Restart Codex after installing new skills.
- Ensure `SKILL.md` starts with YAML frontmatter and includes `name` and `description`.

## Claude Code doesn’t see my skills

- Confirm skills are mirrored into `.claude/skills/` (or installed in `~/.claude/skills/`).
- If you installed from `skills-all.zip`, confirm you unzipped into the *skills directory* (e.g., `~/.claude/skills/`) so the zip’s top-level folders become `~/.claude/skills/<skill-name>/`.
- Ensure the directory is `.../skills/<skill-name>/SKILL.md` (not `.../skills/<skill-name>.md`).
- Verify `name` matches the folder name.

## A skill triggers too often / not often enough

- Tighten or broaden the `description` field in `SKILL.md`.
- Add more explicit “When to use” language in `SKILL.md`.
- Keep skills narrow; overlapping skills confuse automatic selection.

## I want stricter safety controls

- Keep mirrors project-local (`.codex/skills`, `.claude/skills`) so scope is limited.
- Prefer sandboxed execution (Codex) and avoid scripts unless you need determinism.
