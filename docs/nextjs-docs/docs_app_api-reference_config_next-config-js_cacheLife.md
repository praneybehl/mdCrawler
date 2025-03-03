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
Menu
Using App Router
Features available in /app
Using Latest Version
15.2.0
Using App Router
Features available in /app
Using Latest Version
15.2.0
Configurationnext.config.jscacheLife
# cacheLife
This feature is currently available in the canary channel and subject to change. Try it out by upgrading Next.js, and share your feedback on GitHub.
The `cacheLife` option allows you to define **custom cache profiles** when using the `cacheLife` function inside components or functions, and within the scope of the `use cache` directive.
## Usage
To define a profile, enable the `dynamicIO` flag and add the cache profile in the `cacheLife` object in the `next.config.js` file. For example, a `blog` profile:
next.config.ts
TypeScript
JavaScriptTypeScript
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
 experimental: {
  dynamicIO:true,
  cacheLife: {
   blog: {
    stale:3600,// 1 hour
    revalidate:900,// 15 minutes
    expire:86400,// 1 day
   },
  },
 },
}
exportdefault nextConfig
```

You can now use this custom `blog` configuration in your component or function as follows:
app/actions.ts
TypeScript
JavaScriptTypeScript
```
import { unstable_cacheLife as cacheLife } from'next/cache'
exportasyncfunctiongetCachedData() {
'use cache'
cacheLife('blog')
constdata=awaitfetch('/api/data')
return data
}
```

## Reference
The configuration object has key values with the following format:
**Property**| **Value**| **Description**| **Requirement**  
---|---|---|---  
`stale`| `number`|  Duration the client should cache a value without checking the server.| Optional  
`revalidate`| `number`| Frequency at which the cache should refresh on the server; stale values may be served while revalidating.| Optional  
`expire`| `number`| Maximum duration for which a value can remain stale before switching to dynamic.| Optional - Must be longer than `revalidate`  
Was this helpful?
supported.
Send
