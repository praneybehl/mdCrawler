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
API ReferenceFunctionsunstable_noStore
# unstable_noStore
This is a legacy API and no longer recommended. It's still supported for backward compatibility.
**In version 15, we recommend using`connection` instead of `unstable_noStore`.**
`unstable_noStore` can be used to declaratively opt out of static rendering and indicate a particular component should not be cached.
```
import { unstable_noStore as noStore } from'next/cache';
exportdefaultasyncfunctionServerComponent() {
noStore();
constresult=awaitdb.query(...);
...
}
```

> **Good to know** :
>   * `unstable_noStore` is equivalent to `cache: 'no-store'` on a `fetch`
>   * `unstable_noStore` is preferred over `export const dynamic = 'force-dynamic'` as it is more granular and can be used on a per-component basis
> 

  * Using `unstable_noStore` inside `unstable_cache` will not opt out of static generation. Instead, it will defer to the cache configuration to determine whether to cache the result or not.


## Usage
If you prefer not to pass additional options to `fetch`, like `cache: 'no-store'`, `next: { revalidate: 0 }` or in cases where `fetch` is not available, you can use `noStore()` as a replacement for all of these use cases.
```
import { unstable_noStore as noStore } from'next/cache';
exportdefaultasyncfunctionServerComponent() {
noStore();
constresult=awaitdb.query(...);
...
}
```

## Version History
Version| Changes  
---|---  
`v15.0.0`| `unstable_noStore` deprecated for `connection`.  
`v14.0.0`| `unstable_noStore` introduced.  
Was this helpful?
supported.
Send
