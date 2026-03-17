# Hiring Manager Interview: Senior Product Manager, Provider Scheduling

**Company context:** Series B healthcare SaaS, ~80 employees
**Product scope:** Provider-facing scheduling product
**Interview duration:** 45 minutes
**Candidate background:** Consumer health app experience; no prior B2B experience

---

## Interview Objectives

Evaluate the candidate across four dimensions:

| Dimension | Weight | Why it matters for this role |
|---|---|---|
| Product Sense | 30% | Must design workflows that fit into complex provider operations without oversimplifying |
| Execution Rigor | 25% | Series B pace demands disciplined prioritization and reliable delivery with a small team |
| Healthcare Domain Curiosity | 20% | No B2B healthcare background means learning speed and genuine interest are proxies for future ramp |
| Cross-Functional Collaboration | 25% | Must partner daily with engineering (small team, high leverage) and clinical ops (domain gatekeepers) |

---

## Question Map (45-minute allocation)

### Opening & Context Setting (3 minutes)

**Goal:** Settle the candidate, frame the conversation, set expectations.

Script:

> "Thanks for joining. I lead [team/org] here. Today I want to spend about 45 minutes going deep on a few topics rather than racing through many. I'll share context where it helps but I'm mostly here to learn how you think. There are no trick questions. Ready?"

Brief the candidate on the product: "We build scheduling software used by medical practices -- think multi-provider clinics, specialty groups, health systems. The core user is the front-desk scheduler and the providers themselves."

---

### Section 1: Product Sense (12 minutes)

#### Q1 -- Live Design Exercise (8 min)

> "Imagine you just joined us and I tell you: our provider-facing scheduling product has a 35% drop-off rate during the appointment-type selection step. Walk me through how you would diagnose and address this."

**What to listen for:**

- Asks clarifying questions before jumping to solutions (user segment, device, data available)
- Distinguishes between UX friction, information architecture, and underlying data/config issues
- Considers the provider's mental model vs. a consumer user's mental model
- Proposes a sequenced approach (instrument, hypothesize, test) rather than a single silver-bullet feature
- Acknowledges tradeoffs (e.g., simplifying selection vs. supporting clinical complexity)

**Behavioral probe (follow-up):**

> "Tell me about a time you inherited a product metric that was underperforming and your diagnosis surprised you -- the root cause was different from what the team initially assumed."

**What to listen for:**

- Concrete example with specifics (numbers, timeline, who was involved)
- Demonstrates intellectual honesty about initial wrong assumptions
- Shows structured investigation, not just intuition

#### Q2 -- Consumer-to-B2B Translation (4 min)

> "Your background is in consumer health. What do you think is the single biggest difference in how you'd need to think about product decisions when your user is a medical office coordinator juggling 12 providers' schedules vs. an individual consumer managing their own health?"

**What to listen for:**

- Recognizes multi-stakeholder complexity (buyer != user != beneficiary)
- Mentions workflow integration, not just UI polish
- Awareness that switching costs and change management matter more in B2B
- Bonus: mentions compliance, interoperability, or EHR integration unprompted

---

### Section 2: Execution Rigor (10 minutes)

#### Q3 -- Prioritization Under Constraints (5 min)

> "You have a 5-person engineering team, a quarterly planning cycle, and three competing requests: (1) a top-3 customer threatening churn wants a calendar sync with their proprietary EHR, (2) your data shows a self-serve onboarding flow could increase activation by 20%, (3) clinical ops is asking for a provider availability rules engine that would reduce scheduling errors by half. How do you decide what to build next quarter?"

**What to listen for:**

