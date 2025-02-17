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
![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-light.cf7eca76.svg)![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-dark.01246f11.svg)
Search...
`⌘ K`
Feedback
Log In
Sign Up
Workflow
Draft Mode
How-to
# Draft Mode
Vercel's Draft Mode enables you to view your unpublished headless CMS content on your site before publishing it.
Table of Contents
Next.js (/app)
Draft Mode lets you view your unpublished headless CMS content on your website rendered with all the normal styling and layout that you would see once published.
Both Next.js and SvelteKit support Draft Mode. Any framework that uses the Build Output API can support Draft Mode by adding the `bypassToken` option to prerender configuration.
Draft Mode was called Preview Mode before the release of Next.js 13.4 . The name was changed to avoid confusion with preview deployments, which is a different product.
You can use Draft Mode if you:
  1. Use Incremental Static Regeneration (ISR) to fetch and render data from a headless CMS
  2. Want to view your unpublished headless CMS content on your site without rebuilding your pages when you make changes
  3. Want to protect your unpublished content from being viewed publicly


## How Draft Mode works
Draft Mode allows you to bypass ISR caching to fetch the latest CMS content at request time. This is useful for seeing your draft content on your website without waiting for the cache to refresh, or manually revalidating the page.
The process works like this:
  1. Each ISR route has a `bypassToken` configuration option, which is assigned a generated, cryptographically-secure value at build time
  2. When someone visits an ISR route with a `bypassToken` configured, the page will check for a `__prerender_bypass` cookie
  3. If the `__prerender_bypass` cookie exists and has the same value as the `bypassToken` your project is using, the visitor will view the page in Draft Mode


Only team members will be able to view pages in Draft Mode.
## Getting started
To use Draft Mode with Next.js on Vercel, you must:
  1. Enable ISR on pages that fetch content. Using ISR is required on pages that you want to view in Draft Mode
  2. Add code to your ISR pages to detect when Draft Mode is enabled and render the draft content
  3. Toggle Draft Mode in the Vercel Toolbar by selecting the eye icon to view your draft content. Once toggled, the toolbar will turn purple, indicating that Draft Mode is enabled
Next.js (/app)Next.js (/pages)SvelteKit
app/page.tsx
TypeScript
TypeScriptJavaScript
```
import { draftMode } from'next/headers';
asyncfunctiongetContent() {
const { isEnabled } =awaitdraftMode();
constcontentUrl= isEnabled
?'https://draft.example.com'
:'https://production.example.com';
// This line enables ISR, required for draft mode
constres=awaitfetch(contentUrl, { next: { revalidate:120 } });
returnres.json();
}
exportdefaultasyncfunctionPage() {
const { title,desc } =awaitgetContent();
return (
  <main>
   <h1>{title}</h1>
   <p>{desc}</p>
  </main>
 );
}
```

Open inOpen in v0


See the Next.js docs to learn how to use Draft Mode with self-hosted Next.js projects:
  * App Router
  * Pages Router


Once implemented, team members can access Draft Mode from the Vercel Toolbar by selecting the eye icon . Once selected, the toolbar will turn purple to indicate that Draft Mode is enabled.
## Sharing drafts
To share a draft URL, it must have the `?__vercel_draft=1` query parameter. For example:
```
https://my-site.com/blog/post-01?__vercel_draft=1
```

Viewers outside your Vercel team cannot enable Draft Mode or see your draft content, even with a draft URL.
Last updated on September 27, 2024
Previous
Edit Mode
Next
Conformance
Was this helpful?
supported.
Send
AskAsk v0
Draft Mode
Next.js (/app)
AskAsk v0
