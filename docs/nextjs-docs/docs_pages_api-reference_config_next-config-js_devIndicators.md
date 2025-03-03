Menu
Using Pages Router
Features available in /pages
Using Latest Version
15.2.0
Using Pages Router
Features available in /pages
Using Latest Version
15.2.0
Configurationnext.config.js OptionsdevIndicators
# devIndicators
`devIndicators` allows you to configure the on-screen indicator that gives context about the current route you're viewing during development.
Types
```
 devIndicators:false| {
  position?:'bottom-right'
|'bottom-left'
|'top-right'
|'top-left',// defaults to 'bottom-left',
 },
```

Setting `devIndicators` to `false` will hide the indicator, however Next.js will continue to surface any build or runtime errors that were encountered.
## Troubleshooting
### Indicator not marking a route as static
If you expect a route to be static and the indicator has marked it as dynamic, it's likely the route has opted out of static rendering.
You can confirm if a route is static or dynamic by building your application using `next build --debug`, and checking the output in your terminal. Static (or prerendered) routes will display a `○` symbol, whereas dynamic routes will display a `ƒ` symbol. For example:
Build Output
```
Route (app)               Size   First Load JS
┌○/_not-found0B0kB
└ƒ/products/[id]0B0kB
○ (Static)  prerendered as static content
ƒ (Dynamic) server-rendered on demand
```

When exporting `getServerSideProps` or `getInitialProps` from a page, it will be marked as dynamic.
## Version History
Version| Changes  
---|---  
`v15.2.0`| Improved on-screen indicator with new `position` option. `appIsrStatus`, `buildActivity`, and `buildActivityPosition` options have been deprecated.  
`v15.0.0`| Static on-screen indicator added with `appIsrStatus` option.  
Was this helpful?
supported.
Send
