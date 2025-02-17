![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-light.cf7eca76.svg)![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-dark.01246f11.svg)
Search...
`⌘ K`
Feedback
Log In
Sign Up
# Vercel Storage
Store key-value data, transactional data, large files, and more with Vercel's suite of storage products.
Table of Contents
Vercel KV and Vercel Postgres migration
The migration for Pro and Hobby customers has been successfully completed. As part of our transition to the Vercel Marketplace, Vercel KV and Vercel Postgres will no longer be available as standalone services and we plan to transition these services to the Vercel Marketplace by the end of February.
For guidance on migrating Vercel Postgres storage, review the Vercel Postgres Transition Guide.
Enterprise customers
If you are currently using Vercel KV or Vercel Postgres, please reach out to your account manager or customer success manager to discuss available migration options.
For alternative solutions, visit the Vercel Marketplace.
  * Explore Marketplace Redis (KV) integrations
  * Explore Marketplace Postgres integrations


Vercel offers a suite of managed, serverless storage products that integrate with your frontend framework.
  * Vercel Blob: Large file storage
  * Vercel Edge Config: Global, low-latency data store


This page will help you choose the right storage product for your use case.
## Choosing a storage product
Choosing the correct storage solution depends on your needs for latency, durability, and consistency, among many other considerations.
To help you choose, we've created a table below to summarize the benefits of each storage option in relation to each other:
Product| Reads| Writes| Use Case| Limits| Plans  
---|---|---|---|---|---  
Blob| Fast| Milliseconds| Large, content-addressable files ("blobs")| Learn more| Hobby, Pro  
Edge Config| Ultra-fast| Seconds| Runtime configuration (e.g., feature flags)| Learn more| Hobby, Pro, Enterprise  
Read our section on best practices to get the most out of our storage products.
## Vercel Blob
Vercel Blob is available in Beta on Hobby and Pro plans
Those with the owner, member, developer role can access this feature
Vercel Blob offers optimized storage for images, videos, and other files.
You should use Vercel Blob if you need to:
  * Store images: For example, storing user avatars or product images
  * Store videos: For example, storing user-generated video content


### Explore Vercel Blob
  * Overview
  * Quickstart


## Edge Config
Edge Config is available on all plans
An Edge Config is a global data store that enables you to read data at the edge without querying an external database or hitting upstream servers. Most lookups return in less than 1ms, and 99% of reads will return under 10ms.
You should use Edge Config if you need to:
  * Fetch data at ultra-low latency: For example, you should store feature flags in an Edge Config store.
  * Store data that is read often but changes rarely: For example, you should store critical redirect URLs in an Edge Config store.
  * Read data in every region: Edge Config data is actively replicated to all regions in the Vercel Edge Network.


### Explore Edge Config
  * Overview
  * Quickstart
  * Limits & Pricing


## Best practices
When choosing a storage option, we recommend considering these best practices:
### Locate your data close to your functions
To ensure low-latency responses, it's crucial to have compute close to your databases. Always deploy your databases in regions closest to your Functions to avoid long network roundtrips.
  * Serverless Functions: Defaults to `iad1`, but can be deployed to any region 
    * If using Vercel Postgres, ensure your database is in the same region as your Function
    * If using Vercel KV and replicated regions, place your stores in the same regions as your Functions
    * If using Vercel Postgres, ensure your database is in the same region as your Function
    * If using Vercel KV and replicated regions, place your stores in the same regions as your Functions
  * Edge Middleware: Global only; always executed in the region nearest the user 
    * Since Edge Middleware as part of request processing, it is best suited for extremely fast and globally replicated data like Edge Config


### Optimize for high cache hit rates
Vercel's Edge Network provides caching in every region globally. To ensure the fastest response times, ensure data fetched from your data store is properly cached at the Edge.
Incremental Static Regeneration automates properly setting up caching headers and globally storing generated assets for you. This ensures the highest availability for your traffic and prevents accidental misconfiguration of cache-control headers.
You can manually configure cache-control headers when using Vercel Functions to cache the response data in every Edge region. Edge Middleware runs before the Edge Network cache layer and cannot use cache-control headers.
Last updated on December 17, 2024
Next
Vercel Blob
Was this helpful?
supported.
Send
AskAsk v0
StorageAskAsk v0
