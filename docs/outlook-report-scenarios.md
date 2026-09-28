# Synthetic Outlook report-delivery scenarios

Use these cases to review [report handling](../skills/m365-browser-admin/references/reports-and-exports.md). They require no real tenant, email, draft or attachment upload. All addresses and filenames below are synthetic. Package checks validate structure and links; these cases describe expected behavior rather than proving a live Outlook send.

| Case | Expected behavior |
| --- | --- |
| Windows employee or macOS owner requests “send the complete license inventory to reviewer@example.invalid”; an authenticated Outlook tab exists | Reuse that Outlook web tab in the active Chrome profile; verify the employee mailbox and From address; use exactly the requested recipient. No native Outlook, COM, AppleScript or owner-specific settings. |
| Outlook tab is absent and the tenant uses a sovereign cloud | Follow a live compatible Outlook/app-launcher link in the same Chrome profile; preserve the cloud rather than inventing or using a public-cloud root. |
| Admin portal offers **Email**, but report delivery was requested through Outlook | Collect/export in the portal and compose in Outlook web; do not silently use the portal's Email action or Gmail. |
| “Email me the inventory”; requester identity and address are established and verified | Use that grounded address without another confirmation. If identity/address is unresolved, ask for the exact recipient instead of inferring the owner's personal email. |
| Tenant administrator and signed-in Outlook employee use different accounts | Verify both roles independently and inspect From before Send; do not switch the employee mailbox to the tenant administrator or a remembered owner mailbox. |
| Complete inventory contains six verified rows; no attachment requested; upload capability absent | Put the complete inventory and scope in the body. Continue sending under matching authorization; no unnecessary file-capability blocker. |
| User asks for CSV; export returns a verified nonempty `license-inventory.csv` | Follow current download/upload tool documentation, inspect content and completeness, upload the verified file reference and verify filename, available size metadata and completed attachment before Send. A body summary alone is insufficient. |
| Outlook displays the attached filename without its size | Use the verified download/upload evidence and completed attachment state; do not block solely because Outlook omits size. |
| Requested CSV download or upload is unsupported, required file/content evidence cannot be verified, or upload remains pending | Finish independent report work and state only the required missing capability or user step. Do not invent paths, claim attachment success or substitute another mail application. |
| User asks only to prepare/review a report | Prepare the report without sending; report creation does not authorize email. |
| Explicit send authorization already names scope and exact recipient | Inspect the final message and send once without a duplicate skill-imposed permission prompt. Do not add unrequested CC/BCC, recipients, schedules or subscriptions. |
| Send returns a toast or times out | Inspect Sent Items for the matching message before considering further action. If present, report sent/accepted, not recipient delivery; if ambiguous, report unverified without resending. |
| Filtered table displays one page of a larger inventory | Verify export/list completeness and requested columns across the full scope before calling the report complete; mark any unverified completeness as partial. |
