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
API ReferenceFunctionspermanentRedirect
# permanentRedirect
The `permanentRedirect` function allows you to redirect the user to another URL. `permanentRedirect` can be used in Server Components, Client Components, Route Handlers, and Server Actions.
When used in a streaming context, this will insert a meta tag to emit the redirect on the client side. When used in a server action, it will serve a 303 HTTP redirect response to the caller. Otherwise, it will serve a 308 (Permanent) HTTP redirect response to the caller.
If a resource doesn't exist, you can use the `notFound` function instead.
> **Good to know** : If you prefer to return a 307 (Temporary) HTTP redirect instead of 308 (Permanent), you can use the `redirect` function instead.
## Parameters
The `permanentRedirect` function accepts two arguments:
```
permanentRedirect(path, type)
```

Parameter| Type| Description  
---|---|---  
`path`| `string`| The URL to redirect to. Can be a relative or absolute path.  
`type`| `'replace'` (default) or `'push'` (default in Server Actions)| The type of redirect to perform.  
By default, `permanentRedirect` will use `push` (adding a new entry to the browser history stack) in Server Actions and `replace` (replacing the current URL in the browser history stack) everywhere else. You can override this behavior by specifying the `type` parameter.
The `type` parameter has no effect when used in Server Components.
## Returns
`permanentRedirect` does not return a value.
## Example
Invoking the `permanentRedirect()` function throws a `NEXT_REDIRECT` error and terminates rendering of the route segment in which it was thrown.
app/team/[id]/page.js
```
import { permanentRedirect } from'next/navigation'
asyncfunctionfetchTeam(id) {
constres=awaitfetch('https://...')
if (!res.ok) returnundefined
returnres.json()
}
exportdefaultasyncfunctionProfile({ params }) {
const { id } =await params
constteam=awaitfetchTeam(id)
if (!team) {
permanentRedirect('/login')
 }
// ...
}
```

> **Good to know** : `permanentRedirect` does not require you to use `return permanentRedirect()` as it uses the TypeScript `never` type.
## Next Steps
### redirect
API Reference for the redirect function.
Was this helpful?
supported.
Send
