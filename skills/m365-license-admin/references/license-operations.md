# License operations

## Inventory and assignment

1. Confirm tenant and exact product SKU; record total, assigned, and available seats.
2. Resolve exact user or group and inspect direct, inherited, pending, and error states.
3. Set a valid usage location before user assignment.
4. Review disabled plans, mutually exclusive products, and required base entitlements.
5. Prefer the tenant's approved group-based model. Add a direct license only when intended state requires it.
6. Reopen the user/group license view and verify assignment status and service-plan errors.

Group-based assignment is eventually consistent. Report pending evaluation rather than adding a duplicate direct license.

## Removal

Before removal, identify Exchange mailbox, OneDrive, Teams, Intune, Power Platform, retention, and other dependent behavior. During offboarding, preserve data before removing its supporting license. Removing a direct license does not remove an entitlement inherited from a group.

## Entitlement boundaries

Do not infer bundled rights from a similarly named product. In particular, a Power Automate entitlement alone does not grant Teams, Exchange, OneDrive, SharePoint, or desktop Office rights. Verify enabled service plans in the actual SKU.

## Search and scale

Use exact UPN/object ID and server-side filters before paging. For bulk work, capture unique target IDs, expected count, succeeded/failed/skipped totals, and per-object errors. Stop if observed scope exceeds the approved target set.

