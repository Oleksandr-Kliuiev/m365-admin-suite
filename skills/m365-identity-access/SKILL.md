---
name: m365-identity-access
description: Administer Microsoft Entra access through an authenticated browser, including directory roles, PIM assignments and activation, Conditional Access, authentication methods, named locations, access reviews, and privileged groups. Use for identity-policy or privileged-access requests. Do not use for routine password support, ordinary group membership, or full employee onboarding/offboarding.
---

# Microsoft 365 Identity and Access

Treat identity policy and privileged access as high-impact production configuration. Confirm tenant, administrator, exact object IDs, current policy state, and authorization scope before mutation.

Read [references/privileged-access.md](references/privileged-access.md) for role, PIM, Conditional Access, authentication, and access-review procedures.

## Boundaries

- Never infer an administrative role from title, department, or onboarding profile.
- Prefer least privilege, scoped assignment, and eligible/time-bound PIM assignment when that matches the request and tenant capability.
- Never add a user to a Conditional Access exclusion or modify emergency-access accounts without explicit intent.
- For policy changes, inspect include/exclude users, groups, roles, applications, platforms, locations, conditions, grant controls, session controls, and current state.
- A production-wide policy change may be performed when explicitly requested; verify break-glass exclusions and expected blast radius before enabling it.

Report exact role/policy IDs, scope, assignment type, activation requirements, changed controls, exclusions, verified state, and residual risk.

