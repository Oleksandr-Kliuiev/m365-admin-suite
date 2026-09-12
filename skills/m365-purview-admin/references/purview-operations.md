# Purview operations

## Retention and records

Resolve the exact policy/label ID, scope type, locations, inclusions, exclusions, retention duration, event trigger, record behavior, disposition review, and current deployment state. Before changing or removing retention, identify affected workloads, holds, records, and legal dependencies. Saving a policy is not proof that it has propagated to every workload.

## Sensitivity labels

Distinguish label definition, publishing policy, auto-labeling policy, container settings, encryption, markings, priority, and user scope. Verify conflicts with existing labels and policies. Do not expose encryption keys or weaken protection to solve an access problem without explicit authorization.

## Data Loss Prevention

Capture locations, users/groups, sensitive-info conditions, thresholds, exceptions, actions, user notifications, policy tips, incident reports, priority, and simulation/enforcement state. For production enablement, verify exact evaluated scope and expected business impact.

## Audit, content search, and eDiscovery

Confirm case, search, custodians, locations, query, time range/time zone, hold state, reviewers, and export destination. Investigation authorizes read-only search and review only. Export, purge, hold creation/removal, case closure, and deletion require explicit scope.

Preserve stable case/search/export IDs and chain-of-custody-relevant timestamps. Never alter or dismiss evidence simply to complete a workflow.

## Verification

Reopen the exact policy, label, case, or search and verify all fields. Report `Configured`, `Deployed`, `Applied`, `Search completed`, and `Export completed` separately, with pending locations and permission limitations.
