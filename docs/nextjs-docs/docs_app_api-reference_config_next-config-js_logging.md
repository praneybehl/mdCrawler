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
Configurationnext.config.jslogging
# logging
## Options
### Fetching
You can configure the logging level and whether the full URL is logged to the console when running Next.js in development mode.
Currently, `logging` only applies to data fetching using the `fetch` API. It does not yet apply to other logs inside of Next.js.
next.config.js
```
module.exports= {
 logging: {
  fetches: {
   fullUrl:true,
  },
 },
}
```

Any `fetch` requests that are restored from the Server Components HMR cache are not logged by default. However, this can be enabled by setting `logging.fetches.hmrRefreshes` to `true`.
next.config.js
```
module.exports= {
 logging: {
  fetches: {
   hmrRefreshes:true,
  },
 },
}
```

### Incoming Requests
By default all the incoming requests will be logged in the console during development. You can use the `incomingRequests` option to decide which requests to ignore. Since this is only logged in development, this option doesn't affect production builds.
next.config.js
```
module.exports= {
 logging: {
  incomingRequests: {
   ignore: [/\api\/v1\/health/],
  },
 },
}
```

Or you can disable incoming request logging by setting `incomingRequests` to `false`.
next.config.js
```
module.exports= {
 logging: {
  incomingRequests:false,
 },
}
```

### Disabling Logging
In addition, you can disable the development logging by setting `logging` to `false`.
next.config.js
```
module.exports= {
 logging:false,
}
```

Was this helpful?
supported.
Send
