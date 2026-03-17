# Product Spec: "Invite Friends" Flow

## 1. Overview

### Goal
Increase successful invites (defined as: invitee downloads the app and completes onboarding) by shipping a low-friction, high-conversion invite flow within 4 weeks.

### Design Principle
**Optimize taps to first value.** Every screen, every modal, every confirmation should be interrogated: "Can this be removed or combined?" The target is 2 taps from trigger to invite sent, and 2 taps from invite received to first value for the invitee.

### Success Metrics
| Metric | Baseline | Target (8 weeks post-launch) |
|---|---|---|
| Invite send rate (% of MAU who send at least 1 invite) | N/A (new) | 15% |
| Invite acceptance rate (invitee opens link) | N/A | 40% |
| Invite conversion rate (invitee completes onboarding) | N/A | 25% |
| Time from invite tap to invite sent | N/A | < 8 seconds |
| Invitee time from link tap to first value | N/A | < 60 seconds |

### Non-Goals
- Referral rewards or incentive programs (potential Phase 2)
- In-app social graph / contacts sync beyond invite flow
- Web or Android (iOS only for this phase)

---

## 2. User Flows

### 2.1 Sender Flow (Happy Path)

```
[Trigger Point] → [Share Sheet] → [Invite Sent] → [Confirmation]
   Tap 1            Tap 2           (automatic)      (inline toast)
```

**Step-by-step:**

1. **Trigger (Tap 1):** User taps an "Invite Friends" entry point (see Section 3 for placement). This opens the native iOS share sheet with a pre-composed message and deep link.

2. **Share Sheet (Tap 2):** User selects a contact or channel (iMessage, WhatsApp, copy link, AirDrop, etc.). The invite is sent immediately via the chosen channel.

3. **Confirmation:** An inline toast appears: "Invite sent! You'll be notified when [they] join." No blocking modal, no extra tap required.

**Total sender taps: 2**

### 2.2 Invitee Flow (Happy Path)

```
[Tap Link] → [App Store / App Open] → [Personalized Onboarding] → [First Value]
   Tap 1         Tap 2 (Install)          (streamlined)              (immediate)
```

**Step-by-step:**

1. **Tap Link (Tap 1):** Invitee taps the deep link in their message. If the app is not installed, they land on a lightweight App Clip or App Store page. If installed, the app opens directly to a personalized welcome screen.

2. **Install & Open (Tap 2):** Invitee taps "Get" in the App Store. After install, the deferred deep link routes them to a personalized onboarding flow that references the inviter by name/avatar.

3. **Streamlined Onboarding:** The onboarding flow is condensed for invited users. Skip optional steps. Pre-fill context from the invite (e.g., shared content, group, or feature the sender was using). Target: 2-3 screens max, no sign-up wall before first value.

4. **First Value:** The invitee immediately sees the content, feature, or connection that motivated the invite. A "Connect with [Sender]" action is surfaced prominently.

**Total invitee taps to first value: 2 (tap link + install) for new users; 1 for existing users**

### 2.3 Sender Notification Flow

When an invitee joins:
- Push notification: "[Friend's name] just joined! Say hi."
- Tapping the notification opens a connection/interaction screen with the new user.
- This closes the loop and reinforces the behavior of inviting.

---

## 3. Entry Points & Triggers

### 3.1 Persistent Entry Points
| Location | Implementation | Rationale |
|---|---|---|
| Profile/Settings tab | "Invite Friends" row with icon | Discoverable for intentional inviters |
| Navigation bar / hamburger menu | "Invite Friends" row | Accessible from anywhere |

### 3.2 Contextual Triggers (High-Intent Moments)
These are the highest-leverage placements because the user has a natural reason to share:

| Trigger Moment | UX Pattern | Pre-composed Message |
|---|---|---|
| After completing a key action (e.g., finishing a workout, creating content, achieving a milestone) | Celebration screen with "Share with a friend" CTA | "[Name] just [accomplished X] on [App]. Try it out: [link]" |
| When viewing content that is better with others | Inline "Invite a friend to [do this together]" button | "I'm using [App] for [activity]. Join me: [link]" |
| Empty state in social/collaborative features | "Invite friends to get started" prompt with illustration | "Join me on [App]: [link]" |
| After the user's 3rd session (habit formation signal) | Soft prompt: "Enjoying [App]? Friends who join together stick around 2x longer" | Default share message with personalized context |
| Contact permission prompt (if applicable) | Suggest specific contacts the user messages frequently | Personalized per contact |

