# `user-stories.md`

## Epic 1 – SaaS Discovery & Inventory  

| # | User Story (Connextra) | Acceptance Criteria | Complexity |
|---|------------------------|---------------------|------------|
| 1 | **As an MSP admin, I want to automatically discover every SaaS application used by my clients’ employees, so that I can maintain a complete inventory without manual data entry.** | - The system scans OAuth‑protected SaaS directories (e.g., Azure AD, Okta, Google Workspace) and lists all connected apps.<br>- Discovered apps are de‑duplicated and grouped by tenant.<br>- Each app entry shows name, vendor, last‑login date, and number of active users.<br>- Discovery runs on a configurable schedule (daily, weekly, monthly).<br>- A “Refresh Now” button triggers an on‑demand scan and shows progress. | M |
| 2 | **As a security analyst, I want to see a risk score for each discovered SaaS app, so that I can prioritize investigations.** | - Risk score is calculated from a weighted mix of data‑loss exposure, user count, and known vulnerability feeds.<br>- Scores are displayed on the inventory list with color‑coded badges (low/medium/high).<br>- Clicking a score opens a drill‑down view with the underlying factors.<br>- Scores update automatically after each discovery cycle.<br>- Ability to override the auto‑score with a manual rating. | M |
| 3 | **As a compliance officer, I want to tag SaaS apps with regulatory categories (e.g., GDPR, HIPAA), so that I can quickly filter non‑compliant services.** | - A taxonomy of regulatory tags is pre‑loaded and can be edited by admins.<br>- Tags can be applied in bulk from the inventory view or individually.<br>- Filter bar allows “Show only un‑tagged” and “Show only HIPAA‑tagged”.<br>- Export of tagged inventory to CSV/JSON includes tag metadata.<br>- Audit log records every tag addition/removal with user and timestamp. | S |
| 4 | **As an IT manager, I want to import a list of known SaaS subscriptions from a spreadsheet, so that legacy contracts are captured even if not discoverable via APIs.** | - Upload accepts .xlsx, .csv, or .json with required columns (App Name, Vendor, License Count, Expiration).<br>- System validates format and reports any rows with missing/invalid data.<br>- Imported rows merge with auto‑discovered inventory, preserving existing data where conflicts arise.<br>- Imported entries are flagged as “Manual Import” and can be edited later.<br>- Import operation is reversible via an “Undo Import” button within 24 h. | S |

---

## Epic 2 – Policy & Governance  

| # | User Story (Connextra) | Acceptance Criteria | Complexity |
|---|------------------------|---------------------|------------|
| 5 | **As an MSP policy admin, I want to define usage policies (e.g., max users, allowed regions) for each SaaS app, so that I can enforce contractual or security limits.** | - Policy editor supports numeric limits, list of allowed IP ranges, and boolean flags (e.g., “SAML‑only”).<br>- Policies can be applied at the app level, tenant level, or globally.<br>- Violations are highlighted in the inventory with a red icon.<br>- Policy changes trigger a re‑evaluation of existing usage data within 5 min.<br>- Version history is kept for each policy change. | M |
| 6 | **As a security engineer, I want the system to automatically block access to SaaS apps that violate a policy, so that risk is mitigated in real time.** | - Integration with IdP (Okta, Azure AD) to enforce Conditional Access rules.<br>- When a violation is detected, the system creates a “block” rule that denies SSO for the offending user/group.<br>- Blocked users receive an automated email with remediation steps.<br>- Admin can override or lift the block from the UI.<br>- Audit log records block creation, duration, and removal. | L |
| 7 | **As a compliance auditor, I want a “policy compliance” dashboard that shows the percentage of SaaS apps meeting their assigned policies, so that I can report on governance health.** | - Dashboard shows overall compliance % and a breakdown by tenant and policy type.<br>- Clicking a non‑compliant app drills down to the specific rule(s) violated.<br>- Time‑series chart displays compliance trend over the past 90 days.<br>- Exportable PDF/CSV report with timestamps and responsible owners.<br>- Role‑based access controls restrict who can view the dashboard. | M |

---

## Epic 3 – Alerting & Remediation  

| # | User Story (Connextra) | Acceptance Criteria | Complexity |
|---|------------------------|---------------------|------------|
| 8 | **As an IT ops lead, I want real‑time alerts (email, Slack, webhook) when a new high‑risk SaaS app is detected, so that I can act before data is exposed.** | - Alert triggers when a newly discovered app receives a risk score ≥ 8 / 10.<br>- Notification includes app name, risk factors, and a one‑click “Investigate” link.<br>- Channels configurable per tenant (email, Slack, Teams, custom webhook).<br>- Alert throttling prevents duplicate alerts for the same app within a 24 h window.<br>- Alert history view shows status (sent, acknowledged, resolved). | S |
| 9 | **As a security analyst, I want a “Remediation Playbook” that suggests concrete steps for each type of violation, so that I can resolve issues efficiently.** | - Playbooks are auto‑generated based on violation type (e.g., “exceeds user limit”, “unapproved region”).<br>- Each step includes a short description, responsible role, and an actionable button (e.g., “Reduce license count”).<br>- Playbooks can be customized per MSP or per tenant.<br>- Completion status is tracked and reflected in the compliance dashboard.<br>- PDF export of the playbook for audit purposes. | M |
| 10 | **As a manager, I want to assign remediation tickets automatically to the appropriate owner when a violation occurs, so that accountability is clear.** | - Integration with ticketing systems (Jira, ServiceNow, Asana).<br>- Ticket contains violation details, risk score, and suggested playbook steps.<br>- Owner is selected based on a mapping (e.g., app → responsible team).<br>- Ticket status syncs back to the SaaS Guard UI (open, in‑progress, resolved).<br>- SLA SLA timers are visible on the violation card. | L |

---

## Epic 4 – Reporting & Insights  

| # | User Story (Connextra) | Acceptance Criteria | Complexity |
|---|------------------------|---------------------|------------|
| 11 | **As a CFO, I want a cost‑optimization report that shows duplicate SaaS subscriptions across the organization, so that we can consolidate spend.** | - Report lists apps with > 1 active subscription per tenant.<br>- Shows total monthly cost per app and potential savings if consolidated.<br>- Includes a “Contact Vendor” button that pre‑populates an email template.<br>- Exportable to Excel with pivot‑ready formatting.<br>- Updated after each discovery cycle. | M |
| 12 | **As a product strategist, I want trend analytics that visualize SaaS adoption growth over time, so that I can forecast licensing needs.** | - Time‑series chart displays number of active users per app per month for the last 12 months.<br>- Ability to filter by tenant, app category, or risk tier.<br>- Forecast model (linear regression) projects next 6 months with confidence interval.<br>- Exportable PNG or embed code for external dashboards.<br>- Data refreshes automatically after each scheduled discovery. | S |

---  

*All stories are scoped for the **saas-visibility-guard** MVP. Complexity estimates follow the internal sizing rubric (S = ≤ 2 person‑days, M = 2‑5 person‑days, L = > 5 person‑days).*
