---
name: m365-license-admin
description: "Microsoft 365 licenses in Chrome: inventory, capacity, direct or group assignment, removal, service plans and errors. Use for license-focused tasks."
---

# Microsoft 365 License Admin

Read the [shared Chrome contract](../m365-browser-admin/references/browser-operation-contract.md) only if not already loaded; reuse it for this session.

Resolve the exact SKU and target by stable identifiers. Read current assignment sources before mutation and avoid duplicate direct licensing when a group already supplies the entitlement.

Read [references/license-operations.md](references/license-operations.md) for assignment, removal, group licensing, pagination, and verification.

Use `.m365-admin/tenant-catalog.yaml` when available to identify approved SKUs, disabled service plans, and license groups. Verify every catalog entry against the live tenant.

Production license groups are valid targets. Do not create a pilot group unless requested. Before bulk or group changes, verify SKU capacity, evaluated membership, exclusions, existing assignment errors, and downstream workloads affected.

For an inventory request, report the requested user's licenses and relevant assignment/service-plan state; do not change usage location or assignments. For changes, retain seats before/after, exact users/groups changed, assignment source, errors, pending propagation, and material workload risks. Keep the spoken result brief.
