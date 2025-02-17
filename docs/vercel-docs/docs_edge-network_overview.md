![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-light.cf7eca76.svg)![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-dark.01246f11.svg)
Search...
`⌘ K`
Feedback
Log In
Sign Up
Infrastructure
Edge Network
# Edge Network
Table of Contents
Vercel's Edge Network lets you store content close to your customers and compute in regions close to your data, reducing latency and improving end-user performance.
Our Edge Network is both a Content Delivery Network (CDN) and a globally distributed platform for running compute in regions around the globe.
If you're deploying an app on Vercel, you already use our Edge Network. These docs will teach you how to optimize your apps and deployment configuration to get the best performance for your use case.
![Our global Edge Network has 119 Points of Presence in 94 cities across 51 countries.](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1724702247%2Ffront%2Fdocs%2Fedge-network%2Flight-pops.png&w=1920&q=75)![Our global Edge Network has 119 Points of Presence in 94 cities across 51 countries.](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1724702247%2Ffront%2Fdocs%2Fedge-network%2Fdark-pops.png&w=1920&q=75)Our global Edge Network has 119 Points of Presence in 94 cities across 51 countries.
## Global network architecture
Vercel's Edge Network is built on a robust global infrastructure designed for optimal performance and reliability:
  * Points of Presence (PoPs): Our network includes over 100 PoPs distributed worldwide. These PoPs act as the first point of contact for incoming requests and route requests to the nearest Edge region.
  * Edge Regions: Behind these PoPs, we maintain 18 compute-capable regions where your code runs close to your data.
  * Private Network: Traffic flows through private, low-latency connections from PoPs to the nearest Edge region, ensuring fast and efficient data transfer.


This architecture balances the widespread geographical distribution benefits with the efficiency of concentrated caching and computing resources. By maintaining fewer, dense regions, we increase cache hit probabilities while ensuring low-latency access through our extensive PoP network.
## Features
  * Redirects: Redirects tell the client to make a new request to a different URL. They are useful for enforcing HTTPS, redirecting users, and directing traffic.
  * Rewrites: Rewrites change the URL the server uses to fetch the requested resource internally, allowing for dynamic content and improved routing.
  * Headers: Headers can modify the request and response headers, improving security, performance, and functionality.
  * Caching: Caching stores responses at the edge, reducing latency and improving performance
  * Streaming: Streaming enhances your user's perception of your app's speed and performance.
  * HTTPS / SSL: Vercel serves every deployment over an HTTPS connection by automatically provisioning SSL certificates.
  * Compression: Compression reduces data transfer and improves performance, supporting both gzip and brotli compression.


## Pricing
Vercel's Edge Network pricing is divided into three resources:
  * Fast Data Transfer: Data transfer between the Vercel Edge Network and the user's device.
  * Fast Origin Transfer: Data transfer between the Edge Network and Vercel Functions.
  * Edge Requests: Requests made to the Edge Network.

![An overview of how items relate to the Edge Network](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1712323807%2Ffront%2Fdocs%2Fpricing%2Fpricing-blog-light.png&w=3840&q=75)![An overview of how items relate to the Edge Network](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1712323806%2Ffront%2Fdocs%2Fpricing%2Fpricing-infradark.png&w=3840&q=75)An overview of how items relate to the Edge Network
All resources are billed based on usage with each plan having an included allotment. Those on the Pro plan are billed according to additional allotments.
The pricing for each resource is based on the region from which requests to your site come. Use the dropdown to select your preferred region and see the pricing for each resource.
Select a Region
Cape Town, South Africa (cpt1)Cleveland, USA (cle1)Dublin, Ireland (dub1)Frankfurt, Germany (fra1)Hong Kong (hkg1)London, United Kingdom (lhr1)Mumbai, India (bom1)Osaka, Japan (kix1)Paris, France (cdg1)Portland, USA (pdx1)San Francisco, USA (sfo1)São Paulo, Brazil (gru1)Seoul, South Korea (icn1)Singapore (sin1)Stockholm, Sweden (arn1)Sydney, Australia (syd1)Tokyo, Japan (hnd1)Washington, D.C., USA (iad1)
Managed Infrastructure pricingResource| Hobby Included| Pro Included| Pro Extra  
---|---|---|---  
Resource| Hobby Included| Pro Included| Pro Extra  
Fast Data Transfer| First 100 GB| First 1 TB| $0.15 per 1 GB  
Fast Origin Transfer| First 10 GB| First 100 GB| $0.06 per 1 GB  
Edge Requests| First 1,000,000| First 10,000,000| $2.00 per 1,000,000 Requests  
## Usage
The table below shows the metrics for the Networking section of the Usage dashboard.
To view information on managing each resource, select the resource link in the Metric column. To jump straight to guidance on optimization, select the corresponding resource link in the Optimize column.
Manage and Optimize pricingMetric| Description| Priced| Optimize  
---|---|---|---  
Top Paths| The paths that consume the most resources on your team| N/A| N/A  
Fast Data Transfer| The data transfer between Vercel's Edge Network and your sites' end users.| Yes| Learn More  
Fast Origin Transfer| The data transfer between Vercel's Edge Network to Vercel Compute| Yes| Learn More  
Edge Requests| The number of cached and uncached requests that your deployments have received| Yes| Learn More  
See the manage and optimize networking usage section for more information on how to optimize your usage.
## Supported protocols
The Edge Network supports the following protocols (negotiated with ALPN):
  * HTTPS
  * HTTP/1.1
  * HTTP/2


## Using Vercel's Edge Network locally
Vercel supports 35 frontend frameworks. These frameworks provide a local development environment used to test your app before deploying to Vercel.
Through framework-defined infrastructure, Vercel then transforms your framework build outputs into globally managed infrastructure for production.
If you are using Vercel Functions or other compute on Vercel _without_ a framework, you can use the Vercel CLI to test your code locally with `vercel dev`.
## Using Vercel's Edge Network with other CDNs
While sometimes necessary, proceed with caution when you place another CDN in front of Vercel:
  * Vercel's Edge Network is designed to deploy new releases of your site without downtime by purging the Edge Network cache globally and replacing the current deployment.
  * If you use an additional CDN in front of Vercel, it can cause issues because Vercel has no control over the other provider, leading to the serving of stale content or returning 404 errors.
  * To avoid these problems while still using another CDN, we recommend you either configure a short cache time or disable the cache entirely. Visit the documentation for your preferred CDN to learn how to do either option or learn more about using a proxy in front of Vercel.


Last updated on December 19, 2024
Previous
Infrastructure
Next
Regions
Was this helpful?
supported.
Send
AskAsk v0
Edge NetworkAskAsk v0
