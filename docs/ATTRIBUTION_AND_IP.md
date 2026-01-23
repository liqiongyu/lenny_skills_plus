# Attribution & IP policy (Refound/Lenny)

This project exists to make the “Lenny skills” content easier for modern AI agents to **execute** (concrete artifacts, checklists, templates, quality gates), while **respecting the upstream creators**.

## Upstream source / credit

- Primary upstream source: RefoundAI “Lenny skills” database: `https://refoundai.com/lenny-skills/`
- This repository is **not affiliated with RefoundAI** or with Lenny / Lenny’s Podcast.
- If you operate this as a public/community project, we recommend requesting explicit permission: `REQUESTING_UPSTREAM_PERMISSION.md`.

## What this repo contains (and avoids)

- ✅ `skills/`: “agent-executable” skill packs in the open Agent Skills folder format.
- ✅ `sources/refound/`: a manifest + URL list pointing to upstream pages (for attribution and traceability).
- ❌ We do **not** commit bulk-downloaded upstream pages/content to git. Local copies belong in `sources/refound/raw/` (gitignored).

## Intent (why we’re doing this)

We believe the upstream “Lenny skills” are valuable but often **too high-level** for reliable agent execution. This repo converts them into:

- Clear scope boundaries (when to use / when not to use)
- An explicit input/output contract
- A short, step-by-step workflow
- Required quality gates (checklists + rubric)

## IP & takedown policy (non-legal, practical)

We aim to respect all intellectual property rights and handle concerns quickly.

If you are a rights holder (or authorized agent) and believe any content in this repository should be removed or changed:

1) Open a GitHub issue with:
   - The skill slug(s) (e.g., `writing-prds`)
   - The upstream URL(s)
   - The specific concern and requested action (remove / modify / attribute differently)
2) We will respond and take appropriate action (including removal) as needed.

If you prefer formal channels, GitHub also provides a DMCA takedown process.

## Contributor expectations (attribution-safe contributions)

- Do **not** paste upstream content verbatim into the repo.
- Keep skill packs **English** (tool compatibility).
- Prefer small, reviewable PRs (1 skill or a small batch).
- If you edit a skill, keep it artifact-driven and update `references/EXAMPLES.md` so others can test it.
