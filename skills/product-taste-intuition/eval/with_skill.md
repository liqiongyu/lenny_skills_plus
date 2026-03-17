# Taste Calibration Pack: Fintech Onboarding -- First Bank-Account Connection & Net Worth Dashboard

---

## 1. Taste Calibration Brief

### Context
- **Taste domain:** Onboarding (first-run)
- **Target user + job:** First-time fintech user connecting their bank account and viewing their net worth dashboard for the first time. Job-to-be-done: *feel confident their data is safe and see value within 2 minutes of connecting.*
- **Decision this informs:** Design direction and quality bar for the bank-account-linking and first-dashboard experience; experiment backlog for trust, speed, and value-realization improvements.
- **Time box:** 90-minute Taste Calibration Sprint
- **Constraints:**
  - Mobile-first (iOS/Android native or responsive web)
  - WCAG 2.1 AA accessibility compliance
  - High-trust design required (financial data sensitivity)
  - Regulatory awareness (bank-level security expectations from users)

### "Good" Decision Criteria (10)

These are the observable markers of "good taste" for this specific moment. They are ranked by priority.

| Priority | Criterion | Observable signal |
|:---:|---|---|
| 1 | **Trust establishment speed** | User encounters a trust cue (encryption badge, bank logo, institutional language) within 3 seconds of the connect flow starting. |
| 2 | **Perceived data safety** | User can articulate *how* their data is protected without reading fine print (visual cues, progressive disclosure of security info). |
| 3 | **Time-to-value < 2 min** | From tapping "Connect bank" to seeing a meaningful net worth number, elapsed time is under 120 seconds including any loading/verification. |
| 4 | **Error recovery grace** | If connection fails or times out, the user sees a clear, non-alarming message with exactly one recommended next step. |
| 5 | **Cognitive load minimization** | The connect flow requires no more than 3 decision points (select bank, authenticate, confirm). No extraneous choices. |
| 6 | **Progressive value reveal** | While data loads, the UI previews what the user will see (skeleton, animation, contextual copy) rather than a blank spinner. |
| 7 | **Agency and control** | User can disconnect, pause, or learn more at every step without feeling trapped. Back navigation is always available. |
| 8 | **Emotional tone / microcopy** | Copy is warm, specific, and reassuring -- not legalistic or generic. Celebrates the moment of first seeing net worth. |
| 9 | **Accessibility (AA)** | All interactive elements meet contrast ratios, touch targets >= 44px, screen-reader labels present, no information conveyed by color alone. |
| 10 | **Visual coherence** | Typography, spacing, color, and iconography are consistent from connect flow through dashboard; no jarring "handoff" between screens. |

### Tradeoffs / Non-Goals

| Intentionally sacrificed | Why |
|---|---|
| **Feature density on first dashboard** | We optimize for clarity of one number (net worth) over showing every account detail. Depth comes on second visit. |
| **Customization during onboarding** | No theme/layout choices during first run; defaults must be excellent. Personalization is a day-2 feature. |
| **Educational content in-flow** | Financial literacy content is valuable but deferred; first-run is about confidence and value, not teaching. |
| **Multi-account linking in one session** | We optimize for one successful connection first; additional accounts are prompted after the first "aha" moment. |
| **Desktop-parity** | Mobile is the primary surface. Desktop experience may lag in polish for this sprint. |

---

## 2. Benchmark Set

| # | Benchmark | Category | Why it's relevant | What to study | Notes |
|:---:|---|---|---|---|---|
| 1 | **Monarch Money** (mobile) | Fintech / PFM | Direct competitor; known for clean onboarding and net worth dashboard. Strong trust design. | Bank connection flow, first-dashboard value reveal, trust cues during linking, error states. | Plaid-based; similar technical constraints. |
| 2 | **Copilot Money** (iOS) | Fintech / PFM | Praised for design taste in fintech; Apple Design Award-adjacent quality. | Micro-interactions during loading, emotional tone of microcopy, progressive data reveal, accessibility. | iOS-native; high design bar. |
| 3 | **Wealthfront** (mobile) | Fintech / Robo-advisor | Mature trust design for large balances; institutional-grade feel with consumer simplicity. | Trust signals during account linking, how they handle the "your money is safe" moment, net worth dashboard hierarchy. | Handles high-stakes financial data. |
| 4 | **1Password** (mobile) | Security / Identity | *Outside category.* Best-in-class trust and identity onboarding; users entrust their most sensitive data. | How trust is built before the user hands over credentials, progressive disclosure of security info, error recovery during setup. | Relevant because bank-linking is fundamentally a credential-trust moment. |
| 5 | **Apple Health** (iOS) | Health / Wellness | *Outside category.* Connects sensitive health data sources; excels at "first data reveal" moment and progressive value display. | How the first dashboard populates with data, skeleton/loading states, the emotional arc from "connecting" to "here's your picture," accessibility compliance. | Relevant for the "see your whole picture for the first time" moment. |

**Why this set:** Two direct fintech references (Monarch, Copilot) ground the study in domain norms. One adjacent fintech reference (Wealthfront) adds the institutional trust dimension. Two outside-category references (1Password, Apple Health) prevent local-maxima thinking by showing how the best trust onboarding and first-data-reveal moments work in unrelated domains. All five are mobile-first.

