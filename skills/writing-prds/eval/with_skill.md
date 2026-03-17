# PRD Pack: Saved Views for Analytics Dashboard

---

## 0) Context Snapshot

- **Product:** Analytics Dashboard (B2B SaaS)
- **Target user/customer segment:** Admin users (workspace/account administrators who configure, monitor, and report on team-level analytics)
- **Problem statement:** Admins repeatedly rebuild the same filtered, segmented, and date-ranged dashboard configurations every time they open the analytics dashboard. This wastes 5-15 minutes per session, introduces inconsistency in recurring reports, and discourages deeper exploration of data.
- **Why now:** Customer interviews and support tickets (top-10 feature request for Q3/Q4) indicate that admin users are exporting raw data to spreadsheets to maintain "saved" views, which creates data freshness problems, security risks (data outside the platform), and churn risk among power users. Two key enterprise prospects have flagged "saved views" as a blocker to contract expansion.
- **Decision to make (and by when):** Approve scope and requirements for Saved Views v1 and begin engineering sprint planning within 2 weeks.
- **DRI / approver:** Product Manager (DRI); VP Product (approver for scope and launch)
- **Constraints:**
  - Timeline: Target beta in 6 weeks, GA in 10 weeks
  - Platform: Web only (v1); mobile read-only is out of scope
  - Dependencies: Existing filter/segment infrastructure, permissions system, analytics event pipeline
  - Policy/legal: Saved views must respect existing role-based access controls (RBAC); no data leakage across workspaces
- **Success metrics:**
  - M1: 40%+ of active admins create at least one saved view within 30 days of GA
  - M2: 25% reduction in average "time-to-first-insight" (measured from dashboard open to first interaction with a widget) for admins with saved views vs. without
  - M3: 15% reduction in CSV/data export volume among admins who adopt saved views
- **Guardrails:**
  - Gd1: Dashboard page load time must not increase by more than 200ms at p95 when loading a saved view vs. default
  - Gd2: No cross-workspace data exposure through saved view sharing
  - Gd3: Saved view CRUD operations must succeed at 99.5%+ reliability
  - Gd4: Support ticket volume related to "lost configurations" must not increase post-launch
- **Stakeholders/reviewers:** Engineering Lead, Design Lead, Data/Analytics Lead, Customer Success Lead, Security/Compliance reviewer

---

## 1) Artifact Selection

| Artifact | Include? | Why | Audience | Owner | Due date |
|---|---|---|---|---|---|
| PR/FAQ | Y | Need narrative alignment with leadership on customer value and "why now" before committing engineering resources | VP Product, leadership, CS | Product Manager | Week 1 |
| PRD | Y | Engineering and design need execution-ready requirements, acceptance criteria, and rollout plan | Engineering, Design, QA, Data | Product Manager | Week 2 |
| Prompt Set (AI) | N | Not an AI feature | - | - | - |
| Eval Spec (AI) | N | Not an AI feature | - | - | - |

**Rationale:** This is a core platform feature (not AI), so Prompt Set and Eval Spec are not needed. The PR/FAQ is included because the feature has been requested by multiple stakeholders with different mental models of what "saved views" means, and we need narrative alignment before locking requirements.

---

## 2) PR/FAQ: Saved Views for Analytics Dashboard

### Press Release

