![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-light.cf7eca76.svg)![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-dark.01246f11.svg)
Search...
`⌘ K`
Feedback
Log In
Sign Up
Security
Firewall
Web Application Firewall
How-to
# Vercel WAF
Learn how to secure your website with the Vercel Web Application Firewall (WAF)
Table of Contents
Vercel WAF is available on all plans
Those with the member, viewer, developer and administrator roles can access this feature
The Vercel WAF, part of the Firewall, provides security controls to monitor and control the internet traffic to your site through logging, blocking and challenging. When you apply a configuration change to the firewall, it takes effect globally within 300ms and can be instantly rolled back to prior configurations.
  * Configure your first Custom Rule
  * Add IP Blocks
  * Explore Managed Rulesets


## Traffic control
You can control the internet traffic to your website in the following ways:
  * IP blocking: Learn how to configure IP blocking
  * Custom rules: Learn how to configure custom rules for your project
  * Managed rulesets: Learn how to enable managed rulesets for your project (Enterprise plan)


## Instant rollback
You can quickly revert to a previous version of your firewall configuration. This can be useful in situations that require a quick recovery from unexpected behavior or rule creation.
To restore to a previous version:
  1. From your dashboard, select the project that you'd like to configure a rule for and then select the Firewall tab
  2. Select the View Audit Log option by clicking on the ellipsis menu at the top right
  3. Find the version that you would like to restore to by using the date and time selectors
  4. Select Restore and then Restore Configuration on the confirmation modal


## Limits
Depending on your plan, there are limits for each Vercel WAF feature.
Feature| Hobby| Pro| Enterprise  
---|---|---|---  
Project level IP Blocking| Up to 10| Up to 100| Custom  
Account-level IP Blocking| N/A| N/A| Custom  
Custom Rules| Up to 3| Up to 40| Up to 1000  
Custom Rule Parameters| All| All| All  
Managed Rulesets| N/A| N/A| Contact sales  
  * For Account-level IP Blocking, CIDR rules are limited to `/16` for IPv4 and `/48` for IPv6
  * For Custom Rule Parameters, JA3 (Legacy) is available on Enterprise plans


**Note:** If your project needs more than these limits or for managed rulesets, contact us to discuss the Enterprise plan.
Contact Sales
Last updated on December 12, 2024
Previous
DDoS Mitigation
Next
Custom Rules
Was this helpful?
supported.
Send
AskAsk v0
Web Application FirewallAskAsk v0
