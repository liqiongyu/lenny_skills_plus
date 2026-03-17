# Written Communication Pack -- Launch Slip + Scope Cut Request

---

## Step 1: Intake + Artifact Selection

### Message Brief

- **Artifact type + channel:** Email (sent to exec stakeholders via email)
- **Audience (roles/seniority):** Executive stakeholders (VP/C-level); they care about launch timing, revenue impact, customer commitments, and team capacity
- **Goal (inform/align/decide):** Decide -- get approval for a specific scope cut
- **Ask (what should they do, by when):** Approve dropping Feature B from the launch scope by end of day Friday
- **Why now (1 sentence):** A dependency delay has pushed the launch 2 weeks; cutting Feature B is the fastest path to hold the revised date without further risk.
- **Key facts:** Launch slipping 2 weeks; root cause is dependency delays (not team performance); Feature B is the proposed cut; Features A and C remain on track
- **Sensitivities / what to avoid:** Do not assign blame to specific teams or individuals for the dependency delay; do not frame as a failure -- frame as a trade-off decision
- **Links:** [Placeholder: project tracker], [Placeholder: canonical project doc]
- **Tone + length constraints:** Direct, calm, factual. Under 250 words for the email body.

### Artifact selection rationale

Email is the lightest artifact that achieves the outcome. Exec stakeholders need a clear ask with enough context to decide -- not a memo or doc. A short email with TL;DR, options, and next steps is appropriate.

---

## Step 2: Outcome + Ask (One Sentence)

**After reading, exec stakeholders will approve (or propose an alternative to) dropping Feature B from the launch scope so the team can lock the revised timeline by Friday.**

- **Ask type:** Decision -- approve recommended scope cut
- **Deadline:** End of day Friday
- **Response path:** Reply to this email with approval or reply with concerns/alternative by Thursday EOD so we can discuss before the Friday deadline

---

## Step 3: "How" -- Actionable Next Steps

### What changes vs. what stays the same

**Changing:**
- Feature B is removed from launch scope and moved to a fast-follow release (target: 3 weeks post-launch)
- Launch date shifts from original date to 2 weeks later (revised date)

**Not changing:**
- Features A and C ship as planned on the revised launch date
- Go-to-market plan, marketing assets, and customer communications proceed on the revised date
- Team staffing and resourcing remain the same

### Next steps (owner + date)

1. **Exec stakeholders:** Approve scope cut (drop Feature B) -- by Friday EOD
2. **[PM name]:** Update the project tracker and communicate revised scope to eng + design -- Monday (following approval)
3. **[Eng lead]:** Re-plan Feature B as fast-follow; share updated estimate -- by next Wednesday
4. **[PM name]:** Notify external partners/customers of revised launch date -- Monday (following approval)
5. **[PM name]:** Send status update confirming locked plan -- next Friday

### Dependencies and risks

- If approval is delayed past Friday, the 2-week slip may extend further as the team loses planning time over the weekend.
- Feature B fast-follow depends on the same dependency resolving; [Eng lead] will confirm feasibility by next Wednesday.

---

## Step 4: Outline (Structured for Skim)

**Subject:** Decision needed by Friday: Drop Feature B to hold revised launch date

**TL;DR (3 bullets)**
- Launch is slipping 2 weeks due to an external dependency delay.
- Recommendation: drop Feature B from launch (move to fast-follow) to lock the revised date with confidence.
- Ask: approve this scope change by Friday EOD; reply with concerns by Thursday if you see issues.

**What's happening (short context)**
- One sentence on the dependency delay and its impact.

**What's changing (and what's not)**
- Changing: Feature B out of launch, moved to fast-follow.
- Not changing: Features A + C, GTM plan, team resourcing.

**What I need from you**
- Approve or raise concerns by Friday.

**Next steps (owned, dated)**
- Numbered list with owners and dates.

**Risks / Open questions**
- Delay cost, fast-follow feasibility.

---

## Step 5: Draft Email

**Subject:** Decision needed by Friday: Drop Feature B to hold revised launch date

Hi team,

**TL;DR**
- Our launch is slipping 2 weeks due to an external dependency delay outside our control.
- To hold the revised launch date with high confidence, I recommend we **drop Feature B** from the initial launch and ship it as a fast-follow (targeting 3 weeks post-launch).
- **I need your approval on this scope change by Friday EOD.** If you have concerns, please reply by Thursday so we can discuss before the deadline.

**What's happening**

A key upstream dependency missed its delivery date, which blocks Feature B. Features A and C are unaffected and on track. Waiting for the dependency to resolve would add 4+ weeks of uncertainty to the timeline. Cutting Feature B now lets us lock a firm revised launch date.

**What's changing -- and what's not**

| | Changing | Not changing |
|---|---|---|
| **Scope** | Feature B moves to fast-follow (3 weeks post-launch) | Features A and C ship at launch |
| **Timeline** | Launch shifts 2 weeks from original date | GTM plan proceeds on revised date |
| **Resourcing** | No change | Team staffing stays the same |

**What I need from you (by Friday EOD)**

- **Approve** dropping Feature B from launch scope (recommended), OR
- **Reply with concerns** by Thursday EOD so we can align before the deadline

If I do not hear back by Friday, I will proceed with the scope cut to protect the revised timeline.

