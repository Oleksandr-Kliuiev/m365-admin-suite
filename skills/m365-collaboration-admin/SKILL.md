---
name: m365-collaboration-admin
description: Administer Microsoft 365 collaboration services through an authenticated browser, including Teams and Microsoft 365 Group membership and ownership, Teams policies, SharePoint sites and permissions, OneDrive administrative access, and routine Power Automate flow ownership and run checks. Use for collaboration-focused requests. Do not use for Exchange recipient work, Intune deployment, or full employee lifecycle.
---

# Microsoft 365 Collaboration Admin

Resolve exact team/group ID, site URL, user UPN, flow ID, and Power Platform environment. Read [references/collaboration-operations.md](references/collaboration-operations.md) for workload distinctions and verification.

Use current authenticated portals. Confirm tenant after moving among Teams, SharePoint, Microsoft 365 admin center, and Power Automate.

Do not modify a tenant-wide sharing or global Teams policy to satisfy a single-user request unless the user explicitly requests that policy change. Before removing an owner, verify that every Team, group, site, flow, and application retains an approved owner.

Report membership source, ownership, policies, site permission source, flow connection/owner state, run outcome, propagation, and any end-user sign-in dependency.

