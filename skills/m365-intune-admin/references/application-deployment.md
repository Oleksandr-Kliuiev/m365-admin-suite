# Intune application deployment

## Classify and specify

Choose Microsoft Store app, Microsoft 365 Apps, Windows app (Win32), or supported line-of-business type according to source and management behavior. Establish exact name, publisher, version, architecture, source, installer files, install context, silent install/uninstall/repair commands, restart behavior, return codes, requirements, detection, dependencies, supersedence, assignment intent, scope, filters, deadline, notifications, and rollback.

Never invent installer switches, product codes, registry paths, detection scripts, file versions, or uninstall commands. Stop before production assignment if the package owner cannot validate them.

## Source and inventory

Confirm approved source and redistribution rights. Capture signer, version, and hash when local inspection is available. Search Intune by exact name, publisher, version, and product code. Inspect existing assignments, detection, dependencies, and supersedence before creating or replacing an object.

## Win32 preparation

Package Win32 content as `.intunewin` with the official Microsoft Win32 Content Prep Tool in an authorized Windows environment. Keep the prep executable outside the source folder and include only required files. A macOS browser session can upload an existing package but cannot perform the official packaging step alone.

## Create and configure

1. Select the correct app type and exact source/package.
2. Wait for upload and metadata extraction.
3. Validate metadata and Company Portal visibility.
4. Configure commands, System/User context, requirements, return codes, and restart behavior.
5. Configure stable detection: MSI product/version, file version, registry version, or vendor-validated script.
6. Add true technical dependencies without cycles.
7. Configure supersedence according to in-place upgrade versus remove-and-replace behavior.
8. Apply exact assignments and verify conflicting Required, Available, or Uninstall intent.
9. Save, wait for content readiness, and capture app ID.

## Verify and recover

Confirm upload readiness, assignments, target enrollment/licensing, check-in, and per-device/user install status. Inspect requirements-not-met, pending reboot, dependency, detection, and installer errors. Assignment is not installation; installation is not a successful launch test.

For rollback, limit/remove assignment, use a validated uninstall assignment, or supersede with a known-good version. Deleting the Intune app object does not uninstall software already installed.
