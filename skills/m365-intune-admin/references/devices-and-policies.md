# Devices and policies

## Preflight

Verify Intune entitlement, MDM authority, enrollment scope, restrictions, device limits, platform, exact target group, assignment filters, existing compliance/configuration/endpoint-security policies, applications, and related Conditional Access requirements.

Actual enrollment, BitLocker, application installation, compliance evaluation, remediation, and check-in require a supported endpoint.

## Policy work

1. Search exact policy name and ID to avoid duplicates.
2. Inspect platform, technology, settings, scope tags, assignments, exclusions, filters, and current status.
3. Create or update only the requested settings.
4. Apply the exact production scope and verify assignment after save.
5. Inspect per-setting/device status when available; aggregate success alone can hide errors.

## Device validation

Resolve device using at least two stable attributes such as serial number, Entra device ID, Intune managed-device ID, hostname, or primary user. Verify ownership, enrollment date, last check-in, compliance, configuration, applications, and encryption. Use bounded sync/retry and report pending state.

## Lifecycle actions

Retire removes managed company data/settings where supported; Wipe resets the device; Delete removes a management record; Fresh Start and Autopilot Reset have distinct effects; deleting an Autopilot record is separate. State the exact action and data/enrollment impact before destructive execution. Afterward check Intune, Entra, and Autopilot records separately when relevant.

