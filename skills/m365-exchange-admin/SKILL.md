---
name: m365-exchange-admin
description: Administer Exchange Online recipients through an authenticated browser, including user and shared mailboxes, aliases, delegation, forwarding, automatic replies, distribution groups, mailbox conversion, and routine mail-flow settings. Use for Exchange-focused requests. Do not use for full employee lifecycle, tenant-wide security policy, or licensing except dependency checks.
---

# Microsoft 365 Exchange Admin

Use the Exchange admin center and exact recipient identifiers. Verify tenant, administrator, recipient type, primary SMTP address, aliases, object identity, and current provisioning state before mutation.

Read [references/exchange-operations.md](references/exchange-operations.md) for recipient, mailbox, delegation, forwarding, group, and preservation workflows.

Do not treat license assignment as proof that a mailbox exists. Do not treat conversion, forwarding, delegation, automatic reply, retention, and deletion as equivalent operations. Verify each requested state separately.

Before removing licenses or deleting a recipient, inspect mailbox dependencies, holds/retention indicators, delegates, forwarding, ownership, and approved data recipient. Mailbox purge or hold removal requires explicit authorization.

Report exact recipient, verified configuration, provisioning delays, dependent licenses, and any mail-delivery or delegate test that was or was not performed.