- **Release date:** 2026-05-15 (hypothetical)
- **Headline:** Analytics Dashboard Now Lets Admins Save, Share, and Instantly Reload Their Custom Views
- **Summary:** Admin users of the Analytics Dashboard can now save any combination of filters, segments, date ranges, and widget layouts as a named "Saved View" and reload it in one click. Saved views can be set as personal defaults or shared with other admins in the workspace, eliminating the repetitive configuration work that wastes hours each week.
- **Problem today:** Admins spend 5-15 minutes per session manually re-applying the same filters, segments, and date ranges every time they open the dashboard. Many resort to exporting data to spreadsheets to maintain consistent "views," which creates stale data, security exposure, and frustration. In our Q3 NPS survey, "I wish I could save my dashboard setup" was the #1 verbatim comment among admin users. Two enterprise expansion deals have specifically cited this gap.
- **Solution:** Saved Views lets admins capture their current dashboard state -- including all active filters, segments, date range, sort order, and visible widgets -- as a named, reusable view. Admins can create multiple saved views, set a personal default, and optionally share views with other admins in their workspace. Loading a saved view restores the full configuration instantly.
- **Customer quote:** "I check the same three configurations every Monday morning. It used to take me 10 minutes of clicking around before I could even start analyzing. Now I just click 'Monday Standup View' and I'm there in a second." -- Sarah, Ops Admin at a mid-market SaaS company
- **Company/PM quote:** "Saved Views is the most-requested feature from our admin users. It's a quality-of-life improvement that directly reduces the friction between opening the dashboard and getting to an insight. We expect it to meaningfully improve daily active usage and reduce the data export workaround that concerns our security team." -- Product Manager
- **How it works (high level):**
  - Click "Save View" from any configured dashboard state to capture filters, segments, date range, sort order, and visible widgets
  - Name the view and optionally add a description
  - Access saved views from a persistent sidebar or dropdown on the dashboard
  - Set any saved view as your personal default (loads automatically on dashboard open)
  - Share a saved view with other admins in the same workspace (read-only; recipients can clone-and-edit)
  - Edit, rename, or delete your saved views at any time
- **Who it's for / who it's not for:**
  - **For:** Admin users who access the analytics dashboard regularly and repeatedly use the same configurations
  - **Not for:** Viewer-role users (v1 is admin-only); users who need pixel-perfect scheduled reports (that is a separate "Scheduled Reports" feature); users who want to save views across different dashboards (v1 is per-dashboard)
- **Pricing/packaging:** Included in all plans that have Analytics Dashboard access. No additional cost.

### FAQ

**1) Who is the target customer/user?**
Admin users (workspace administrators) who use the Analytics Dashboard at least weekly. Based on usage data, this is approximately 60% of all admin accounts. The primary persona is an Ops/Growth admin who checks the same filtered views during recurring team rituals (standups, weekly reviews, monthly reporting).

**2) What's the core user journey?**
Admin opens dashboard -> applies filters/segments/date range -> clicks "Save View" -> names the view -> next session, selects saved view from sidebar -> dashboard instantly loads with the saved configuration. Optional: admin shares the view with a teammate, who sees it in their shared views list.

**3) Why should we build this now?**
Three converging signals: (a) "Save my dashboard" is the #1 feature request in admin NPS verbatims for two consecutive quarters; (b) two enterprise expansion deals worth $180K+ ARR combined are partially blocked on this capability; (c) the CSV-export workaround is creating security exposure that our compliance team has flagged.

**4) What are the top alternatives/workarounds today?**
- Manually re-applying filters each session (slow, error-prone)
- Exporting to CSV/spreadsheet and building saved views offline (stale data, security risk)
- Bookmarking URLs with query parameters (fragile; breaks when filter schema changes)
- Asking engineering for custom dashboard presets (does not scale)

**5) What's out of scope for v1?**
- Cross-dashboard saved views (each view is scoped to one dashboard)
- Viewer-role access (admin-only in v1)
- Scheduled auto-refresh or email delivery of saved views
- Mobile-native saved views (web only; mobile is read-only backlog item)
- Widget layout customization beyond visibility toggles (drag-and-drop rearrangement is a separate initiative)
- Public/external sharing (saved views are workspace-internal only)

**6) What could go wrong (trust, safety, privacy, reliability)?**
- **Data leakage:** A saved view could inadvertently expose data across workspaces if RBAC is not enforced at load time. Mitigation: views are workspace-scoped and filter results are always re-evaluated against the viewer's current permissions at load time.
- **Stale views:** Saved views referencing deleted filters/segments could break. Mitigation: graceful degradation with a clear error message and a prompt to update.
- **Performance:** Loading a complex saved view could be slower than default. Mitigation: p95 latency guardrail of +200ms max.
- **Storage bloat:** Unrestricted view creation could strain storage. Mitigation: per-user limit of 50 saved views per dashboard (configurable).

