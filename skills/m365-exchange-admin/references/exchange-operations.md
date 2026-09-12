# Exchange operations

## Resolve and inspect

Search exact primary SMTP address, UPN, alias, or object ID. Confirm recipient type, accepted domain domain, provisioning status, mailbox size/features when visible, aliases, delegates, forwarding, automatic replies, group ownership/membership, and retention/hold indicators relevant to the request.

## Mailbox changes

- Wait for mailbox provisioning before configuration.
- Verify aliases and primary address after save.
- Resolve delegates by exact UPN and distinguish Full Access, Send As, and Send on Behalf.
- Treat forwarding address and delivery-to-both behavior as separate settings.
- Convert user/shared mailbox only when requested and compatible with size, archive, hold, and license requirements.
- Do not claim delivery works without an observed mailbox and an authorized controlled delivery test when one is required.

## Distribution and Microsoft 365 groups

Confirm group type, source, owners, moderation, delivery restrictions, external-sender state, and membership mode. Do not edit synchronized membership in the cloud. Ensure a Team/Microsoft 365 group retains an owner before removing one.

## Preservation and removal

Verify delegation, forwarding, conversion, retention dependencies, and recipient ownership before license removal or deletion. Soft deletion, mailbox deletion, and permanent purge have different recovery behavior; perform only the exact authorized action.

