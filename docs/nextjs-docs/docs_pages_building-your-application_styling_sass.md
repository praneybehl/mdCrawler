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
Building Your ApplicationStylingSass
# Sass
Next.js has built-in support for integrating with Sass after the package is installed using both the `.scss` and `.sass` extensions. You can use component-level Sass via CSS Modules and the `.module.scss`or `.module.sass` extension.
First, install `sass`:
Terminal
```
npminstall--save-devsass
```

> **Good to know** :
> Sass supports two different syntaxes, each with their own extension. The `.scss` extension requires you use the SCSS syntax, while the `.sass` extension requires you use the Indented Syntax ("Sass").
> If you're not sure which to choose, start with the `.scss` extension which is a superset of CSS, and doesn't require you learn the Indented Syntax ("Sass").
### Customizing Sass Options
If you want to configure your Sass options, use `sassOptions` in `next.config`.
next.config.ts
TypeScript
JavaScriptTypeScript
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
 sassOptions: {
  additionalData:`$var: red;`,
 },
}
exportdefault nextConfig
```

#### Implementation
You can use the `implementation` property to specify the Sass implementation to use. By default, Next.js uses the `sass` package.
next.config.ts
TypeScript
JavaScriptTypeScript
```
importtype { NextConfig } from'next'
constnextConfig:NextConfig= {
 sassOptions: {
  implementation:'sass-embedded',
 },
}
exportdefault nextConfig
```

### Sass Variables
Next.js supports Sass variables exported from CSS Module files.
For example, using the exported `primaryColor` Sass variable:
app/variables.module.scss
```
$primary-color: #64ff00;
:export {
primaryColor:$primary-color;
}
```

pages/_app.js
```
import variables from'../styles/variables.module.scss'
exportdefaultfunctionMyApp({ Component, pageProps }) {
return (
  <Layoutcolor={variables.primaryColor}>
   <Component {...pageProps} />
  </Layout>
 )
}
```

Was this helpful?
supported.
Send
