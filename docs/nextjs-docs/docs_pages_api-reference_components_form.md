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
API ReferenceComponentsForm
# Form
The `<Form>` component extends the HTML `<form>` element to provide **client-side navigation** on submission, and **progressive enhancement**.
It's useful for forms that update URL search params as it reduces the boilerplate code needed to achieve the above.
Basic usage:
/ui/search.js
TypeScript
JavaScriptTypeScript
```
import Form from'next/form'
exportdefaultfunctionPage() {
return (
  <Formaction="/search">
   {/* On submission, the input value will be appended to
     the URL, e.g. /search?query=abc */}
   <inputname="query" />
   <buttontype="submit">Submit</button>
  </Form>
 )
}
```

## Reference
The behavior of the `<Form>` component depends on whether the `action` prop is passed a `string` or `function`.
  * When `action` is a **string** , the `<Form>` behaves like a native HTML form that uses a **`GET`**method. The form data is encoded into the URL as search params, and when the form is submitted, it navigates to the specified URL. In addition, Next.js:
    * Performs a client-side navigation instead of a full page reload when the form is submitted. This retains shared UI and client-side state.


### `action` (string) Props
When `action` is a string, the `<Form>` component supports the following props:
Prop| Example| Type| Required  
---|---|---|---  
`action`| `action="/search"`| `string` (URL or relative path)| Yes  
`replace`| `replace={false}`| `boolean`| -  
`scroll`| `scroll={true}`| `boolean`| -  
  * **`action`**: The URL or path to navigate to when the form is submitted.
    * An empty string `""` will navigate to the same route with updated search params.
  * **`replace`**: Replaces the current history state instead of pushing a new one to thebrowser's history stack. Default is `false`.
  * **`scroll`**: Controls the scroll behavior during navigation. Defaults to`true` , this means it will scroll to the top of the new route, and maintain the scroll position for backwards and forwards navigation.


### Caveats
  * **`onSubmit`**: Can be used to handle form submission logic. However, calling`event.preventDefault()` will override `<Form>` behavior such as navigating to the specified URL.
  * **`method`,`encType`, `target`**: Are not supported as they override `<Form>` behavior. 
    * Similarly, `formMethod`, `formEncType`, and `formTarget` can be used to override the `method`, `encType`, and `target` props respectively, and using them will fallback to native browser behavior.
    * If you need to use these props, use the HTML `<form>` element instead.
  * **`<input type="file">`**: Using this input type when the`action` is a string will match browser behavior by submitting the filename instead of the file object.


Was this helpful?
supported.
Send
