---
name: m365-exchange-admin
description: "Exchange Online in Chrome: mailboxes, recipients, aliases, delegation, forwarding, groups and mail flow. Use for Exchange-focused administration."
---

# Microsoft 365 Exchange Admin

Read the [shared Chrome contract](../m365-browser-admin/references/browser-operation-contract.md) only if not already loaded; reuse it for this session.

Use the Exchange admin center and exact recipient identifiers. Verify tenant, administrator, recipient type, primary SMTP address, aliases, object identity, and current provisioning state before mutation.

Read [references/exchange-operations.md](references/exchange-operations.md) for recipient, mailbox, delegation, forwarding, group, and preservation workflows.

Do not treat license assignment as proof that a mailbox exists. Do not treat conversion, forwarding, delegation, automatic reply, retention, and deletion as equivalent operations. Verify each requested state separately.

Before removing licenses or deleting a recipient, inspect mailbox dependencies, holds/retention indicators, delegates, forwarding, ownership, and approved data recipient. Mailbox purge or hold removal requires explicit authorization.

Report exact recipient, verified configuration, provisioning delays, dependent licenses, and any mail-delivery or delegate test that was or was not performed.
