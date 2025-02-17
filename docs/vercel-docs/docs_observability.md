![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-light.cf7eca76.svg)![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-dark.01246f11.svg)
Search...
`⌘ K`
Feedback
Log In
Sign Up
# Observability
Observability on Vercel provides framework-aware insights enabling you to optimize infrastructure and application performance.
Table of Contents
Observability is available on all plans
Observability provides a way for you to monitor and analyze the performance and traffic of your projects on Vercel through a variety of events and insights, aligned with your app's architecture.
Users on all plans can use Observability to monitor their projects, while users on the Pro and Enterprise plans can upgrade to Observability Plus to get access to additional features and metrics, Monitoring access, higher limits, and increased retention.
Try Observability to get started.
![](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1733926757%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fobservability%2FO11y-Tab-Light.png&w=3840&q=75)![](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1733926756%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fobservability%2FO11y-Tab-Dark.png&w=3840&q=75)
## Observability Plus
Observability Plus is an optional upgrade that enables Pro and Enterprise teams to explore data at a more granular level, helping you to pinpoint exactly when and why issues occurred.
To learn more about Observability Plus, see Limitations or pricing.
### Enabling Observability Plus
By default, all users on all plans have access to Observability at both a team and project level.
To upgrade to Observability Plus:
  1. From your dashboard, navigate to the Observability tab.
  2. Next to the time range selector, click the button and select Upgrade to Observability Plus.
  3. From the Upgrade to Observability Plus modal, click Continue. 
     * If you're an existing Monitoring user, the modal will be Migrate from Monitoring to Observability Plus and will display the reduced pricing.
     * If you're an Enterprise user, you may be prompted to Contact Support to upgrade.
  4. Then, view the charges and click Confirm and Pay.


You'll be charged and upgraded immediately. You will immediately have access to the Observability Plus features and can view events based on data that was collected before you enabled it.
## Available insights
Observability provides a set of features that help you monitor, analyze, and manage your applications either at the team or the project level. The following table shows the availability of each feature at each level:
Feature| Team Level| Project Level  
---|---|---  
Vercel Functions| ✓| ✓  
Edge Functions| ✓| ✓  
External APIs| ✓| ✓  
Edge Requests| ✓| ✓  
Fast Data Transfer| ✓| ✓  
ISR (Incremental Static Regeneration)| ✓| ✓  
Build Diagnostics| ✓  
## Using Observability
How you use Observability depends on the needs of your project, for example, perhaps builds are taking longer than expected, or your serverless functions seem to be increasing in cost. A brief overview of how you might use the tab would be:
  1. Decide what feature you want to investigate. For example, Vercel Functions.
  2. Use the date picker or the time range selector to choose the time period you want to investigate. Users on Observability Plus will have a longer retention period and more granular data.
  3. Let's investigate our graphs in more detail, for example, Error Rate. Click and drag to select a period of time and press the Zoom In button. ![](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1733312925%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fobservability%2Ferror-rate-light.png&w=1080&q=75)![](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1733312925%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fobservability%2Ferror-rate-dark.png&w=1080&q=75)
  4. Then, from the list of routes below, choose to reorder either based on the error rate or the duration to get an idea of which routes are causing the most issues.
  5. To learn more about specific routes, click on the route.
  6. The functions view will show you the performance of each route or function, including details about the function, latency, paths, and External APIs. Note that Latency and breakdown by path are only available for Observability Plus users.
  7. The function view also provides a direct link to the logs for that function, enabling you to pinpoint the cause of the issue.


You can learn more about the specific sections of Observability below:
### Vercel Functions
The Vercel Functions tab provides a detailed view of the performance of your Vercel Functions. You can see the number of invocations and the error rate of your functions. You can also see the performance of your functions broken down by route.
For more information, see Vercel Functions. See understand the cost impact of function invocations for more information on how to optimize your functions.
### Edge Functions
The Edge Functions tab provides a detailed view of the performance of your Edge Functions. You can see the number of invocations and the error rate of your functions. You can also see the performance of your functions broken down by route.
For more information, see Vercel Functions.
### External APIs
You can use the External APIs tab to understand more information about requests from your functions to external APIs. You can organize by number of requests, p75 (latency), and error rate to help you understand potential causes for slow upstream times or timeouts.
#### External APIs Recipes
  * Investigate Latency Issues and Slowness on Vercel


### Edge Requests
You can use the Edge Requests tab to understand the requests to each of static and dynamic routes through the edge network. This includes the number of requests, the regions, and the requests that have been cached for each route.
### Fast Data Transfer
You can use the Fast Data Transfer tab to understand how data is being transferred within the edge network for your project.
For more information, see Fast Data Transfer.
### ISR (Incremental Static Regeneration)
You can use the ISR tab to understand your revalidations and cache hit ratio to help you optimize towards cached requests by default.
For more information on ISR, see Incremental Static Regeneration.
### Build Diagnostics
You can use the Build Diagnostics tab to view the performance of your builds. You can see the build time and resource usage for each of your builds. In addition, you can see the build time broken down by each step in the build and deploy process.
To learn more, see Builds.
## Pricing and limitations
Users on all plans can use Observability at no additional cost, with some limitations. The Observability tab is available on the project dashboard for all projects in the team.
Owners on Pro and Enterprise teams can upgrade to Observability Plus to get access to additional features higher limits, and increased retention.
For more information on pricing, see Pricing.
## Existing Monitoring users
Monitoring is now automatically included with Observability Plus and cannot be purchased separately. For existing Monitoring users, the Monitoring tab on your dashboard will continue to exist and can be used in the same way that you've always used it.
Teams that are currently paying for Monitoring, will not automatically see the Observability Plus features and benefits on the Observability tab, but will be able to see reduced pricing. In order to use Observability Plus you should migrate using the modal. Once you upgrade to Observability Plus, you cannot roll back to the original Monitoring plan. To learn more, see Monitoring Limits and Pricing.
In addition, teams that subscribe to Observability Plus will have access to the Monitoring tab and its features.
Last updated on December 18, 2024
Next
Limits & Pricing
Was this helpful?
supported.
Send
AskAsk v0
ObservabilityAskAsk v0
Interested in talking to
a Vercel product expert?
Schedule a call
