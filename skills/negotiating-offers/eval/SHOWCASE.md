# Showcase: Negotiating Offers

> Demonstrates the value of the `negotiating-offers` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `negotiating-offers`. I received a PM offer from a Series B developer tools startup (60 people): $165k base, 0.08% equity (4-year vest, 1-year cliff), $5k signing bonus, standard benefits. My current comp is $175k base + RSUs worth ~$40k/year at a public company. The startup role has better scope (own the entire developer experience product line) but seems under-resourced (no designer allocated, 3 engineers). I want to negotiate for a higher base ($180k+), better equity (0.12%+), a dedicated designer within 6 months, and a $10k learning budget. Draft an Offer Negotiation Pack with a success-conditions analysis, A/B/C package strategy, a recruiter email, and a hiring-manager conversation agenda. Output: Offer Negotiation Pack.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 8 sections: situation summary, success-conditions analysis, A/B/C packages, recruiter email draft, hiring-manager conversation agenda, negotiation tactics, timeline, risk assessment + equity valuation appendix | 8 sections: offer snapshot + timeline, goals/priorities/BATNA, success conditions + resourcing asks, offer components + tradeoff matrix, A/B/C ask packages + strategy, scripts pack (4 scripts), alternative structure proposal, and risks/open questions |
| Completeness | Covers all requested elements; adds useful extras: negotiation tactics do's/don'ts, equity valuation sanity check, and a 10-day decision timeline | Covers all elements plus a formal BATNA statement, 4 success-condition asks with verification methods, a "features vs experiences" assessment, and an explicit decision rule |
| Actionability | Recruiter email is detailed and well-structured; hiring-manager agenda has time-blocked segments with specific questions and "what you're listening for" coaching | 4 complete scripts (recruiter email, hiring-manager agenda with if/then branches, comp call script with pushback responses, and a follow-up recap template); success conditions include "how we verify in writing" column |
| Specificity | A/B/C packages have specific numbers; success conditions table with achievability ratings; equity valuation appendix walks through back-of-envelope math | A/B/C packages have specific numbers with explicit trade-offs between them; must-haves, tradeables, nice-to-haves, and dealbreakers are clearly separated; each lever has a priority label and rationale |
| Quality gates | Pilot scorecard not included; no formal self-assessment | 17-item checklist plus an 8-dimension rubric scoring 16/16 |

## Key Differences

1. **BATNA and decision rule clarity.** The skill output states the BATNA explicitly ("stay in current role at $215k total comp") and defines a precise decision rule ("Accept if package >= C AND designer commitment is in writing; otherwise stay"). The baseline discusses leverage and walk-away floors but does not formalize them into a decision rule that can be applied in the moment.

2. **Success conditions tied to outcomes.** The skill version defines 4 success conditions (ship quality DX improvements, execute roadmap, drive cross-functional alignment, demonstrate measurable impact) and maps each to a likely blocker, an ask, a rationale, and a verification method. The baseline identifies success conditions but frames them primarily through the lens of negotiation leverage rather than role success.

3. **Four-script pack with if/then branches.** The skill output provides 4 distinct scripts: initial recruiter email, hiring-manager conversation agenda with if/then response branches (e.g., "if they say 'we'll see' on the designer, follow up with..."), a comp call script with responses to three types of pushback, and a follow-up recap template. The baseline provides a recruiter email and HM agenda but the HM agenda focuses on question sequencing rather than response handling.

4. **Tradeoff matrix with priority labels.** The skill version inventories every offer component across 5 categories (cash, equity, role, lifestyle, experience) with current offer, ask, priority level (Must/Trade/Nice), rationale, and explicit trades ("Will accept $175k base if equity is at 0.12%+"). The baseline organizes packages in A/B/C tiers but does not map inter-component trade-offs as explicitly.

5. **Sequence strategy.** The skill output explicitly recommends leading with success conditions (hiring-manager conversation) before negotiating comp (recruiter), explaining the strategic logic: it shows you care about impact before money, builds the case for higher comp through scope, and creates goodwill. The baseline recommends having the HM conversation after the recruiter call, which reverses this sequence.

## Verdict

Both outputs produce high-quality, practical negotiation plans. The baseline adds unique value through its equity valuation appendix and negotiation tactics section. The skill-guided version excels in operational readiness: its four scripts with if/then branches, explicit decision rule, outcome-tied success conditions, and inter-component tradeoff matrix make it more robust for live negotiation scenarios where decisions happen in real time.

## With Skill Output

<details>
<summary>Expand full output (~26k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~17k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
