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
API ReferenceFunctionsredirect
# redirect
The `redirect` function allows you to redirect the user to another URL. `redirect` can be used in Server Components, Route Handlers, and Server Actions.
When used in a streaming context, this will insert a meta tag to emit the redirect on the client side. When used in a server action, it will serve a 303 HTTP redirect response to the caller. Otherwise, it will serve a 307 HTTP redirect response to the caller.
If a resource doesn't exist, you can use the `notFound` function instead.
> **Good to know** :
>   * In Server Actions and Route Handlers, `redirect` should be called after the `try/catch` block.
>   * If you prefer to return a 308 (Permanent) HTTP redirect instead of 307 (Temporary), you can use the `permanentRedirect` function instead.
> 

## Parameters
The `redirect` function accepts two arguments:
```
redirect(path, type)
```

Parameter| Type| Description  
---|---|---  
`path`| `string`| The URL to redirect to. Can be a relative or absolute path.  
`type`| `'replace'` (default) or `'push'` (default in Server Actions)| The type of redirect to perform.  
By default, `redirect` will use `push` (adding a new entry to the browser history stack) in Server Actions and `replace` (replacing the current URL in the browser history stack) everywhere else. You can override this behavior by specifying the `type` parameter.
The `type` parameter has no effect when used in Server Components.
## Returns
`redirect` does not return a value.
## Example
### Server Component
Invoking the `redirect()` function throws a `NEXT_REDIRECT` error and terminates rendering of the route segment in which it was thrown.
app/team/[id]/page.tsx
TypeScript
JavaScriptTypeScript
```
import { redirect } from'next/navigation'
asyncfunctionfetchTeam(id:string) {
constres=awaitfetch('https://...')
if (!res.ok) returnundefined
returnres.json()
}
exportdefaultasyncfunctionProfile({
 params,
}: {
 params:Promise<{ id:string }>
}) {
const { id } =await params
constteam=awaitfetchTeam(id)
if (!team) {
redirect('/login')
 }
// ...
}
```

> **Good to know** : `redirect` does not require you to use `return redirect()` as it uses the TypeScript `never` type.
### Client Component
`redirect` can be used in a Client Component through a Server Action. If you need to use an event handler to redirect the user, you can use the `useRouter` hook.
app/client-redirect.tsx
TypeScript
JavaScriptTypeScript
```
'use client'
import { navigate } from'./actions'
exportfunctionClientRedirect() {
return (
  <formaction={navigate}>
   <inputtype="text"name="id" />
   <button>Submit</button>
  </form>
 )
}
```

app/actions.ts
TypeScript
JavaScriptTypeScript
```
'use server'
import { redirect } from'next/navigation'
exportasyncfunctionnavigate(data:FormData) {
redirect(`/posts/${data.get('id')}`)
}
```

## FAQ
### Why does `redirect` use 307 and 308?
When using `redirect()` you may notice that the status codes used are `307` for a temporary redirect, and `308` for a permanent redirect. While traditionally a `302` was used for a temporary redirect, and a `301` for a permanent redirect, many browsers changed the request method of the redirect, from a `POST` to `GET` request when using a `302`, regardless of the origins request method.
Taking the following example of a redirect from `/users` to `/people`, if you make a `POST` request to `/users` to create a new user, and are conforming to a `302` temporary redirect, the request method will be changed from a `POST` to a `GET` request. This doesn't make sense, as to create a new user, you should be making a `POST` request to `/people`, and not a `GET` request.
The introduction of the `307` status code means that the request method is preserved as `POST`.
  * `302` - Temporary redirect, will change the request method from `POST` to `GET`
  * `307` - Temporary redirect, will preserve the request method as `POST`


The `redirect()` method uses a `307` by default, instead of a `302` temporary redirect, meaning your requests will _always_ be preserved as `POST` requests.
Learn more about HTTP Redirects.
## Version History
Version| Changes  
---|---  
`v13.0.0`| `redirect` introduced.  
## Next Steps
### permanentRedirect
API Reference for the permanentRedirect function.
Was this helpful?
supported.
Send
