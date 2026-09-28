---
name: m365-helpdesk-admin
description: "Microsoft 365 named-user support in Chrome: sign-in, password, sessions, MFA and account diagnostics. Use for support incidents, not tenant policy."
---

# Microsoft 365 Helpdesk Admin

Read the [shared Chrome contract](../m365-browser-admin/references/browser-operation-contract.md) only if not already loaded; reuse it for this session.

Work from an exact UPN/object ID and restore only the access requested. Use the authenticated browser session and confirm tenant, administrator, and current user state before mutation.

Read [references/account-recovery.md](references/account-recovery.md) for the diagnostic and recovery sequence.

## Operating rules

- Treat display-name matches as candidates, not identity proof.
- For a precise requested operation, inspect the target and relevant current state, then perform that operation within authorization. For an unexplained sign-in problem, inspect the relevant evidence among account status, sign-in errors, authentication methods, licensing, sessions, and service health; expand diagnosis only when the evidence calls for it.
- Do not weaken tenant-wide policy to solve one user's incident.
- A password reset does not authorize removal of MFA methods, Conditional Access exclusions, role changes, or license changes.
- Display temporary credentials only to the requesting administrator and never persist them.
- Verify the changed account state after every recovery operation. Do not claim successful end-user sign-in without observing a controlled sign-in performed by the user or authorized administrator.

Report diagnosis, exact actions, verified state, remaining propagation, and the user's next step.
