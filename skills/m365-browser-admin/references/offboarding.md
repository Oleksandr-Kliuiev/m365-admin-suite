# Safe employee offboarding

Safe offboarding contains access and preserves business data. It does not permanently delete the identity, mailbox, OneDrive, device, or retention configuration unless the user explicitly requests that exact action.

## Inventory impact

Resolve exact UPN/object ID and inspect sign-in state, roles, privileged memberships, licenses, mailbox, aliases, delegation, forwarding, holds, OneDrive, SharePoint, Teams ownership, groups, managed devices, Autopilot records, Power Automate flows/connections, application ownership, retention indicators, manager, and nominated data recipient.

If ownership, legal hold, retention, or the target's status as an emergency/sole administrator is unclear, preserve the dependent resource and report the blocker.

## Contain access

Unless offboarding is scheduled for a future time:

1. Block sign-in for the exact account.
2. Revoke active sessions and refresh tokens.
3. Reset the password when the approved policy calls for it, without exposing it.
4. Remove direct privileged roles and privileged group memberships in scope.
5. Reopen the user and verify blocked and role states.

## Preserve and transfer

Before license removal, transfer or delegate the mailbox, configure approved autoreply/forwarding, convert to shared mailbox when requested and eligible, grant the nominated recipient OneDrive access, and transfer ownership of Teams, groups, SharePoint sites, flows, connections, and applications. Verify every recipient by UPN/object ID.

## Remove access and licenses

After preservation is verified, remove ordinary memberships and application access, then direct licenses last. Account for licenses inherited from groups and recheck preservation features that may depend on a license.

For devices, distinguish Retire, Wipe, Delete, Fresh Start, Autopilot Reset, and Autopilot record deletion. Require explicit authorization for destructive device actions.

Delete or purge the user only when explicitly requested after presenting exact target, preserved resources, remaining dependencies, and visible recovery behavior. Verify Deleted users after soft deletion.