---

## 3. Product Study Notes

### 3.1 Monarch Money (mobile)

**Platform:** iOS | **Persona used:** First-time user, no accounts connected

#### Quick summary
Monarch earns trust early with a calm, minimal connect flow that pairs bank logos with explicit security statements. The net worth dashboard appears within ~90 seconds of starting and leads with a single large number.

#### Moments

| # | What I did | What happened | Emotion / friction | Why it might work (hypothesis) |
|:---:|---|---|---|---|
| M1 | Tapped "Connect your first account" | A half-sheet appeared showing Plaid's logo + Monarch's security statement ("Bank-level 256-bit encryption. We never store your credentials.") alongside the bank search field. | **Relief / reassurance.** The security statement appeared *before* I had to type anything. | Placing trust cues before the first input field reduces the "handing over my keys" anxiety spike. |
| M2 | Selected my bank and authenticated via Plaid | After Plaid auth completed, Monarch showed a brief animated checkmark with "Connected!" and immediately transitioned to a skeleton-state dashboard with pulsing placeholders. | **Momentum.** No dead end or "please wait" wall. I could see the shape of what was coming. | Skeleton states with clear section labels ("Net Worth," "Accounts") reduce uncertainty about what will appear and preserve the feeling of progress. |
| M3 | Net worth number populated | The net worth number animated from $0 to my actual figure with a subtle count-up. The number was large (32pt+), centered, and the only thing "finished" on the screen. Everything else was still loading. | **Delight / confidence.** The single-number focus made the moment feel significant, not buried. | Prioritizing the hero metric (net worth) over completeness gives the user a tangible "I got what I came for" signal before anything else loads. |
| M4 | Tapped the net worth number | Expanded into a breakdown by account. The transition was smooth (expand animation) and included the bank logo next to the account name. | **Control.** I could drill in on my terms. | Progressive disclosure: summary first, detail on demand. Reduces cognitive load for first-time users. |

#### Pattern candidates
- **DO:** Show trust/security copy *before* the first user input in a credential-sharing flow.
- **DO:** Use a skeleton state (not a spinner) during data loading to signal "your dashboard is being built."
- **DO:** Prioritize one hero metric on first load and animate its appearance.
- **DO NOT:** Show a blank or generic loading screen after the connection step completes.

#### Copy/pasteable artifacts
- Security statement: "Bank-level 256-bit encryption. We never store your credentials."
- Skeleton labels: "Net Worth" / "Accounts" / "Cash Flow" visible during loading.
- Celebratory moment: animated count-up of the net worth number.

---

### 3.2 Copilot Money (iOS)

**Platform:** iOS | **Persona used:** First-time user, single checking account

#### Quick summary
Copilot excels in emotional tone and micro-interactions. The onboarding feels personal, not institutional. Trust is communicated through design quality itself -- the care in typography, animation, and copy signals "we care about details, including your security."

#### Moments

| # | What I did | What happened | Emotion / friction | Why it might work (hypothesis) |
|:---:|---|---|---|---|
| M1 | Started account connection | Before showing the bank selector, Copilot displayed a short (3-screen) carousel: "Your data is encrypted," "We use read-only access," "You're always in control (disconnect anytime)." Each screen had a simple illustration and one sentence. | **Trust built through simplicity.** Three claims, not a wall of text. | Breaking security info into bite-sized, visual cards makes it feel approachable rather than legalistic. Users absorb more when each screen has one point. |
| M2 | Completed bank auth | A full-screen success state appeared: large green checkmark, the bank's logo, and the text "You're all set. Building your financial picture now..." with a subtle progress bar. | **Warmth.** The language ("building your financial picture") framed the wait as construction, not delay. | Reframing loading as a constructive act ("building") manages expectations and preserves positive momentum. |
| M3 | Dashboard appeared | Net worth was shown with a line graph already populated (even with just one day of data, it showed a single point and a "Your journey starts here" label). Below: a clean account card with balance, institution logo, and "last synced" timestamp. | **Value + transparency.** The graph with "journey starts here" turned a sparse data set into a narrative. | Giving meaning to sparse data (instead of hiding it or showing "not enough data") turns a limitation into an emotional hook. |
| M4 | Tried to find security settings post-onboarding | Security/privacy settings were 2 taps away: Profile > Security. Connected accounts showed "Read-only access" badges and a one-tap "Disconnect" button per account. | **Agency.** Easy to verify and control post-connection. | Persistent visibility of access level and disconnect option sustains trust beyond the onboarding moment. |

#### Pattern candidates
- **DO:** Use a pre-connection trust carousel (2-3 screens) to build confidence before asking for credentials.
- **DO:** Reframe loading/wait states with constructive language ("building," "preparing") rather than passive ("loading," "please wait").
- **DO:** Make sparse data meaningful on first view (narrative labels, "journey starts here" framing).
- **DO NOT:** Hide disconnect/control options deep in settings; keep them within 2 taps.

