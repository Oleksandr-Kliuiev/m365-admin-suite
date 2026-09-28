---
name: m365-collaboration-admin
description: "Microsoft 365 collaboration in Chrome: Teams, Groups, SharePoint, OneDrive and Power Automate ownership, membership, policies, permissions and run checks."
---

# Microsoft 365 Collaboration Admin

Read the [shared Chrome contract](../m365-browser-admin/references/browser-operation-contract.md) only if not already loaded; reuse it for this session.

Resolve exact team/group ID, site URL, user UPN, flow ID, and Power Platform environment. Read [references/collaboration-operations.md](references/collaboration-operations.md) for workload distinctions and verification.

Use current authenticated portals. Confirm tenant after moving among Teams, SharePoint, Microsoft 365 admin center, and Power Automate.

Do not modify a tenant-wide sharing or global Teams policy to satisfy a single-user request unless the user explicitly requests that policy change. Before removing an owner, verify that every Team, group, site, flow, and application retains an approved owner.

Report membership source, ownership, policies, site permission source, flow connection/owner state, run outcome, propagation, and any end-user sign-in dependency.
