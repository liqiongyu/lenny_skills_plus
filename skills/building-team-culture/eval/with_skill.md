# Team Culture Operating System Pack

**Prepared for:** New Head of Product, Series B Developer Tools Company
**Team:** 12 people (3 PMs, 4 designers, 5 researchers) -- fully remote, US + EU time zones
**Timeline:** 8-week transformation target
**Date:** 2026-03-17

---

## 1) Culture Snapshot (Current State)

### Context
- **Team:** Product (PM, Design, Research)
- **Size/composition:** 12 ICs across three functions -- 3 PMs, 4 designers, 5 researchers. Includes 2 senior ICs who appear disengaged.
- **Working model:** Fully remote, distributed across US and EU time zones (likely 6-9 hour overlap gap between US West Coast and Central Europe).
- **Stage/constraints:** Series B developer tools company. New Head of Product joining -- no existing trust capital with the team. 8-week transformation timeline.

### What's true today (lived culture)

**Strengths to preserve (assumptions -- to be validated during listening tour):**
1. The team has specialized craft depth across three distinct disciplines (PM, design, research) -- this cross-functional composition is a structural advantage.
2. The company has reached Series B, implying the team has shipped meaningful work and has some product-market traction.
3. People care enough to relitigate decisions in Slack -- this signals engagement (misdirected, but present). Apathy would be worse.
4. Retros exist as a format, even if candor is low -- the ritual infrastructure is in place.
5. The team has not yet had a mass exodus despite low trust, suggesting some commitment to the mission or each other.

**Friction / gaps:**
1. **Decisions are relitigated after meetings.** Agreements made in synchronous meetings are re-opened in Slack. This signals that either the wrong people are in the room, decisions are not documented, people do not feel heard during meetings, or there is no clear "disagree and commit" norm.
2. **Low candor in retros.** People avoid giving real feedback in the one forum explicitly designed for it. This indicates psychological safety is low enough that the cost of honesty outweighs the perceived benefit.
3. **Two senior ICs are checked out.** Likely root causes: feeling unheard, disagreeing with direction, lack of growth/challenge, or burnout. Their disengagement signals to the rest of the team that caring is optional or even punished.
4. **No clear decision-making framework.** The relitigating pattern suggests there is no shared understanding of who decides, how dissent is registered, and when a decision is final.
5. **New leader = additional uncertainty.** The team is about to get a new boss they did not choose. Trust is already low; a leader who comes in "swinging" will make it worse.
6. **Time zone friction (US/EU).** Without explicit async norms, synchronous meetings default to US-convenient times, EU members feel excluded from decisions, and Slack becomes a shadow decision channel.
7. **Implicit hierarchy between functions.** In product teams, PMs often default to decision authority. If designers and researchers feel like "service providers" rather than partners, ownership and candor suffer.

### Evidence (anonymized examples)

| # | What happened | What behavior was rewarded/punished? | Impact |
|---|---|---|---|
| 1 | A decision was made in a meeting about feature direction. Within hours, 2-3 people re-opened the discussion in a Slack thread, questioning the rationale and proposing alternatives. | The meeting decision was punished (undermined). The Slack behavior was rewarded (it got attention and sometimes reversed the decision). | People learned that meetings don't matter -- the real decision happens in Slack. Attendance and preparation declined. |
| 2 | In a retro, someone raised a concern about process. The response was defensive or dismissive (or simply silence). The concern was not acted on. | Candor was punished (no change resulted). Silence was rewarded (no risk, no exposure). | People stopped raising real issues. Retros became performative -- "what went well" is safe, "what to improve" stays superficial. |
| 3 | Two senior ICs reduced their engagement -- fewer contributions in meetings, less initiative on new work, minimal cross-functional collaboration. | Disengagement was tolerated (no visible consequences or intervention). Proactive effort was implicitly punished (extra work with no visible impact on outcomes or recognition). | Mid-level team members noticed. The implicit message: high performance is not recognized, and coasting is acceptable. |
| 4 | EU-based team members were absent from a key decision meeting (time zone conflict). The decision was communicated async, but they had no real input. | Being in the US time zone was rewarded (access to decisions). Being in EU was punished (decisions were made without you). | EU members feel like second-class citizens. They learned to either accept decisions or relitigate in Slack -- reinforcing pattern #1. |

