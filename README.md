# Microsoft 365 Admin Suite

This Codex plugin provides focused skills for supervised Microsoft 365 administration through an already authenticated Chrome session. It accepts natural-language and voice requests and is designed for real tenant work: exact tenant and object resolution, current-state inspection, pagination, idempotent changes, production scope, and after-state verification.

## Included skills

- `m365-admin-suite`: routes requests across domains or when the owning specialist is unclear.
- `m365-browser-admin`: multi-portal onboarding, transfer, and safe offboarding.
- `m365-helpdesk-admin`: sign-in, password, session, and MFA support.
- `m365-license-admin`: license inventory, assignment, removal, and group-based licensing.
- `m365-identity-access`: Entra roles, PIM, Conditional Access, authentication, and access reviews.
- `m365-intune-admin`: devices, enrollment, policies, applications, and remediation.
- `m365-exchange-admin`: mailboxes, recipients, delegation, forwarding, and mail flow.
- `m365-collaboration-admin`: Teams, Microsoft 365 Groups, SharePoint, OneDrive, and routine Power Automate ownership.
- `m365-security-audit`: read-oriented security and audit investigations.
- `m365-service-operations`: Service Health, Message Center, and incident checks.
- `m365-purview-admin`: retention, labels, DLP, audit, and eDiscovery.
- `m365-tenant-catalog`: discovery and maintenance of private tenant profiles.

Describe the work naturally, by typing or speaking; an explicit skill name is unnecessary:

```text
Conduct a complete onboarding for a new employee.
Review this tenant's license assignments.
```

Focused domain requests select their specialist directly. The suite selects one owning specialist for cross-domain or unclear requests; the lifecycle specialist covers its complete cross-portal workflow. Load another specialist only for an independent operation outside the owner's scope. Explicit `$m365-admin-suite` invocation remains available. The unrelated `m365-admin-stack` is reserved for an explicit request to install, repair, configure, or verify CLI/MCP infrastructure.

All 12 skills install together. Their sibling links share one [Chrome contract](skills/m365-browser-admin/references/browser-operation-contract.md), read once per session and reused. Load only the selected specialist's relevant workflow. Read [navigation guidance](skills/m365-browser-admin/references/browser-navigation.md) only for an unknown route or navigation problem, and [report handling](skills/m365-browser-admin/references/reports-and-exports.md) for complete lists, reports, exports, or email.

## Tenant catalog

Copy `skills/m365-tenant-catalog/assets/tenant-catalog.example.yaml` to the administrator's working directory as `.m365-admin/tenant-catalog.yaml`, then adapt it to the tenant. Keep the real catalog private. It must contain identifiers and intended configuration, never passwords, tokens, or other credentials.

The catalog is optional. Without it, the selected skill performs read-only discovery and asks only for missing decisions that would materially change the result.

## Operating model

The administrator signs in to the required Microsoft portals, opens the intended tenant, and gives Codex the task. The selected skill reuses authenticated Chrome unless the administrator explicitly chooses another browser. It verifies the live administrator, requested tenant, and exact target; rechecks tenant and target after context changes; and inspects current state before a change. Catalogs describe intended configuration and do not replace live verification or authorization.

The skill performs routine authorized operations, verifies each persisted change, and reports completed, already-correct, pending, and blocked work. A complete lifecycle request covers ordinary reversible steps for the named user and stated profile. Privileged access, broad policy changes, deletion, device wipe, mailbox purge, and hold removal require clear authorization for the exact operation and target. Preserve data, retention, ownership, and workload dependencies throughout lifecycle work. Interactive authentication and physical-device actions remain administrator checkpoints. Reports distinguish configuration and assignment from observed provisioning, application, and testing.

Requested report emails use Outlook on the web in the same authenticated Chrome profile on Windows and macOS. The skill verifies the signed-in employee's sending mailbox and exact recipient, supports short complete reports in the body or verified file attachments, and checks Sent Items after sending once under the user's explicit authorization. See [report handling](skills/m365-browser-admin/references/reports-and-exports.md) and the [synthetic delivery scenarios](docs/outlook-report-scenarios.md).
