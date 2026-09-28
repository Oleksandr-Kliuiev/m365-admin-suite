# AI context map

Use this map to load the smallest sufficient context. All 12 skills install together and share `skills/m365-browser-admin/references/browser-operation-contract.md`. For live administration, read that Chrome contract only if not already loaded; reuse it for the session. Local catalog edits do not require a browser session.

| Task | Start here | Load next only when needed |
|---|---|---|
| Cross-domain or unclear natural-language/voice request; explicit suite request | `skills/m365-admin-suite/SKILL.md` | One owning specialist and its relevant workflow; another only for an independent operation outside the owner's scope |
| Full onboarding, transfer, offboarding | `skills/m365-browser-admin/SKILL.md` | Only the requested lifecycle reference |
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
| Report email through Outlook on Windows or macOS | `skills/m365-browser-admin/references/reports-and-exports.md` | `docs/outlook-report-scenarios.md` only when changing or validating delivery behavior |

Focused domain requests start directly with their specialist; no suite invocation or explicit skill name is required. Do not load the complete `skills/` tree for a domain change. The lifecycle owner covers its cross-portal workflow without loading every domain skill. Routing descriptions live in each `SKILL.md` frontmatter.

Shared references are conditional: read `skills/m365-browser-admin/references/browser-navigation.md` only to resolve an unknown route or navigation problem; read `skills/m365-browser-admin/references/reports-and-exports.md` for complete lists, reports, exports, or email. Reuse loaded instructions, but refresh affected live state before later mutations and verify saved results. After context loss, reread only missing instructions for the active task, including workflow prerequisites, checkpoints, and verification.

The unrelated `m365-admin-stack` handles explicit CLI/MCP installation, repair, configuration, or verification requests; it is not a substitute for tenant administration.

Run `python3 scripts/check_package.py` from the repository root to check package structure, local links, descriptions of at most 220 characters, implicit invocation, and the 700-line context ceiling.