### Diagnosis

**Root causes:**
- **Structural:** No decision-making model (DRI, DACI, or equivalent). No documentation norm for decisions. Meetings lack explicit decision authority.
- **Incentive/norm:** Relitigating in Slack works -- it sometimes changes outcomes. There is no cost to reopening decisions and no mechanism for "disagree and commit."
- **Leadership behavior:** Previous leadership likely did not model vulnerability, did not enforce decision finality, and did not address disengagement directly.
- **Time zone inequity:** Sync-heavy culture disadvantages EU members, creating a two-tier participation structure.

**Sacred cows to examine:**
1. "Everyone should weigh in on everything." -- Likely an implicit norm that consensus is required. This slows decisions and rewards the loudest/most persistent voices.
2. "Slack is where real work happens." -- If the team's mental model is that Slack > meetings for influence, then meetings are theater and Slack is the arena.
3. "Senior people have earned the right to coast." -- If the two checked-out senior ICs are protected by tenure or institutional knowledge, the team learns that performance standards are optional.

**Where psychological safety breaks:**
- In retros (people self-censor).
- After decisions (disagreement goes underground into Slack DMs and channels rather than being raised in the room).
- Around the two disengaged seniors (likely no one has named this directly to them or to the team).
- Cross-function (researchers and designers may not feel empowered to push back on PM-driven decisions).

**Where stagnation shows up:**
- The two checked-out senior ICs are a visible symptom.
- Retros that produce no change signal that improvement is performative.
- Decision relitigating creates a loop where the team debates but does not ship or learn from shipped work.

---

## 2) Culture Code (v1)

### Purpose

This culture code exists so that any member of this product team can make a hard call, give honest feedback, or challenge a decision without needing permission from the Head of Product. It prioritizes trust, speed, and craft -- in that order -- because a developer tools team that does not trust each other cannot build tools developers trust.

### Principles

#### Principle 1: Decisions Have Owners and Deadlines

- **Definition:** Every consequential decision has a single owner (DRI) who is responsible for gathering input, making the call, and documenting the rationale. Decisions are final once documented, unless new material evidence emerges.
- **Do:**
  - Name the DRI and decision deadline before discussion begins.
  - Document the decision, rationale, alternatives considered, and who was consulted -- in writing, within 24 hours.
  - Register disagreement explicitly during the decision process ("I disagree because X, and here is what I'd do instead").
  - Commit to execution after the decision is made, even if you disagreed.
- **Don't:**
  - Re-open a decision in Slack or a side channel without new evidence.
  - Make decisions in DMs or hallway conversations that affect the whole team.
  - Treat silence as agreement -- explicitly ask for dissent.
- **Decision rules:**
  - If you disagree with a decision: raise it with the DRI directly within 24 hours with your alternative and evidence. After that, commit.
  - If a decision affects another function (e.g., PM decision that changes design scope): the DRI must consult the affected function's lead before finalizing.
  - If no one is named DRI, the most senior person in the relevant function owns the call by default.
- **Anti-patterns:**
  - "Let's take this offline" that never comes back online.
  - Consensus theater: discussing until everyone is exhausted, then the loudest voice wins.
  - DRI in name only: someone is named the owner but a senior leader overrides without explanation.
- **Signals (healthy):**
  - Decisions are documented in a shared log within 24 hours.
  - Slack threads about past decisions reference the decision doc, not re-argue the merits.
  - People say "I disagree, and here's why" in meetings -- and then commit after the DRI decides.

#### Principle 2: Candor Is a Gift, Not a Threat

- **Definition:** We give each other honest, specific, timely feedback because we believe people on this team want to do great work and can handle the truth. Withholding feedback is not kindness -- it is letting someone fail in slow motion.
- **Do:**
  - Give feedback within 48 hours of the event, privately first for personal feedback, publicly for work/process feedback.
  - Use the format: "I observed [specific behavior], the impact was [concrete effect], and I'd suggest [alternative]."
  - Start retros and critiques with genuine, specific positives -- then move to real issues.
  - As a leader: share your own mistakes and what you learned before asking others to be vulnerable.
