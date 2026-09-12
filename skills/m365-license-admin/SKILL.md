---
name: m365-license-admin
description: Administer Microsoft 365 product licenses and service plans through an authenticated browser, including inventory, seat capacity, direct and group-based assignment, removal, disabled plans, usage-location prerequisites, and license-error diagnosis. Use for license-focused requests. Do not use for complete employee lifecycle, Intune configuration, or mailbox administration beyond license dependency analysis.
---

# Microsoft 365 License Admin

Resolve the exact SKU and target by stable identifiers. Read current assignment sources before mutation and avoid duplicate direct licensing when a group already supplies the entitlement.

Read [references/license-operations.md](references/license-operations.md) for assignment, removal, group licensing, pagination, and verification.

Use `.m365-admin/tenant-catalog.yaml` when available to identify approved SKUs, disabled service plans, and license groups. Verify every catalog entry against the live tenant.

Production license groups are valid targets. Do not create a pilot group unless requested. Before bulk or group changes, verify SKU capacity, evaluated membership, exclusions, existing assignment errors, and downstream workloads affected.

Finish with seats before/after, exact users/groups changed, assignment source, service-plan state, errors, pending propagation, and license-dependent workload risks.

