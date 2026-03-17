# PM Coaching Plan: Strengthening Problem Framing & Tradeoff Decision-Making

## Context

- **Team:** Growth team, weekly release cadence
- **PM Profile:** Reliable shipper; strong execution. Key development areas: problem framing and making crisp tradeoffs.

---

## 1. Diagnosis: Understanding the Gaps

### Problem Framing Weakness — What It Looks Like

- Features ship on time but sometimes solve the wrong problem or a symptom rather than a root cause.
- PRDs jump to solutions before clearly articulating the user pain or business opportunity.
- Discovery work tends to be shallow — confirmation-seeking rather than genuinely exploratory.
- Stakeholders occasionally push back with "why are we building this?" after work has begun.

### Tradeoff Weakness — What It Looks Like

- Difficulty saying no; scope creeps because every request feels equally important.
- Decisions get escalated or delayed when two reasonable options exist.
- Rationale behind prioritization choices is hard to reconstruct after the fact.
- The team sometimes feels whiplash when direction changes mid-sprint.

---

## 2. Coaching Philosophy

1. **Coach in the workflow, not beside it.** Attach coaching to real artifacts (PRDs, roadmap reviews, retros) rather than adding standalone "coaching sessions" that feel like overhead.
2. **Reps over theory.** Each week's release is a live practice ground. Use it.
3. **Make thinking visible.** The goal is not to change what the PM decides but to make *how* they decide legible to themselves and others.
4. **Progressively remove scaffolding.** Start with structured templates and prompts; fade them as the PM internalizes the habits.

---

## 3. Twelve-Week Coaching Plan

### Phase 1: Foundations (Weeks 1–4) — "See the Problem Clearly"

**Focus:** Sharpen problem framing before any solution work begins.

#### Week 1: Baseline & Contracting

- **Activity:** 1:1 coaching kickoff (60 min).
  - Review the PM's last 3 shipped features. For each, ask: *"What was the problem we were solving? How did we know it was the right problem? What did we choose not to solve?"*
  - Collaboratively identify 2–3 specific moments where better framing would have changed the outcome.
- **Agreement:** Establish a coaching rhythm — 30 min weekly check-in, plus async review of one artifact per week.
- **Homework:** PM writes a one-page "problem brief" for the next feature in the pipeline, using the format below.

**Problem Brief Template:**

| Section | Prompt |
|---|---|
| **Who** is affected? | Specific user segment, not "users" |
| **What** is the pain/opportunity? | Observable behavior or metric, not an assumed need |
| **Evidence** | 3+ data points (quantitative or qualitative) |
| **Why now?** | What changed or what's the cost of delay? |
| **What's out of scope?** | Adjacent problems we are explicitly not solving |
| **Success looks like** | Leading indicator we'd see in 2–4 weeks |

#### Week 2: Problem vs. Solution Separation Drill

- **Activity:** Review the problem brief together. Coach pushes back anywhere a solution has leaked into the problem statement.
  - Technique: *"Read me only the problem. Now — could three completely different solutions address this? If not, you've defined a solution, not a problem."*
- **Live exercise:** Take an incoming stakeholder request and rewrite it as a problem statement in real time.
- **Homework:** PM interviews 3 users or reviews 3 support tickets related to the current project. Writes updated problem brief incorporating what they learned.

#### Week 3: The "5 Whys" and Upstream Framing

- **Activity:** Introduce root-cause framing.
  - Walk through a past feature where the team solved a symptom. Apply "5 Whys" retroactively to find the upstream problem.
  - Discuss: *"If we'd framed the problem one level up, what would we have built differently?"*
- **Live exercise:** Apply 5 Whys to the current sprint's top priority.
- **Homework:** PM documents the "problem tree" (symptom → root cause → upstream opportunity) for the next planned feature.

#### Week 4: Phase 1 Checkpoint

- **Activity:** PM presents their problem brief and problem tree to the coaching manager and one peer PM.
  - Rubric: Can the audience articulate the problem without referencing any solution? Do they agree the evidence supports the framing?
- **Reflection:** What's feeling different? Where is it still hard?
- **Deliverable:** PM commits to using the problem brief format for all new work going forward.

---

### Phase 2: Tradeoff Muscle (Weeks 5–8) — "Decide and Defend"

**Focus:** Build a repeatable framework for making and communicating tradeoffs.

#### Week 5: Tradeoff Frameworks Introduction

- **Activity:** Teach 2–3 lightweight tradeoff tools:
  1. **2x2 Matrix** — Impact vs. Effort, with explicit criteria for each axis.
  2. **Reversibility Test** — *"Is this a one-way door or a two-way door?"* One-way doors deserve more deliberation; two-way doors should be decided fast.
  3. **Opportunity Cost Framing** — *"If we do X, what can't we do? What's the cost of that?"*
- **Live exercise:** Take the current backlog and force-rank the top 5 items using one of these tools, talking through the reasoning aloud.
- **Homework:** PM writes a one-paragraph "tradeoff memo" for the biggest scoping decision in the current sprint: what was chosen, what was rejected, and why.

#### Week 6: Saying No with Evidence

- **Activity:** Role-play exercise. Coach plays a stakeholder making a reasonable but low-priority request. PM must decline or defer using data and the problem brief.
  - Debrief: What language felt natural? What felt uncomfortable? Practice reframing "no" as "not now, because..."
- **Live exercise:** Identify one thing currently in the sprint that shouldn't be. PM drafts the Slack message or conversation to remove it.
- **Homework:** PM logs every request that comes in during the week. For each, note: accepted/declined/deferred, and the one-sentence rationale.

