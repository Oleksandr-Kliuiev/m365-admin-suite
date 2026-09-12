---
name: m365-helpdesk-admin
description: Resolve routine Microsoft 365 user support through an authenticated browser, including blocked sign-in, password reset, session revocation, authentication-method review, MFA re-registration, account status, and user-specific service diagnostics. Use for a named user's support incident. Do not use for tenant-wide identity policy, Conditional Access design, licensing-only work, or full onboarding/offboarding.
---

# Microsoft 365 Helpdesk Admin

Work from an exact UPN/object ID and restore only the access requested. Use the authenticated browser session and confirm tenant, administrator, and current user state before mutation.

Read [references/account-recovery.md](references/account-recovery.md) for the diagnostic and recovery sequence.

## Operating rules

- Treat display-name matches as candidates, not identity proof.
- Inspect sign-in block, account enabled state, recent sign-in errors, license status, authentication methods, session state, and service health before choosing a remedy.
- Do not weaken tenant-wide policy to solve one user's incident.
- A password reset does not authorize removal of MFA methods, Conditional Access exclusions, role changes, or license changes.
- Display temporary credentials only to the requesting administrator and never persist them.
- Verify the changed account state after every recovery operation. Do not claim successful end-user sign-in without observing a controlled sign-in performed by the user or authorized administrator.

Report diagnosis, exact actions, verified state, remaining propagation, and the user's next step.

