# Conversion workflow (recommended)

> 中文版: `WORKFLOW.zh-CN.md`

This is the repeatable process for converting one Refound/Lenny skill into an executable skill pack.

1. Fetch source material
   - Prefer downloading `/skills/<slug>/SKILL.md` (Agent Skills format).
   - If blocked, save the HTML page (`/lenny-skills/s/<slug>/`) and convert from that.

2. Create a target slug
   - Use lowercase + hyphens (Agent Skills naming constraints).
   - Keep the slug stable (it becomes the skill command name).

3. Invoke `$lenny-skillpack-creator`
   Provide:
   - Source content path (SKILL.md or page.html)
   - Intended persona
   - Desired deliverables

4. Ensure the generated skill pack has:
   - skillpack.json (per-skill version + authors + upstream link)
   - SKILL.md (short + operational)
   - references/INTAKE.md
   - references/WORKFLOW.md
   - references/TEMPLATES.md
   - references/CHECKLISTS.md
   - references/RUBRIC.md
   - references/SOURCE_SUMMARY.md
   - README.md (install + invoke + examples)

5. Run the linter
   - `python3 skills/lenny-skillpack-creator/scripts/lint_skillpack.py <skill-dir>`

6. Smoke test
   - Run 1–2 realistic tasks and check that outputs match the “Output contract”.

7. Generate local mirrors (recommended)
   - Run `python3 scripts/mirror_skills.py --overwrite` to populate `.codex/skills/` and `.claude/skills/` for tool auto-discovery.

8. Commit
   - Commit after each skill or small batch; keep diffs reviewable.
