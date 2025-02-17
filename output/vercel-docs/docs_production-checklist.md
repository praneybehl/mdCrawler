![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-light.cf7eca76.svg)![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-dark.01246f11.svg)
Search...
`⌘ K`
Feedback
Log In
Sign Up
Platform
Going Live Checklist
Reference
# Production checklist for launch
Ensure your application is ready for launch with this comprehensive production checklist by the Vercel engineering team. Covering operational excellence, security, reliability, performance efficiency, and cost optimization.
Table of Contents
When launching your application on Vercel, it is important to ensure that it's ready for production. This checklist is prepared by the Vercel engineering team and designed to help you prepare your application for launch by running through a series of questions to ensure operational excellence, security, reliability, performance efficiency, and cost optimization.
## Operational excellence
  * Define an incident response plan for your team, including escalation paths, communication channels, and rollback strategies for deployments
  * Enable Monitoring to debug and optimize performance, investigate errors and traffic, and more
  * Familiarize yourself with the ability to promote and rollback
  * Ensure caching is configured if deploying using a monorepo to prevent unnecessary builds
  * Perform a zero downtime migration to Vercel DNS
  * Add a `www` subdomain and redirect your apex domain
  * Consider using v0 to quickly generate and iterate on React and Tailwind CSS components
  * Configure enhanced build hardware with larger memory and storage _(Enterprise plans only)_
  * Enable Conformance to run automated checks on your code for product critical issues, such as performance, security, and code health _(Enterprise plans only)_


## Security
  * Implement a Content Security Policy (CSP) and proper security headers
  * Enable Deployment Protection to prevent unauthorized access to your deployments
  * Configure the Vercel Web Application Firewall (WAF) to monitor, block, and challenge incoming traffic. This includes setting up custom rules, IP blocking, and enabling managed rulesets for enhanced security
  * Enable Log Drains to persist logs from your deployments
  * Review common SSL certificate issues
  * Enable a Preview Deployment Suffix to use a custom domain for Preview Deployments
  * Commit your lockfiles to pin dependencies and speed up builds through caching
  * Consider implementing rate limiting to prevent abuse
  * Consider allowing multi-tenant user applications to report abuse
  * Review and implement access roles to ensure the correct permissions are set for your team members
  * Enable SAML SSO and SCIM _(Enterprise plans with Owner role only)_
  * Enable Audit Logs to track and analyze team member activity _(Enterprise plans with Owner role only)_
  * Ensure that cookies comply with the allowed cookie policy to enhance security. _(Enterprise plans with Owner role only)_
  * Setup a firewall rule to block requests from unwanted bots to your project deploymentAdd firewall rule


## Reliability
  * Enable Monitoring to debug and optimize performance, investigate errors and traffic, and more
  * Enable automatic Function failover to add multi-region redundancy and protect against regional outages
  * Implement caching headers for static assets or Function responses to reduce usage or origin requests
  * Understand the differences between caching headers and Incremental Static Regeneration
  * Consider using OpenTelemetry to instrument your application for distributed tracing
  * Consider running a load test on your application to stress your upstream services _(Enterprise plans only)_


## Performance
  * Enable Speed Insights for instant access to field performance data and Core Web Vitals
  * Review your Time To First Byte (TTFB) to ensure your application is responding quickly
  * Ensure you are using Image Optimization to reduce the size of your images
  * Ensure you are using Script Optimization to optimize script loading performance
  * Ensure you are using Font Optimization to remove external network requests for improved privacy and performance
  * Ensure your Vercel Function region is the same as your origin API or database
  * Consider the limitations of placing a third-party proxy in front of Vercel


## Cost optimization
  * Follow our manage and optimize usage guides to understand how to optimize your usage, and manage your costs
  * Configure Spend Management to manage your usage and trigger alerts on usage changes
  * Review or adjust the maximum duration for your Vercel Functions
  * Ensure Incremental Static Regeneration (ISR) revalidation times are set appropriately to match content changes or move to on-demand revalidation
  * Ensure optimized images are using a consistent value for source images
  * Move large media files such as GIFs and videos to blob storage


Last updated on September 27, 2024
Previous
Troubleshooting Domains
Next
Pricing
Was this helpful?
supported.
Send
AskAsk v0
Going Live ChecklistAskAsk v0
Interested in white glove support
for your production rollout?
Schedule a call
