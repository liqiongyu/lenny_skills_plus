# Refound / Lenny 上游来源说明

> English version: `README.md`

本目录包含用于发现/下载 RefoundAI “Lenny skills” 原始内容的辅助文件：

- `refound_lenny_skills_manifest.csv` — category/title/slug + URLs
- `refound_lenny_skills_manifest.md` — 同一份 manifest 的 Markdown 版本
- `refound_lenny_skills_manifest.zh-CN.md` — 同一份 manifest 的中文版本
- `refound_lenny_skill_md_urls.txt` — `/skills/<slug>/SKILL.md` URL 的纯文本列表

如果你需要批量下载上游源材料，请运行：

`python3 skills/lenny-skillpack-creator/scripts/fetch_refound_skills.py --out sources/refound/raw`

它会：
1) 抓取 browse 页以发现 slugs
2) 尝试下载每个 `/skills/<slug>/SKILL.md`
3) 如果被限制，会保存该 skill 的 HTML 页面作为兜底
