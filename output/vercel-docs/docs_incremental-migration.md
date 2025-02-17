# Your Privacy
This site uses tracking technologies. You may opt in or opt out of the use of these technologies.
DenyAccept all
Consent Settings
Privacy Policy
Your Privacy
This site uses tracking technologies. You may opt in or opt out of the use of these technologies.
Marketing
Off
Marketing cookies and services are used to deliver personalized advertisements, promotions, and offers. These technologies enable targeted advertising and marketing campaigns by collecting information about users' interests, preferences, and online activities. 
Analytics
Off
Analytics cookies and services are used for collecting statistical information about how visitors interact with a website. These technologies provide insights into website usage, visitor behavior, and site performance to understand and improve the site and enhance user experience.
Functional
Off
Functional cookies and services are used to offer enhanced and personalized functionalities. These technologies provide additional features and improved user experiences, such as remembering your language preferences, font sizes, region selections, and customized layouts. Opting out of these cookies may render certain services or functionality of the website unavailable.
Essential
On
Essential cookies and services are used to enable core website features, such as ensuring the security of the website. 
SaveDenyAccept all
Privacy Policy
![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-light.cf7eca76.svg)![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-dark.01246f11.svg)
Search...
`⌘ K`
Feedback
Log In
Sign Up
Platform
Incremental Migration
# Incremental Migration to Vercel
Learn how to migrate your app or website to Vercel with minimal risk and high impact.
Table of Contents
When migrating to Vercel you should use an incremental migration strategy. This allows your current site and your new site to operate simultaneously, enabling you to move different sections of your site at a pace that suits you.
In this guide, we'll explore incremental migration benefits and different strategies.
## Why opt for incremental migration?
Incremental migrations offer several advantages:
  * Reduced risk due to smaller migration steps
  * A smoother rollback path in case of unexpected issues
  * Earlier technical implementation and business value validation
  * Downtime-free migration without maintenance windows


### Disadvantages of one-time migrations
One-time migration involves developing the new site separately before switching traffic over. This approach has certain drawbacks:
  * Late discovery of expensive product issues
  * Difficulty in assessing migration success upfront
  * Potential for reaching a point of no-return, even with major problem detection
  * Possible business loss due to legacy system downtime during migration


### When to use incremental migration?
Despite requiring more effort to make the new and legacy sites work concurrently, incremental migration is beneficial if:
  * Risk reduction and time-saving benefits outweigh the effort
  * The extra effort needed for specific increments to interact with legacy data doesn't exceed the time saved


## Incremental migration strategies
![](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1689795055%2Fdocs-assets%2Fstatic%2Fdocs%2Fincremental-migration%2Fincremental-migration-steps-light.png&w=3840&q=75)![](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1689795055%2Fdocs-assets%2Fstatic%2Fdocs%2Fincremental-migration%2Fincremental-migration-steps-dark.png&w=3840&q=75)
Incremental migration process
With incremental migration, legacy and new systems operate simultaneously. Depending on your strategy, you'll select a system aspect, like a feature or user group, to migrate incrementally.
### Vertical migration
This strategy targets system features with the following process:
  1. Identify all legacy system features
  2. Choose key features for the initial migration
  3. Repeat until all features have been migrated


Throughout, both systems operate in parallel with migrated features routed to the new system.
### Horizontal migration
This strategy focuses on system users with the following process:
  1. Identify all user groups
  2. Select a user group for initial migration to the new system
  3. Repeat until all users have been migrated


During migration, a subset of users accesses the new system while others continue using the legacy system.
### Hybrid migration
A blend of vertical and horizontal strategies. For each feature subset, migrate by user group before moving to the next feature subset.
## Next steps
### Migration Guide
Transitioning your site to Vercel incrementally.
### Technical Guidelines
Key factors to consider for enhancing the effectiveness, performance, and reliability of your migration.
Last updated on July 17, 2024
Previous
What is Streaming?
Next
Migration Guide
Was this helpful?
supported.
Send
AskAsk v0
Incremental MigrationAskAsk v0
