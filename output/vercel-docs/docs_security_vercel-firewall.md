![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-light.cf7eca76.svg)![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-dark.01246f11.svg)
Search...
`⌘ K`
Feedback
Log In
Sign Up
Security
Firewall
# Vercel Firewall
Learn how Vercel Firewall helps protect your applications and websites from malicious attacks and unauthorized access.
Table of Contents
The Vercel Firewall is a robust, multi-layered security system designed to protect your applications from a wide range of threats. Every incoming request goes through the following firewall layers:
  * Platform-wide firewall: With DDoS mitigation, it protects against large-scale attacks such as DDoS and TCP floods and is available for free for all customers without any configuration required.
  * Web Application Firewall (WAF): A customizable layer for fine-tuning security measures with logic tailored to your needs and observability into your web traffic.


### Concepts
Understand the fundamentals:
  * How Vercel protects every request.
  * Why DDoS needs to be mitigated.
  * How the firewall decides which rule to apply first.
  * How the firewall uses JA3 and JA4 TLS fingerprints to identify and restrict malicious traffic.


## Rule execution order
The automatic rules of the platform-wide firewall and the custom rules of the WAF work together in the following execution order:
  1. DDoS mitigation rules
  2. WAF IP blocking rules
  3. WAF custom rules
  4. Managed rulesets


When you have more than one custom rule, you can customize their order in the Firewall tab of the project.
## Platform-wide firewall
DDoS Mitigation is available on all plans
Vercel provides automated DDoS mitigation for all deployments, regardless of the plan that you are on. With this automated DDoS mitigation, we block incoming traffic if we identify abnormal or suspicious levels of incoming requests.
## Vercel WAF
Vercel WAF is available on all plans
Those with the member, viewer, developer and administrator roles can access this feature
The Vercel WAF complements the platform-wide firewall by allowing you to define custom protection strategies using the following tools:
  * Custom Rules
  * IP Blocking
  * Managed Rulesets
  * Attack Challenge Mode


## Observability
You can use the following tools to monitor the internet traffic at your team or project level:
  * The Monitoring feature at the team level allows you to create queries to visualize the traffic across your Vercel projects.
  * The Firewall tab of the Vercel dashboard on every project allows you to monitor the internet traffic to your deployments with a traffic monitoring view that includes a live traffic window.
  * Firewall alerts allow you to react quickly to potential security threats.
  * Use Log Drains to send your application logs to a Security Information and Event Management (SIEM) system.


Last updated on December 9, 2024
Previous
Encryption
Next
DDoS Mitigation
Was this helpful?
supported.
Send
AskAsk v0
FirewallAskAsk v0
