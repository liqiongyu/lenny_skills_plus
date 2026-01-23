# sales-compensation

Design a **Sales Comp Plan Pack**: OTE & pay mix + quotas & ramp + commission mechanics + retention-aligned incentives + rep-facing docs.

## What this skill produces
- Context snapshot + assumptions
- Role → metric mapping (what gets paid on)
- OTE + base/variable mix table
- Quota + ramp model (incl. scenarios)
- Commission mechanics spec (rates, accelerators, crediting, payout timing, clawbacks)
- Retention-alignment addendum (choose one approach)
- Admin & governance (CRM fields, payout process, disputes, exceptions)
- Rep-facing one-pager + FAQ
- Risks / Open questions / Next steps

## How to use (prompt)
Use language like:

“Use `sales-compensation`. Context: <company stage + GTM motion>. Roles: <AE/SDR/AM>. Product/pricing: <ACV/ARR + sales cycle>. Targets: <bookings/revenue/NRR + timeframe>. Constraints: <budget, margin, simplicity>. Output: a Sales Comp Plan Pack.”

If key details are missing, the skill asks up to 5 intake questions (see `references/INTAKE.md`) and then proceeds with explicit assumptions.

## Optional file output
If you want the deliverables as files, ask the agent to write them under a folder you specify (e.g., `docs/sales-compensation/`) using `references/TEMPLATES.md`.

## Example prompts
- “Set an OTE + quota + 4-month ramp plan for our first 2 AEs.”
- “Add retention alignment (90-day churn) without making the plan too complex.”
- “Create rep-facing comms + FAQ for rolling out a new comp plan.”

