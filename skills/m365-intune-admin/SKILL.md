---
name: m365-intune-admin
description: Administer Microsoft Intune through an authenticated browser, including enrollment, managed devices, compliance, configuration and endpoint-security policies, application packaging and assignments, sync, remediation, updates, retirement, wipe, and Autopilot records. Use for device or application management. Do not use for ordinary user creation, licensing-only work, or unrelated tenant lifecycle operations.
---

# Microsoft Intune Admin

Operate the live Intune tenant using exact device, application, policy, user, and group identifiers. Inspect current assignments and status before mutation.

- For devices, enrollment, configuration, compliance, remediation, and lifecycle actions, read [references/devices-and-policies.md](references/devices-and-policies.md).
- For application packaging, detection, dependencies, supersedence, assignments, monitoring, and removal, read [references/application-deployment.md](references/application-deployment.md).

Load only the relevant reference unless the request genuinely spans both.

Use the exact requested production scope, including named targets, production groups, rings, `All users`, or `All devices`. Do not require a pilot. Verify inclusions, exclusions, assignment filters, deadlines, notifications, restart behavior, and rollback before broad changes.

Distinguish `Created`, `Assigned`, `Device checked in`, `Applied`, and `Tested`. A browser-only operation cannot prove endpoint application without a managed device reporting status.

Require explicit authorization for Wipe, Fresh Start, Autopilot Reset, Autopilot deletion, or another destructive device action. Verify action status before retrying.