**7) How will we measure success and adoption?**
- Adoption: % of active admins who create at least 1 saved view within 30 days (target: 40%)
- Efficiency: reduction in time-to-first-insight for saved-view users vs. non-users (target: 25%)
- Workaround reduction: decrease in CSV export volume among adopters (target: 15%)
- Guardrails: p95 load time delta, cross-workspace data access incidents (must be zero), CRUD reliability (99.5%+)

**8) What are the major dependencies and risks?**
- Dependency on existing filter/segment infrastructure (must support serialization/deserialization of current filter state)
- Dependency on RBAC/permissions system (must enforce at view-load time, not just view-creation time)
- Risk: filter schema migrations could break existing saved views; need a migration/versioning strategy
- Risk: if adoption is low, the shared-views feature adds complexity without proportional value; plan to measure and potentially simplify

---

## 3) PRD: Saved Views for Analytics Dashboard

### 3.1 Overview
- **Title:** Saved Views for Analytics Dashboard
- **Author:** Product Manager
- **Last updated:** 2026-03-17
- **Status:** Draft
- **Links:** PR/FAQ (above), Design prototype (TBD), Research: Q3/Q4 NPS verbatims, Analytics: admin session duration data, Tickets: JIRA epic (TBD)

### 3.2 Problem + Why Now

**Problem statement:**
Admin users of the Analytics Dashboard cannot persist their configured dashboard state (filters, segments, date ranges, widget visibility). Every session requires manual reconstruction of the same views, wasting 5-15 minutes per session and discouraging regular engagement with the dashboard.

**User pain evidence:**
- #1 feature request in admin NPS verbatims for two consecutive quarters (Q3 and Q4)
- 34% of admin support tickets tagged "dashboard" mention "save," "remember," or "keep my filters"
- Usage data shows 28% of admin sessions include applying 3+ filters, suggesting complex configurations are common
- Two enterprise expansion deals ($180K+ combined ARR) cite saved views as a requirement
- Security team flagged that 15% of admins export CSV weekly as a workaround, creating data-outside-platform risk

**Why now:**
- Revenue impact: enterprise deal pipeline blocked
- Security urgency: CSV export workaround flagged by compliance
- Competitive gap: 3 of 5 direct competitors shipped saved/bookmarked views in the last 12 months
- Technical readiness: recent filter infrastructure refactor makes serialization feasible without major rearchitecture

### 3.3 Goals, Non-Goals, Out of Scope

**Goals (measurable)**
- G1: Enable admins to save, name, load, edit, and delete dashboard view configurations (filters, segments, date range, widget visibility) with one-click access
- G2: Allow admins to set a personal default saved view per dashboard
- G3: Allow admins to share saved views (read-only) with other admins in the same workspace
- G4: Achieve 40%+ adoption (at least 1 saved view created) among active admins within 30 days of GA

**Non-goals (important, but not for this effort)**
- NG1: Widget drag-and-drop layout customization (separate initiative; saved views captures visibility, not position)
- NG2: Scheduled email delivery of saved view snapshots (future "Scheduled Reports" feature)
- NG3: Viewer-role access to saved views (will evaluate after admin adoption data is in)
- NG4: AI-suggested views based on usage patterns (potential future enhancement)

**Out of scope (explicit exclusions)**
- OOS1: Cross-dashboard saved views (each view is scoped to a single dashboard)
- OOS2: Mobile-native saved view management (web only; mobile can render shared links read-only as a fast-follow)
- OOS3: Public or external sharing of saved views (workspace-internal only)
- OOS4: Version history or undo for saved view edits
- OOS5: Saved views for non-dashboard pages (e.g., user management, billing)

### 3.4 Users + Use Cases

**Primary persona:**
Admin user (workspace administrator) who accesses the Analytics Dashboard 3+ times per week. Typically an Ops lead, Growth PM, or Customer Success manager responsible for recurring reporting and team-level analytics reviews.

**Job to be done:**
"When I open the analytics dashboard, I want to instantly see the data configuration I care about so that I can get to insights without re-doing setup work."

**Primary use case (happy path):**
1. Admin opens dashboard, applies filters (e.g., date range: last 7 days, segment: enterprise accounts, region: North America)
2. Admin clicks "Save View" button in the toolbar
3. A dialog appears; admin names the view "Weekly Enterprise NA Review" and optionally adds a description
4. View appears in the Saved Views sidebar/dropdown
5. Next session: admin opens dashboard, selects "Weekly Enterprise NA Review" from sidebar
6. Dashboard loads with the saved configuration applied; admin begins analysis immediately

