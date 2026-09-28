# Portal navigation

Prefer an existing destination or a tenant deep link observed in live UI. Open another portal only in the same authenticated Chrome context. Never invent tenant-specific IDs/private URLs; follow the tenant's cloud rather than moving sovereign tenants to public-cloud roots.

| Work | Owning portal |
| --- | --- |
| Users, licenses, organization settings, Service Health | Microsoft 365 admin center; public-cloud root `https://admin.microsoft.com` |
| Identity, roles, authentication, sign-ins, Conditional Access | Entra portal or its live Admin centers link |
| Devices, enrollment, compliance, apps, endpoint security | Intune; public-cloud root `https://intune.microsoft.com` |
| Recipients, delegation, forwarding, mail flow | Exchange admin center via live portal links |
| Teams, sites, OneDrive, flows | Teams, SharePoint or Power Automate respectively |
| Retention, DLP, eDiscovery | Purview |

For a hidden item, try visible **Show all** or portal search once within the shared recovery limit. Labels may be localized; documented routes do not prove current availability.

Historical observation (2026-09-28), not cached live state: `admin.microsoft.com` redirected to `admin.cloud.microsoft`; preserve authenticated redirects. **Current Tenant** opened organization information with domain/tenant ID, not a switcher. Inspect the actual panel before switching and close overlays before using the underlying page.

Microsoft sources checked 2026-09-28: [admin navigation](https://learn.microsoft.com/en-us/microsoft-365/admin/admin-overview/admin-center-overview?view=o365-worldwide), [Entra areas](https://learn.microsoft.com/en-us/entra/fundamentals/entra-admin-center), [Intune/cloud roots](https://learn.microsoft.com/en-us/mem/get-support). Use the selected workflow's routes; successful UI execution needs no extra documentation tour.