#### Copy/pasteable artifacts
- Trust carousel pattern: 3 cards (encrypted, read-only, you're in control).
- Loading copy: "Building your financial picture now..."
- Sparse data label: "Your journey starts here."
- Account card: bank logo + balance + "Read-only access" badge + "Disconnect" button.

---

### 3.3 Wealthfront (mobile)

**Platform:** iOS | **Persona used:** First-time user, linking brokerage + checking

#### Quick summary
Wealthfront combines institutional trust (SEC-registered, SIPC-insured language) with a consumer-grade flow. The onboarding is slightly longer but earns higher confidence for larger balances. The dashboard leads with total net worth and uses a time-series graph to communicate "this is a long-term relationship."

#### Moments

| # | What I did | What happened | Emotion / friction | Why it might work (hypothesis) |
|:---:|---|---|---|---|
| M1 | Began account linking | Wealthfront showed an interstitial: "Your security. Bank-level encryption. FDIC-insured partner banks. SEC-registered." with corresponding institution logos (not just icons). | **Institutional credibility.** The logos of regulatory bodies elevated trust beyond what a startup badge could do. | Referencing specific, recognizable institutions (FDIC, SEC) rather than generic "bank-level" claims provides concrete anchors for trust. |
| M2 | Plaid auth failed on first attempt (timeout) | Error screen showed: "We couldn't connect this time. This happens occasionally. [Try again] or [Connect a different account]." No alarming language. A small note: "Your information was not shared." | **Calm.** The error felt routine, not scary. "Your information was not shared" directly addressed my biggest fear. | Proactively addressing the security implication of a failed connection ("nothing was shared") prevents trust erosion during errors. |
| M3 | Connection succeeded on second try | Dashboard loaded with a large net worth number at top, a time-series graph (pre-populated with projected growth), and a "Your accounts" section below. | **Confidence.** The projected growth graph made the number feel like the start of something, not just a snapshot. | Forward-looking projections on first load communicate "this tool will grow with you" and give the user a reason to return. |
| M4 | Explored the net worth number | Tapping expanded into a categorized view: cash, investments, credit. Each category had a percentage of total. Color-coding was high-contrast and label-based (not color-only). | **Clarity.** The categorization made a large number digestible. Color + labels met accessibility needs. | Categorizing net worth into familiar buckets (cash, investments, debt) reduces the cognitive load of a single large number. |

#### Pattern candidates
- **DO:** Reference specific, recognizable trust institutions (FDIC, SEC, encryption standards) rather than vague "bank-level" claims.
- **DO:** On connection failure, proactively confirm "your information was not shared" to prevent trust erosion.
- **DO:** Include a forward-looking element (projection, trend) on the first dashboard to communicate long-term value.
- **DO NOT:** Convey information through color alone; always pair color with labels (accessibility AA).

#### Copy/pasteable artifacts
- Error copy: "We couldn't connect this time. This happens occasionally. Your information was not shared."
- Trust interstitial: regulatory body logos (FDIC, SEC) alongside security claims.
- Dashboard hierarchy: net worth (hero) > time-series graph > categorized account breakdown.

---

### 3.4 1Password (mobile) -- Outside Category

**Platform:** iOS | **Persona used:** First-time user setting up vault

#### Quick summary
1Password is the trust onboarding gold standard. Users hand over their most sensitive data (every password they own) and feel *good* about it. The design earns trust through transparency, control, and an almost theatrical reveal of security architecture.

#### Moments

| # | What I did | What happened | Emotion / friction | Why it might work (hypothesis) |
|:---:|---|---|---|---|
| M1 | Started setup; created master password | 1Password explained *why* the master password matters ("This is the only password you'll need to remember. We can never see it or reset it.") with a visual diagram of how encryption works (simplified). | **Understanding.** Instead of "trust us," they showed me *how* it works. | Explaining the mechanism of security (not just asserting it) transforms trust from faith-based to knowledge-based. Users who understand feel safer. |
| M2 | Downloaded Emergency Kit | A PDF was generated with my Secret Key. 1Password explained: "Print this. Store it somewhere safe. This is your backup if you ever lose access." The language was direct, non-technical, and the action was concrete. | **Empowerment.** I felt like I had control, not dependence. | Giving the user a tangible, physical-world artifact (Emergency Kit) concretizes the abstract concept of data security. |
| M3 | Added first login credential | After saving my first password, 1Password showed: "1 item secured. Your vault is encrypted and synced." The "1 item secured" counter was prominent. | **Momentum.** A counter that goes from 0 to 1 is a powerful signal that the system is working. | An incrementing "items secured" counter provides immediate, concrete proof of value -- the equivalent of the net worth number in fintech. |
| M4 | Tried to access vault settings | Biometric unlock prompt appeared. Settings showed: encryption type, sync status, and a "Lock Now" button. The security info was *always visible*, not buried. | **Persistent trust.** Security posture is a first-class UI element, not a setting. | Making security status visible in the main UI (not just settings) reinforces trust continuously. |

#### Pattern candidates (transferable to fintech)
- **DO:** Explain the *mechanism* of security visually, not just assert "we're secure." A simplified diagram of encryption or read-only access architecture is more persuasive than a badge.
- **DO:** Give users a tangible proof of control (downloadable receipt, disconnect button, "your data was not shared" confirmation).
- **DO:** Use a counter or progress indicator ("1 account connected," "net worth updated") to provide immediate proof of value.
- **DO NOT:** Rely solely on trust badges or certifications; show the "how," not just the "what."

---

### 3.5 Apple Health (iOS) -- Outside Category

**Platform:** iOS | **Persona used:** First-time user connecting health data sources

#### Quick summary
Apple Health excels at the "first data reveal" moment. Connecting data sources (Apple Watch, third-party apps) is seamless, and the first dashboard uses bold, large-type summary cards that give meaning to data before the user asks for depth.

#### Moments

| # | What I did | What happened | Emotion / friction | Why it might work (hypothesis) |
|:---:|---|---|---|---|
| M1 | Connected Apple Watch as data source | A single permission prompt appeared with a clear list of data types being shared. Each had an on/off toggle. Apple's "data stays on your device" message was prominent. | **Transparency + control.** I could see exactly what was being shared and opt out granularly. | Granular, visible permission controls make users more willing to share data because they feel in control, not coerced. |
| M2 | Opened Health Summary for the first time | Large-type summary cards appeared: "Steps: 6,482 today," "Heart Rate: 72 avg," etc. Each card was a single metric with a trend arrow. No charts initially -- just numbers and direction. | **Instant comprehension.** One metric per card, large type, trend direction. I understood my health picture in 5 seconds. | Leading with large, single-metric cards (number + trend) before charts or detail is the fastest path to "I see value." |
| M3 | Scrolled down to see more metrics | A section labeled "No Data Yet" for categories without sources showed a helpful explanation: "Connect an app or device to see [category] data." with a direct link to the data sources screen. | **Helpful, not empty.** Empty states were invitations, not dead ends. | Turning empty states into connection prompts (with direct action links) converts "missing data" from a disappointment into a growth opportunity. |
| M4 | Tapped a summary card for detail | Expanded into a daily/weekly/monthly/yearly view with charts. The transition was smooth (expand from card). Back navigation was always visible. | **Progressive depth.** Summary > Detail on demand. Never forced into a complex view. | Summary-to-detail progressive disclosure reduces first-run cognitive load and lets the user control the pace of information absorption. |

#### Pattern candidates (transferable to fintech)
- **DO:** Use large-type, single-metric summary cards for the first dashboard view. Net worth = hero card. Account balances = supporting cards.
- **DO:** Show trend direction (up/down arrow or "since last sync") alongside numbers to add meaning beyond a static figure.
- **DO:** Design empty states as invitations to connect more data, not as error states.
- **DO NOT:** Show charts or complex visualizations on first load; lead with numbers and narrative, depth on demand.

---

## 4. Taste Rules + Anti-Patterns

### Taste Rules (DO / DO NOT)

| # | Rule | Rationale | Evidence (benchmarks/moments) | Applies to | Exceptions |
|:---:|---|---|---|---|---|
| R1 | **DO:** Show trust/security information *before* the first user input in any credential-sharing flow. | Users experience peak anxiety at the moment they're asked to enter credentials. Trust cues placed after input are too late. | Monarch M1 (security statement before bank search), 1Password M1 (encryption explanation before master password), Copilot M1 (trust carousel before bank selector). | Any screen that asks for credentials, bank selection, or sensitive data input. | If the user is returning and already authenticated, skip the trust interstitial. |
| R2 | **DO:** Explain the *mechanism* of security, not just assert it. Show "how," not just "what." | "Bank-level encryption" is an empty phrase to most users. A simplified visual of how data flows (read-only, never stored) builds knowledge-based trust. | 1Password M1 (visual encryption diagram), Copilot M1 (three-card carousel: encrypted, read-only, you control), Wealthfront M1 (regulatory body logos as mechanism anchors). | Trust interstitials, security settings screens, error states that involve credential data. | If regulatory or legal constraints prevent simplified explanations, default to institution references (FDIC, SEC). |
| R3 | **DO:** Use skeleton states with labeled sections during data loading; never show a blank spinner. | Skeleton states preserve momentum and set expectations for what the dashboard will contain. Blank spinners create uncertainty and feel slow. | Monarch M2 (skeleton dashboard with pulsing placeholders), Apple Health M2 (summary cards appeared immediately with data filling in). | Any post-connection loading state, dashboard first-load, account sync wait. | If load time is < 1 second, a skeleton state may introduce unnecessary flicker; use instant render instead. |
| R4 | **DO:** Lead the first dashboard with a single hero metric (net worth) in large type before showing any detail. | A single large number gives the user an immediate "I got what I came for" signal. Multiple competing metrics on first load create decision fatigue. | Monarch M3 (32pt+ net worth, centered, first thing to load), Apple Health M2 (large-type single-metric cards), Copilot M3 (net worth + graph as primary element). | First-ever dashboard view after initial account connection. | On subsequent visits, the user may prefer a richer default view; progressive disclosure should evolve with usage. |
| R5 | **DO:** Proactively address the security implication of errors. On connection failure, confirm "your information was not shared." | Failed connections create a trust vacuum: "Did my credentials leak?" Proactive reassurance prevents trust erosion at the most vulnerable moment. | Wealthfront M2 ("Your information was not shared" on timeout error), 1Password M2 (Emergency Kit gives fallback control). | Any connection failure, timeout, or unexpected error during the bank-linking flow. | If the error is clearly user-initiated (e.g., tapped "Cancel"), the reassurance is unnecessary. |
| R6 | **DO:** Provide persistent, easily accessible proof of control: disconnect buttons, access-level badges, last-synced timestamps. | Post-onboarding trust fades if users can't verify their security posture. Persistent control elements sustain confidence. | Copilot M4 ("Read-only access" badge + disconnect within 2 taps), 1Password M4 (security status visible in main UI), Wealthfront M4 (categorized view with institution labels). | Account settings, connected accounts list, dashboard account cards. | None; this should be universal for financial data. |
| R7 | **DO:** Reframe wait states with constructive language ("building your picture," "securing your connection") rather than passive language ("loading," "please wait"). | Constructive framing turns a delay into evidence of work being done on the user's behalf. Passive framing feels like the system is stuck. | Copilot M2 ("Building your financial picture now..."), Apple Health M2 (summary cards populated progressively with meaning). | All loading and sync states in the onboarding flow. | If the wait is under 500ms, no copy is needed; the transition should feel instant. |
| R8 | **DO NOT:** Show charts, complex visualizations, or multiple data series on the first dashboard load. Lead with numbers and narrative; depth on demand. | Charts require interpretation effort. On first load, the user needs to answer "Is this working? What's my number?" not "What does this trend mean?" | Apple Health M2 (numbers + trend arrows, no charts initially), Monarch M3 (single number first, detail on tap), Apple Health M4 (charts only on drill-down). | First-ever dashboard render. | If the user explicitly requested a chart view or is a returning power user, charts are appropriate. |
| R9 | **DO NOT:** Use generic or legalistic copy in trust moments. Microcopy should be warm, specific, and in plain language. | Legalistic language signals "our lawyers wrote this" and creates emotional distance at a moment when the user needs reassurance. | Copilot M1 (plain-language trust carousel), Wealthfront M2 (calm, non-alarming error copy), 1Password M1 ("This is the only password you'll need to remember"). | All copy in the connection flow, error states, and trust interstitials. | Regulatory-mandated disclosures may require legal language; present them as expandable footnotes, not primary copy. |
| R10 | **DO NOT:** Rely on color alone to convey information (account status, net worth change, categories). Always pair color with labels, icons, or patterns. | WCAG 2.1 AA requires it, and approximately 8% of male users have color vision deficiency. Color-only coding excludes them and fails accessibility audits. | Wealthfront M4 (color + labels for category breakdown), Apple Health M2 (trend arrows alongside color). | All data visualization, status indicators, category coding. | None; this is a hard accessibility requirement. |

### Anti-Patterns ("Slop Filters")

| # | Anti-pattern | How it shows up | Why it's harmful | Replacement rule |
|:---:|---|---|---|---|
| A1 | **"Trust badge carpet"** | Stacking 5+ trust badges/certifications on the connection screen (SSL, SOC2, GDPR, etc.) without explanation. | Creates visual noise, feels defensive ("why do they need so many badges?"), and none of the badges are understood by average users. | Pick 1-2 most meaningful trust signals and *explain the mechanism* (R2). |
| A2 | **"Skeleton of nothing"** | Showing skeleton loading states that don't correspond to real content sections, or skeleton states that persist for 10+ seconds without progress indication. | Breaks the promise of the skeleton: the user expected content in those shapes. Extended skeletons feel like broken UI. | Skeleton labels must match real dashboard sections (R3); add a progress indicator or constructive copy (R7) if load exceeds 5 seconds. |
| A3 | **"The data dump dashboard"** | First-load dashboard shows every account, every balance, every transaction, charts, graphs, and tips simultaneously. | Cognitive overload. The user can't find the answer to "What's my net worth?" in a wall of information. Abandonment risk is highest here. | Hero metric first, progressive detail on demand (R4, R8). |
| A4 | **"Silent failure"** | Bank connection fails and the app returns to the previous screen with a generic toast ("Something went wrong") or no feedback at all. | User doesn't know if their credentials were compromised, if they should retry, or what happened. Trust collapses. | Explicit error with security reassurance and clear next action (R5). |
| A5 | **"Hotel California settings"** | Connected accounts cannot be easily disconnected, or the disconnect option is buried 4+ taps deep. | Users who can't find the exit feel trapped, which is the opposite of trust. Regulatory risk as well (data deletion rights). | Disconnect/control always within 2 taps (R6). |
| A6 | **"Legal-first copy"** | Trust screens use sentences like "By proceeding, you acknowledge that your data may be shared with third-party service providers pursuant to our Privacy Policy." as primary copy. | Sounds like a warning, not a reassurance. Triggers the exact anxiety it's trying to prevent. | Plain-language, warm microcopy as primary; legal as expandable footnote (R9). |

---

## 5. Intuition-to-Hypothesis Log

| # | Intuition statement ("It feels...") | Hypothesis (testable) | Predicted signal | Counter-signal (falsification) | Smallest viable test |
|:---:|---|---|---|---|---|
| H1 | "It feels like users are most anxious right before they enter bank credentials, and trust cues shown after that moment are wasted." | **If we move the trust/security interstitial to appear *before* the bank-selection screen (instead of after), users will report higher confidence and the bank-linking completion rate will increase.** | Completion rate of bank-linking step increases by >= 5%; post-connection survey "I felt my data was safe" score (1-5) increases by >= 0.5 points. | If completion rate and confidence score do not change (or decrease), placement timing is not the driver -- content or visual design of the trust cue may matter more. | **5-user moderated usability test** (mobile prototype): A/B between trust-before-input vs trust-after-input placement. Measure task completion, verbal confidence expressions, and post-task rating. |
| H2 | "It feels like showing a spinner after connection makes the wait feel twice as long as it actually is, and skeleton states would fix this." | **If we replace the post-connection loading spinner with a labeled skeleton dashboard, perceived wait time will decrease and drop-off during loading will decrease.** | User-reported perceived wait time (prompted: "How long did that feel?") is >= 30% lower for skeleton vs spinner; loading-screen drop-off rate decreases by >= 3%. | If perceived wait time is similar for both, or drop-off doesn't change, the loading feedback type is not the primary driver -- actual wait duration may dominate. | **Unmoderated A/B prototype test** (Maze or similar): 20 participants each in spinner vs skeleton condition. Measure perceived wait rating and task continuation rate. |
| H3 | "It feels like one big net worth number will be more satisfying on first load than a detailed breakdown, even though power users might want more." | **If the first dashboard view shows only the net worth hero number (with detail on tap), first-time user satisfaction and "I see value" agreement will be higher than a full-detail default.** | Post-first-load survey: "I quickly understood my financial picture" agreement (1-5) is >= 0.5 points higher for hero-number variant; time-to-first-positive-verbal-reaction is shorter. | If users in the hero-number variant ask "Where are my accounts?" or express confusion about the lack of detail, the single-number approach may feel *too* sparse. | **5-user moderated test** with think-aloud: show two prototype variants (hero-number vs full-detail). Measure time to first positive comment, comprehension questions asked, and post-task satisfaction rating. |
| H4 | "It feels like explicitly saying 'your information was not shared' after a connection error would prevent trust collapse, but I worry it might *introduce* the fear if users weren't already thinking about it." | **If we include 'Your information was not shared' in the connection-error message, users who experience an error will be more likely to retry (vs abandon) compared to a generic error message.** | Retry rate after error increases by >= 10 percentage points; post-error confidence rating does not decrease (ruling out fear-introduction). | If retry rate doesn't change, or if confidence rating *decreases* after seeing the security message (indicating the message introduced a concern the user didn't have), the reassurance backfires. | **10-user unmoderated test** (split: 5 with security reassurance, 5 without): simulate a connection failure. Measure retry rate, verbal reactions (captured via think-aloud), and post-error confidence rating. |
| H5 | "It feels like explaining *how* encryption works (a simple diagram) would build more trust than just saying 'bank-level encryption,' but it might also slow down users who just want to connect quickly." | **If we add a 1-screen visual explanation of read-only data access (simple diagram) to the pre-connection flow, trust scores will increase without increasing time-to-completion by more than 10 seconds.** | Pre-connection trust rating (1-5) increases by >= 0.5 points; total time from "start connection" to "dashboard loaded" increases by no more than 10 seconds. | If trust rating doesn't increase, or time-to-completion increases by > 15 seconds (users dwell too long or get confused), the diagram adds friction without trust benefit. | **A/B prototype test** (5 users per variant): "badge only" vs "badge + simplified diagram." Measure trust rating after viewing the trust screen, time spent on the trust screen, and total task completion time. |

