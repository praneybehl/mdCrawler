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
Building Your ApplicationStylingTailwind CSS
# Tailwind CSS
Tailwind CSS is a utility-first CSS framework that works exceptionally well with Next.js.
## Installing Tailwind
Install the Tailwind CSS packages and run the `init` command to generate both the `tailwind.config.js` and `postcss.config.js` files:
Terminal
```
npminstall-Dtailwindcsspostcssautoprefixer
npxtailwindcssinit-p
```

## Configuring Tailwind
Inside your Tailwind configuration file, add paths to the files that will use Tailwind class names:
tailwind.config.ts
TypeScript
JavaScriptTypeScript
```
importtype { Config } from'tailwindcss'
exportdefault {
 content: [
'./app/**/*.{js,ts,jsx,tsx,mdx}',// Note the addition of the `app` directory.
'./pages/**/*.{js,ts,jsx,tsx,mdx}',
'./components/**/*.{js,ts,jsx,tsx,mdx}',
// Or if using `src` directory:
'./src/**/*.{js,ts,jsx,tsx,mdx}',
 ],
 theme: {
  extend: {},
 },
 plugins: [],
} satisfiesConfig
```

You do not need to modify `postcss.config.js`.
## Importing Styles
Add the Tailwind CSS directives that Tailwind will use to inject its generated styles to a Global Stylesheet in your application, for example:
styles/globals.css
```
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Inside the custom app file (`pages/_app.js`), import the `globals.css` stylesheet to apply the styles to every route in your application.
pages/_app.tsx
TypeScript
JavaScriptTypeScript
```
// These styles apply to every route in the application
import'@/styles/globals.css'
importtype { AppProps } from'next/app'
exportdefaultfunctionApp({ Component, pageProps }:AppProps) {
return <Component {...pageProps} />
}
```

## Using Classes
After installing Tailwind CSS and adding the global styles, you can use Tailwind's utility classes in your application.
pages/index.tsx
TypeScript
JavaScriptTypeScript
```
exportdefaultfunctionPage() {
return <h1className="text-3xl font-bold underline">Hello, Next.js!</h1>
}
```

## Usage with Turbopack
As of Next.js 13.1, Tailwind CSS and PostCSS are supported with Turbopack.
Was this helpful?
supported.
Send
