---
name: m365-tenant-catalog
description: Discover, create, compare, validate, and maintain a private tenant-specific Microsoft 365 administration catalog containing approved access profiles, licenses, groups, applications, policies, naming rules, protected accounts, and lifecycle defaults. Use when preparing or updating reusable tenant profiles. Do not use the catalog itself as authorization to mutate the live tenant.
---

# Microsoft 365 Tenant Catalog

Build a private intended-state catalog from administrator input and read-only tenant discovery. The catalog accelerates other Microsoft 365 skills but never replaces live verification or task authorization.

## Location and privacy

Use a user-provided path or `.m365-admin/tenant-catalog.yaml` in the current working directory. Create the parent directory when the user asks to create a catalog. Never store passwords, temporary credentials, tokens, certificates, private keys, session material, recovery codes, or unnecessary personal data.

Read [references/catalog-schema.md](references/catalog-schema.md) before creating or materially changing a catalog. Use [assets/tenant-catalog.example.yaml](assets/tenant-catalog.example.yaml) as the structural template.

## Discovery workflow

1. Confirm tenant and administrator in the authenticated browser.
2. Inventory verified domains, license SKUs/capacity, relevant groups, roles, applications, Intune policies, collaboration resources, and lifecycle conventions.
3. For each job/access profile, compare three to five representative users when available. Record common state and exceptions; never clone one user's accidental access.
4. Distinguish `observed` state from administrator-approved `intended` state. Ask for a decision only where the difference would materially change future assignments.
5. Prefer group-driven entitlement profiles. Record stable object IDs alongside human-readable names whenever available.
6. Add protected accounts and groups that lifecycle operations must not change automatically.
7. Save the private catalog and run `scripts/validate_catalog.py` when Python and PyYAML are available.

## Update rules

Preserve administrator-authored comments and unknown forward-compatible keys when practical. Do not silently remove profiles or change production scope because a sampled user differs. Record discovery date and the tenant identity used for verification.

Finish with profiles added/changed, unresolved differences, unverified IDs, and validation results. Do not make tenant mutations during catalog discovery unless separately requested.