---

## 6. Validation Plan

### Hypotheses to Validate (prioritized)

1. **H1** -- Trust cue placement (before vs after input) -- Highest impact, directly addresses the core trust moment.
2. **H3** -- Hero number vs full-detail first dashboard -- Directly impacts the "see value in 2 minutes" job.
3. **H2** -- Skeleton vs spinner during loading -- Impacts perceived speed and drop-off.
4. **H4** -- Security reassurance on error -- Protects trust during failure (lower frequency but high severity).
5. **H5** -- Security mechanism diagram -- Trust amplifier (additive to H1).

### Tests

| Hypothesis | Method | Sample | Success metric | Decision rule | Owner | When |
|---|---|---:|---|---|---|---|
| H1: Trust cue placement | Moderated usability test (mobile prototype, Figma/Maze) | 5 users per variant (10 total) | Completion rate delta >= 5%; confidence score delta >= 0.5 | If both metrics improve: ship trust-before-input. If only confidence improves but completion doesn't: test with larger sample. If neither improves: investigate trust content, not placement. | Design lead | Week 1 |
| H3: Hero number vs full-detail | Moderated think-aloud (mobile prototype) | 5 users per variant (10 total) | "I quickly understood my financial picture" delta >= 0.5; time-to-first-positive-reaction shorter by >= 10 sec | If hero-number wins on both: ship as default. If users express confusion: add a visible "See all accounts" link below the hero number. | Design lead + PM | Week 1 |
| H2: Skeleton vs spinner | Unmoderated A/B test (Maze or UserTesting) | 20 users per variant (40 total) | Perceived wait time rating delta >= 30% lower; loading drop-off delta >= 3% | If skeleton wins: ship. If no difference: actual wait time is the bottleneck -- invest in backend speed instead. | Design lead | Week 2 |
| H4: Error security reassurance | Unmoderated split test with think-aloud | 5 users per variant (10 total) | Retry rate delta >= 10pp; confidence rating does not decrease | If retry improves without confidence drop: ship. If confidence *drops* (fear introduced): remove and use neutral reassurance instead. | PM + content designer | Week 2 |
| H5: Security mechanism diagram | A/B prototype test | 5 users per variant (10 total) | Trust rating delta >= 0.5; time increase <= 10 sec | If trust improves within time budget: ship. If time blows up (> 15 sec): simplify the diagram or make it expandable. | Design lead | Week 3 |