- **Don't:**
  - Save up feedback for quarterly reviews.
  - Give feedback as a character judgment ("you're not detail-oriented") instead of a behavior observation.
  - Punish people who give you feedback you don't like (defensiveness, cold shoulder, retaliation).
  - Use "just being honest" as cover for cruelty or status games.
- **Decision rules:**
  - If you see a problem with someone's work: say it to them directly, not to a third party. If it is not resolved in one conversation, escalate to the shared manager.
  - If you receive feedback you disagree with: thank the person, reflect for 24 hours, then respond.
  - If a retro surfaces a recurring issue that has not been addressed: the DRI for that area must respond with an action plan within one week, or explicitly say "we are choosing not to fix this, and here is why."
- **Anti-patterns:**
  - Retros where the only "improvements" are logistical trivia (tool settings, meeting times) and the real issues stay unspoken.
  - "Feedback sandwich" used so reflexively that the real message is lost.
  - Feedback only flows downward (managers to ICs) and never upward or laterally.
- **Signals (healthy):**
  - Retro action items include at least one uncomfortable topic per cycle.
  - Team members give each other unsolicited feedback (not just when prompted).
  - New team members report within their first month that the team is "more honest than expected."

#### Principle 3: Every Function Is a Partner, Not a Service Desk

- **Definition:** PMs, designers, and researchers are equal contributors to product outcomes. No function "owns" the product while others "support." Each discipline brings irreplaceable expertise; the best outcomes come from genuine cross-functional debate, not handoffs.
- **Do:**
  - Include all three functions from the start of problem framing (not after the PM has already written the brief).
  - Assign DRI based on the nature of the decision, not the function's hierarchy (e.g., a design DRI for UX architecture, a research DRI for methodology).
  - Credit contributions by name in demos, write-ups, and reviews.
  - Rotate facilitation of cross-functional meetings.
- **Don't:**
  - Use "the PM decided" as shorthand for a product decision. Product decisions are cross-functional.
  - Treat research or design as a "validation step" that happens after the real decision.
  - Create function-specific Slack channels for decisions that affect the whole product team.
- **Decision rules:**
  - If a PM wants to skip research or design input due to time pressure: they must document the tradeoff explicitly and get sign-off from the Head of Product.
  - If a designer or researcher disagrees with a PM's direction: they have the standing to escalate to the Head of Product without it being seen as "going over someone's head."
- **Anti-patterns:**
  - PMs writing specs, then asking designers to "make it pretty" and researchers to "validate it."
  - "Research said X, but we're going to do Y anyway" without documenting the rationale.
  - Cross-functional meetings where one function presents and the others are silent.
- **Signals (healthy):**
  - Product briefs list contributions from all three functions.
  - Designers and researchers regularly initiate product direction conversations (not just respond to PM requests).
  - In cross-functional meetings, speaking time is roughly balanced across functions.

#### Principle 4: Remote Means Written, Not Slower

- **Definition:** In a distributed team, writing is the primary medium for decisions, context-sharing, and feedback. "Remote-first" does not mean more meetings over Zoom -- it means better writing, explicit async norms, and sync time reserved for what truly requires real-time interaction.
- **Do:**
  - Write a pre-read or brief before any meeting that requires a decision (circulate at least 24 hours in advance).
  - Default to async for updates, status, and FYI communication. Reserve sync for debate, alignment, and relationship-building.
  - Record decisions and context in durable locations (docs, project boards), not Slack threads.
  - Schedule overlap-friendly sync windows (rotate between US-friendly and EU-friendly times).
- **Don't:**
  - Schedule a meeting that could be a doc or a Loom.
  - Make decisions in sync meetings without a written summary that async participants can review and respond to within 24 hours.
  - Expect instant Slack responses. Default response expectation: 4 business hours within overlap, next business day outside overlap.
- **Decision rules:**
  - If a decision must be made in a sync meeting and EU/US members cannot attend: the meeting owner must share the pre-read 24 hours prior, collect async input, and share the decision doc within 24 hours. Async participants have a 24-hour "raise concerns" window before the decision is final.
  - If a Slack thread exceeds 10 messages: move it to a doc with a clear question and decision deadline.
