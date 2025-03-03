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
API ReferenceFile Conventionsloading.js
# loading.js
A **loading** file can create instant loading states built on Suspense.
By default, this file is a Server Component - but can also be used as a Client Component through the `"use client"` directive.
app/feed/loading.tsx
TypeScript
JavaScriptTypeScript
```
exportdefaultfunctionLoading() {
// Or a custom loading skeleton component
return <p>Loading...</p>
}
```

Loading UI components do not accept any parameters.
> **Good to know** :
>   * While designing loading UI, you may find it helpful to use the React Developer Tools to manually toggle Suspense boundaries.
> 

## Version History
Version| Changes  
---|---  
`v13.0.0`| `loading` introduced.  
Was this helpful?
supported.
Send