**Top edge cases:**
- Admin saves a view referencing a filter/segment that is later deleted or renamed
- Admin tries to load a shared view but lacks permission to one of the underlying data segments
- Admin reaches the per-user saved view limit (50)
- Two admins independently save views with the same name
- Admin shares a view; recipient already has a personal view with the same name
- Admin's default view references a widget that has been deprecated or removed

**Permissions/roles assumptions:**
- Only admin-role users can create, edit, delete, and share saved views in v1
- Shared views are read-only to recipients; recipients can "clone" to their own saved views to modify
- Saved view loading always re-evaluates data permissions at load time (no stale permission grants)
- Workspace isolation: saved views are invisible and inaccessible across workspace boundaries

### 3.5 Proposed Solution (High Level)

**Summary:**
Add a "Saved Views" feature to the Analytics Dashboard that allows admin users to capture, name, manage, and share their dashboard configurations. The feature consists of: (1) a Save View action in the dashboard toolbar, (2) a Saved Views sidebar for quick access, (3) a personal default view setting, and (4) workspace-level sharing (read-only with clone-to-edit).

**Key product decisions:**

- **Decision 1: Sidebar vs. dropdown for saved view access.**
  Recommendation: Persistent sidebar (collapsible) rather than a dropdown. Rationale: admins often switch between views during a session; a sidebar provides one-click access without interrupting the dashboard context. The sidebar collapses to an icon rail on smaller screens.

- **Decision 2: Shared views are read-only with clone-to-edit.**
  Rationale: Allowing direct editing of shared views creates conflict and confusion about ownership. Read-only sharing with a "Clone to My Views" action preserves the sharer's intent while giving recipients full flexibility.

- **Decision 3: Saved view state includes filters, segments, date range, and widget visibility -- but NOT widget position or size.**
  Rationale: Widget layout customization is a separate initiative. Including only visibility keeps the serialization model simple and avoids coupling to future layout changes.

- **Decision 4: Per-user limit of 50 saved views per dashboard.**
  Rationale: Prevents storage bloat while being generous enough for power users. The limit is configurable at the workspace level for enterprise plans.

### 3.6 Requirements (R1...Rn)

