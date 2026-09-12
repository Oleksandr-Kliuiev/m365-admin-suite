# Employee transfer and access change

Use for department, manager, location, job-function, or responsibility changes that alter access across more than one Microsoft 365 domain.

## Compare intended and current state

Resolve the exact user and both old and new profiles. Build a delta for properties, manager, usage location, licenses, groups, Teams ownership, SharePoint access, mailbox permissions, applications, Intune assignments, roles, and business-resource ownership.

Do not treat the new profile as permission to remove historical access blindly. Identify access that is personal, project-specific, temporary, privileged, inherited, synchronized, or required for handover.

## Apply the transition

1. Update identity properties that drive dynamic rules and wait for evaluated membership where relevant.
2. Add the new access required for continuity.
3. Transfer responsibilities and ownership before removing old access.
4. Remove obsolete direct access and licenses after dependencies are verified.
5. Preserve exceptions explicitly supplied by the administrator.

Verify the final state against the new profile plus approved exceptions. Report dynamic-group and downstream policy changes as pending until observed.
