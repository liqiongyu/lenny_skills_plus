# Maintenance

## Updating upstream sources

Upstream Refound content can change. This repo keeps “raw sources” out of git by default.

If you want to refresh upstream sources locally:

```bash
python3 skills/lenny-skillpack-creator/scripts/fetch_refound_skills.py --out sources/refound/raw
```

(You may need a browser-like User-Agent depending on upstream policies.)

## Adding a new skill pack

1) Create `skills/<new-skill>/`
2) Add `SKILL.md` + `README.md` + `references/`
3) Run lint:
   ```bash
   python3 skills/lenny-skillpack-creator/scripts/lint_skillpack.py skills/<new-skill>
   ```
4) Mirror for local use:
   ```bash
   python3 scripts/mirror_skills.py --overwrite
   ```

## Regenerating / converting again

If you re-run conversion via Codex, prefer:

- One skill per Codex run (keeps context small and avoids drift)
- Lint after each skill
- Smoke-test 1–2 real prompts per category before scaling

## Regenerating repo docs

- Skills catalog:
  - `python3 scripts/generate_skills_catalog.py`
- Audit report:
  - `python3 scripts/generate_audit_report.py`