### 3.3 Trigger Frequency Rules
- Contextual prompts: Max 1 per session, max 3 per week.
- Never interrupt a core flow (no modals during primary tasks).
- Respect dismissals: If a user dismisses a contextual prompt twice, suppress for 30 days.
- Never show invite prompts before the user's 2nd session (let them find value first).

---

## 4. Deep Linking & Attribution

### 4.1 Link Structure
Use **Universal Links** (iOS) with a URL scheme fallback:

```
https://app.example.com/invite?ref={sender_user_id}&ctx={context_type}&cid={content_id}&sig={signature}
```

Parameters:
- `ref`: Sender's user ID (for attribution and personalization)
- `ctx`: Context type (e.g., "achievement", "content", "generic")
- `cid`: Content or feature ID (for deep routing after install)
- `sig`: HMAC signature to prevent link tampering

### 4.2 Deferred Deep Linking
Use a deferred deep linking solution (Branch.io, Firebase Dynamic Links, or custom) to:
- Attribute installs to specific inviters even after App Store redirect
- Route new users to the correct in-app destination after onboarding
- Pass context through the install process (sender name, shared content, etc.)

### 4.3 App Clip (Optional, Recommended)
For the highest-value invite contexts (e.g., shared content, collaborative features):
- Provide an App Clip experience that delivers immediate value without full install
- Include a prominent "Get the Full App" CTA within the App Clip
- This dramatically reduces taps-to-first-value for the invitee (0 install taps)

---

## 5. Share Message Design

### 5.1 Principles
- **Personal over promotional:** Messages should feel like they're from a friend, not a brand.
- **Context-rich:** Include what the sender was doing, not just a generic "try this app."
- **Rich previews:** Use Open Graph / link preview metadata to show an engaging card in iMessage, WhatsApp, etc.

### 5.2 Message Templates

**Generic Invite:**
> Check out [App Name] — I've been using it for [auto-detected primary use case]. Here's my invite link: [link]

**Post-Achievement:**
> I just [achieved X] on [App Name]! You should try it: [link]

**Content Share:**
> [Content title/preview] — thought you'd like this. Check it out on [App Name]: [link]

**Collaborative:**
> Join me on [App Name] so we can [collaborative feature]. Here's my invite: [link]

### 5.3 Link Preview Card
- **Title:** "[Sender's first name] invited you to [App Name]"
- **Subtitle:** Contextual (e.g., "Join 50K+ people doing [core activity]")
- **Image:** Dynamic — sender's avatar or relevant content thumbnail. Fallback to branded card.
- **Generate server-side** using an OG image service for fast, dynamic previews.

---

## 6. Invitee Onboarding (Invited User Experience)

