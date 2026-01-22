# Refound / Lenny skill sources

This folder contains helper files for discovering and downloading the original RefoundAI “Lenny Skills”:

- `refound_lenny_skills_manifest.csv` — category/title/slug + URLs
- `refound_lenny_skills_manifest.md` — the same manifest in Markdown
- `refound_lenny_skill_md_urls.txt` — a plain list of the `/skills/<slug>/SKILL.md` URLs

To download sources in bulk, run:

`python .codex/skills/lenny-skillpack-creator/scripts/fetch_refound_skills.py --out sources/refound/raw`

It will:
1) Fetch the browse page to discover slugs
2) Attempt to download `/skills/<slug>/SKILL.md`
3) If blocked, it saves the HTML page for that skill as a fallback