- **Anti-patterns:**
  - "Did you see my Slack message?" as a follow-up to an important decision.
  - Meeting-heavy culture where every question gets a 30-minute Zoom.
  - EU members consistently learning about decisions after they are made.
- **Signals (healthy):**
  - Decision log is updated weekly with clear entries.
  - EU and US team members report equal influence on decisions in pulse surveys.
  - Meeting count decreases while decision throughput increases over the 8-week period.

#### Principle 5: Show the Work, Ship the Learning

- **Definition:** We make progress visible and learn from what we ship. Stagnation is the enemy -- not failure. We would rather ship something imperfect, learn from it, and iterate than debate endlessly and ship nothing. We celebrate learning and visible progress, not just polished launches.
- **Do:**
  - Demo work-in-progress every week -- even if it is rough, incomplete, or a failed experiment.
  - After every major ship or decision: run a brief "what did we learn?" review (15 min, written output).
  - Share customer/user feedback (positive and negative) with the whole team within 48 hours of receiving it.
  - When a project stalls: name it explicitly and decide whether to kill it, scope it down, or recommit.
- **Don't:**
  - Wait until something is "ready" to show it. If you have not shared work-in-progress in two weeks, something is wrong.
  - Treat failed experiments as failures. Treat them as data.
  - Let projects silently die. Every project deserves an explicit "stop" decision with a written rationale.
- **Decision rules:**
  - If a project has had no visible output in two weeks: the DRI must post a status update explaining the blocker, the plan, or the request for help.
  - If an experiment fails: the DRI writes a one-paragraph "what we learned" note. No blame, no apology -- just the learning.
- **Anti-patterns:**
  - "We're still working on it" with no visible artifacts for weeks.
  - Demo sessions that are only polished presentations, not real work-in-progress.
  - Post-mortems that assign blame instead of extracting learning.
- **Signals (healthy):**
  - Weekly demos happen every week, with at least 80% of the team presenting something over a month.
  - The team can point to 2-3 learnings from the past month that changed their approach.
  - Stalled projects are surfaced and resolved within two weeks, not left in limbo.

### How we make decisions here

- **Decision model:** DRI (Directly Responsible Individual). For cross-functional decisions, the DRI consults affected functions but owns the final call.
- **How we disagree and commit:** Disagreement is registered explicitly during the decision window (in the meeting or in the pre-read response). Once the DRI makes the call and documents it, we commit. Reopening requires new material evidence, presented to the DRI directly.
- **Where decisions get documented:** Shared Decision Log (Notion or equivalent). Every entry includes: decision, DRI, date, rationale, alternatives considered, who was consulted, and a "revisit by" date if applicable.

---

## 3) Team Norms

### Communication

- **Async vs sync defaults:**
  - **Async (default):** Status updates, FYIs, feedback on written artifacts, non-urgent questions. Use docs, Loom, or structured Slack posts.
  - **Sync (intentional):** Debates requiring real-time back-and-forth, relationship-building, alignment on ambiguous problems, retrospectives.
- **Response time expectations:**
  - Slack (non-urgent): 4 business hours within time zone overlap; next business day outside overlap.
  - Slack (urgent, marked with "URGENT:" prefix): 1 hour during business hours. Use sparingly -- more than 2 per week means the system is broken.
  - Doc reviews / pre-reads: 24 hours.
  - Decision feedback windows: 24 hours from doc being shared.
- **Documentation norms:**
  - Decisions go in the Decision Log (not Slack).
  - Meeting notes are posted within 24 hours, including decisions made, action items with owners, and open questions.
  - Project status is updated weekly in the shared project tracker.
- **Escalation norms:**
  - First: raise directly with the person or DRI.
  - If unresolved after one conversation: bring to Head of Product with a written summary of the disagreement and both perspectives.
  - Head of Product resolves within 48 hours or explicitly extends the timeline.

### Meetings

- **When to schedule a meeting:**
  - YES: Unresolved disagreements, alignment on ambiguous strategy, retros, 1:1s, cross-functional problem-framing.
  - NO: Status updates (use async), decisions where the DRI has enough input (write the decision doc), anything that could be a 3-minute Loom.