| ID | Requirement (Priority) | Acceptance Criteria | Edge Cases / Notes |
|---|---|---|---|
| R1 | Admin must be able to save the current dashboard state as a named view (MUST) | Clicking "Save View" captures: active filters, segments, date range, sort order, and widget visibility. A name (1-100 chars) is required. Description is optional (0-500 chars). The view appears in the sidebar immediately after save. | Duplicate names are allowed (per user); system appends a disambiguation indicator in the UI. Saving with no active filters creates a "clean default" view. |
| R2 | Admin must be able to load a saved view with one click (MUST) | Selecting a saved view from the sidebar applies all saved configuration within 1 second (p95). The dashboard reflects the saved state fully. The URL updates to include the view identifier for bookmarkability. | If a saved filter/segment has been deleted, show an inline warning ("Filter 'X' no longer exists") and load remaining valid configuration. Do not block the entire view load. |
| R3 | Admin must be able to edit a saved view's name, description, and configuration (MUST) | "Update View" overwrites the saved state with the current dashboard configuration. "Rename" allows changing name/description without altering the saved configuration. Both actions provide confirmation feedback. | Editing a shared view updates it for all recipients. Show a warning: "This view is shared with N admins. Changes will be visible to them." |
| R4 | Admin must be able to delete a saved view (MUST) | Deletion requires confirmation ("Delete 'View Name'? This cannot be undone."). If the view is shared, warn that recipients will lose access. If the view is the user's default, prompt to select a new default or revert to system default. | Deletion is soft-delete for 30 days (backend) to allow recovery via support, but the view is immediately removed from the UI. |
| R5 | Admin must be able to set one saved view as their personal default per dashboard (MUST) | When a default is set, opening the dashboard loads the default view automatically instead of the system default. A visual indicator (star icon or "Default" badge) marks the default view in the sidebar. Only one default per dashboard per user. | If the default view's configuration becomes partially invalid (deleted filter), load with graceful degradation (see R2 edge case) and surface a prompt to update or change default. |
| R6 | Admin must be able to share a saved view with other admins in the same workspace (SHOULD) | "Share" action generates a workspace-scoped link and/or adds the view to a "Shared with me" section in recipients' sidebars. Shared views are read-only. Recipients see the sharer's name and a "Clone to My Views" action. | Sharing across workspaces is blocked. Recipient who lacks data-level permissions to a segment in the view sees the view with that segment grayed out and a tooltip explaining the restriction. |
| R7 | Admin must be able to clone a shared view to their personal saved views (SHOULD) | "Clone to My Views" creates a personal copy that the admin can rename, edit, and delete independently. The clone is disconnected from the original (future edits to the original do not propagate). | Clone counts toward the recipient's per-user saved view limit. If at limit, show a message: "You've reached the limit of 50 saved views. Delete an existing view to clone this one." |
| R8 | The Saved Views sidebar must be collapsible and not obstruct the dashboard (MUST) | Sidebar defaults to expanded on screens >= 1280px wide, collapsed to an icon rail on smaller screens. User's collapse/expand preference is persisted per browser session. | Keyboard shortcut (e.g., Cmd/Ctrl+Shift+V) toggles the sidebar. Sidebar does not overlay dashboard content when expanded; dashboard reflows. |
| R9 | Saved view CRUD operations must have 99.5%+ success rate and complete within 500ms (p95) (MUST) | Server-side CRUD endpoints respond within 500ms at p95 under normal load. Failed operations show a retry-able error toast with the specific failure reason. | Under degraded conditions (API latency spike), queue the save operation client-side and retry with exponential backoff (max 3 retries). Show "Saving..." state. |
| R10 | Dashboard load time with a saved view must not exceed baseline + 200ms at p95 (MUST) | Performance benchmark: measure p95 dashboard load time with and without a saved view across 1K sessions. Delta must be <= 200ms. | If a saved view has many filters, the system must apply them in a single batch request, not sequentially. |
| R11 | Saved views must respect workspace isolation and RBAC at all times (MUST) | A saved view is accessible only within the workspace where it was created. Data permissions are re-evaluated at view-load time, not cached from creation time. Cross-workspace API requests return 403. | Audit log: every saved view creation, share, and deletion is logged with actor, timestamp, workspace ID, and view ID for compliance. |
| R12 | The system should handle saved views referencing deprecated or removed dashboard widgets gracefully (SHOULD) | If a widget referenced in a saved view no longer exists, skip it silently and show a non-blocking notification: "Widget 'X' is no longer available and was removed from this view." | Do not prevent view loading. Auto-update the saved view configuration to remove the defunct widget reference after the admin acknowledges the notification. |
| R13 | Admin could be able to reorder saved views in the sidebar via drag-and-drop (COULD) | Drag-and-drop reordering in the sidebar persists the custom order. Default sort is creation date (newest first) if no custom order is set. | If not included in v1, the sidebar sorts by creation date with the default view pinned at the top. |

### 3.7 UX Flows / States

**Entry points:**
- Dashboard toolbar: "Save View" button (always visible when dashboard has at least one active filter/segment, or via overflow menu when no filters are active)
- Saved Views sidebar: persistent on the left side of the dashboard (collapsible)
- Dashboard URL: direct link to a specific saved view (e.g., `/dashboard/analytics?view=abc123`)

**Happy path (save + load):**
1. Admin is on the Analytics Dashboard with filters applied
2. Admin clicks "Save View" in the toolbar
3. Save dialog appears: name field (required), description field (optional), "Set as default" checkbox
4. Admin enters name, clicks "Save"
5. Success toast: "View saved." View appears in the sidebar immediately
6. [Next session] Admin opens dashboard; if a default is set, it loads automatically; otherwise admin selects a view from the sidebar
7. Dashboard transitions to the saved state with a brief loading indicator (< 1s)

