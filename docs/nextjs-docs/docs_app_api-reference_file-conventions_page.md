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
API ReferenceFile Conventionspage.js
# page.js
The `page` file allows you to define UI that is **unique** to a route. You can create a page by default exporting a component from the file:
app/blog/[slug]/page.tsx
TypeScript
JavaScriptTypeScript
```
exportdefaultfunctionPage({
 params,
 searchParams,
}: {
 params:Promise<{ slug:string }>
 searchParams:Promise<{ [key:string]:string|string[] |undefined }>
}) {
return <h1>My Page</h1>
}
```

## Good to know
  * The `.js`, `.jsx`, or `.tsx` file extensions can be used for `page`.
  * A `page` is always the **leaf** of the route subtree.
  * A `page` file is required to make a route segment **publicly accessible**.
  * Pages are Server Components by default, but can be set to a Client Component.


## Reference
### Props
#### `params` (optional)
A promise that resolves to an object containing the dynamic route parameters from the root segment down to that page.
app/shop/[slug]/page.tsx
TypeScript
JavaScriptTypeScript
```
exportdefaultasyncfunctionPage({
 params,
}: {
 params:Promise<{ slug:string }>
}) {
const { slug } =await params
}
```

Example Route| URL| `params`  
---|---|---  
`app/shop/[slug]/page.js`| `/shop/1`| `Promise<{ slug: '1' }>`  
`app/shop/[category]/[item]/page.js`| `/shop/1/2`| `Promise<{ category: '1', item: '2' }>`  
`app/shop/[...slug]/page.js`| `/shop/1/2`| `Promise<{ slug: ['1', '2'] }>`  
  * Since the `params` prop is a promise. You must use `async/await` or React's `use` function to access the values. 
    * In version 14 and earlier, `params` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.


#### `searchParams` (optional)
A promise that resolves to an object containing the search parameters of the current URL. For example:
app/shop/page.tsx
TypeScript
JavaScriptTypeScript
```
exportdefaultasyncfunctionPage({
 searchParams,
}: {
 searchParams:Promise<{ [key:string]:string|string[] |undefined }>
}) {
constfilters= (await searchParams).filters
}
```

Example URL| `searchParams`  
---|---  
`/shop?a=1`| `Promise<{ a: '1' }>`  
`/shop?a=1&b=2`| `Promise<{ a: '1', b: '2' }>`  
`/shop?a=1&a=2`| `Promise<{ a: ['1', '2'] }>`  
  * Since the `searchParams` prop is a promise. You must use `async/await` or React's `use` function to access the values. 
    * In version 14 and earlier, `searchParams` was a synchronous prop. To help with backwards compatibility, you can still access it synchronously in Next.js 15, but this behavior will be deprecated in the future.
  * `searchParams` is a **Dynamic API** whose values cannot be known ahead of time. Using it will opt the page into **dynamic rendering** at request time.
  * `searchParams` is a plain JavaScript object, not a `URLSearchParams` instance.


## Examples
### Displaying content based on `params`
Using dynamic route segments, you can display or fetch specific content for the page based on the `params` prop.
app/blog/[slug]/page.tsx
TypeScript
JavaScriptTypeScript
```
exportdefaultasyncfunctionPage({
 params,
}: {
 params:Promise<{ slug:string }>
}) {
const { slug } =await params
return <h1>Blog Post: {slug}</h1>
}
```

### Handling filtering with `searchParams`
You can use the `searchParams` prop to handle filtering, pagination, or sorting based on the query string of the URL.
app/shop/page.tsx
TypeScript
JavaScriptTypeScript
```
exportdefaultasyncfunctionPage({
 searchParams,
}: {
 searchParams:Promise<{ [key:string]:string|string[] |undefined }>
}) {
const { page='1',sort='asc',query='' } =await searchParams
return (
  <div>
   <h1>Product Listing</h1>
   <p>Search query: {query}</p>
   <p>Current page: {page}</p>
   <p>Sort order: {sort}</p>
  </div>
 )
}
```

### Reading `searchParams` and `params` in Client Components
To use `searchParams` and `params` in a Client Component (which cannot be `async`), you can use React's `use` function to read the promise:
app/page.tsx
TypeScript
JavaScriptTypeScript
```
'use client'
import { use } from'react'
exportdefaultfunctionPage({
 params,
 searchParams,
}: {
 params:Promise<{ slug:string }>
 searchParams:Promise<{ [key:string]:string|string[] |undefined }>
}) {
const { slug } =use(params)
const { query } =use(searchParams)
}
```

## Version History
Version| Changes  
---|---  
`v15.0.0-RC`| `params` and `searchParams` are now promises. A codemod is available.  
`v13.0.0`| `page` introduced.  
Was this helpful?
supported.
Send
