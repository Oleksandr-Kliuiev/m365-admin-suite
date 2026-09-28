---
name: m365-admin-suite
description: "Microsoft 365 admin in Chrome: route natural-language or voice requests across domains or to an unclear specialist. Excludes CLI/MCP setup."
---

# Microsoft 365 Admin Suite

Accept spoken or typed requests without requiring skill names. Load one owning specialist and only its relevant reference; a directly selected specialist need not route here. Reuse instructions already loaded in this session.

| Request | Owner |
| --- | --- |
| Full onboarding, transfer, safe offboarding, cross-portal lifecycle | [Browser admin](../m365-browser-admin/SKILL.md) |
| Password, blocked sign-in, sessions, MFA, named-user support | [Helpdesk](../m365-helpdesk-admin/SKILL.md) |
| License inventory/capacity, assignment/removal, service plans, group licensing | [Licenses](../m365-license-admin/SKILL.md) |
| Entra roles, PIM, Conditional Access, authentication policy, access reviews | [Identity/access](../m365-identity-access/SKILL.md) |
| Enrollment, devices, policies, apps, remediation, wipe, Autopilot | [Intune](../m365-intune-admin/SKILL.md) |
| Mailboxes, recipients, aliases, delegation, forwarding, mail flow | [Exchange](../m365-exchange-admin/SKILL.md) |
| Teams, Groups, SharePoint, OneDrive, Power Automate ownership/runs | [Collaboration](../m365-collaboration-admin/SKILL.md) |
| Sign-ins, risks, alerts, activity, incident evidence, security posture | [Security audit](../m365-security-audit/SKILL.md) |
| Service Health, incidents, advisories, Message Center | [Service operations](../m365-service-operations/SKILL.md) |
| Retention, labels, DLP, content search, eDiscovery, compliance audit | [Purview](../m365-purview-admin/SKILL.md) |
| Discover, compare, create or validate reusable tenant profiles | [Tenant catalog](../m365-tenant-catalog/SKILL.md) |

The lifecycle owner covers its cross-portal workflow without loading every domain skill. Add another specialist only for an independent operation the owner does not cover. Browser, tenant, authorization, session-state and voice rules live in the shared contract linked by each specialist.

Use `m365-admin-stack` only for an explicit request to install, repair, configure or verify the CLI/MCP stack.
