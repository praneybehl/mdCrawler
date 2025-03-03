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
Using Pages Router
Features available in /pages
Using Latest Version
15.2.0
Using Pages Router
Features available in /pages
Using Latest Version
15.2.0
Configurationnext.config.js OptionsbundlePagesRouterDependencies
# bundlePagesRouterDependencies
Enable automatic server-side dependency bundling for Pages Router applications. Matches the automatic dependency bundling in App Router.
next.config.js
```
/** @type{import('next').NextConfig} */
constnextConfig= {
 bundlePagesRouterDependencies:true,
}
module.exports= nextConfig
```

Explicitly opt-out certain packages from being bundled using the `serverExternalPackages` option.
## Version History
Version| Changes  
---|---  
`v15.0.0`| Moved from experimental to stable. Renamed from `bundlePagesExternals` to `bundlePagesRouterDependencies`  
Was this helpful?
supported.
Send
