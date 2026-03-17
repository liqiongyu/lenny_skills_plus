# Showcase: Enterprise Sales

> Demonstrates the value of the `enterprise-sales` skill pack by comparing
> skill-guided output vs. a vanilla LLM response to the same prompt.

## Test Prompt

> Use `enterprise-sales`. Product: <...>. Account: <...>. Deal: ACV ~$80k, timeline 6 weeks. Stakeholders: champion in Ops, economic buyer in Finance, security review owned by IT. Blocker: procurement vendor onboarding + security questionnaire. Output: an Enterprise Deal Execution Pack with a MAP, procurement/security tracker, and champion one-pagers.

## Results Summary

| Dimension | Without Skill | With Skill |
|-----------|--------------|------------|
| Structure | 6 sections (MAP, trackers, champion one-pagers, risk register, communication cadence, contacts) | 8 numbered sections following a deal lifecycle: Deal Snapshot through Close + Implementation Handoff |
| Completeness | MAP, procurement/security trackers, 3 champion enablement one-pagers, risk register, communication cadence | All of the above plus a buying committee map, champion plan with backup path, objection/FAQ kit, decision guide with "do nothing" analysis, POC/pilot plan with ROI model, and implementation handoff |
| Actionability | Weekly MAP milestones with owners and dates; tracker with status columns | MAP with specific dates (March 17-May 5), evidence/output per milestone, buyer-owned commitments listed separately, and a procurement email template ready to send |
| Specificity | One-pagers use placeholder brackets for product details; security tracker lists 10 requirements | One-pagers include specific framing for IT, Procurement, Legal, and Economic Buyer audiences; security packet index with availability status per document |
| Quality gates | Risk register with 7 risks rated by likelihood/impact | Quality gate checklist covering 7 categories (scope, buying committee, enablement, decision enablement, POC, procurement, completeness) plus rubric self-score |

## Key Differences

1. **Buying committee map with champion plan.** The skill output maps 6 stakeholder roles with their goals, risk concerns, required evidence, and specific next actions. It includes a champion risk assessment and a backup path if the champion is lost. The baseline lists contacts in a table without analyzing their decision dynamics.

2. **Decision enablement framework.** The skill output includes a 1-page decision guide with 3 options (do nothing, expand existing tool, pilot), a "make do-nothing concrete" section quantifying inaction costs, and explicit decision criteria. The baseline focuses on the MAP timeline without a framework for helping the buyer decide.

3. **POC/pilot as business case.** The skill output frames the pilot goal as "produce a decision-ready business case," not just "test if it works." It includes 5 success metrics with baselines, targets, data sources, and owners, plus a simple ROI model. The baseline does not include a structured pilot plan.

4. **Champion enablement depth.** The skill output provides 4 distinct one-pagers (IT/Security, Procurement, Legal, Economic Buyer) plus an internal pitch memo and objection/FAQ cheat sheet -- all designed to be forwardable without seller involvement. The baseline has 3 one-pagers (business case, security, talking points) that are similarly useful but lacks the objection-handling and legal materials.

5. **Procurement proactive management.** The skill output includes a ready-to-send procurement email, a security packet index with availability tracking, and a proactive communications cadence with escalation rules. The baseline provides a thorough tracker but relies more on the seller managing the process rather than making it easy for the buyer.

## Verdict

The skill output is designed around a core insight: enterprise deals stall not because of missing information but because the buyer lacks internal decision-support tools. The champion enablement kit, decision guide, and "do nothing" cost analysis address the real blocker -- internal buyer alignment. The baseline is a solid execution tracker but is more seller-centric than buyer-enabling.

## With Skill Output

<details>
<summary>Expand full output (~19k)</summary>

See [with_skill.md](with_skill.md)

</details>

## Without Skill Output (Baseline)

<details>
<summary>Expand full output (~9k)</summary>

See [without_skill.md](without_skill.md)

</details>

---

**Metadata**
- Model: `claude-opus-4-6`
- Date: 2026-03-17
