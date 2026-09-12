---
name: m365-admin-suite
description: Unified entrypoint for the Microsoft 365 Admin Suite. Use only when the user explicitly names m365-admin-suite, with or without the $ prefix, to route and execute browser-based Microsoft 365 administration across lifecycle, helpdesk, licenses, Entra, Intune, Exchange, collaboration, security, service health, Purview, or tenant catalog work. Never route this request to m365-admin-stack, which is only for CLI/MCP stack installation and repair.
---

# Microsoft 365 Admin Suite

Act as the dispatcher and owner of the user's explicit `$m365-admin-suite` request. Select the smallest applicable suite skill, read it completely, and follow its authorization, execution, and verification rules. Do not stop after naming the selected skill; carry out the requested work with the available browser tools.

## Route the request

- Full onboarding, employee transfer, safe offboarding, or another multi-portal lifecycle process: read [m365-browser-admin](../m365-browser-admin/SKILL.md).
- Password, blocked sign-in, sessions, MFA, or named-user support: read [m365-helpdesk-admin](../m365-helpdesk-admin/SKILL.md).
- License inventory, capacity, assignment, removal, service plans, or group-based licensing: read [m365-license-admin](../m365-license-admin/SKILL.md).
- Entra roles, PIM, Conditional Access, authentication policy, named locations, or access reviews: read [m365-identity-access](../m365-identity-access/SKILL.md).
- Intune enrollment, devices, compliance, configuration, endpoint security, applications, remediation, wipe, or Autopilot: read [m365-intune-admin](../m365-intune-admin/SKILL.md).
- Exchange mailboxes, recipients, aliases, delegation, forwarding, groups, or mail flow: read [m365-exchange-admin](../m365-exchange-admin/SKILL.md).
- Teams, Microsoft 365 Groups, SharePoint, OneDrive, or routine Power Automate ownership/run work: read [m365-collaboration-admin](../m365-collaboration-admin/SKILL.md).
- Sign-ins, audit evidence, risky users, alerts, incident timeline, or read-oriented security posture: read [m365-security-audit](../m365-security-audit/SKILL.md).
- Service Health, incidents, advisories, or Message Center: read [m365-service-operations](../m365-service-operations/SKILL.md).
- Retention, sensitivity labels, DLP, content search, audit, or eDiscovery: read [m365-purview-admin](../m365-purview-admin/SKILL.md).
- Tenant profile discovery, comparison, creation, or validation: read [m365-tenant-catalog](../m365-tenant-catalog/SKILL.md).

`m365-admin-stack` is outside this routing table. Use it only when the user explicitly asks to install, repair, configure, or verify the Microsoft 365 CLI/MCP administration stack.

## Keep routing efficient

Choose one owning skill whenever possible. For a lifecycle request, `m365-browser-admin` owns the complete cross-portal workflow; do not load every domain skill separately. For a standalone domain task, load only that domain skill and the references it directs you to read.

Read a second skill only when the request contains a genuine independent domain operation that the owner does not cover. State the selected route briefly in commentary, then continue.

## Browser and tenant context

For live browser work, read [the browser operation contract](../m365-browser-admin/references/browser-operation-contract.md) unless the owning skill already directed you to it. Use the administrator's authenticated browser session, confirm the visible tenant and exact target, inspect current state, execute only the authorized scope, and verify persisted after-state.

Use `.m365-admin/tenant-catalog.yaml` when present or when the user provides a catalog path. Read only the relevant profile and verify every referenced object in the live tenant. The catalog is intended state, not additional authorization.

## Completion

Finish with the selected route, tenant and exact targets, verified changes, already-correct items, pending propagation, blockers, destructive actions, and required administrator/end-user/device steps. Never report a task as complete based only on a click or toast.
