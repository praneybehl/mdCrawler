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
Building Your ApplicationTestingVitest
# Setting up Vitest with Next.js
Vite and React Testing Library are frequently used together for **Unit Testing**. This guide will show you how to setup Vitest with Next.js and write your first tests.
> **Good to know:** Since `async` Server Components are new to the React ecosystem, Vitest currently does not support them. While you can still run **unit tests** for synchronous Server and Client Components, we recommend using an **E2E tests** for `async` components.
## Quickstart
You can use `create-next-app` with the Next.js with-vitest example to quickly get started:
Terminal
```
npxcreate-next-app@latest--examplewith-vitestwith-vitest-app
```

## Manual Setup
To manually set up Vitest, install `vitest` and the following packages as dev dependencies:
Terminal
```
# Using TypeScript
npminstall-Dvitest@vitejs/plugin-reactjsdom@testing-library/react@testing-library/domvite-tsconfig-paths
# Using JavaScript
npminstall-Dvitest@vitejs/plugin-reactjsdom@testing-library/react@testing-library/dom
```

Create a `vitest.config.mts|js` file in the root of your project, and add the following options:
vitest.config.mts
TypeScript
JavaScriptTypeScript
```
import { defineConfig } from'vitest/config'
import react from'@vitejs/plugin-react'
import tsconfigPaths from'vite-tsconfig-paths'
exportdefaultdefineConfig({
 plugins: [tsconfigPaths(),react()],
 test: {
  environment:'jsdom',
 },
})
```

For more information on configuring Vitest, please refer to the Vitest Configuration docs.
Then, add a `test` script to your `package.json`:
package.json
```
{
"scripts": {
"dev":"next dev",
"build":"next build",
"start":"next start",
"test":"vitest"
 }
}
```

When you run `npm run test`, Vitest will **watch** for changes in your project by default.
## Creating your first Vitest Unit Test
Check that everything is working by creating a test to check if the `<Page />` component successfully renders a heading:
app/page.tsx
TypeScript
JavaScriptTypeScript
```
import Link from'next/link'
exportdefaultfunctionPage() {
return (
  <div>
   <h1>Home</h1>
   <Linkhref="/about">About</Link>
  </div>
 )
}
```

__tests__/page.test.tsx
TypeScript
JavaScriptTypeScript
```
import { expect, test } from'vitest'
import { render, screen } from'@testing-library/react'
import Page from'../app/page'
test('Page', () => {
render(<Page />)
expect(screen.getByRole('heading', { level:1, name:'Home' })).toBeDefined()
})
```

> **Good to know** : The example above uses the common `__tests__` convention, but test files can also be colocated inside the `app` router.
## Running your tests
Then, run the following command to run your tests:
Terminal
```
npmruntest
# or
yarntest
# or
pnpmtest
# or
buntest
```

## Additional Resources
You may find these resources helpful:
  * Next.js with Vitest example
  * Vitest Docs
  * React Testing Library Docs


Was this helpful?
supported.
Send