- **Standard agenda template (required for all meetings with 3+ people):**
  1. Purpose of this meeting (1 sentence).
  2. Pre-read link (circulated 24 hours prior).
  3. Discussion items with time boxes.
  4. Decisions to be made (list them explicitly).
  5. Last 5 minutes: capture decisions, action items, owners.
- **Facilitation rules:**
  - Rotate facilitator monthly across functions.
  - Leader (Head of Product) speaks last on opinion questions.
  - Actively invite input from quiet participants: "I'd like to hear from the research/design perspective on this."
  - Time-box discussions. If a topic exceeds its box by 50%, table it with a DRI and deadline for async resolution.
- **Decision capture:**
  - Every meeting that involves a decision must produce a written decision within 24 hours, posted in the Decision Log.
  - Action items include: what, who (single owner), and by when.

### Feedback & Conflict

- **How to challenge ideas:**
  - Challenge the work, not the person. "I think this approach has a gap in X" -- not "You didn't think about X."
  - Use the "yes, and" or "what if" frame for generative critique: "What if we also considered..."
  - In structured critiques (design reviews, research readouts): the presenter sets the question they want feedback on. Feedback focuses on that question first.
- **How to give feedback (format):**
  - **Observation:** "In [specific situation], I noticed [specific behavior]."
  - **Impact:** "The impact was [concrete effect on the work, the team, or me]."
  - **Suggestion:** "Going forward, I'd suggest [alternative behavior]."
  - For positive feedback: be equally specific. "Great job" is not feedback. "Your synthesis of the research findings in the brief made the decision much clearer for the team" is.
- **Repair after conflict:**
  - After a tense exchange: the person who raised the issue (or the manager, if needed) checks in within 48 hours. "I want to make sure we're good after that conversation. How are you feeling about it?"
  - If trust was damaged: name it explicitly and agree on a specific behavior change. "I felt dismissed when X happened. Going forward, can we agree to Y?"
  - Head of Product models repair by publicly acknowledging when they handle something poorly: "I cut you off in that meeting, and that was wrong. I want to hear your full perspective."

---

## 4) Rituals & Cadence Map

| Ritual | Purpose (principle) | Cadence | Owner | Agenda | Outputs |
|---|---|---|---|---|---|
| **Weekly WIP Demo** | Show the Work, Ship the Learning (P5) + Every Function Is a Partner (P3) | Weekly, 45 min (alternate US-friendly / EU-friendly times) | Rotating facilitator (one per function per month) | 3-4 demos (10 min each) of work-in-progress from across functions. No slides required -- show the actual work. Last 5 min: "What did we learn this week?" | Recorded for async viewing. 1-paragraph summary posted in team channel. |
| **Blameless Retro** | Candor Is a Gift (P2) + Show the Work (P5) | Biweekly, 50 min | Head of Product (first 4 weeks), then rotating | Silent brainstorm (5 min) -> Group + vote (10 min) -> Discuss top 3 (25 min) -> Action items with DRIs and deadlines (10 min). Rule: no names, no blame -- focus on systems, norms, and processes. | Written retro notes with action items. Action items reviewed at start of next retro. |
| **Decision Review** | Decisions Have Owners and Deadlines (P1) | Monthly, 30 min | Head of Product | Review the Decision Log from past month: Were decisions made on time? Were any relitigated? Were async participants included? Identify 1-2 process improvements. | Updated decision norms if needed. Monthly health note posted. |
| **Cross-Function Problem Framing** | Every Function Is a Partner (P3) | Per project kickoff (as needed, ~2x/month) | PM for the project (but all three functions present) | Problem statement -> Each function shares their lens (PM: business/user, Design: experience/feasibility, Research: evidence/unknowns) -> Jointly define success criteria and open questions. | Written problem brief with contributions from all functions. |
| **1:1s (Head of Product with each direct report)** | Candor Is a Gift (P2) | Weekly, 30 min | Each direct report owns the agenda | Report's agenda first (blockers, feedback, growth). Head of Product asks: "What's the hardest thing right now?" and "What feedback do you have for me?" | Private notes. Head of Product tracks themes across 1:1s. |
| **Monthly Culture Pulse** | Measurement (P2 + P1 + P5) | Monthly, async | Head of Product | 6-question anonymous pulse survey (see Measurement Plan). Results shared transparently with the team within 1 week. | Pulse results + 1-2 actions based on findings. |
| **Quarterly Culture Retro** | All principles | Quarterly, 90 min | Head of Product | Review culture code: What's working? What's not? What should we change? Review pulse trends. Decide on 1-2 culture code updates. | Updated Culture Code (v2, v3, etc.) with changelog. |

