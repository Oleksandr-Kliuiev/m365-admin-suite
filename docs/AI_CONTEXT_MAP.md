# AI context map

Use this map to load the smallest sufficient context.

| Task | Start here | Load next only when needed |
|---|---|---|
| Full onboarding, transfer, offboarding | `skills/m365-browser-admin/SKILL.md` | Relevant lifecycle reference and browser contract |
| Password, sign-in, MFA, sessions | `skills/m365-helpdesk-admin/SKILL.md` | `references/account-recovery.md` |
| Licenses and license groups | `skills/m365-license-admin/SKILL.md` | `references/license-operations.md` |
| Entra roles and access policy | `skills/m365-identity-access/SKILL.md` | `references/privileged-access.md` |
| Intune device, policy, or application | `skills/m365-intune-admin/SKILL.md` | Device or application reference, not both by default |
| Exchange recipient administration | `skills/m365-exchange-admin/SKILL.md` | `references/exchange-operations.md` |
| Teams, SharePoint, OneDrive, flows | `skills/m365-collaboration-admin/SKILL.md` | `references/collaboration-operations.md` |
| Security investigation | `skills/m365-security-audit/SKILL.md` | `references/security-review.md` |
| Service incident or advisory | `skills/m365-service-operations/SKILL.md` | `references/service-health.md` |
| Retention, DLP, labels, eDiscovery | `skills/m365-purview-admin/SKILL.md` | `references/purview-operations.md` |
| Tenant profile discovery/catalog | `skills/m365-tenant-catalog/SKILL.md` | Schema, example, validator |

Do not load the complete `skills/` tree for a domain change. Routing descriptions live in each `SKILL.md` frontmatter.

