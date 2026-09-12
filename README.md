# Microsoft 365 Admin Suite

This Codex plugin provides focused skills for supervised Microsoft 365 administration through an already authenticated browser session. It is designed for real tenant work: exact object resolution, current-state inspection, pagination, idempotent changes, production scope, and after-state verification.

## Included skills

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

Codex can select a focused skill from a natural-language request. Explicit invocation remains available when an administrator wants to lock the route, for example:

```text
$m365-browser-admin conduct a complete onboarding for a new employee
```

## Tenant catalog

Copy `skills/m365-tenant-catalog/assets/tenant-catalog.example.yaml` to the administrator's working directory as `.m365-admin/tenant-catalog.yaml`, then adapt it to the tenant. Keep the real catalog private. It must contain identifiers and intended configuration, never passwords, tokens, or other credentials.

The catalog is optional. Without it, the selected skill performs read-only discovery and asks only for missing decisions that would materially change the result.

## Operating model

The administrator signs in to the required Microsoft portals, opens the intended tenant, and gives Codex the task. The skill performs routine authorized operations, verifies each persisted change, and reports completed, already-correct, pending, and blocked work. Interactive authentication, physical-device actions, and unrequested irreversible actions remain administrator checkpoints.