---

## 5) Rollout + Reinforcement Plan (30/60/90)

### 0-30 Days: Listen, Build Trust, Draft (Weeks 1-4)

**Week 1-2: Listening tour (no changes yet)**
- **Listening plan:** Conduct 30-45 minute 1:1s with all 12 team members. Use the listening prompts:
  1. "What's the best part of working on this team?"
  2. "When have you felt proud of our work? What enabled it?"
  3. "When do we move too slowly? Why?"
  4. "What's hard to say out loud here?"
  5. "What behaviors get rewarded (explicitly or implicitly)?"
  6. "If you led this team, what 1-2 changes would you make first?"
  7. "What should we absolutely not change?"
- **Special attention:** Schedule dedicated conversations with the two disengaged senior ICs. Listen for root causes: lack of growth, disagreement with direction, burnout, feeling unheard. Do not try to "fix" them yet -- build understanding.
- **EU-specific:** Schedule at least half of EU 1:1s at EU-friendly times. Ask specifically about time zone inclusion.
- **Output:** Synthesized themes document (anonymized). Share back with the team: "Here's what I heard."

**Week 3-4: Draft and socialize**
- **Draft artifacts:** Culture snapshot (validated against listening tour data), Culture code v1, proposed norms, proposed rituals.
- **Socialization:** Share the draft Culture Code v1 with the team asynchronously. Give 1 week for written feedback. Frame it as: "This is a draft based on what I heard from you. What's wrong? What's missing? What resonates?"
- **First ritual pilot:** Start weekly WIP Demos in week 3. This is the lowest-risk, highest-signal ritual -- it makes progress visible without requiring trust.
- **DRI:** Head of Product owns all artifacts and socialization in this phase.

**Key milestones (Day 30):**
- All 12 listening tour conversations completed.
- Themes synthesized and shared with team.
- Culture Code v1 draft shared for feedback.
- Weekly WIP Demo running for 2 weeks.

### 31-60 Days: Pilot Norms, Build Muscle (Weeks 5-8)

**Norms rollout (prioritized):**
1. **Decision norms (Week 5):** Roll out the DRI model and Decision Log. Start with a 15-minute team walkthrough of "how we make decisions now." Every decision from this point forward gets a DRI and a log entry.
2. **Communication norms (Week 5):** Publish async/sync defaults and response time expectations. Post in team channel and pin.
3. **Feedback norms (Week 6):** Introduce the Observation-Impact-Suggestion format. Head of Product models it first (give public positive feedback using the format, and share a piece of self-critical feedback).
4. **Meeting norms (Week 6):** Require agenda + pre-read for all meetings 3+ people. Head of Product enforces by declining meetings without agendas.

**Ritual rollout:**
- **Week 5:** Start Blameless Retro (biweekly). Head of Product facilitates the first two.
- **Week 6:** Start Cross-Function Problem Framing for the next project kickoff.
- **Week 7:** Conduct first Monthly Culture Pulse survey.

**Coaching approach:**
- **Head of Product 1:1s:** Weekly with all direct reports. Ask explicitly: "How are the new norms landing? What's not working?"
- **Peer coaching pairs:** Pair one person from each function (PM-Designer, Designer-Researcher, Researcher-PM) for a monthly 30-minute "craft exchange." Purpose: build cross-functional empathy and trust. Voluntary in this phase.
- **Senior IC re-engagement:** Based on listening tour findings, co-create a growth/challenge plan with each disengaged senior IC. This might include: a high-impact project they own end-to-end, a mentoring/coaching role, or explicit feedback about what the team needs from them.

**Key milestones (Day 60):**
- DRI model and Decision Log in active use for 4+ weeks.
- All norms published and socialized.
- Blameless Retro running biweekly for 4 weeks.
- First pulse survey completed and results shared.
- Each senior IC has a co-created engagement plan.

### 61-90 Days: Embed, Measure, Iterate (Weeks 9-12)