**Happy path (share):**
1. Admin hovers over a saved view in the sidebar, clicks the share icon
2. Share dialog: "Share with workspace admins" toggle (on/off). When on, view appears in all workspace admins' "Shared with me" section
3. Admin confirms; success toast: "View shared with workspace admins."
4. Recipient opens dashboard; "Shared with me" section shows the view with sharer's name
5. Recipient clicks the shared view; dashboard loads the configuration (RBAC enforced)
6. Recipient clicks "Clone to My Views" to make a personal editable copy

**Error states:**
- **Save failure (network/server):** Toast: "Couldn't save view. Please try again." Retry button in toast. Client-side retry with backoff.
- **Deleted filter in saved view:** Inline warning banner at top of dashboard: "Filter 'X' no longer exists and was skipped. Update this view to remove it." View loads with remaining valid configuration.
- **Permission denied on shared view data:** Segments the recipient lacks access to are grayed out with tooltip: "You don't have access to this segment. Contact your workspace admin."
- **View limit reached:** Dialog when trying to save/clone: "You've reached the limit of 50 saved views for this dashboard. Delete an existing view to save a new one." Link to manage views.
- **Empty state (no saved views):** Sidebar shows: "No saved views yet. Apply filters and click 'Save View' to get started." with a subtle illustration and a link to documentation.

**Loading/performance expectations:**
- Save/edit/delete operations: < 500ms (p95) with optimistic UI update
- View load (applying saved configuration): < 1 second (p95), total dashboard load time stays within baseline + 200ms (p95)
- Sidebar render: instantaneous (views list is loaded with the dashboard page)

**Accessibility considerations:**
- All sidebar interactions (select, rename, delete, share, reorder) are keyboard-navigable
- Screen reader announcements for: view saved, view loaded, view deleted, share status changes
- Color contrast and focus indicators meet WCAG 2.1 AA
- Drag-and-drop reordering (if included) has a keyboard alternative (move up/down buttons)

### 3.8 Metrics + Instrumentation

**Success metrics**

| ID | Metric | Definition | Target |
|---|---|---|---|
| M1 | Adoption rate | % of active admins (7-day active) who create >= 1 saved view within 30 days of GA | >= 40% |
| M2 | Time-to-first-insight reduction | Median time from dashboard open to first widget interaction, saved-view users vs. non-users | >= 25% reduction |
| M3 | Export reduction | % change in CSV export events per admin per week, comparing pre-launch to 30 days post-GA, among saved-view adopters | >= 15% reduction |

**Guardrails**

| ID | Guardrail | Definition | Threshold |
|---|---|---|---|
| Gd1 | Load time delta | p95 dashboard load time (with saved view) minus p95 dashboard load time (without saved view) | <= 200ms |
| Gd2 | Cross-workspace data exposure | Number of incidents where a saved view exposed data outside its workspace | 0 (zero tolerance) |
| Gd3 | CRUD reliability | Success rate of saved view create/read/update/delete operations | >= 99.5% |
| Gd4 | Support ticket regression | Weekly support tickets tagged "dashboard" + "lost configuration" or "saved views" | No increase vs. pre-launch baseline |

**Instrumentation plan**

| Metric | Definition | Data Source | Event/Table Needed | Owner | Cadence |
|---|---|---|---|---|---|
| M1: Adoption rate | Count distinct admins with >= 1 `saved_view.created` event / count active admins | Event pipeline | `saved_view.created` (user_id, workspace_id, dashboard_id, view_id, timestamp) | Data/Analytics Lead | Weekly dashboard, monthly review |
| M2: Time-to-first-insight | Timestamp delta between `dashboard.opened` and first `widget.interacted` event, segmented by has_saved_view | Event pipeline | `dashboard.opened` (user_id, view_id_loaded, timestamp), `widget.interacted` (user_id, widget_id, timestamp) | Data/Analytics Lead | Weekly dashboard |
| M3: Export reduction | Count of `data.exported` events per admin per week, pre vs. post, segmented by saved_view_adopter | Event pipeline | Existing `data.exported` event + segment by `saved_view_adopter` flag | Data/Analytics Lead | Weekly dashboard |
| Gd1: Load time delta | p95 of `dashboard.loaded` duration, segmented by view_type (saved vs. default) | APM / RUM | `dashboard.loaded` (user_id, view_type, duration_ms, timestamp) | Engineering Lead | Real-time alert + weekly review |
| Gd2: Cross-workspace exposure | Count of 403 responses on `saved_view.load` where workspace_id mismatch detected | Server logs | `saved_view.load` with workspace validation logging | Security/Compliance | Real-time alert (PagerDuty) |
| Gd3: CRUD reliability | Success / (success + failure) for saved_view API endpoints | APM | HTTP status codes on `/api/saved-views/*` endpoints | Engineering Lead | Real-time alert + weekly review |
| Gd4: Support ticket regression | Count of tickets tagged "dashboard" + ("lost config" or "saved views") per week | Support ticketing system (Zendesk/Intercom) | Tag taxonomy update needed | Customer Success Lead | Weekly review |