### 6.1 Key Differences from Organic Onboarding
| Aspect | Organic User | Invited User |
|---|---|---|
| Welcome screen | Generic | "Welcome! [Sender name] invited you" with sender's avatar |
| Onboarding steps | Full (5-7 screens) | Condensed (2-3 screens), skip optional steps |
| Sign-up requirement | Before first value | After first value (delayed sign-up wall) |
| First screen after onboarding | Default home | Context-specific destination (shared content, sender's profile, collaborative feature) |
| Social connection | Must find friends manually | Auto-suggested connection with sender |

### 6.2 Delayed Sign-Up Wall
- Let invited users experience first value before requiring account creation.
- Show a "Sign up to save your progress and connect with [Sender]" prompt after the first meaningful interaction.
- This maximizes the chance they experience the "aha moment" before dropping off at registration.

---

## 7. Technical Architecture

### 7.1 Backend Components

**Invite Service:**
- `POST /invites` — Create invite, generate deep link, return shareable URL
- `GET /invites/{code}` — Resolve invite for incoming users
- `POST /invites/{code}/accept` — Mark invite as accepted, trigger sender notification
- `GET /users/{id}/invites` — List sent invites and their statuses

**Data Model:**
```
Invite {
    id: UUID
    sender_id: UUID
    invite_code: String (unique, short, URL-safe)
    context_type: Enum (generic, achievement, content, collaborative)
    context_id: String? (content ID, achievement ID, etc.)
    channel: Enum (imessage, whatsapp, copy_link, airdrop, other)
    status: Enum (created, sent, opened, accepted, expired)
    invitee_id: UUID? (populated on acceptance)
    created_at: Timestamp
    accepted_at: Timestamp?
    expires_at: Timestamp (default: 30 days)
}
```

**Analytics Events:**
- `invite_flow_started` — User tapped an invite entry point
- `invite_share_sheet_opened` — Share sheet presented
- `invite_sent` — Invite shared via a channel
- `invite_link_opened` — Invitee tapped the link
- `invite_app_installed` — Invitee installed the app (deferred deep link callback)
- `invite_onboarding_started` — Invitee began invited-user onboarding
- `invite_onboarding_completed` — Invitee completed onboarding
- `invite_first_value` — Invitee reached first value moment
- `invite_accepted` — Invitee and sender connected
- `invite_prompt_shown` — Contextual trigger displayed
- `invite_prompt_dismissed` — Contextual trigger dismissed

### 7.2 iOS Client Components

| Component | Description |
|---|---|
| `InviteManager` | Singleton. Handles invite creation, deep link generation, share sheet presentation. |
| `InviteDeepLinkHandler` | Parses incoming universal links, routes to appropriate flow. |
| `InvitedUserOnboardingVC` | Condensed onboarding flow for invited users. |
| `InvitePromptManager` | Controls when/where contextual invite prompts appear. Enforces frequency rules. |
| `InviteStatusTracker` | Polls/subscribes for invite acceptance events, triggers sender notifications. |

### 7.3 Infrastructure
- **Deep linking:** Branch.io SDK or Firebase Dynamic Links (evaluate setup time vs. flexibility)
- **Push notifications:** Existing push infra; new notification type for invite acceptance
- **OG image generation:** Serverless function (e.g., Cloudflare Worker or AWS Lambda) that renders dynamic link preview images
- **Rate limiting:** Max 50 invites per user per day to prevent abuse

---

## 8. Edge Cases & Error Handling

| Scenario | Handling |
|---|---|
| Invitee already has the app installed | Deep link opens app directly, shows "[Sender] wants to connect" screen. Skip onboarding. |
| Invitee already has an account and is connected to sender | Toast: "You're already connected with [Sender]!" |
| Invite link expired (>30 days) | Landing page: "This invite has expired. Download [App] to get started." Still route to App Store. |
| Sender's account deleted/suspended | Invite link still works but without personalization. Generic onboarding. |
| Share sheet dismissed without sending | Log `invite_share_sheet_dismissed`. No toast. Invite record stays in `created` status. |
| User spams invites | Rate limit at 50/day. After limit: "You've sent a lot of invites today. Try again tomorrow." |
| Deep link attribution fails | Fall back to generic onboarding. Log for debugging. |
| No internet when tapping invite entry point | Show inline error: "Check your connection and try again." Queue invite creation for retry. |
| Invitee on Android | Link opens a mobile web page: "Thanks for your interest! [App] is currently available on iOS. We'll notify you when Android launches." Capture email. |

---

## 9. Privacy & Compliance

- **No contacts upload without explicit consent.** The invite flow uses the native iOS share sheet, which does not require contacts permission.
- If a "suggested contacts" feature is added later, it must use the Contacts framework with explicit permission and clear explanation of why.
- Invite links contain no PII — only opaque user IDs and content IDs.
- HMAC signature on links prevents enumeration/tampering.
- Comply with App Store Review Guidelines Section 5.1.1 (Data Collection and Storage) and 5.1.2 (Data Use and Sharing).
- Include invite-related data in GDPR/CCPA data export and deletion flows.

---

## 10. 4-Week Delivery Plan

### Week 1: Foundation
- [ ] Backend: Invite service API (create, resolve, accept)
- [ ] Backend: Deep link generation and resolution
- [ ] iOS: `InviteManager` and share sheet integration
- [ ] iOS: Universal link handling in `AppDelegate` / `SceneDelegate`
- [ ] Design: Finalize share message templates and link preview cards
- [ ] Set up Branch.io / Firebase Dynamic Links SDK

### Week 2: Core Flows
- [ ] iOS: Sender flow end-to-end (entry point → share sheet → toast)
- [ ] iOS: Invitee deep link routing (existing users)
- [ ] iOS: Invited user onboarding flow (condensed)
- [ ] Backend: Invite status tracking and acceptance webhook
- [ ] Backend: OG image generation for link previews
- [ ] QA: Sender flow testing across iMessage, WhatsApp, copy link

### Week 3: Polish & Contextual Triggers
- [ ] iOS: 2-3 highest-value contextual invite triggers
- [ ] iOS: `InvitePromptManager` with frequency capping
- [ ] iOS: Sender notification on invite acceptance (push + in-app)
- [ ] iOS: Deferred deep linking for new installs
- [ ] Backend: Analytics event pipeline for all invite events
- [ ] QA: Full end-to-end testing (new install → onboarding → first value)

### Week 4: Testing, Optimization & Launch
- [ ] QA: Edge case testing (expired links, existing users, no internet, rate limits)
- [ ] QA: Performance testing (link resolution latency < 200ms)
- [ ] A/B test setup: Contextual triggers on/off, message variants
- [ ] Instrument all analytics events and verify in dashboard
- [ ] App Store submission
- [ ] Staged rollout: 10% → 50% → 100% over 5 days
- [ ] Monitor: Crash rates, invite funnel metrics, support tickets

---

## 11. A/B Testing Plan

### Experiment 1: Share Message Personalization
- **Control:** Generic message ("Check out [App]!")
- **Variant:** Context-rich message ("[Sender] just [did X] on [App]!")
- **Primary metric:** Invite acceptance rate
- **Sample size:** 5,000 invites per variant

### Experiment 2: Invitee Onboarding Length
- **Control:** Standard onboarding (5-7 screens)
- **Variant:** Condensed onboarding (2-3 screens) with delayed sign-up
- **Primary metric:** Onboarding completion rate, 7-day retention
- **Sample size:** 1,000 invited users per variant

### Experiment 3: Contextual Trigger Placement
- **Control:** No contextual triggers (profile entry point only)
- **Variant:** Post-achievement + empty state triggers
- **Primary metric:** Invite send rate
- **Sample size:** 10,000 MAU per variant

---

## 12. Post-Launch Monitoring & Iteration

### Key Dashboards
1. **Invite Funnel:** Entry point tap → Share sheet open → Invite sent → Link opened → App installed → Onboarding completed → First value reached
2. **Channel Performance:** Conversion rates by share channel (iMessage vs. WhatsApp vs. copy link vs. other)
3. **Trigger Performance:** Invite send rate by entry point / contextual trigger
4. **Invitee Quality:** 7-day / 30-day retention of invited users vs. organic users

### Phase 2 Candidates (Post-Launch)
- Referral incentive program (both sender and invitee rewards)
- "Invite your contacts" feature with contacts permission
- In-app invite status page ("3 friends joined, 2 pending")
- Smart suggestions: "You and [contact] both like [activity]. Invite them?"
- Android support
- Leaderboard / social proof ("You've brought 5 friends to [App]!")

---

## 13. Summary of Tap Optimization

| User | Action | Taps |
|---|---|---|
| Sender | Trigger to invite sent | 2 (tap entry point + select contact in share sheet) |
| Invitee (new) | Link tap to first value | 2 (tap link + tap Install); first value on app open |
| Invitee (existing) | Link tap to first value | 1 (tap link; app opens to destination) |
| Sender | Notification to reconnection | 1 (tap push notification) |

The entire invite loop — from sender's intent to invitee experiencing value — is designed to complete in **4 total taps** (2 sender + 2 invitee), with the goal of making sharing feel as natural and effortless as sending a text message.
