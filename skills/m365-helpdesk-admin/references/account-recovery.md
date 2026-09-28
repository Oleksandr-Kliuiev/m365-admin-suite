# Account recovery

## Start at the exact user

In the existing Microsoft 365 admin center, use **Users → Active users**, search the exact UPN, and inspect the matched record. A requested license-status check uses **Licenses and Apps**. Follow the visible portal link for specialized identity diagnostics when needed; do not tour every admin center.

Read-only Chrome check on 2026-09-28 verified **Users → Active users** in the current admin center. Its search field said **Press Enter key to search active users list**: filling the field alone does not prove that results have updated. Follow the actual current search instruction and verify the returned UPN. License/status filters were visible; no user or license changes were performed.

Source checked 2026-09-28: [Microsoft user and license route](https://learn.microsoft.com/en-us/entra/fundamentals/license-users-groups). Use current UI labels rather than memorized selectors.

## Diagnose before changing

For a precise requested action, verify only the target, relevant current state and dependencies. Use the broader diagnostic sequence below for an unexplained access problem.

1. Confirm exact UPN/object ID, tenant, and administrator role.
2. Inspect enabled/blocked state and recent sign-in records when available.
3. Identify the error class: password, account block, MFA method, Conditional Access, risk policy, missing entitlement, service outage, device compliance, or downstream provisioning.
4. Check whether the identity is cloud-managed or synchronized. Do not edit an on-premises-mastered attribute in the cloud as a workaround.

## Apply the narrowest remedy

- Unblock sign-in only when the block is unintended and the request authorizes restoration.
- Reset the password only when requested or supported by diagnosis; require change at next sign-in when appropriate.
- Revoke sessions when compromise, stale sessions, or explicit request justifies it.
- Remove or require re-registration of authentication methods only for the exact user and with clear authorization.
- Do not add Conditional Access exclusions or privileged roles as a helpdesk shortcut.

## Verify

Reopen the user, confirm changed status and methods, and inspect a new sign-in only if the user performs one. Separate `account recovered administratively` from `successful interactive sign-in tested`.

