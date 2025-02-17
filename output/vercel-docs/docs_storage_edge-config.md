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
Storage
Edge Config
# Vercel Edge Config
An Edge Config is a global data store that enables experimentation with feature flags, A/B testing, critical redirects, and more.
Table of Contents
Edge Config is available on all plans
An Edge Config is a global data store that enables experimentation with feature flags, A/B testing, critical redirects, and IP blocking. It enables you to read data at the edge without querying an external database or hitting upstream servers.
With Vercel's optimizations, you can read Edge Config data at negligible latency. The vast majority of your reads will complete within 15ms at P99, or as low as 0ms in some scenarios.
You can use an Edge Config in Edge Middleware and Vercel Functions.
Vercel's Edge Config read optimizations are only available on the Edge and Node.js runtimes. Optimizations can be enabled for other runtimes,  such as Ruby, Go, and Python  upon request. See  our Edge Config limits docs  to learn more.
## Use cases
Edge Configs are great for data that is accessed frequently and updated infrequently. Here are some examples of storage data suitable for Edge Config:
**Feature flags and A/B testing** : Experiment with A/B testing by storing feature flags in your Edge Config. Fetching such data from Edge Config rather than a database can cut page loads by hundreds of milliseconds.  Deploy the template 
**Critical redirects** : When you need to redirect a URL urgently, Edge Configs offer a fast solution that doesn't require you to redeploy your website. With Edge Middleware, you can read from your Edge Config to redirect users visiting incorrect URLs. For an example, see the Maintenance Page template .
Alternatively, use the Vercel WAF to configure a Redirect action based on specific conditions. For more details, check the emergency redirect example.
**Malicious IP and User Agent blocking** : Store a set of malicious IPs in your Edge Config, then block them upon detection without invoking upstream servers
## Getting started
You can create and manage your Edge Config from either Vercel REST API or Dashboard. You can scope your Edge Configs to your Hobby team or team, and connect them to as many projects as you want.
To get started, see our quickstart.
Get started in minutes
## Deploy an Edge Config Template
View All Templates
![LaunchDarkly Integration example](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F5at5W00aNo6noTLTx7q8AM%2F158dc4f49131706f60864f37861c675f%2FCleanShot_2023-06-20_at_12.43.11.png&w=1200&q=75)
LaunchDarkly Integration example
Learn how to set up the LaunchDarkly integration to read flags from Edge Config
![Dynamic Model Usage with AI SDK](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F0YgPDxAUUI9MD8EhGCbI5%2Fec6e59b3d4615792ec32f398397b72df%2FUntitled_design__3_.png&w=1200&q=75)
Dynamic Model Usage with AI SDK
A chatbot that allows you to dynamically set the LLM using Vercel AI SDK with Feature Flags and Edge Config
![Maintenance Page](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F4MY7E65qHkruy3TluLsB0S%2Fdd589bb3288c370326295a088d001512%2Fmaintenance-page.png&w=1200&q=75)
Maintenance Page
This template shows how to quickly trigger a maintenance page using Edge Config
View All Templates
## Using Edge Config in your workflow
If you'd like to know whether or not Edge Config can be integrated into your workflow, it's worth knowing the following:
  * You can have one or more Edge Configs per Vercel account, depending on your plan as explained in Limits
  * You can use multiple Edge Configs in one Vercel project
  * Each Edge Config can be accessed by multiple Vercel projects
  * Edge Configs can be scoped to different environments within projects using environment variables
  * Edge Config access is secure by default. A read access token is required to read from them, and an API token is required to write to them


See our Edge Config limits docs to learn more
## Why use Edge Config instead of alternatives?
There are alternative solutions to Edge Config for handling A/B testing, feature flags, and IP blocking. The following table lays out how those solutions compare to Edge Config:
Edge Config vs alternatives| Read latency| Write latency| Redeployment required| Added risk of downtime  
---|---|---|---|---  
Edge Config| Ultra-low | Varies | No | No  
Remote JSON files| Varies | Varies| No | Yes   
Embedded JSON files| Lowest| Highest | Yes | No  
Environment Variables| Lowest| Highest | Yes | No  
## Limits
To learn about Edge Config limits and pricing, see our Edge Config limits docs.
## More resources
### Quickstart
Create and read from your Edge Config in minutes.
### Read with the SDK
Read from your Edge Config at the fastest speeds.
### Use the Dashboard
Manage your Edge Configs in the Vercel dashboard.
### Manage with the API
Manage your Edge Configs with the Vercel API.
### Edge Config Limits
Learn about the limits of Edge Configs.
Last updated on September 26, 2024
Previous
Usage & Pricing
Next
Quickstart
Was this helpful?
supported.
Send
AskAsk v0
Edge ConfigAskAsk v0