**Hiring/onboarding hooks:**
- **Onboarding:** Add "Culture Code walkthrough" to the first-week onboarding for any new team member. Include: read the Culture Code, attend a WIP Demo, meet 3 people from different functions in 1:1s.
- **Hiring signals:** For any open roles, define interview questions aligned to principles. Examples:
  - P1 (Decisions): "Tell me about a time you disagreed with a decision. What did you do after the decision was made?"
  - P2 (Candor): "Describe a time you gave difficult feedback to a peer. What happened?"
  - P3 (Cross-function): "How do you work with [other function]? Give me an example of a disagreement that led to a better outcome."
  - Replace any "culture fit" language in job descriptions with observable behavioral expectations.

**Recognition/reward hooks:**
- In weekly WIP Demos, Head of Product highlights behaviors that exemplify principles (not just good work, but good process): "I want to call out how [person] documented their decision rationale this week -- that's exactly what Principle 1 looks like."
- In 1:1s, connect feedback to principles: "The way you gave that design critique was a great example of Candor is a Gift."

**Iteration cadence:**
- **Week 10:** Review first two pulse survey results. Identify the principle/norm with the lowest score. Develop one specific intervention.
- **Week 12:** Conduct the first Quarterly Culture Retro. Update the Culture Code to v2 based on team input. Publish a brief "what changed and why" changelog.

**Key milestones (Day 90):**
- Culture Code v2 published (team-edited, not just leader-authored).
- Onboarding and hiring hooks documented and in use.
- Pulse survey trend data for 3 months available.
- At least one norm or ritual has been explicitly modified based on team feedback (proving the system iterates).

---

## 6) Measurement Plan

### Leading Indicators (6)

| Indicator | Definition | How measured | 8-week target |
|---|---|---|---|
| **Decision cycle time** | Time from "decision needed" to "documented in Decision Log" | Track in Decision Log (date opened -> date closed) | Median < 3 business days (down from current undefined/relitigated state) |
| **Decision relitigating rate** | Number of documented decisions re-opened in Slack without new evidence per month | Manual count by Head of Product (review Slack weekly) | < 2 per month (down from current baseline -- measure in week 1) |
| **Retro action completion rate** | Percentage of retro action items completed by the next retro | Track in retro notes | > 70% by week 8 |
| **WIP Demo participation** | Percentage of team members who present at least once per month | Track in demo log | > 80% of team presenting monthly by week 8 |
| **Cross-function involvement** | Percentage of project briefs with contributions from all three functions | Track in project tracker | 100% of new projects from week 6 onward |
| **Pulse survey response rate** | Percentage of team completing the monthly pulse | Survey tool | > 90% response rate |

### Pulse Questions (6 -- administered monthly, anonymous, 1-5 scale)

1. **"I feel safe raising concerns or disagreeing on this team."** (Maps to: Candor Is a Gift, P2)
2. **"Decisions are made quickly and clearly, and I understand who owns them."** (Maps to: Decisions Have Owners and Deadlines, P1)
3. **"My function (PM/Design/Research) is treated as an equal partner in product decisions."** (Maps to: Every Function Is a Partner, P3)
4. **"I can participate meaningfully in decisions regardless of my time zone."** (Maps to: Remote Means Written, Not Slower, P4)
5. **"We make visible progress every week, and I can point to what we learned recently."** (Maps to: Show the Work, Ship the Learning, P5)
6. **"I receive honest, useful feedback from my teammates regularly."** (Maps to: Candor Is a Gift, P2)

**Measurement cadence:**
- **Monthly:** Pulse survey administered on the first Monday of each month. Results shared (transparently, with scores and anonymized comments) within 1 week.
- **Monthly:** Head of Product reviews leading indicators and posts a brief "culture health" note to the team.
- **Quarterly:** Quarterly Culture Retro reviews pulse trends, leading indicators, and qualitative examples. Team decides what to update.

**How findings lead to changes:**
- Any pulse question scoring below 3.0 average triggers a focused discussion in the next retro with a DRI and action plan.
- Any pulse question improving by 0.5+ points gets celebrated in the WIP Demo ("here's what we changed and it's working").
- The Culture Code is explicitly versioned. Changes are documented in a changelog so the team can see the system evolving based on their input.

