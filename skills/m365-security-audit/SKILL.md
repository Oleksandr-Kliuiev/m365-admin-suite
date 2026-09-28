---
name: m365-security-audit
description: "Microsoft 365 security investigation in Chrome: sign-ins, activity, risks, alerts, timelines and posture. Read-oriented; findings do not authorize remediation."
---

# Microsoft 365 Security Audit

Read the [shared Chrome contract](../m365-browser-admin/references/browser-operation-contract.md) only if not already loaded; reuse it for this session.

Default to evidence collection and analysis. A request to investigate, audit, review, or explain does not authorize configuration changes, account containment, alert dismissal, or evidence deletion.

Read [references/security-review.md](references/security-review.md) for scope, pagination, evidence correlation, and reporting.

Confirm tenant, time zone, time range, exact identities/resources, data availability, and the administrator's portal role. Use stable event IDs and timestamps; preserve source distinctions among Entra sign-ins, audit logs, Defender/security alerts, and workload audit records.

If the user separately authorizes remediation, verify exact target and current state immediately before mutation, then record before/after evidence. Never clear or dismiss evidence merely to make the dashboard appear healthy.
