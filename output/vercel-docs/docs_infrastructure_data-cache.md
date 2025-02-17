![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-light.cf7eca76.svg)![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-dark.01246f11.svg)
Search...
`⌘ K`
Feedback
Log In
Sign Up
Infrastructure
Data Cache
Conceptual
# Vercel Data Cache
Vercel Data Cache is a specialized cache that stores responses from data fetches. Learn more about how it works with Next.js
Table of Contents
Next.js (/app)
Data Cache is available in Beta on all plans
The Vercel Data Cache is a specialized, granular cache for storing responses from fetches while using frontend frameworks like Next.js.
Frameworks that integrate with the Data Cache (currently Next.js) are able to cache data per fetch instead of per route. This means you can have static, dynamic, and revalidated data together in the same route.
With Vercel, you write application code, like component-level data fetching with `fetch`, and we scaffold globally distributed infrastructure for you with no additional effort. See our examples to learn how to implement this.
## Features
  * Ephemeral, globally available, regional cache: Every region in which your function runs has an independent cache, so any data used in server side rendering or Next.js route handlers is cached close to where the function executes.
  * Time-based revalidation: All cached data can define a revalidation interval, after which the data will be marked as stale, triggering a re-fetch from origin.
  * On-demand revalidation: Any data can be triggered for revalidation on-demand, regardless of the revalidation interval. The revalidation propagates to all regions within 300ms.
  * Tag based revalidation: Next.js allows associating tags with data, which can be used to revalidate all data with the same tag at once with `revalidateTag`. For example, you could use this to revalidate all responses from a CMS with the same author ID tag.


## Comparing with ISR and Edge Cache
Next.js combines Vercel Data Cache with Incremental Static Regeneration (ISR) to provide optimized caching infrastructure for your pages.
When a page contains _entirely static data_ , Vercel will use ISR to generate the whole page. However, when a page contains a _mix of static and dynamic data_ , the dynamic data needs to be re-fetched when rendering the page. In this scenario, Vercel Data Cache is used to cache the static data to avoid slow origin fetches.
Both ISR and Vercel Data Cache support time-based revalidation, on-demand revalidation, and tag based revalidation.
Vercel's Edge Cache is used for caching entire static assets at the edge, such as images, fonts, and JavaScript bundles. The Vercel Data Cache is used for caching data fetched during a function's execution, such as API responses.
## Managing Data Cache
When you deploy a Next.js project that uses App Router to Vercel, the Vercel Data Cache is automatically enabled to cache segment-level data alongside ISR in the app router.
To learn more about managing your Data Cache, including disabling it, and purging the cache, see Managing Data Cache.
## Examples
These examples use the Next.js App Router:
### Time-based revalidation
Next.js (/app)Next.js (/pages)
app/page.tsx
TypeScript
TypeScriptJavaScript
```
exportdefaultasyncfunctionPage() {
constres=awaitfetch('https://api.vercel.app/blog', {
  next: {
   revalidate:3600,// 1 hour
  },
 });
constdata=awaitres.json();
return'...';
}
```

Open inOpen in v0
### Tag-based revalidation
app/page.tsx
TypeScript
TypeScriptJavaScript
```
exportdefaultasyncfunctionPage() {
constres=awaitfetch('https://api.vercel.app/blog', {
  next: {
   tags: ['blog'],// Invalidate with revalidateTag('blog') on-demand
  },
 });
constdata=awaitres.json();
return'...';
}
```

Open inOpen in v0
app/actions.ts
TypeScript
TypeScriptJavaScript
```
'use server';
import { revalidateTag } from'next/cache';
exportdefaultasyncfunctionaction() {
revalidateTag('blog');
}
```

Open inOpen in v0
## Revalidation behavior
The Vercel Data Cache is unique per Vercel project, isolated per deployment environment (`production` or `preview`).
Cached data is persisted across deployments, unless invalidated through `revalidate` or programmatically calling `revalidateTag` or `revalidatePath`. It is not updated at build time. When invalidated, it will be updated at run time with the next new request to the path that was invalidated.
When a revalidation is triggered, the path or cache tag is marked stale globally in every Vercel Edge Network region. The next request to that path or tag, in any region, will trigger a revalidation and update the cache globally. The regional cache in all regions is purged and updated within 300ms.
## Limits
For information, see the usage page for the Data Cache.
## Additional resources
### Edge Regions
Learn more about the available regions for functions
### Next.js App Router template
Get started by deploying a Next.js project that uses App Router.
Last updated on September 23, 2024
Previous
Usage & Pricing
Next
Managing Data Cache
Was this helpful?
supported.
Send
AskAsk v0
Data Cache
Next.js (/app)
AskAsk v0
