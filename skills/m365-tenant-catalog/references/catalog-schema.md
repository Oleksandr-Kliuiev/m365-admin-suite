# Tenant catalog schema

The catalog is YAML with `schema_version: 1`. Keep keys stable and values human-reviewable. Object IDs are strongly preferred for mutable tenant objects, with display names retained for readability.

## Top-level keys

- `schema_version`: required integer, currently `1`.
- `tenant`: required map with `display_name`, `primary_domain`, optional `tenant_id`, and `verified_at`.
- `naming`: optional UPN, alias, display-name, device, and group conventions.
- `profiles`: required map keyed by a short stable profile name.
- `offboarding`: optional default safe-offboarding behavior.
- `safety`: optional protected accounts, groups, devices, sites, and policy IDs.

## Profile keys

A profile may contain:

- `description` and optional `extends` list.
- `identity`: usage location, department, company, employee type, or other intended properties.
- `licenses.required` and `licenses.optional`.
- `groups.required` and `groups.optional`.
- `exchange`: aliases, mailbox behavior, delegates, and policies.
- `collaboration`: Teams, Microsoft 365 Groups, SharePoint sites, and OneDrive expectations.
- `intune`: enrollment groups, applications, compliance, configuration, endpoint-security policies, and filters.
- `power_automate`: environment, flow, and ownership expectations.
- `first_sign_in`: password change, MFA registration, Company Portal, and device-enrollment steps.

Lists of tenant objects may use a string when an exact stable name is sufficient or a mapping with `name`, `id`, and optional `assignment`. Live skills must verify object identity before mutation regardless of representation.

## Inheritance

`extends` names one or more profiles applied before the child. Merge maps recursively; append unique list items while preserving order; let the child override scalar values. Reject unknown parents and cycles. Catalog inheritance describes intended state and does not prove that assignments currently exist.

## Safety keys

`safety.protected_accounts` should include break-glass, service, synchronization, and automation identities that lifecycle skills must not disable, delete, or strip without exact explicit authorization. Use UPN and object ID where available.

Do not include secrets under any key. The validator rejects common secret-bearing key names but cannot detect every sensitive value; human review remains required.