- Uses a framework but doesn't hide behind it (RICE, ICE, or similar -- adapted, not recited)
- Quantifies or attempts to quantify impact (revenue at risk, activation funnel math, error-cost estimate)
- Considers second-order effects (e.g., churn customer's contract size vs. long-term platform leverage)
- Acknowledges what they would need to learn before deciding (e.g., "I'd want to understand the EHR integration scope")
- Ultimately commits to a recommendation rather than hedging indefinitely

**Behavioral probe (follow-up):**

> "Tell me about a time you had to say no to a loud stakeholder or a large customer request. What happened?"

**What to listen for:**

- Shows the "no" was principled, not arbitrary
- Describes how they communicated the decision and what alternative they offered
- Outcome: did the relationship survive? Did they learn anything?

#### Q4 -- Shipping Discipline (5 min)

> "Describe the most complex feature you shipped end-to-end. Walk me through how you scoped it, what you cut, and how you knew it was ready to launch."

**What to listen for:**

- Clear articulation of scope-setting process (MLP/MVP thinking)
- Evidence of written specs, success metrics defined upfront, launch criteria
- Willingness to cut scope to protect timelines -- with examples of what was cut and why
- Post-launch follow-through (monitoring, iteration, retro)

---

### Section 3: Healthcare Domain Curiosity (8 minutes)

#### Q5 -- Domain Learning (4 min)

> "You're coming from consumer health. What have you already learned or started exploring about the provider-side scheduling problem? What surprised you or what questions do you still have?"

**What to listen for:**

- Evidence of genuine pre-interview research (mentions specific pain points like no-shows, overbooking, template management, multi-location complexity)
- Asks intelligent questions back (signals curiosity, not just prep)
- Bonus: references conversations with clinicians, office managers, or relevant reading
- Red flag: superficial or purely theoretical answers with no evidence of self-directed exploration

**Behavioral probe (follow-up):**

> "Tell me about a time you had to become competent in a domain you knew nothing about. How did you ramp, and how long did it take before you felt you could challenge domain experts constructively?"

**What to listen for:**

- Describes a deliberate learning system (not just "I asked people")
- Mentions primary sources: observing users, reading documentation, shadowing
- Realistic timeline -- not "two weeks" for a genuinely complex domain
- Evidence they eventually earned credibility with domain experts

#### Q6 -- Regulatory Awareness (4 min)

> "In healthcare SaaS, regulatory and compliance considerations can shape product decisions. Without needing to be an expert, what compliance or regulatory factors do you think might affect a provider scheduling product, and how would you make sure those factors are represented in your product process?"

**What to listen for:**

- Mentions HIPAA as a baseline (PHI in scheduling data, access controls)
- May reference state-level regulations, payer requirements, or accessibility standards
- Key insight: articulates that they'd build relationships with compliance/legal stakeholders early and embed checkpoints in the product process
- Red flag: dismisses compliance as "someone else's problem"

---

### Section 4: Cross-Functional Collaboration (9 minutes)

#### Q7 -- Working with Engineering (5 min)

> "You'll work with a small engineering team -- 5 engineers, including a tech lead who's been here since the seed round and knows the codebase inside out. How do you think about the PM-engineering relationship, especially when you're the new person and they have deep context you lack?"

**What to listen for:**

- Respect for engineering's existing context and institutional knowledge
- Describes earning trust through competence, not title
- Concrete tactics: joint discovery, shared problem framing, involving engineers early in customer conversations
- Acknowledges tension points honestly (scope disagreements, technical debt vs. features) and how they navigate them

**Behavioral probe (follow-up):**

> "Give me an example of a significant disagreement you had with an engineering lead about product direction. How did you resolve it?"

**What to listen for:**

- Disagreement was substantive, not trivial
- Resolution involved data, user evidence, or principled tradeoff discussion -- not escalation or pulling rank
- Relationship was maintained or strengthened afterward

#### Q8 -- Partnering with Clinical Ops (4 min)

> "Clinical ops is a team of people who come from healthcare -- former practice managers, nurses, clinical coordinators. They are the voice of the customer internally and also run implementation. How would you structure your working relationship with them in your first 90 days?"

**What to listen for:**

- Plans to learn from them before trying to influence them
- Proposes regular touchpoints, shared artifacts (e.g., customer feedback loops, co-owned metrics)
- Recognizes clinical ops as partners in discovery, not just a service team
- Bonus: asks what the current relationship between PM and clinical ops looks like today

---

### Closing (3 minutes)

> "That covers what I wanted to explore. What questions do you have for me about the role, the team, or the company?"

**Evaluate their questions for:**

- Strategic curiosity (market, competitive dynamics, company trajectory)
- Role clarity (team structure, decision-making authority, success metrics)
- Self-awareness (what support they'd need, what concerns them about the transition)

---

## Scorecard

Rate each dimension on a 1-4 scale. Avoid 2.5 -- force a lean.

### Product Sense (30%)

| Rating | Anchor |
|---|---|
| 4 -- Strong Hire | Structured the diagnosis clearly; unpacked provider vs. consumer mental models without prompting; proposed a phased, evidence-based approach; articulated sharp tradeoffs. Consumer-to-B2B answer showed genuine depth, not rehearsed talking points. |
| 3 -- Hire | Solid diagnostic instinct; asked good clarifying questions; recognized key B2B differences. May have needed one nudge to go deeper on tradeoffs or provider-specific considerations. |
| 2 -- No Hire | Jumped to solutions without diagnosis; treated the scheduling problem like a consumer funnel optimization; B2B translation was surface-level ("B2B has longer sales cycles"). Lacked nuance on multi-stakeholder dynamics. |
| 1 -- Strong No Hire | Could not structure the problem; proposed generic best practices; no awareness of how provider workflows differ from consumer experiences. |

### Execution Rigor (25%)

| Rating | Anchor |
|---|---|
| 4 -- Strong Hire | Prioritization was quantified and principled; committed to a recommendation with clear rationale; shipping example showed disciplined scoping, defined launch criteria, and post-launch follow-through. "No" story was specific and showed stakeholder management skill. |
| 3 -- Hire | Used a reasonable framework; made a defensible prioritization call; shipping example showed good process. May have been slightly vague on metrics or post-launch measurement. |
| 2 -- No Hire | Framework-dependent without adapting to context; could not commit to a prioritization call; shipping example lacked evidence of scope discipline or success metrics. Avoided the "no" question or gave a weak example. |
| 1 -- Strong No Hire | No discernible prioritization logic; could not describe shipping a feature end-to-end with any rigor; showed no evidence of saying no to anything. |

### Healthcare Domain Curiosity (20%)

| Rating | Anchor |
|---|---|
| 4 -- Strong Hire | Did meaningful pre-interview research; referenced specific provider scheduling pain points; asked sharp questions back; domain ramp story showed a deliberate learning system and realistic timeline; regulatory answer went beyond HIPAA basics to process integration. |
| 3 -- Hire | Showed genuine interest and some preparation; domain ramp story was solid; regulatory awareness was at least HIPAA-level with a reasonable plan for embedding compliance in process. |
| 2 -- No Hire | Preparation was superficial; domain ramp story was generic ("I just talk to people"); regulatory awareness was absent or hand-wavy ("legal handles that"). |
| 1 -- Strong No Hire | No evidence of curiosity or preparation; could not articulate any healthcare-specific considerations; showed no interest in learning the domain. |

### Cross-Functional Collaboration (25%)

| Rating | Anchor |
|---|---|
| 4 -- Strong Hire | Described earning engineering trust through specific, credible tactics; disagreement example showed maturity and a data-driven resolution; clinical ops plan was concrete, relationship-first, and showed understanding of their unique value. |
| 3 -- Hire | Good instincts on collaboration; engineering disagreement was resolved reasonably; clinical ops plan was sensible if somewhat generic. |
| 2 -- No Hire | PM-as-CEO mentality; engineering story suggested escalation or avoidance rather than resolution; clinical ops plan was transactional ("I'll send them a weekly update"). |
| 1 -- Strong No Hire | Dismissive of engineering context; no credible collaboration examples; treated clinical ops as subordinate or irrelevant. |

### Overall Recommendation

| Rating | Definition |
|---|---|
| Strong Hire | Scored 3+ on all dimensions with at least two 4s. Would raise the bar on the team. |
| Hire | Scored 3+ on at least three dimensions with no 1s. Gaps are coachable within 90 days. |
| No Hire | Scored 2 on two or more dimensions, or scored 1 on any dimension. |
| Strong No Hire | Scored 1 on two or more dimensions, or showed a fundamental misalignment with role requirements. |

---

## Debrief Summary Template

Complete within 24 hours of the interview. Share with the hiring panel before the debrief meeting.

---

**Candidate name:** ____________________
**Interview date:** ____________________
**Interviewer:** ____________________

### Scores

| Dimension | Score (1-4) | Confidence (High/Med/Low) |
|---|---|---|
| Product Sense | | |
| Execution Rigor | | |
| Healthcare Domain Curiosity | | |
| Cross-Functional Collaboration | | |

### Overall Recommendation

- [ ] Strong Hire
- [ ] Hire
- [ ] No Hire
- [ ] Strong No Hire

### Key Evidence (one to two sentences per dimension)

**Product Sense:**


**Execution Rigor:**


**Healthcare Domain Curiosity:**


**Cross-Functional Collaboration:**


### Top Strength

_What is this candidate's single biggest asset for this role?_


### Top Risk

_What is the biggest gap or concern, and is it coachable within 90 days?_


### B2B Transition Readiness

_Specific assessment: Based on this interview, how prepared is this candidate to operate in a B2B healthcare context despite their consumer background? What support would they need?_


### Open Questions for Panel

_What should other interviewers probe further?_


### Verbatim Moments

_One to two direct quotes that capture the candidate's strongest and weakest moments. These anchor the debrief discussion in evidence rather than impression._

**Strongest moment:**

>

**Weakest moment:**

>

---

*End of interview plan.*
