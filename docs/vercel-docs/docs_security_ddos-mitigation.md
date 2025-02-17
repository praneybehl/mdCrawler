![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-light.cf7eca76.svg)![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-dark.01246f11.svg)
Search...
`⌘ K`
Feedback
Log In
Sign Up
Security
Firewall
DDoS Mitigation
Conceptual
# DDoS Mitigation
Learn how the Vercel Firewall mitigates against DoS and DDoS attacks
Table of Contents
DDoS Mitigation is available on all plans
Vercel provides automatic DDoS mitigation for all deployments, regardless of the plan that you are on. We block incoming traffic if we identify abnormal or suspicious levels of incoming requests. It works by:
  * Monitoring traffic: Vercel Firewall continuously analyzes incoming traffic to detect signs of DDoS attacks. This helps to identify and mitigate threats in real-time
  * Blocking traffic: Vercel Firewall filters out malicious traffic while allowing legitimate requests to pass through
  * Scaling resources: During a DDoS attack, Vercel Firewall dynamically scales resources to absorb the increased traffic, preventing your applications or sites from being overwhelmed


If you need further control over incoming traffic, you can temporarily enable Attack Challenge Mode to challenge all traffic to your site, ensuring only legitimate users can access it.
**Note:** If you need dedicated DDoS support, contact us to discuss Enterprise.
Contact Sales
## Understanding DDoS
Learn more about DoS, DDoS and the Open System Interconnection model.
Understanding DDoS
## Responding to DDoS attacks
Vercel mitigates against L3, L4, and L7 DDoS attacks regardless of the plan you are on. The Vercel Firewall uses hundreds of signals and detection factors to fingerprint request patterns, determining if they appear to be an attack, and challenging or blocking requests if they appear illegitimate.
However, there are other steps you can take to protect your site during DDoS attacks:
  * Enable Attack Challenge Mode to challenge all visitors to your site. This is a temporary measure and provides another layer of security to ensure all traffic to your site is legitimate
  * You can set up IP Blocking to block specific IP addresses from accessing your projects. Enterprise teams can also receive dedicated DDoS support
  * You can add Custom Rules to deny or challenge specific traffic to your site based on the conditions of the rules
  * You can also use Edge Middleware to block requests based on specific criteria or to implement rate limiting.


Pro teams can set up Spend Management to get notified or to automatically take action, such as using a webhook or pausing your projects when your usage hits a set spend amount.
## Bypass System-level Mitigations
Bypass System-level Mitigations are available on Pro and Enterprise plans
While Vercel's system-level mitigations (such as DDoS protection) safeguards your websites and applications, it can happen that they block traffic from trusted sources like proxies or shared networks in situations where traffic from these proxies or shared networks was identified as malicious. You can temporarily disable all automatic mitigations for a specific project. This can be useful on business-critical events such as Black Friday.
To temporarily disable all automatic mitigations for a specific project:
  1. Click the menu button with the ellipsis icon at the top right of the Firewall tab for your project.
  2. Select Disable System Mitigations.
This will not disable any Web Application Firewall IP Blocking, Custom Rule or Managed Ruleset set up on your project.
  3. Review the warning in the Disable All System Mitigations dialog and confirm that you would like to disable all automatic mitigations for that project for the next 24 hours.


To enable the automatic mitigations before the 24 hour period ends:
  1. Click the menu button with the ellipsis icon at the top right of the Firewall tab for your project.
  2. Select Enable System Mitigations.
  3. Select Enable from the Enable All System Mitigations dialog.


You are responsible for all usage fees incurred when using this feature, including illegitimate traffic that may otherwise have been blocked.
### System Bypass Rules
In situations where you need a more granular and permanent approach, you can use System Bypass Rules to ensure that essential traffic is never blocked by DDoS protection.
This feature is available for Pro and Enterprise customers. Learn how to set up a System Bypass rule for your project and limits that apply based on your plan.
## Dedicated DDoS support for Enterprise teams
Dedicated DDoS support is available on Enterprise plans
For larger, distributed attacks on Enterprise Teams, we collaborate with you to keep your site(s) online during an attack. Automated prevention and direct communication from our Customer Success Managers ensure your site remains resilient.
Contact our sales team to learn more:
Contact Sales
## DDoS and billing
Vercel automatically mitigates against L3, L4, and L7 DDoS attacks at the platform level for all plans. Vercel does not charge customers for traffic that gets blocked by the Firewall.
Usage will be incurred for requests that are successfully served prior to us automatically mitigating the event. Usage will also be incurred for requests that are not recognized as a DDoS event, which may include bot and crawler traffic.
For an additional layer of security, we recommend that you enable Attack Challenge Mode when you are under attack, which is available for free on all plans. While some malicious traffic is automatically challenged, enabling Attack Challenge Mode will challenge all traffic, including legitimate traffic to ensure that only real users can access your site.
You can monitor usage in the Vercel Dashboard under the Usage tab, although you will receive notifications when nearing your usage limits.
Last updated on December 20, 2024
Previous
Firewall
Next
Web Application Firewall
Was this helpful?
supported.
Send
AskAsk v0
DDoS MitigationAskAsk v0
