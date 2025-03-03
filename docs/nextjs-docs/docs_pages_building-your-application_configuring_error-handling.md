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
Building Your ApplicationConfiguringError Handling
# Error Handling
This documentation explains how you can handle development, server-side, and client-side errors.
## Handling Errors in Development
When there is a runtime error during the development phase of your Next.js application, you will encounter an **overlay**. It is a modal that covers the webpage. It is **only** visible when the development server runs using `next dev` via `pnpm dev`, `npm run dev`, `yarn dev`, or `bun dev` and will not be shown in production. Fixing the error will automatically dismiss the overlay.
Here is an example of an overlay:
![Example of an overlay when in development mode](https://assets.vercel.com/image/upload/v1645118290/docs-assets/static/docs/error-handling/overlay.png)
## Handling Server Errors
Next.js provides a static 500 page by default to handle server-side errors that occur in your application. You can also customize this page by creating a `pages/500.js` file.
Having a 500 page in your application does not show specific errors to the app user.
You can also use 404 page to handle specific runtime error like `file not found`.
## Handling Client Errors
React Error Boundaries is a graceful way to handle a JavaScript error on the client so that the other parts of the application continue working. In addition to preventing the page from crashing, it allows you to provide a custom fallback component and even log error information.
To use Error Boundaries for your Next.js application, you must create a class component `ErrorBoundary` and wrap the `Component` prop in the `pages/_app.js` file. This component will be responsible to:
  * Render a fallback UI after an error is thrown
  * Provide a way to reset the Application's state
  * Log error information


You can create an `ErrorBoundary` class component by extending `React.Component`. For example:
```
classErrorBoundaryextendsReact.Component {
constructor(props) {
super(props)
// Define a state variable to track whether is an error or not
this.state = { hasError:false }
 }
staticgetDerivedStateFromError(error) {
// Update state so the next render will show the fallback UI
return { hasError:true }
 }
componentDidCatch(error, errorInfo) {
// You can use your own error logging service here
console.log({ error, errorInfo })
 }
render() {
// Check if the error is thrown
if (this.state.hasError) {
// You can render any custom fallback UI
return (
    <div>
     <h2>Oops, there is an error!</h2>
     <button
type="button"
onClick={() =>this.setState({ hasError:false })}
     >
      Try again?
     </button>
    </div>
   )
  }
// Return children components in case of no error
returnthis.props.children
 }
}
exportdefault ErrorBoundary
```

The `ErrorBoundary` component keeps track of an `hasError` state. The value of this state variable is a boolean. When the value of `hasError` is `true`, then the `ErrorBoundary` component will render a fallback UI. Otherwise, it will render the children components.
After creating an `ErrorBoundary` component, import it in the `pages/_app.js` file to wrap the `Component` prop in your Next.js application.
```
// Import the ErrorBoundary component
import ErrorBoundary from'../components/ErrorBoundary'
functionMyApp({ Component, pageProps }) {
return (
// Wrap the Component prop with ErrorBoundary component
  <ErrorBoundary>
   <Component {...pageProps} />
  </ErrorBoundary>
 )
}
exportdefault MyApp
```

You can learn more about Error Boundaries in React's documentation.
### Reporting Errors
To monitor client errors, use a service like Sentry, Bugsnag or Datadog.
Was this helpful?
supported.
Send
