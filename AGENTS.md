# Repository guidance

Read `docs/AI_CONTEXT_MAP.md` before changing a skill. Work inside the smallest relevant skill folder and avoid loading unrelated references.

Install and maintain all 12 suite skills together. Focused skills are directly invocable and share the Chrome contract in `skills/m365-browser-admin/references/browser-operation-contract.md`; preserve their relative sibling links. Read that contract once per session, rereading only missing instructions after context loss. Domain procedures belong in the owning skill's `references/` directory.

Never commit tenant exports, user lists, credentials, temporary passwords, session material, package signing keys, or a real `.m365-admin/tenant-catalog.yaml`. The public catalog is an example only.

Keep automatic invocation descriptions mutually discriminating. `m365-admin-suite` routes natural-language or voice requests across domains or when the specialist is unclear; no explicit skill name is required. `m365-browser-admin` owns complete multi-portal lifecycle work, and focused skills own standalone domain requests without a detour through the suite. Load one owning specialist and its relevant workflow; add another only for an independent operation outside that owner's scope. Do not substitute the unrelated `m365-admin-stack` unless the request explicitly concerns installing, repairing, configuring, or verifying CLI/MCP infrastructure.

Reuse the active authenticated Chrome session unless the user explicitly chooses another browser. Load shared navigation guidance only for an unknown route or navigation problem, and report handling only for complete lists, reports, exports, or email. Reuse loaded instructions, while refreshing affected live state before later changes and verifying saved results.

Treat Microsoft 365 tenants as production unless the user explicitly identifies a lab. Preserve exact targets, current-state checks, authorization boundaries, idempotency, pagination handling, and independent after-state verification.
