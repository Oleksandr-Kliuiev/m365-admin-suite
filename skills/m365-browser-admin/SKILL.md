---
name: m365-browser-admin
description: Execute end-to-end Microsoft 365 employee lifecycle workflows through an authenticated browser, especially full onboarding, employee transfer, and safe offboarding that span multiple admin portals. Use when the request crosses at least two of identity, licenses, Exchange, Teams, SharePoint, OneDrive, Intune, or Power Automate, or when the user explicitly invokes $m365-browser-admin. Do not use for a standalone domain task when a focused m365 skill applies.
---

# Microsoft 365 Browser Admin

Own the complete multi-portal workflow and keep one evidence record for the exact user. Use the administrator's authenticated browser session. Never store credentials, session tokens, tenant secrets, or temporary passwords in the skill, tenant catalog, or durable report.

## Establish context

1. Attach to the user-mentioned browser tab when present; otherwise reuse the authenticated tab for the owning portal.
2. Confirm the visible administrator, tenant, portal, and exact target. Prefer UPN and object ID over display name.
3. Inspect current state before mutation. Continue partially completed workflows idempotently; never create duplicates to compensate for uncertain state.
4. Look for `.m365-admin/tenant-catalog.yaml` in the current working directory or use a user-provided path. Read only the selected profile and relevant defaults. Treat the catalog as intended state, then verify that referenced objects exist in the live tenant.
5. Read [references/browser-operation-contract.md](references/browser-operation-contract.md) for navigation, pagination, mutation, and verification rules.

## Choose the lifecycle workflow

- For a new employee, read [references/onboarding.md](references/onboarding.md).
- For a departing employee, read [references/offboarding.md](references/offboarding.md).
- For department, manager, location, or responsibility changes, read [references/employee-transfer.md](references/employee-transfer.md).

Load only the workflow reference required by the request. Focused sibling skills are independently selectable for standalone work; do not load all of them as part of lifecycle orchestration.

## Authorization

A request for complete onboarding, transfer, or safe offboarding authorizes the ordinary reversible steps of that workflow for the named user and stated profile. It does not authorize unrelated tenant-wide changes, privileged-role assignment, Conditional Access exclusions, permanent user deletion, mailbox purge, device wipe, or Autopilot deletion.

Production groups, rings, named targets, `All users`, and `All devices` are valid when they match the explicit request or verified tenant profile. Do not impose a pilot stage. Before a broad assignment, verify exact scope, exclusions, filters, deadlines, restart behavior, and a viable rollback.

## Finish

Report the tenant, exact target, verified changes, already-correct items, pending propagation, blocked steps, affected licenses/groups/workloads/devices, and any required first-login or physical-device action. Use `Configured`, `Assigned`, `Provisioned`, `Applied`, and `Tested` precisely; never call an unobserved state working.

