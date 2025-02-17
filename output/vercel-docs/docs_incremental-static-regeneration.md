![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-light.cf7eca76.svg)![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-dark.01246f11.svg)
Search...
`⌘ K`
Feedback
Log In
Sign Up
Infrastructure
Incremental Static Regeneration
Reference
# Incremental Static Regeneration (ISR)
Learn how Vercel's Incremental Static Regeneration (ISR) provides better performance and faster builds.
Table of Contents
Next.js (/app)
Incremental Static Regeneration is available on all plans
Incremental Static Regeneration (ISR) allows you to create or update content on your site without redeploying. ISR's main benefits for developers include:
  1. Better Performance: Static pages can be consistently fast because ISR allows Vercel to cache generated pages in every region on our global Edge Network and persist files into durable storage
  2. Reduced Backend Load: ISR helps reduce backend load by using cached content to make fewer requests to your data sources
  3. Faster Builds: Pages can be generated when requested by a visitor or through an API instead of during the build, speeding up build times as your application grows


ISR is available to applications built with:
  * Next.js
  * SvelteKit
  * Nuxt
  * Astro
  * Gatsby
  * Or any custom framework solution that implements the Build Output API


Get started in minutes
## Explore ISR with a project template
View All Templates
![On-Demand ISR](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F5TY3yVmUYix5mHgfUjhSD0%2Fe505b67dc1ff11c76e1cff9f680ad74f%2FCleanShot_2022-04-13_at_17.12.05_2x.png&w=1200&q=75)
On-Demand ISR
Instantly update content without redeploying.
![ISR Blog with Next.js and WordPress](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F2QHjwNHn9NzlflFlEqcwJv%2F1f7b5363a4a4591c4a85d106c868da71%2FCleanShot_2022-08-08_at_15.58.48.png&w=1200&q=75)
ISR Blog with Next.js and WordPress
An Incremental Static Regeneration Blog Example Using Next.js and WordPress
![SvelteKit Route Config](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F2K2rLNPlEyw84WRZPb1ibk%2F309717064d1c0c915a10eedacd350c85%2FScreen_Shot_2023-03-23_at_10.29.30_PM.png&w=1200&q=75)
SvelteKit Route Config
This template shows how to configure Edge Functions, Serverless Functions, and ISR in SvelteKit applications on a per-route basis.
View All Templates
### Interested in the Enterprise plan?
Contact our sales team to learn more about the Enterprise plan and how it can benefit your team.
Contact Sales
## Using ISR with Next.js
Next.js will automatically create a Serverless Vercel Function that can revalidate when you add `next: { revalidate: 10 }` to the options object passed to a `fetch` request.
The following example demonstrates a Next.js page that uses ISR to render a list of blog posts:
Next.js (/app)Next.js (/pages)
app/blog-posts/page.tsx
TypeScript
TypeScriptJavaScript
```
exportconstrevalidate=10; // seconds
interfacePost {
 title:string;
 id:number;
}
exportdefaultasyncfunctionPage() {
constres=awaitfetch('https://api.vercel.app/blog');
constposts= (awaitres.json()) asPost[];
return (
  <ul>
   {posts.map((post: Post) => {
    return <li key={post.id}>{post.title}</li>;
   })}
</ul>
 );
}
```

Open inOpen in v0
To learn more about using ISR with Next.js in the App router, such as enabling on-demand revalidation, see the official Next.js documentation.
## Using ISR with SvelteKit or Nuxt
  * See our dedicated SvelteKit docs to learn how to use ISR with your SvelteKit projects on Vercel
  * See our dedicated Nuxt docs to use ISR with Nuxt


## Using ISR with the Build Output API
When using the Build Output API, the Serverless Vercel Functions generated for your ISR routes are called Prerender Functions.
Build Output API Prerender Functions are Serverless Functions with accompanying JSON files that describe the Function's cache invalidation rules. See our Prerender configuration file docs to learn more.
## Differences between ISR and `Cache-Control` headers
Both ISR and `Cache-Control` headers help reduce backend load by using cached content to make fewer requests to your data source. However, there are key architectural differences between the two.
  * Shared Global Cache: ISR has cache shielding built-in automatically, which helps improve the cache `HIT` ratio. The cache for your ISR route's Vercel Function output is distributed globally. In the case of a cache `MISS`, it looks up the value in a single, global bucket. With only `cache-control` headers, caches expire (by design) and are not shared across regions
  * 300ms Global Purges: When revalidating (either on-demand or in the background), your ISR route's Vercel Function is re-run, and the cache is brought up to date with the newest content within 300ms in all regions globally
  * Instant Rollbacks: ISR allows you to roll back instantly and not lose your previously generated pages by persisting them between deployments
  * Simplified Caching Experience: ISR abstracts common issues with HTTP-based caching implementations, adds additional features for availability and global performance, and provides a better developer experience for implementation


See our Cache control options docs to learn more about `Cache-Control` headers.
### ISR vs `Cache-Control` comparison table
ISR vs Cache-Control comparison tableFeature| ISR| Caching Headers  
---|---|---  
On-demand purging & regeneration| Limited   
Synchronized global purging| Limited   
Support for fallbacks upon `MISS`| N/A  
Durable storage| N/A  
Atomic updates| N/A  
Cache shielding| N/A  
Slow origin protection| Limited   
Automatic support for `stale-if-error`| Limited   
Automatic support for `stale-while-revalidate`  
Usage within popular frontend frameworks  
Caching static page responses  
## On-demand revalidation limits
On-demand revalidation is scoped to the domain and deployment where it occurs, and doesn't affect sub domains or other deployments.
For example, if you trigger on-demand revalidation for `example-domain.com/example-page`, it won't revalidate the same page served by sub domains on the same deployment, such as `sub.example-domain.com/example-page`.
See Revalidating across domains to learn how to get around this limitation.
## ISR pricing
When using ISR with a framework on Vercel, a function is created based on your framework code. This means that you incur usage when the ISR function is invoked, when ISR reads and writes occur, and on the Fast Origin Transfer:
  * You incur usage when the function is invoked – ISR functions are invoked whenever they revalidate in the background or through on-demand revalidation
  * You incur ISR writes when new content is stored in the ISR cache – Fresh content returned by ISR functions is persisted to durable storage for the duration you specify, until it goes unaccessed for 31 days
  * You incur Incur ISR reads when content is accessed from the ISR cache – The content served from the ISR cache when there is an edge-cache miss
  * You add to your Fast Origin Transfer usage


Explore your usage top paths to better understand ISR usage and pricing.
## More resources
### Observe your ISR routes to understand traffic and usage.
Monitor ISR on Vercel
### See Next's Caching docs to learn more about implementing ISR.
Next.js Caching
### Quickstart
### Get started using ISR on Vercel with Next.js or the Build Output API.
Incremental Static Regeneration Quickstart
Last updated on October 9, 2024
Previous
Managing Costs
Next
Quickstart
Was this helpful?
supported.
Send
AskAsk v0
Incremental Static Regeneration
Next.js (/app)
AskAsk v0
