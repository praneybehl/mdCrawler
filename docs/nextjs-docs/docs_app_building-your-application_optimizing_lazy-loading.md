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
Building Your ApplicationOptimizingLazy Loading
# Lazy Loading
Lazy loading in Next.js helps improve the initial loading performance of an application by decreasing the amount of JavaScript needed to render a route.
It allows you to defer loading of **Client Components** and imported libraries, and only include them in the client bundle when they're needed. For example, you might want to defer loading a modal until a user clicks to open it.
There are two ways you can implement lazy loading in Next.js:
  1. Using Dynamic Imports with `next/dynamic`
  2. Using `React.lazy()` with Suspense


By default, Server Components are automatically code split, and you can use streaming to progressively send pieces of UI from the server to the client. Lazy loading applies to Client Components.
## `next/dynamic`
`next/dynamic` is a composite of `React.lazy()` and Suspense. It behaves the same way in the `app` and `pages` directories to allow for incremental migration.
## Examples
### Importing Client Components
app/page.js
```
'use client'
import { useState } from'react'
import dynamic from'next/dynamic'
// Client Components:
constComponentA=dynamic(() =>import('../components/A'))
constComponentB=dynamic(() =>import('../components/B'))
constComponentC=dynamic(() =>import('../components/C'), { ssr:false })
exportdefaultfunctionClientComponentExample() {
const [showMore,setShowMore] =useState(false)
return (
  <div>
   {/* Load immediately, but in a separate client bundle */}
   <ComponentA />
   {/* Load on demand, only when/if the condition is met */}
   {showMore && <ComponentB />}
   <buttononClick={() =>setShowMore(!showMore)}>Toggle</button>
   {/* Load only on the client side */}
   <ComponentC />
  </div>
 )
}
```

> **Note:** When a Server Component dynamically imports a Client Component, automatic code splitting is currently **not** supported.
### Skipping SSR
When using `React.lazy()` and Suspense, Client Components will be prerendered (SSR) by default.
> **Note:** `ssr: false` option will only work for client components, move it into client components ensure the client code-splitting working properly.
If you want to disable pre-rendering for a Client Component, you can use the `ssr` option set to `false`:
```
constComponentC=dynamic(() =>import('../components/C'), { ssr:false })
```

### Importing Server Components
If you dynamically import a Server Component, only the Client Components that are children of the Server Component will be lazy-loaded - not the Server Component itself. It will also help preload the static assets such as CSS when you're using it in Server Components.
app/page.js
```
import dynamic from'next/dynamic'
// Server Component:
constServerComponent=dynamic(() =>import('../components/ServerComponent'))
exportdefaultfunctionServerComponentExample() {
return (
  <div>
   <ServerComponent />
  </div>
 )
}
```

> **Note:** `ssr: false` option is not supported in Server Components. You will see an error if you try to use it in Server Components. `ssr: false` is not allowed with `next/dynamic` in Server Components. Please move it into a client component.
### Loading External Libraries
External libraries can be loaded on demand using the `import()` function. This example uses the external library `fuse.js` for fuzzy search. The module is only loaded on the client after the user types in the search input.
app/page.js
```
'use client'
import { useState } from'react'
constnames= ['Tim','Joe','Bel','Lee']
exportdefaultfunctionPage() {
const [results,setResults] =useState()
return (
  <div>
   <input
type="text"
placeholder="Search"
onChange={async (e) => {
const { value } =e.currentTarget
// Dynamically load fuse.js
constFuse= (awaitimport('fuse.js')).default
constfuse=newFuse(names)
setResults(fuse.search(value))
    }}
   />
   <pre>Results: {JSON.stringify(results,null,2)}</pre>
  </div>
 )
}
```

### Adding a custom loading component
app/page.js
```
'use client'
import dynamic from'next/dynamic'
constWithCustomLoading=dynamic(
 () =>import('../components/WithCustomLoading'),
 {
loading: () => <p>Loading...</p>,
 }
)
exportdefaultfunctionPage() {
return (
  <div>
   {/* The loading component will be rendered while <WithCustomLoading/> is loading */}
   <WithCustomLoading />
  </div>
 )
}
```

### Importing Named Exports
To dynamically import a named export, you can return it from the Promise returned by `import()` function:
components/hello.js
```
'use client'
exportfunctionHello() {
return <p>Hello!</p>
}
```

app/page.js
```
import dynamic from'next/dynamic'
constClientComponent=dynamic(() =>
import('../components/hello').then((mod) =>mod.Hello)
)
```

Was this helpful?
supported.
Send