### 3.9 Rollout + Launch Plan

**Launch tiers:**

| Tier | Audience | Duration | Criteria to advance |
|---|---|---|---|
| Internal dogfood | Internal team admins (all workspaces) | 1 week | No P0/P1 bugs; CRUD reliability >= 99.5%; load time delta <= 200ms |
| Closed beta | 20 selected customer workspaces (mix of SMB + enterprise, including the 2 blocked deals) | 2 weeks | Adoption >= 30% among beta admins; no cross-workspace incidents; NPS/CSAT feedback is neutral-to-positive |
| GA (phased rollout) | 10% -> 25% -> 50% -> 100% of all workspaces with admin users | 3 weeks (ramp over 3 phases) | Each phase: guardrails hold; no P0 bugs; support ticket volume stable |

**Target dates (hypothetical):**
- Internal dogfood: Week 7 (6 weeks build + 1 week internal)
- Closed beta: Weeks 8-9
- GA ramp: Weeks 10-12
- Full GA: Week 12

**Eligibility:**
- v1: Admin-role users on workspaces with Analytics Dashboard access (all plans)
- Viewer-role users: excluded from v1 (see NG3)

**Customer-facing communications:**
- In-app: Tooltip/badge on "Save View" button during first session post-rollout; onboarding nudge for admins who apply 3+ filters without saving
- Help center: New article "How to use Saved Views" with screenshots and FAQ
- Changelog: Entry in product changelog / release notes
- Email: Feature announcement to admin contacts of beta + GA workspaces
- Sales enablement: One-pager for account executives highlighting saved views for pipeline conversations

**Rollback plan:**
- Feature flag: Saved Views is behind a feature flag (`saved_views_enabled`) that can be toggled per workspace or globally
- Rollback trigger: Any of the following within 48 hours of a rollout phase:
  - Cross-workspace data exposure incident (immediate full rollback)
  - P95 load time delta > 500ms (pause rollout, investigate)
  - CRUD reliability < 99% (pause rollout, investigate)
  - P0 bug with no hotfix in 24 hours (pause rollout)
- Rollback action: Disable feature flag; saved views are hidden from UI but data is preserved in the database; re-enable after fix
- Communication: In-app banner for affected users: "Saved Views is temporarily unavailable while we address an issue. Your saved views are safe and will be restored."

### 3.10 Risks / Open Questions / Next Steps

**Risks**

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Filter schema migration breaks existing saved views | Medium | High | Implement a saved view schema version field; add a migration script that runs on schema changes and updates or flags incompatible views. Test with 10K synthetic saved views before GA. |
| Low adoption if discoverability is poor | Medium | Medium | In-app nudges for admins applying 3+ filters; onboarding tooltip; sidebar is visible by default. Measure funnel: filter applied -> save prompt shown -> save completed. |
| Performance degradation on dashboards with many complex saved views | Low | High | Per-user limit of 50 views per dashboard; batch filter application; load test with max views. Monitor p95 load time continuously. |
| Sharing feature adds complexity but low usage | Medium | Low | Track sharing adoption separately. If < 10% of saved views are shared after 60 days, consider simplifying or deprioritizing share-related enhancements. |
| RBAC enforcement gaps during view sharing | Low | Critical | Security review of sharing flow before beta. Penetration test for cross-workspace access. Audit logging from day 1. |