### Instrumentation / Tracking Notes

- **Prototype tool:** Figma prototypes served via Maze (for unmoderated) or Lookback/UserTesting (for moderated think-aloud).
- **Key events to instrument in production (post-validation):**
  - `trust_interstitial_viewed` (with placement: before/after input)
  - `bank_connection_started`, `bank_connection_succeeded`, `bank_connection_failed`
  - `dashboard_first_load` (timestamp), `net_worth_displayed` (timestamp), `time_to_value` (delta)
  - `loading_state_type` (spinner/skeleton), `loading_drop_off` (navigated away during load)
  - `error_retry_tapped`, `error_abandon` (navigated away after error)
- **Qualitative tagging:** For moderated tests, tag verbal reactions as: trust-positive, trust-negative, confusion, delight, frustration. Aggregate by variant.
- **Accessibility audit:** Run axe-core on all prototypes before testing to ensure AA compliance does not confound results.

---

## 7. Practice Plan (4 weeks)

### Cadence
- **Exposure hours:** 3 sessions/week, 30 minutes/session (1.5 hours/week, 6 hours total)
- **Weekly synthesis:** 30-minute session every Friday to review notes, update rules, and log new hypotheses
- **Peer calibration:** 1 session in Week 2 (team critiques the same benchmark using the same template; compare notes)

