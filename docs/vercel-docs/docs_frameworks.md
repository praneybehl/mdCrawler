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
Platform
Frameworks
Reference
# Frameworks on Vercel
Vercel supports a wide range of the most popular frontend frameworks, optimizing how your site builds and runs no matter what tool you use.
Table of Contents
Vercel has first-class support for a wide range of the most popular frontend frameworks. You can build your web applications with anything from Astro to SvelteKit, and in many cases deploy them without having to do any upfront configuration. Learn how to get started with Vercel or clone one of our example repos to your favorite git provider and deploy it on Vercel using one of the templates below:
Get started in minutes
## Deploy a Template
View All Templates
![Next.js Boilerplate](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F1aHobcZ8H6WY48u5CMXlOe%2F0f0efe6bd469985b692555fbcad1cc01%2Fnextjs-template.png&w=1200&q=75)
Next.js Boilerplate
Get started with Next.js and React in seconds.
![Nuxt.js 3 Boilerplate](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2FleiZ1j6r8MPRgnugYyWf3%2F01c94495dd082a948af73e871347c93e%2FCleanShot_2022-11-18_at_13.58.42_2x.png&w=1200&q=75)
Nuxt.js 3 Boilerplate
A Nuxt.js 3 app, bootstrapped with create-nuxt-app.
![SvelteKit Boilerplate](https://vercel.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2Fe5382hct74si%2F5WIYQtnSEfZKYFB9kvsR0w%2F974bee31f87aa376a54dccdb0713629d%2FCleanShot_2022-05-23_at_22.13.20_2x.png&w=1200&q=75)
SvelteKit Boilerplate
A SvelteKit app including nested routes, layouts, and page endpoints.
View All Templates
Vercel deployments can integrate with your git provider to generate preview URLs for each pull request you make to your project.
Deploying on Vercel with one of our supported frameworks gives you access to many features, such as:
  * Vercel Functions enable developers to write functions that scale based on traffic demands, preventing failures during peak hours and reducing costs during low activity.
  * Edge Middleware is code that executes before a request is processed on a site, enabling you to modify the response. Because it runs before the cache, Edge Middleware is an effective way to personalize statically generated content.
  * Multi-runtime Support allows the use of various runtimes for your functions, each with unique libraries, APIs, and features tailored to different technical requirements.
  * Incremental Static Regeneration enables content updates without redeployment. Vercel caches the page to serve it statically and rebuilds it on a specified interval.
  * Speed Insights provide data on your project's Core Web Vitals performance in the Vercel dashboard, helping you improve loading speed, responsiveness, and visual stability.
  * Analytics offer detailed insights into your website's performance over time, including metrics like top pages, top referrers, and user demographics.
  * Skew Protection uses version locking to ensure that the client and server use the same version of your application, preventing version skew and related errors.


## Frameworks infrastructure support matrix
The following table shows which features are supported by each framework on Vercel. The framework list represents the most popular frameworks deployed on Vercel.
    Supported
    Not Supported
    Not Applicable
Framework feature matrixFeature| Next.js| SvelteKit| Nuxt| Astro| Remix| Vite| Gatsby| CRA  
---|---|---|---|---|---|---|---|---  
Feature| Next.js| SvelteKit| Nuxt| Astro| Remix| Vite| Gatsby| CRA  
Static AssetsSupport for static assets being served and cached directly from the edge  
Edge Routing RulesLets you configure incoming requests, set headers, and cache responses  
Edge MiddlewareExecute code before a request is processed  
Server-Side RenderingRender pages dynamically on the server  
Streaming SSRStream responses and render parts of the UI as they become ready  
Incremental Static RegenerationCreate or update content on your site without redeploying  
Image OptimizationOptimize and cache images at the edge  
Data CacheA granular cache for storing responses from fetches  
Native OG Image GenerationGenerate dynamic open graph images using Vercel Functions  
Multi-runtime support (different routes)Customize runtime environments per route  
Multi-runtime support (entire app)Lets your whole application utilize different runtime environments  
Output File TracingAnalyzes build artifacts to identify and include only necessary files for the runtime  
Skew ProtectionEnsure that only the latest deployment version serves your traffic by not serving older versions of code  
Native Edge MiddlewareFramework-native integrated middleware convention  
## Build Output API
The Build Output API is a file-system-based specification for a directory structure that produces a Vercel deployment. It is primarily targeted at framework authors who want to integrate their frameworks with Vercel's platform features. By implementing this directory structure as the output of their build command, framework authors can utilize all Vercel platform features, such as Serverless Functions, Edge Functions, Routing, and Caching.
If you are not using a framework, you can still use these features by manually creating and populating the `.vercel/output` directory according to this specification. Complete examples of Build Output API directories can be found in vercel/examples, and you can read our blog post on using the Build Output API to build your own framework with Vercel.
## More resources
Learn more about deploying your preferred framework on Vercel with the following resources:
Reference
### See a full list of supported frameworks
Browse our list of supported frameworks.
Templates
### Explore our template marketplace
Browse popular frameworks and deploy them with Vercel.
Conceptual
### Learn about our deployment features
See how Vercel can help you deploy your projects.
Last updated on August 12, 2024
Previous
Technical Guidelines
Next
Next.js
Was this helpful?
supported.
Send
AskAsk v0
FrameworksAskAsk v0
