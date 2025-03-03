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
App RouterAPI ReferenceTurbopack
# Turbopack
Turbopack is an incremental bundler optimized for JavaScript and TypeScript, written in Rust, and built into Next.js. Turbopack can be used in Next.js in both the `pages` and `app` directories for faster local development.
To enable Turbopack, use the `--turbopack` flag when running the Next.js development server.
package.json
```
{
"scripts": {
"dev":"next dev --turbopack",
"build":"next build",
"start":"next start",
"lint":"next lint"
 }
}
```

## Reference
### Supported features
Turbopack in Next.js requires zero-configuration for most users and can be extended for more advanced use cases. To learn more about the currently supported features for Turbopack, view the API Reference.
### Unsupported features
Turbopack currently only supports `next dev` and does not support `next build`. We are currently working on support for builds as we move closer towards stability.
These features are currently not supported:
  * Turbopack leverages Lightning CSS which doesn't support some low usage CSS Modules features 
    * `:local` and `:global` as standalone pseudo classes. Only the function variant is supported, for example: `:global(a)`.
    * The @value rule which has been superseded by CSS variables.
    * `:import` and `:export` ICSS rules.
  * Invalid CSS comment syntax such as `//`
    * CSS comments should be written as `/* comment */` per the specification.
    * Preprocessors such as Sass do support this alternative syntax for comments.
  * `webpack()` configuration in `next.config.js`
    * Turbopack replaces Webpack, this means that webpack configuration is not supported.
    * To configure Turbopack, see the documentation.
    * A subset of Webpack loaders are supported in Turbopack.
  * Babel (`.babelrc`) 
    * Turbopack leverages the SWC compiler for all transpilation and optimizations. This means that Babel is not included by default.
    * If you have a `.babelrc` file, you might no longer need it because Next.js includes common Babel plugins as SWC transforms that can be enabled. You can read more about this in the compiler documentation.
    * If you still need to use Babel after verifying your particular use case is not covered, you can leverage Turbopack's support for custom webpack loaders to include `babel-loader`.
  * Creating a root layout automatically in App Router. 
    * This behavior is currently not supported since it changes input files, instead, an error will be shown for you to manually add a root layout in the desired location.
  * `@next/font` (legacy font support). 
    * `@next/font` is deprecated in favor of `next/font`. `next/font` is fully supported with Turbopack.
  * Relay transforms
    * We are planning to implement this in the future.
  * Blocking `.css` imports in `pages/_document.tsx`
    * Currently with webpack Next.js blocks importing `.css` files in `pages/_document.tsx`
    * We are planning to implement this warning in the future.
  * `experimental.typedRoutes`
    * We are planning to implement this in the future.
  * `experimental.nextScriptWorkers`
    * We are planning to implement this in the future.
  * `experimental.sri.algorithm`
    * We are planning to implement this in the future.
  * `experimental.fallbackNodePolyfills`
    * We are planning to implement this in the future.
  * `experimental.esmExternals`
    * We are currently not planning to support the legacy esmExternals configuration in Next.js with Turbopack.
  * AMP. 
    * We are currently not planning to support AMP in Next.js with Turbopack.
  * Yarn PnP 
    * We are currently not planning to support Yarn PnP in Next.js with Turbopack.
  * `experimental.urlImports`
    * We are currently not planning to support `experimental.urlImports` in Next.js with Turbopack.
  * `:import` and `:export` ICSS rules
    * We are currently not planning to support `:import` and `:export` ICSS rules in Next.js with Turbopack as Lightning CSS the CSS parser Turbopack uses does not support these rules.
  * `unstable_allowDynamic` configuration in edge runtime


## Examples
### Generating Trace Files
Trace files allow the Next.js team to investigate and improve performance metrics and memory usage. To generate a trace file, append `NEXT_TURBOPACK_TRACING=1` to the `next dev --turbopack` command, this will generate a `.next/trace-turbopack` file.
When reporting issues related to Turbopack performance and memory usage, please include the trace file in your GitHub issue.
Was this helpful?
supported.
Send
