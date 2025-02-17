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
Infrastructure
Vercel Functions
# Vercel Functions
Vercel Functions allow you to run server-side code without managing a server.
Table of Contents
Next.js (/app)
Vercel Functions lets you run server-side code without managing servers. They adapt automatically to user demand, handle connections to APIs and databases, and offer enhanced concurrency through fluid compute, which is useful for AI workloads or any I/O-bound tasks that require efficient scaling
When you deploy your application, Vercel automatically sets up the tools and optimizations for your chosen framework. It ensures low latency by routing traffic through Vercel's Edge Network, and placing your functions in a specific region when you need more control over data locality.
![Functions location within Vercel's managed infrastructure](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1737717848%2Ffront%2Fdocs%2Fvercel-functions%2Ffirst_image_light.png&w=3840&q=75)![Functions location within Vercel's managed infrastructure](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1737717848%2Ffront%2Fdocs%2Fvercel-functions%2Ffirst_image_dark.png&w=3840&q=75)Functions location within Vercel's managed infrastructure
## Getting started
To get started with creating your first function, copy the code below:
Next.js (/app)Next.js (/pages)Other frameworks
app/api/hello/route.ts
TypeScript
TypeScriptJavaScript
```
exportfunctionGET(request:Request) {
returnnewResponse('Hello from Vercel!');
}
```

Open inOpen in v0
To learn more, see the quickstart or deploy a template.
## Functions lifecycle
Vercel Functions run in a single region by default, although you can configure them to run if you have globally replicated data. These functions let you add extra capabilities to your application, such as handling authentication, streaming data, or querying databases.
When a user sends a request to your site, Vercel can automatically run a function based on your application code. You do not need to manage servers, or handle scaling.
Vercel creates a new function invocation for each incoming request. If another request arrives soon after the previous one, Vercel reuses the same function instance to optimize performance and cost efficiency. Over time, Vercel only keeps as many active functions as needed to handle your traffic. Vercel scales your functions down to zero when there are no incoming requests.
By allowing concurrent execution within the same instance (and so using idle time for compute), fluid compute reduces cold starts, lowers latency, and saves on compute costs. It also prevents the need to spin up multiple isolated instances when tasks spend most of their time waiting for external operations.
### Functions and your data source
Functions should always execute close to where your data source is to reduce latency. By default, functions using the Node.js runtime execute in Washington, D.C., USA (`iad1`), a common location for external data sources. You can set a new region through your project's settings on Vercel.
## Viewing Vercel Function metrics
You can view various performance and cost efficiency metrics using Vercel Observability:
  1. Choose your project from the dashboard.
  2. Click on the Observability tab and select the Vercel Functions section.
  3. Click on the chevron icon to expand and see all charts.


From here, you'll be able to see total consumed and saved GB-Hours, and the ratio of the saved usage. When you have fluid enabled, you will also see the amount of cost savings from the optimized concurrency model.
## Related
  * What is compute?
  * What is streaming?
  * Fluid compute
  * Runtimes
  * Configuring functions
  * Streaming
  * Limits
  * Functions logs


Last updated on October 3, 2024
Previous
Directory Listing
Next
Quickstart
Was this helpful?
supported.
Send
AskAsk v0
Vercel Functions
Next.js (/app)
AskAsk v0
