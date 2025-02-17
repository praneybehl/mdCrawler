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
Edge Middleware
Conceptual
# Edge Middleware Overview
Learn how you can use Edge Middleware, code that executes before a request is processed on a site, to provide speed and personalization to your users.
Table of Contents
Next.js (/app)
Edge Middleware is available on all plans
Edge Middleware is code that executes _before_ a request is processed on a site. Based on the request, you can modify the response. Because it runs before the cache, using Middleware is an effective way of providing personalization to statically generated content. Depending on the incoming request, you can execute custom logic, rewrite, redirect, add headers and more, before returning a response.
![Edge Middleware location within Vercel infrastructure.](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1689795055%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Ffunctions%2Fedge-middleware-light.png&w=3840&q=75)![Edge Middleware location within Vercel infrastructure.](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1689795055%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Ffunctions%2Fedge-middleware-dark.png&w=3840&q=75)Edge Middleware location within Vercel infrastructure.
Middleware uses the Edge runtime, which exposes and extends a subset of Web Standard APIs such `FetchEvent`, `Response`, and `Request`. To learn more about writing Middleware, see the Middleware API docs.
## Create Edge Middleware
You can use Edge Middleware with any framework. To add Middleware to your app, you need to create a `middleware.ts` file at your project's root directory.
The `middleware.ts` file should be at the same level as your `app` or `pages` directory (even if you're using a `src` directory). See the  Quickstart  guide for more information.
Get started in minutes
## Deploy an Edge Middleware Template
View All Templates
![Modifying Request Headers in Middleware](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F1ICimocCMonK2k49FN399u%2Fa0d145707459a5ac197932dcdfa936ee%2Fedge-middleware-modify-request-header.vercel.app_.png&w=1200&q=75)
Modifying Request Headers in Middleware
Learn to add/update/delete request headers in a middleware.
![A/B Testing with Google Optimize](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F2mSbNPkZft2qRkqOfea2cI%2Fb7ebf7e5f7f1b2be93a9e55e7286a838%2Fedge-functions-ab-testing-google-optimize.vercel.app___1_.png&w=1200&q=75)
A/B Testing with Google Optimize
Learn to use Google Optimize as an A/B testing solution for experimentation at the edge.
![Hypertune Integration example](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F4ib2VQ78sWRVtRYR3UI5wa%2Fe1a1c054881e38c40f24b4f480de3fee%2Ffeature-flag-hypertune.vercel.app___1_.png&w=1200&q=75)
Hypertune Integration example
Learn to use Hypertune, a powerful feature flag, A/B testing, analytics and app configuration platform.
![Bot Protection with DataDome](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2FakurjrZdUB9bjsmOI1ShQ%2F9e6ffd8ffbd9fdf72fbbd08bf4e7e8a4%2Fedge-functions-bot-protection-datadome.vercel.app_.png&w=1200&q=75)
Bot Protection with DataDome
DataDome can provide real-time bot protection and other security protections to any website. In this template we'll be using it at the edge.
![JWT Authentication](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2FbdcXaoeIdSGU9q6FQ6s7x%2F8c61b9f68ab445823f2881ee2f450c10%2Fedge-functions-jwt-authentication.vercel.app_.png&w=1200&q=75)
JWT Authentication
Learn how to do JWT authentication at the edge.
![IP Blocking with DataDome](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F6mRWoyYv4iI9H5NE44sgsO%2F10a8fbc8324978779a8e6d02a1eec71f%2Fedge-functions-ip-blocking-datadome.vercel.app_.png&w=1200&q=75)
IP Blocking with DataDome
DataDome can provide real-time bot protection, ip blocking, custom rules protection and other security protections to any website.
View All Templates
## Logging
Edge Middleware has full support for the `console` API, including `time`, `debug`, `timeEnd`, etc. Logs will appear inside your Vercel project by clicking View Functions Logs next to the deployment.
## Using a database with Edge Middleware
If your Edge Middleware depends on a database far away from one of our Edge regions, the overall latency of API requests could be slower than expected. To avoid this issue, use a global database. Vercel has multiple global storage products, including Edge Config, Vercel KV, and Vercel Blob. See our storage docs to learn which option is best for you.
## More resources
Learn more about Edge Middleware by exploring the following resources:
### Deploy an Edge Middleware template
Deploy a project setup with Edge Middleware.
### Edge Middleware API
Learn about the available APIs when working with Edge Middleware.
### Usage and pricing
Learn about usage and pricing for using Edge Middleware with Vercel.
### Limitations
Learn about the limitations of using Edge Middleware with Vercel.
Last updated on July 16, 2024
Previous
Usage & Pricing
Next
Quickstart
Was this helpful?
supported.
Send
AskAsk v0
Edge Middleware
Next.js (/app)
AskAsk v0
