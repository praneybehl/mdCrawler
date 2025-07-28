Skip to main content
Version: v7.0.0
On this page
## Internationalization ( intl )​
We are excited to introduce Isomorphic **Multi-Language** support, an enhanced version of our original Isomorphic project built with Next.js. Isomorphic brings robust internationalization ( intl ) capabilities to the table, making it easier than ever to create and maintain multilingual dashboards. See project structure.
  * We followed the Next.js official process for internationalization. You can find more details in the Next.js official documentation.
  * We are using this package for the translation: **Next-Intl**. This package is offering a simple and easy way to add multi-language support to your Next.js project and also recommended in Next.js official documentation. You can find more details in the Next.js official documentation.
  * The `isomorphic-intl/messages` directory contains the translation files. You can add more languages and translations by following the existing files.


## Run Project​
You can run the project in your local environment by following these **Scripts**.
info
We are not providing a full translation for the project. We are just providing a basic structure for multi-language support. You can add more languages and translations by following the existing files. And also you can add more components as you need.
## Routing in ( intl )​
There are some important points to consider when working with routing in internationalization. Check the `src/i18n/routing.ts` file. There are some components `Link`, `redirect`, `usePathname` & `useRouter` components are is being used in the project for routing. `Next-Intl` automatically handles the internationalization routing with locale value in the URL. In the isomorphic-intl workspace we are using these components instead of the default Next.js components.
src/i18n/routing.ts
```
import{ createSharedPathnamesNavigation }from"next-intl/navigation";import{ defineRouting }from"next-intl/routing";exportconst routing =defineRouting({ locales:["en","de","es","ar","zh"], defaultLocale:"en",});exportconst{Link, redirect, usePathname, useRouter }=createSharedPathnamesNavigation(routing);
```

Importing in the component
```
import{Link}from"@/i18n/routing";
```

  * Internationalization ( intl )
  * Run Project
  * Routing in ( intl )