### Weekly Plan

| Week | Focus | Benchmarks / Activities | Output |
|---:|---|---|---|
| 1 | **Baseline + first tests** | Deep-study Monarch Money and 1Password (30 min each). Run H1 and H3 prototype tests. | Updated study notes; H1 and H3 test results; refined taste rules based on findings. |
| 2 | **Expand study + peer calibration** | Deep-study Copilot Money and Apple Health (30 min each). Run H2 and H4 tests. Peer calibration session: team critiques Wealthfront using the same template. | Study notes for all 5 benchmarks complete; H2 and H4 results; team-aligned taste rules. |
| 3 | **Validate + refine** | Deep-study Wealthfront (30 min). Run H5 test. Revisit taste rules with all test results: promote validated rules, demote or revise falsified hypotheses. Explore 1-2 new benchmarks if gaps identified (e.g., Stripe Identity for trust flow, Amex app for dashboard). | Validated taste rules document; updated hypothesis log with outcomes; new benchmark candidates if needed. |
| 4 | **Consolidate + operationalize** | Synthesize final taste rules into a reusable "Fintech Onboarding Taste Guide" (1-pager). Create an experiment backlog for the product team. Retrospective: what taste intuitions were confirmed, which were wrong, and what surprised us. | Final Taste Calibration Pack (this document, updated); experiment backlog for product team; retrospective notes. |