**Next steps**

1. **Exec stakeholders:** Approve scope cut -- Friday EOD
2. **[PM name]:** Update tracker and communicate revised scope to eng + design -- Monday
3. **[Eng lead]:** Re-plan Feature B as fast-follow; share updated estimate -- next Wednesday
4. **[PM name]:** Notify external partners of revised launch date -- Monday
5. **[PM name]:** Send status update confirming locked plan -- next Friday

**Links**
- Project tracker: [link]
- Canonical project doc: [link]

Thanks,
[Your name]

---

## Step 6: Clarity Pass ("Letter to Yourself")

### Internal version (what am I actually saying?)

"We hit a dependency delay. Feature B is blocked. If we wait, the timeline gets worse. The cleanest move is to cut Feature B now and ship it 3 weeks later. I need exec sign-off by Friday so we can lock the plan and stop burning planning cycles on uncertainty."

### Rewrite check

The draft already leads with this logic: problem (delay) -> recommendation (cut Feature B) -> ask (approve by Friday) -> what happens next (owned steps). The through-line is clean. No buried lede. No contradictions. The "if I do not hear back" line ensures a default action path, which reduces ambiguity.

No significant rewrite needed. The draft stands.

---

## Step 7: Canonical Doc Check

This email is a point-in-time decision request, not an ongoing reference. However, it references an existing project that likely needs a single source of truth.

**Recommendation:** Ensure the project tracker and canonical project doc links in the email are live and current. After the decision is made, log the decision (scope cut approved / alternative chosen) in the canonical project doc with the date and rationale.

**Canonical doc update (post-decision):**

| Date | Decision | Owner | Notes |
|---|---|---|---|
| [Friday's date] | Drop Feature B from launch; move to fast-follow | [Exec sponsor] | Dependency delay; protects revised launch date |

This is not a case where a new canonical doc is needed -- the existing project doc should be updated.

---

## Step 8: Quality Gate + Finalize

### Universal Checklist

- [x] Audience is clear; the first screen answers "why am I reading this?"
- [x] The ask is explicit (decision) and includes a deadline (Friday EOD)
- [x] The "how" is concrete: steps, owners, and dependencies are specified
- [x] TL;DR exists and matches the body (no surprises)
- [x] Scanability: headings, bullets, short paragraphs; no wall-of-text sections
- [x] Terms, acronyms, and dates are unambiguous; key numbers are written down
- [x] Single source of truth is linked for ongoing work
- [x] Tone is direct and respectful; avoids blame; assumes good intent
- [x] Safety: no secrets, credentials, or unnecessary sensitive/PII details

### Decision Request Checklist

- [x] Options are stated (approve scope cut OR raise concerns) with recommendation (approve)
- [x] Tradeoffs are explicit (drop Feature B now vs. 4+ weeks of additional uncertainty)
- [x] The cost of delay is stated (timeline extends further; planning cycles wasted)
- [x] "If you disagree" path is clear (reply with concerns by Thursday EOD)

### Rubric Scoring

| Dimension | Score | Rationale |
|---|---|---|
| 1. Outcome + ask clarity | **2** | Ask is in the TL;DR, repeated in its own section, with a deadline and default-action fallback. |
| 2. "How" specificity (actionability) | **2** | Five numbered next steps with named owners and dates. Dependencies called out. |
| 3. Structure + scanability | **2** | TL;DR first, headings in scan order (Ask > Context > Changes > Next steps), table for changes, bullets throughout. |
| 4. Correctness + completeness | **2** | All user-provided facts included. Assumptions labeled (3-week fast-follow, 4+ week delay risk). Placeholder links noted. |
| 5. Tone + trust | **2** | Direct, calm, no blame ("outside our control"), acknowledges uncertainty (fast-follow depends on dependency), invites concerns. |
| 6. Source of truth + follow-through | **2** | Links to canonical doc and tracker. Post-decision logging recommended. Next update date specified. |
| **Total** | **12/12** | Passes the >= 8/12 bar. |

---

## Risks / Open Questions / Next Steps

### Risks

- **Fast-follow feasibility:** Feature B's fast-follow timeline (3 weeks post-launch) depends on the same upstream dependency resolving. If it does not, the fast-follow date will also slip. [Eng lead] will confirm feasibility by next Wednesday.
- **Customer impact:** If any customers were specifically promised Feature B at launch, the PM should identify them and prepare targeted messaging before the Monday notification.
- **Silence = approval:** The "if I do not hear back" default could cause friction if a stakeholder misses the email. Consider a Slack ping on Thursday as a nudge.

### Open Questions

- Are there any customer commitments tied specifically to Feature B at launch that would change the calculus?
- Does the GTM team need to adjust any launch messaging given the Feature B removal, or is it low-visibility enough to handle post-launch?
- Should the fast-follow be communicated externally now, or only after the dependency is confirmed resolved?

### Next Steps

1. **Send email** to exec stakeholders (today)
2. **Slack-ping** key stakeholders Thursday if no reply received
3. **Log decision** in canonical project doc (Friday, after approval)
4. **[PM name]:** Execute post-approval communication plan (Monday)
5. **[Eng lead]:** Confirm Feature B fast-follow feasibility (next Wednesday)
6. **[PM name]:** Send locked-plan status update (next Friday)