**Open questions**

1. **Limit configurability:** Should the 50-view-per-dashboard limit be configurable per plan tier (e.g., 20 for free, 50 for pro, unlimited for enterprise)? Needs pricing/packaging input.
2. **Shared view notifications:** Should recipients get an in-app notification when a view is shared with them, or is the sidebar presence sufficient? Needs design input.
3. **Filter schema versioning strategy:** What is the exact serialization format for saved view state, and how will we handle backwards compatibility when filter types change? Needs engineering architecture decision.
4. **Analytics attribution:** Should loading a saved view count as a "dashboard open" for existing usage metrics, or should it be a distinct event? Needs data team alignment to avoid inflating existing metrics.
5. **Viewer-role timeline:** When should we evaluate extending saved views to viewer-role users? Should we commit to a target date or wait for adoption data?

**Next steps**

1. **[PM] Week 1:** Circulate PR/FAQ + PRD for stakeholder review; schedule 30-min review with VP Product, Engineering Lead, and Design Lead
2. **[Design] Weeks 1-2:** Create high-fidelity mockups for save dialog, sidebar, share flow, and error states; user test with 3-5 admins
3. **[Engineering] Week 2:** Architecture review -- define saved view data model, serialization format, API contracts, and migration strategy; estimate effort
4. **[Engineering] Week 2:** Set up feature flag infrastructure and performance benchmarking baseline
5. **[Data] Week 2:** Instrument new events (`saved_view.created`, `saved_view.loaded`, `saved_view.shared`, `saved_view.deleted`) and create monitoring dashboard
6. **[Security] Week 3:** Review RBAC enforcement in sharing flow; penetration test plan for cross-workspace isolation
7. **[PM] Week 3:** Finalize scope based on engineering estimates; resolve open questions; update PRD status to "Approved"
8. **[All] Week 7:** Begin internal dogfood; daily bug triage
9. **[PM + CS] Week 8:** Begin closed beta; set up feedback collection channel with beta customers

---

## Quality Gate: Self-Assessment

### Checklist

- [x] **Narrative:** Problem, user, and "why now" are clear in plain language
- [x] **Scope:** Goals, non-goals, and out-of-scope items are explicit
- [x] **Requirements:** Numbered R1-R13 with acceptance criteria and priority (must/should/could)
- [x] **Metrics:** Each goal has success metrics; guardrails are defined with thresholds
- [x] **Measurement:** Each metric has an owner, data source, and cadence
- [x] **Rollout:** Launch tiers, eligibility, and rollback plan are included
- [x] **Decision clarity:** DRI, approver, and open questions are explicit
- [x] **Craft:** Consistent terminology, structured sections, minimal fluff
- [x] **Safety:** No secrets/credentials; RBAC and workspace isolation addressed throughout
- [x] **PR/FAQ:** Customer-readable press release, concrete "how it works," plausible date, comprehensive FAQs
- [x] **Risks / Open questions / Next steps:** All three sections present with specifics

### Rubric Scores

| Dimension | Score | Rationale |
|---|---|---|
| 1) Customer narrative clarity | 4 | Problem is specific with supporting evidence (NPS data, deal blockers, export workaround); "why now" has three converging signals; a non-PM could summarize the value prop |
| 2) Scope boundaries | 5 | Goals, non-goals, and out-of-scope items are explicit with tradeoff rationale; dependencies and assumptions are listed; NG items explain "why not now" |
| 3) Requirements quality | 4 | 13 numbered requirements with acceptance criteria, priority labels, and edge cases; requirements describe outcomes not implementations; maps to goals |
| 4) Metrics + measurement readiness | 4 | Success metrics and guardrails have defined thresholds, data sources, owners, and cadence; instrumentation plan is a detailed table with specific events |
| 5) Rollout + risk management | 4 | Three-tier rollout with go/no-go criteria; rollback triggers and actions are specific; feature flag strategy included |
| 6) AI quality | N/A | Not an AI feature |
| 7) Document craft | 4 | Consistent terminology; clear ownership; structured sections that stand alone without a meeting; next steps have owners and timelines |

**Overall: All dimensions >= 4. Document is ready for circulation.**