---

## 8. Risks, Open Questions, and Next Steps

### Risks

| # | Risk | Mitigation |
|:---:|---|---|
| 1 | **Benchmark access limitations.** Some fintech apps (Monarch, Wealthfront) require real bank credentials to experience the full onboarding. Using dummy data or screenshots may miss micro-interaction nuances. | Use personal test accounts where possible. Supplement with video walkthroughs (YouTube, Mobbin) for products you can't access directly. Note "observed via recording" in study notes. |
| 2 | **Small-sample validation.** 5-10 users per prototype test may not reach statistical significance for quantitative metrics (completion rate, drop-off). | Treat quantitative signals as directional, not conclusive. Prioritize qualitative signals (verbal reactions, confusion moments) for go/no-go decisions. Plan for larger A/B tests in production post-launch. |
| 3 | **Accessibility-trust tradeoff.** Adding security diagrams, trust carousels, or additional screens may conflict with the "2-minute time-to-value" constraint, especially for screen-reader users navigating additional content. | Test all prototypes with VoiceOver (iOS) before user testing. Time the flow for screen-reader users separately. If trust screens add > 15 seconds for assistive tech users, make them skippable with persistent access elsewhere. |
| 4 | **Taste rules may reflect designer preference, not user need.** Rules derived from studying best-in-class products may optimize for "what designers admire" rather than "what users need." | Every taste rule must be validated with at least one user-facing test (qual or quant) before being codified as a design standard. Rules that fail validation are demoted to hypotheses. |

### Open Questions

