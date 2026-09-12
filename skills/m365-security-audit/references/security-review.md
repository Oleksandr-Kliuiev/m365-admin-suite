# Security review

## Define scope

Establish tenant, UTC/local time interpretation, inclusive time range, exact users, applications, devices, IPs, resources, event types, and requested output. Record unavailable telemetry and retention-window limits.

## Collect evidence

1. Use exact filters before pagination.
2. Capture stable event/alert ID, timestamp, actor, target, operation, result, source, IP/location, application, device, correlation ID, and risk context when present.
3. Exhaust filtered pages or virtualized results before reporting absence.
4. Correlate records by stable identifiers and time; do not merge events solely by display name.
5. Distinguish portal interpretation from directly observed fields.

## Review configuration

For posture review, inspect effective controls and exclusions rather than only policy names. Mark recommendations separately from verified findings. Do not alter settings during an audit unless remediation is explicitly authorized.

## Report

Provide scope, sources, findings, timeline, affected objects, confidence, gaps, and recommended next actions. Avoid unnecessary personal data and credentials. Preserve evidence that could matter to an investigation.

