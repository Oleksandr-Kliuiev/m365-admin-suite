# Collaboration operations

## Teams and Microsoft 365 Groups

Distinguish Team membership/ownership, backing Microsoft 365 Group membership/ownership, and Teams meeting, messaging, voice, and application policies. Verify direct, group-based, and global policy sources. Do not manually edit dynamic or synchronized group membership.

Before removing an owner, nominate and verify another exact owner. A display-name match is insufficient.

## SharePoint and OneDrive

Use exact site URL and permission source. Site groups, Microsoft 365 Group membership, direct permissions, and sharing links are distinct. Do not weaken tenant-wide external sharing to solve one request.

OneDrive provisioning may require licensed user sign-in. For administrative access or offboarding transfer, verify recipient UPN, access duration, ownership behavior, and retention dependencies before license removal or identity deletion.

## Power Automate

Select exact environment, flow ID, owner, trigger, connections, and connection references. Display names may repeat. For a controlled manual test, save, run, open run details, and verify every required action. A successful save is not a successful run.

Before disabling a departing owner, transfer ownership and repair connection references. Never expose connection secrets or assume another owner can use the original owner's connection.

