# working-backwards

Create a **Working Backwards Pack**: an Amazon-style **PR/FAQ** (future press release + FAQ) plus a **backcasting launch plan** to align teams on customer value, scope, and GTM readiness.

## What this skill produces
- Context snapshot
- 2–3 divergent future press releases (options)
- Selected, refined future press release
- FAQ (customer + business + technical/ops + legal/compliance)
- Backcasting plan (milestones, owners, dependencies)
- Stakeholder + “machinery” plan (approvals, comms, rollout, support readiness)
- Success metrics + guardrails (+ instrumentation notes)
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `working-backwards`. Context: <product + target user + problem>. Constraints: <launch window, platform, policy/legal, dependencies>. Output: a Working Backwards Pack (PR options + PR/FAQ + backcasting plan).”

If details are missing, the skill asks up to 5 intake questions (see [references/INTAKE.md](references/INTAKE.md)) and then proceeds with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/working-backwards/`) using [references/TEMPLATES.md](references/TEMPLATES.md).

## Example prompts
- “We want to launch ‘Team shared templates’ for our B2B design tool. Work backwards: draft 3 PR options, pick one, then write the PR/FAQ and a backcasting plan to beta in 6 weeks.”
- “Create a PR/FAQ for ‘Instant refunds’ and include legal/compliance FAQs and a rollback plan.”
- “We have a proposed solution; sanity-check it by working backwards from the customer problem and current alternatives.”

