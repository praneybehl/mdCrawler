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
API ReferenceFile Conventionsdefault.js
# default.js
The `default.js` file is used to render a fallback within Parallel Routes when Next.js cannot recover a slot's active state after a full-page load.
During soft navigation, Next.js keeps track of the active _state_ (subpage) for each slot. However, for hard navigations (full-page load), Next.js cannot recover the active state. In this case, a `default.js` file can be rendered for subpages that don't match the current URL.
Consider the following folder structure. The `@team` slot has a `settings` page, but `@analytics` does not.
![Parallel Routes unmatched routes](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fparallel-routes-unmatched-routes.png&w=3840&q=75)![Parallel Routes unmatched routes](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fparallel-routes-unmatched-routes.png&w=3840&q=75)
When navigating to `/settings`, the `@team` slot will render the `settings` page while maintaining the currently active page for the `@analytics` slot.
On refresh, Next.js will render a `default.js` for `@analytics`. If `default.js` doesn't exist, a `404` is rendered instead.
Additionally, since `children` is an implicit slot, you also need to create a `default.js` file to render a fallback for `children` when Next.js cannot recover the active state of the parent page.
## Reference
### `params` (optional)
A promise that resolves to an object containing the dynamic route parameters from the root segment down to the slot's subpages. For example:
app/[artist]/@sidebar/default.js
TypeScript
JavaScriptTypeScript
```
exportdefaultasyncfunctionDefault({
 params,
}: {
 params:Promise<{ artist:string }>
}) {
const { artist } =await params
}
```

Example| URL| `params`  
---|---|---  
`app/[artist]/@sidebar/default.js`| `/zack`| `Promise<{ artist: 'zack' }>`  
`app/[artist]/[album]/@sidebar/default.js`| `/zack/next`| `Promise<{ artist: 'zack', album: 'next' }>`  
  * Since the `params` prop is a promise. You must use `async/await` or React's `use` function to access the values. 
    * In version 14 and earlier, `params` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.


## Learn more about Parallel Routes
### Parallel Routes
Simultaneously render one or more pages in the same view that can be navigated independently. A pattern for highly dynamic applications.
Was this helpful?
supported.
Send
