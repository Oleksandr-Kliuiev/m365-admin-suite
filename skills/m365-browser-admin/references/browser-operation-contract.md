# Browser operation contract

## Route to the owning portal

- Microsoft 365 admin center: users, billing, licenses, and general organization settings.
- Microsoft Entra admin center: identities, groups, roles, authentication, sign-ins, and Conditional Access.
- Microsoft Intune admin center: devices, enrollment, compliance, profiles, applications, and endpoint security.
- Exchange admin center: recipients, delegation, forwarding, shared mailboxes, and mail flow.
- Teams admin center: meeting, messaging, voice, application, and Teams policies.
- SharePoint admin center: sites, sharing, ownership, and OneDrive administration.
- Power Automate: environments, flows, connections, ownership, and run history.

Start from the owning portal. Reuse the same browser profile so authenticated state carries across portals. Confirm tenant and administrator after redirects or directory switches.

## Stable interaction loop

1. Observe a fresh accessibility/UI state.
2. Resolve controls by semantic role, accessible name, visible value, or stable ID. Avoid coordinates, row numbers, and stale element references.
3. Perform one coherent action or fill one unchanged form.
4. Wait for the relevant readiness signal: loading completion, changed result count, blade heading, URL, status, or toast.
5. Observe again and verify the intended object state independently.

After navigation, modal changes, refreshes, or asynchronous updates, discard old element references. Before retrying a mutation, read the object to determine whether the first attempt succeeded.

## Search and pagination

Use exact UPN or object ID first, then exact display name plus secondary attributes. Clear old filters before searching. Validate the complete row and details before mutation.

Use server-side search, then filters, then stable sorting, then pagination. When paging, track page number and stable boundary IDs; stop only when the target is found, Next is disabled, or repeated boundary IDs prove the list is exhausted. For virtualized lists, scroll the table container and track unique IDs. Never report `not found` after inspecting only the first page.

## Evidence and recovery

Maintain a compact record of before state, requested change, portal acknowledgement, independently observed after state, and downstream dependencies. A toast is provisional evidence.

Use bounded retries for eventual consistency. Do not create duplicate users, direct licenses, memberships, policies, apps, or device actions because propagation is slow. Classify blockers as authentication, tenant mismatch, permission, licensing, object conflict, synchronized/dynamic source, portal validation, throttling/loading, downstream provisioning, or required end-user/device action.

