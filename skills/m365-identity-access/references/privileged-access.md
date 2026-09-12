# Privileged access operations

## Directory roles and PIM

Resolve user/group and role by object/template ID. Inspect direct and group-inherited assignment, scope, active versus eligible state, schedule, approval, justification, and activation requirements. Verify the resulting assignment in the role and principal views.

Treat Global Administrator and equivalent high-impact roles as exact-intent changes. Do not convert an eligible assignment to permanent active access merely for convenience.

## Conditional Access

Before editing, capture the current policy state and every assignment/control category. Evaluate overlaps with existing policies. Verify emergency-access accounts remain protected from lockout according to tenant policy. Use Report-only only when requested or when the administrator asks for staged validation; do not impose a pilot mode on an explicit production rollout.

After saving, reopen the policy and verify the complete configuration. Enabling a policy is not proof of successful or blocked sign-in; report sign-in testing separately.

## Authentication methods and access reviews

Distinguish tenant-wide authentication-method policy from one user's registered methods. For access reviews, verify resource, reviewers, recurrence, decisions, auto-apply behavior, fallback reviewers, and consequences before creation or update.

Permanent removal of methods, role assignments, or access-review decisions must target exact objects and follow the explicit request.

