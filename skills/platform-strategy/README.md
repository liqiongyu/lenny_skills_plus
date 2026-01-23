# platform-strategy

Create a **Platform Strategy Pack** for internal or external platforms (developer platforms, APIs, ecosystems, and AI platforms): clear users/jobs, interface boundaries, lifecycle stage strategy, ecosystem incentives, governance, metrics, and a roadmap.

## What this skill produces
- Platform Product Charter
- Platform Surface & Interface Map (“paved road” defaults + boundaries)
- Lifecycle Stage & Open/Close Strategy
- Moat & Ecosystem Model (compounding loops + seeding plan)
- Governance & Policy Plan (access, versioning, SLAs, pricing/packaging if relevant)
- Metrics & Operating Model
- 12‑month Roadmap
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `platform-strategy`. Platform type: <internal/external/hybrid>. Users: <who + top jobs>. Current state: <what exists + pain>. Why now: <reason>. Constraints: <security/privacy/compliance, SLOs, budget, timeline>. Decisions: <what’s on the table>. Output: Platform Strategy Pack.”

If details are missing, the skill asks up to 5 intake questions (see `references/INTAKE.md`) and then proceeds with explicit assumptions.

## Optional file output
If you want the pack as files, ask the agent to write the artifacts under a folder you specify (e.g., `docs/platform/<initiative>/`) using `references/TEMPLATES.md`.

## Example prompts
- “Use `platform-strategy` to design the strategy for our internal platform: focus on reducing developer cycle time and making paved-road defaults.”
- “Use `platform-strategy` for an external API platform. Include open/close governance, partner incentives, and a roadmap to 20 integrations.”
- “Use `platform-strategy` for an AI platform; include a context repository plan, permissions/audit logging, and evaluation/monitoring.”