---

## 7) Risks / Open Questions / Next Steps

### Risks

1. **"New leader syndrome."** The team may interpret this culture work as the new Head of Product imposing their preferences. **Mitigation:** Lead with the listening tour. Frame the Culture Code as "articulating what I heard from you" rather than "here's what I want." Involve the team in editing v1 before it becomes official.

2. **Senior IC disengagement may have deeper roots.** If the two checked-out ICs are burned out, in conflict with leadership, or fundamentally misaligned on company direction, a culture operating system will not re-engage them. **Mitigation:** Prioritize honest 1:1s with them in week 1-2. Be prepared for the possibility that the right outcome is a mutual acknowledgment that the role is no longer a fit.

3. **Time zone equity is hard to sustain.** Rotating meeting times is logistically awkward and people revert to defaults. **Mitigation:** Make time zone equity a tracked leading indicator (pulse question #4). Assign a DRI (ideally an EU-based team member) to flag when norms are slipping.

4. **Culture work feels like overhead during a Series B growth phase.** The business needs the team shipping product, not spending weeks on culture docs. **Mitigation:** Keep the artifacts lightweight. The entire Culture Code is a single page. Rituals are designed to replace existing inefficient meetings, not add new ones. Decision norms should accelerate shipping speed, not slow it down.

5. **Psychological safety takes longer than 8 weeks to build.** Trust is rebuilt in small moments over time, not through a document. **Mitigation:** Set expectations with your manager/leadership that 8 weeks is enough for structural changes (norms, rituals, decision model) and early indicators of improvement, but genuine trust transformation takes 2-3 quarters.

6. **Retros may stay performative despite new norms.** If the team has learned that candor is punished, it will take repeated demonstrations of safety before they believe it has changed. **Mitigation:** Head of Product must model vulnerability aggressively in the first month (share mistakes, ask for feedback publicly, act visibly on retro action items). Consider anonymous retro input for the first 2-3 cycles.

### Open Questions

1. **What is the existing meeting cadence?** This plan assumes there is no structured cadence. If there is one, the rituals above should replace or integrate with existing meetings, not add to the load.
2. **What tools does the team use?** The Decision Log and pulse survey need a home (Notion, Confluence, Google Docs, etc.). The specific tool matters less than the norm of using it.
3. **What is the Head of Product's relationship with their manager (VP/CEO)?** If leadership above does not support culture investment, the 8-week timeline is at risk. Clarify: does your manager support you spending 20-30% of your first month on listening and culture?
4. **What caused the low-trust environment?** Was there a specific incident, a previous leader's style, or a structural issue (e.g., layoffs, reorg)? The listening tour should surface this, but it shapes the approach.
5. **Are the two disengaged senior ICs in the same function or different functions?** Their disengagement may have function-specific root causes (e.g., researchers feeling their work is ignored) or personal causes.
6. **Is there appetite for an in-person offsite?** Even for a fully remote team, a single 2-day offsite in the first 60 days could accelerate trust-building significantly. Budget and logistics may constrain this.

### Next Steps (smallest experiments first)

1. **This week:** Schedule all 12 listening tour 1:1s (spread across weeks 1-2). Prepare the listening prompts. No other changes yet.
2. **Week 2:** Synthesize listening tour themes. Share anonymized summary with the team. Validate or update the culture snapshot above.
3. **Week 3:** Start the Weekly WIP Demo. Keep it low-pressure: "Show something you worked on this week, even if it's rough."
4. **Week 3-4:** Draft Culture Code v1 (use this document as the starting point, refined with listening tour data). Share with the team for async feedback.
5. **Week 5:** Roll out the DRI model and Decision Log. This is the single highest-leverage change -- it directly addresses the decision relitigating problem.
6. **Week 5:** Start the Blameless Retro (biweekly). Head of Product facilitates and models vulnerability.
7. **Week 7:** Run the first pulse survey. Share results transparently.
8. **Week 8:** Review progress against all leading indicators. Adjust the plan for weeks 9-12.

---

*This is a living document. Version 1 should be treated as a draft to be refined with team input. The culture code is not real until the team recognizes themselves in it and has had a hand in shaping it.*