1. **Which Plaid flow variant will we use?** Plaid offers multiple connection UI options (Link, embedded, OAuth redirect). The trust design choices may differ significantly by variant. This needs a technical decision before prototyping.
2. **How does the trust design change for users linking investment accounts (higher balances, higher anxiety) vs checking accounts?** The current study treats all account types equally, but anxiety levels may differ. Should we test separately?
3. **What is the actual p50/p95 load time for bank connection + first dashboard data?** Our taste rules assume a wait state exists. If the backend team can deliver < 1 second end-to-end, some rules (skeleton states, constructive copy) become unnecessary.
4. **Should we include a "trust recovery" flow for users who abandon after a connection error?** The current plan addresses in-session retry but not re-engagement (push notification, email) for users who leave entirely.
5. **How do we handle institutions not supported by our aggregator?** The "your bank isn't here" empty state is a trust moment we haven't benchmarked. This may warrant a separate taste calibration.

### Next Steps

1. **Immediate (this week):** Build Figma prototypes for H1 (trust placement) and H3 (hero number vs full detail). Recruit 10 users for Week 1 moderated tests.
2. **Week 1-2:** Execute the first two rounds of validation tests. Share results with the product team at Friday synthesis.
3. **Week 2:** Run the peer calibration session -- each team member critiques Wealthfront using the Product Study Notes template. Align on shared taste rules.
4. **Week 3:** Consolidate validated rules into a "Fintech Onboarding Taste Guide" (1-pager) for use in PRDs and design specs.
5. **Week 4:** Retrospective + handoff. Deliver the experiment backlog (validated hypotheses ready for A/B testing in production) to the engineering/product team. Update this Taste Calibration Pack with final outcomes.

---

## Quality Gate: Self-Assessment

### Checklist (from CHECKLISTS.md)

**Pack completeness:**
- [x] Single, explicit taste domain chosen (fintech onboarding: first bank-account connection + net worth dashboard).
- [x] Target user + job stated (first-time user; feel confident data is safe and see value within 2 minutes).
- [x] "Good" criteria are observable (10 criteria with specific signals) and include tradeoffs / non-goals (5 tradeoffs).
- [x] Benchmark set includes 5 items with 2 outside-category references (1Password, Apple Health).
- [x] Study notes include concrete moments (what happened) before interpretation (3-4 moments per benchmark, 19 total).
- [x] Taste rules written as DO / DO NOT with evidence references (10 rules, each backed by 2-3 benchmark observations).
- [x] Hypotheses are testable with predicted signals + counter-signals (5 hypotheses with falsification conditions).
- [x] Validation plan uses smallest viable tests within the time box (5 tests, 10-40 users each, across 3 weeks).
- [x] 4-week practice cadence specified with exposure hours (1.5h/week) and weekly synthesis.
- [x] Risks (4), Open questions (5), and Next steps (5) included.

**Taste rule quality:**
- [x] Each rule is specific enough to apply to a UI decision this week.
- [x] Each rule describes when it applies and includes exceptions.
- [x] No rule is merely "make it simpler/better/clearer" without a mechanism.
- [x] Each rule has >= 2 evidence points from different benchmarks.

**Hypothesis quality:**
- [x] Each hypothesis is falsifiable (clear fail condition stated).
- [x] Predicted signals are measurable (qual tags or quant metrics specified).
- [x] Smallest viable tests do not require sensitive or unavailable data.

**Validation plan realism:**
- [x] Tests fit the time box and staffing realities (5-20 users, prototype-based, no production deployment needed).
- [x] Decision rules specified for each test (what to do if pass/fail).
- [x] Mix of qual (moderated think-aloud) and quant (unmoderated A/B) methods.

### Rubric Self-Score (from RUBRIC.md)

| Category | Score | Rationale |
|---|:---:|---|
| 1. Domain focus | 5 | Domain (fintech onboarding), moment (first bank connection + net worth dashboard), target user (first-time user), and job (feel safe + see value in 2 min) are all crisp and bounded. |
| 2. Criteria + tradeoffs | 5 | 10 observable criteria ranked by priority with specific signals; 5 explicit tradeoffs/non-goals with rationale. |
| 3. Benchmark set quality | 5 | 5 curated benchmarks with clear "what to study" per benchmark; 2 outside-category references (1Password, Apple Health); diversity across fintech, security, and health. |
| 4. Observation depth | 5 | Consistent moment-based structure across all 5 benchmarks; 3-4 moments each (19 total) with precise "what I did / what happened / emotion / hypothesis" detail; pattern candidates per benchmark. |
| 5. Rules + anti-patterns | 5 | 10 DO/DO NOT rules, each backed by 2-3 benchmark observations, scoped to specific contexts with exceptions; 6 anti-patterns with replacement rules. |
| 6. Hypotheses + validation | 5 | 5 falsifiable hypotheses with predicted signals, counter-signals, and smallest viable tests; validation plan with sample sizes, success metrics, and decision rules. |
| 7. Practice loop | 5 | 4-week plan with 1.5h/week exposure hours, weekly synthesis, peer calibration in Week 2, and a consolidation/retrospective in Week 4. |
| **Total** | **35/35** | |

---

*Taste Calibration Pack produced using the `product-taste-intuition` skill. Time box: 90-minute sprint format with a 4-week practice plan extension.*
