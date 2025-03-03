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
Building Your ApplicationTestingPlaywright
# Setting up Playwright with Next.js
Playwright is a testing framework that lets you automate Chromium, Firefox, and WebKit with a single API. You can use it to write **End-to-End (E2E)** testing. This guide will show you how to set up Playwright with Next.js and write your first tests.
## Quickstart
The fastest way to get started is to use `create-next-app` with the with-playwright example. This will create a Next.js project complete with Playwright configured.
Terminal
```
npxcreate-next-app@latest--examplewith-playwrightwith-playwright-app
```

## Manual setup
To install Playwright, run the following command:
Terminal
```
npminitplaywright
# or
yarncreateplaywright
# or
pnpmcreateplaywright
```

This will take you through a series of prompts to setup and configure Playwright for your project, including adding a `playwright.config.ts` file. Please refer to the Playwright installation guide for the step-by-step guide.
## Creating your first Playwright E2E test
Create two new Next.js pages:
pages/index.ts
```
import Link from'next/link'
exportdefaultfunctionHome() {
return (
  <div>
   <h1>Home</h1>
   <Linkhref="/about">About</Link>
  </div>
 )
}
```

pages/about.ts
```
import Link from'next/link'
exportdefaultfunctionAbout() {
return (
  <div>
   <h1>About</h1>
   <Linkhref="/">Home</Link>
  </div>
 )
}
```

Then, add a test to verify that your navigation is working correctly:
tests/example.spec.ts
```
import { test, expect } from'@playwright/test'
test('should navigate to the about page',async ({ page }) => {
// Start from the index page (the baseURL is set via the webServer in the playwright.config.ts)
awaitpage.goto('http://localhost:3000/')
// Find an element with the text 'About' and click on it
awaitpage.click('text=About')
// The new URL should be "/about" (baseURL is used there)
awaitexpect(page).toHaveURL('http://localhost:3000/about')
// The new page should contain an h1 with "About"
awaitexpect(page.locator('h1')).toContainText('About')
})
```

> **Good to know** : You can use `page.goto("/")` instead of `page.goto("http://localhost:3000/")`, if you add `"baseURL": "http://localhost:3000"` to the `playwright.config.ts` configuration file.
### Running your Playwright tests
Playwright will simulate a user navigating your application using three browsers: Chromium, Firefox and Webkit, this requires your Next.js server to be running. We recommend running your tests against your production code to more closely resemble how your application will behave.
Run `npm run build` and `npm run start`, then run `npx playwright test` in another terminal window to run the Playwright tests.
> **Good to know** : Alternatively, you can use the `webServer` feature to let Playwright start the development server and wait until it's fully available.
### Running Playwright on Continuous Integration (CI)
Playwright will by default run your tests in the headless mode. To install all the Playwright dependencies, run `npx playwright install-deps`.
You can learn more about Playwright and Continuous Integration from these resources:
  * Next.js with Playwright example
  * Playwright on your CI provider
  * Playwright Discord


Was this helpful?
supported.
Send
