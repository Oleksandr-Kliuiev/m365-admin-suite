---
name: m365-security-audit
description: Investigate Microsoft 365 security and audit evidence through authenticated browser portals, including user and admin activity, sign-ins, risky users, alerts, secure-configuration review, and incident timelines. Use for read-oriented investigations, audit questions, and security posture review. Do not use to silently remediate findings, alter Conditional Access, or perform Purview eDiscovery unless the user explicitly expands the request.
---

# Microsoft 365 Security Audit

Default to evidence collection and analysis. A request to investigate, audit, review, or explain does not authorize configuration changes, account containment, alert dismissal, or evidence deletion.

Read [references/security-review.md](references/security-review.md) for scope, pagination, evidence correlation, and reporting.

Confirm tenant, time zone, time range, exact identities/resources, data availability, and the administrator's portal role. Use stable event IDs and timestamps; preserve source distinctions among Entra sign-ins, audit logs, Defender/security alerts, and workload audit records.

If the user separately authorizes remediation, verify exact target and current state immediately before mutation, then record before/after evidence. Never clear or dismiss evidence merely to make the dashboard appear healthy.

