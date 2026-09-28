# Changelog

## 0.2.3

- Send requested reports through Outlook on the web in the active authenticated Chrome profile on Windows and macOS, preserving the tenant's cloud.
- Verify the employee's sending mailbox and exact recipient, support short complete reports in the body and verified export attachments, and check Sent Items without duplicate sends or repeated confirmation.
- Add synthetic report-delivery scenarios covering identity, attachments, missing capabilities, authorization and ambiguous submission.

## 0.2.2

- Route typed or spoken requests to the owning specialist without requiring a skill name, while retaining direct focused-skill selection.
- Reuse authenticated Chrome and one shared session contract across the 12 skills; load only the relevant workflow and conditional navigation or report guidance.
- Preserve exact tenant and target verification, scoped authorization, lifecycle safeguards, and verified outcome reporting.
- Add a local package check for links, routing metadata, and the 700-line context ceiling.
