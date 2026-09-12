# Repository guidance

Read `docs/AI_CONTEXT_MAP.md` before changing a skill. Work inside the smallest relevant skill folder and avoid loading unrelated references.

Keep every skill independently usable after plugin installation. Do not make a focused skill depend on the filesystem location of a sibling skill. Shared operational invariants may be stated concisely in each entrypoint; domain procedures belong in that skill's `references/` directory.

Never commit tenant exports, user lists, credentials, temporary passwords, session material, package signing keys, or a real `.m365-admin/tenant-catalog.yaml`. The public catalog is an example only.

Keep automatic invocation descriptions mutually discriminating. `m365-browser-admin` owns multi-portal lifecycle work; focused skills own standalone domain requests.

Treat Microsoft 365 tenants as production unless the user explicitly identifies a lab. Preserve exact targets, current-state checks, authorization boundaries, idempotency, pagination handling, and independent after-state verification.

