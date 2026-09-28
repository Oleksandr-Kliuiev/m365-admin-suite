---
name: m365-intune-admin
description: "Microsoft Intune in Chrome: devices, enrollment, apps, configuration, compliance, endpoint security and lifecycle actions. Use for device or app management."
---

# Microsoft Intune Admin

Read the [shared Chrome contract](../m365-browser-admin/references/browser-operation-contract.md) only if not already loaded; reuse it for this session.

Operate the live Intune tenant using exact device, application, policy, user, and group identifiers. Inspect current assignments and status before mutation.

- For devices, enrollment, configuration, compliance, remediation, and lifecycle actions, read [references/devices-and-policies.md](references/devices-and-policies.md).
- For application packaging, detection, dependencies, supersedence, assignments, monitoring, and removal, read [references/application-deployment.md](references/application-deployment.md).

Load only the relevant reference unless the request genuinely spans both.

Use the exact requested production scope, including named targets, production groups, rings, `All users`, or `All devices`. Do not require a pilot. Verify inclusions, exclusions, assignment filters, deadlines, notifications, restart behavior, and rollback before broad changes.

Distinguish `Created`, `Assigned`, `Device checked in`, `Applied`, and `Tested`. A browser-only operation cannot prove endpoint application without a managed device reporting status.

Require explicit authorization for Wipe, Fresh Start, Autopilot Reset, Autopilot deletion, or another destructive device action. Verify action status before retrying.