#### Week 7: Decision Journaling

- **Activity:** Introduce a lightweight decision journal.
  - For each non-trivial decision: What did we decide? What were the alternatives? What assumptions are we making? When will we revisit?
- **Discuss:** Review the PM's request log from Week 6. Look for patterns — are certain types of requests harder to triage? Why?
- **Homework:** PM maintains the decision journal for all tradeoffs this sprint. Timebox: 5 minutes per entry.

#### Week 8: Phase 2 Checkpoint

- **Activity:** "Tradeoff review" — PM walks through 3 decisions from the journal. Coach and a peer evaluate:
  - Was the reasoning clear?
  - Were alternatives genuinely considered?
  - Was the decision communicated crisply to the team?
- **Reflection:** Compare to Phase 1 baseline. Where is the PM making sharper calls? Where do they still hedge?

---

### Phase 3: Integration & Independence (Weeks 9–12) — "Own the Narrative"

**Focus:** Combine framing and tradeoff skills into a cohesive PM practice. Reduce coaching scaffolding.

#### Week 9: End-to-End Dry Run

- **Activity:** PM takes a brand-new initiative from intake to kickoff, using all the tools developed so far:
  1. Problem brief
  2. Problem tree / root-cause analysis
  3. Tradeoff memo for scoping decisions
  4. One-pager or PRD that flows from the above
- **Coach role:** Observer only. Gives feedback after, not during.

#### Week 10: Peer Teaching

- **Activity:** PM leads a 30-minute workshop for the growth team on one of the techniques (problem briefs, tradeoff memos, or decision journals).
  - Teaching forces internalization. It also creates team-wide norms that reinforce the PM's new habits.
- **Homework:** PM writes a self-assessment: *"What's my default mode when I face ambiguity? How has it shifted?"*

#### Week 11: Stress Test — Simulated Crunch

- **Activity:** Coach presents a realistic scenario: a key metric is dropping, leadership wants a response by Friday, and three teams have conflicting proposals.
  - PM must frame the problem, evaluate tradeoffs, and present a recommendation in 45 minutes.
  - Debrief: Where did the PM's thinking get muddy? Where was it crisp?

#### Week 12: Graduation & Ongoing Habits

- **Activity:** Final 1:1.
  - Review the full arc: baseline artifacts from Week 1 vs. current work.
  - Celebrate specific growth moments.
  - Agree on 2–3 ongoing habits the PM will maintain without coaching scaffolding. Recommended defaults:
    1. Problem brief for every new initiative (permanent).
    2. Decision journal reviewed at the end of each sprint (permanent).
    3. Quarterly self-assessment on framing and tradeoff quality.
- **Deliverable:** PM writes a one-page "personal operating manual" section on how they make decisions — useful for onboarding future teammates.

---

## 4. Ongoing Reinforcement Mechanisms

| Mechanism | Cadence | Purpose |
|---|---|---|
| **Problem brief review** | Every new initiative | Ensures framing discipline sticks |
| **Decision journal** | Weekly, reviewed at sprint retro | Creates a searchable record of reasoning |
| **Tradeoff memo** | For any scope change or major pivot | Forces explicit reasoning before action |
| **Peer PM review** | Monthly | Fresh eyes on framing and prioritization |
| **Skip-level check-in** | Quarterly | Validates that the PM's framing aligns with leadership's strategic context |

---

## 5. Success Metrics

After 12 weeks, you should observe:

1. **Problem statements are clean.** PRDs and briefs clearly separate the problem from the solution. Stakeholders stop asking "why are we building this?"
2. **Tradeoffs are documented and communicated.** The team can articulate why something was cut or deferred. Fewer mid-sprint scope changes.
3. **Faster decision-making.** Two-way-door decisions are made quickly and confidently. One-way-door decisions have visible reasoning.
4. **Stakeholder confidence increases.** Partners trust the PM's prioritization because the logic is transparent.
5. **Self-sufficiency.** The PM no longer needs the coaching scaffolding to default to good framing and tradeoff habits.

---

## 6. Common Pitfalls to Watch For

- **"I already know the problem."** The PM may resist the problem brief as unnecessary overhead for things that feel obvious. Coach response: *"If it's obvious, the brief takes 10 minutes. If it's not obvious, you just saved us a sprint."*
- **Analysis paralysis on tradeoffs.** Some PMs overcorrect from "no framework" to "too much framework." Remind them: the goal is crisp decisions, not perfect decisions. Timebox tradeoff analysis.
- **Treating the decision journal as a chore.** If entries become perfunctory, switch to voice memos or Loom recordings — lower friction, same benefit.
- **Reverting under pressure.** When timelines are tight, old habits return. The weekly release cadence is actually an advantage here — each week is a fresh repetition.

---

## 7. Recommended Reading & Resources

- **"The Mom Test" by Rob Fitzpatrick** — For sharper problem discovery through customer conversations.
- **"Thinking in Bets" by Annie Duke** — For separating decision quality from outcome quality (directly relevant to tradeoff confidence).
- **"Good Strategy Bad Strategy" by Richard Rumelt** — For understanding that strategy is fundamentally about choosing what not to do.
- **Shreyas Doshi's writing on "High Agency PM"** — Especially his frameworks on LNO (Leverage, Neutral, Overhead) task categorization.
- **"Working Backwards" by Colin Bryar & Bill Carr** — Amazon's PR/FAQ approach is essentially a problem-framing discipline.

---

*This plan is designed for a growth-team PM with weekly releases. Adjust pacing if the team operates on longer cycles. The key principle holds regardless: every release is a coaching rep.*
