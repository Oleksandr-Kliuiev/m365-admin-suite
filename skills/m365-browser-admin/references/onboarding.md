# Full employee onboarding

## Resolve the specification

Establish the legal/display name, UPN, user type, usage location, department, title, employee ID, manager, start date, access profile, licenses, groups, workload access, applications, and Intune scope. Use the tenant catalog when available. Do not infer privileged access from job title.

## Preflight

1. Confirm tenant and administrator.
2. Search exact UPN, aliases, mail nickname, display name, and Deleted users for conflicts.
3. Check required license capacity and usage-location prerequisites.
4. Resolve every group by stable ID and inspect type, source, membership mode, owners, and downstream licensing, applications, policies, roles, or Conditional Access effects.
5. Detect an existing partially onboarded identity and continue idempotently.

## Execute in dependency order

1. Create or update a `Member` identity with tenant-standard UPN and required properties.
2. Use a generated temporary password and require change at first sign-in when appropriate. Display it only to the requesting administrator and never persist it.
3. Capture UPN and object ID and verify that the identity is searchable.
4. Set usage location.
5. Add approved assigned-group memberships. Never manually edit dynamic or synchronized membership.
6. Wait for group-based licensing; add only remaining approved direct licenses and service plans.
7. Verify Exchange provisioning before aliases, mailbox delegation, or forwarding.
8. Apply Teams, Microsoft 365 Group, SharePoint, OneDrive, and approved flow ownership/access.
9. Add approved Intune enrollment, policy, application, and compliance scope.
10. Start approved onboarding flows and verify run details.

## Verify and hand off

Reopen the identity and verify properties, manager, enabled state, direct/inherited groups, license status, workload provisioning visible to an administrator, and Intune assignments. Without employee sign-in or a device, do not claim MFA registration, client access, OneDrive sync, enrollment, compliance, encryption, or application installation was tested.

Report credentials only ephemerally to the requesting administrator, plus first-login actions, pending propagation, missing licenses, and device-dependent work.

