# License operations

## Fast read routes

- Capacity or product inventory: Microsoft 365 admin center → **Billing → Licenses**; select the exact product. Record total, assigned, and available seats without entering assignment controls. Product totals can aggregate multiple subscriptions.
- One user's licenses: **Users → Active users** → exact UPN → **Licenses and Apps**. If the visible search field instructs **Press Enter**, submit the search before reading results. Read current products and enabled plans.
- Product assignments: **Billing → Licenses** → product. A group assignment is represented by the group, not every member; inspect **Teams & groups → Active teams & groups** when the task needs members. Do not treat the visible assignment-row count as a user count.
- Use current visible labels and the shared navigation recovery rules. Inventory is read-only; usage-location edits and assignment steps below apply only when requested.

Source checked 2026-09-28: [Microsoft license management routes](https://learn.microsoft.com/en-us/entra/fundamentals/license-users-groups).

## Assignment

1. Confirm tenant and exact product SKU; record total, assigned, and available seats.
2. Resolve exact user or group and inspect direct, inherited, pending, and error states.
3. Verify usage location before user assignment; set it only when the required value is established by the user or verified tenant profile. Do not infer a country from the interface language.
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

