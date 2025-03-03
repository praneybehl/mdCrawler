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
Building Your ApplicationConfiguringBabel
# Babel
Examples
  * Customizing babel configuration


Next.js includes the `next/babel` preset to your app, which includes everything needed to compile React applications and server-side code. But if you want to extend the default Babel configs, it's also possible.
## Adding Presets and Plugins
To start, you only need to define a `.babelrc` file (or `babel.config.js`) in the root directory of your project. If such a file is found, it will be considered as the _source of truth_ , and therefore it needs to define what Next.js needs as well, which is the `next/babel` preset.
Here's an example `.babelrc` file:
.babelrc
```
{
"presets": ["next/babel"],
"plugins": []
}
```

You can take a look at this file to learn about the presets included by `next/babel`.
To add presets/plugins **without configuring them** , you can do it this way:
.babelrc
```
{
"presets": ["next/babel"],
"plugins": ["@babel/plugin-proposal-do-expressions"]
}
```

## Customizing Presets and Plugins
To add presets/plugins **with custom configuration** , do it on the `next/babel` preset like so:
.babelrc
```
{
"presets": [
  [
"next/babel",
   {
"preset-env": {},
"transform-runtime": {},
"styled-jsx": {},
"class-properties": {}
   }
  ]
 ],
"plugins": []
}
```

To learn more about the available options for each config, visit babel's documentation site.
> **Good to know** :
>   * Next.js uses the **current** Node.js version for server-side compilations.
>   * The `modules` option on `"preset-env"` should be kept to `false`, otherwise webpack code splitting is turned off.
> 

Was this helpful?
supported.
Send
