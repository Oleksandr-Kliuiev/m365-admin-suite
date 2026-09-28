---
name: m365-browser-admin
description: "Microsoft 365 employee onboarding, transfer and offboarding across admin portals in authenticated Chrome; own the complete lifecycle workflow."
---

# Microsoft 365 Browser Admin

Own the complete lifecycle workflow and one evidence record for the exact user. For standalone domain work, use its focused specialist.

Read the [shared Chrome contract](references/browser-operation-contract.md) only if not already loaded. Inspect live current state and resume partial work idempotently. Use a provided catalog path or `.m365-admin/tenant-catalog.yaml` when present; read only the selected profile/defaults and verify its objects live.

Read only the requested workflow:

- New employee: [onboarding](references/onboarding.md).
- Departing employee: [offboarding](references/offboarding.md).
- Department, manager, location or responsibility changes: [transfer](references/employee-transfer.md).

Do not load all lifecycle references or sibling skills.

A complete onboarding, transfer or safe-offboarding request authorizes ordinary reversible workflow steps for the named user and stated profile. It does not authorize unrelated tenant changes, privileged-role grants, Conditional Access exclusions, permanent deletion, mailbox purge, device wipe or Autopilot deletion.

Production groups, rings, named targets, `All users` and `All devices` are valid when requested or established by the verified profile. Do not impose a pilot. Before broad assignment verify scope, exclusions, filters, deadlines, restart behavior and viable rollback.

Retain tenant/target, verified changes, already-correct items, affected workloads and follow-up in the session record. Distinguish `Configured`, `Assigned`, `Provisioned`, `Applied` and `Tested`; never claim an unobserved state works.
