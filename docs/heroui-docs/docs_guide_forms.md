🚀Generate, edit and deploy beautiful apps
HeroUI Chat
Getting Started
  * Introduction
  * Design Principles
  * Installation
  * CLI
  * Routing
  * Forms
Updated
  * NextUI to HeroUI
  * Figma


Frameworks
  * Next.js
  * Vite
  * Remix
  * Astro
  * Laravel


Customization
  * Theme
  * Layout
  * Colors
  * Customize theme
  * Create theme
  * Dark mode
  * Override styles
  * Custom variants


Components
  * Accordion
  * Autocomplete
  * Alert
  * Avatar
  * Badge
  * Breadcrumbs
  * Button
  * Calendar
  * Card
  * Checkbox
Updated
  * Checkbox Group
  * Chip
  * Circular Progress
  * Code
  * Date Input
  * Date Picker
  * Date Range Picker
  * Divider
  * Dropdown
  * Drawer
  * Form
  * Image
  * Input
Updated
  * Input OTP
Updated
  * Kbd
Updated
  * Link
  * Listbox
  * Modal
  * Navbar
  * Number Input
New
  * Pagination
  * Popover
  * Progress
  * Radio Group
Updated
  * Range Calendar
  * Scroll Shadow
  * Select
  * Skeleton
  * Slider
  * Snippet
  * Spacer
  * Spinner
Updated
  * Switch
  * Table
Updated
  * Tabs
Updated
  * Toast
New
  * Textarea
  * Time Input
  * Tooltip
  * User


API References
  * HeroUI CLI
  * HeroUIProvider
Updated


# Forms
HeroUI provides form components with built-in validation and styling to help users input and submit data effectively.
Preview
Code
## Labels and help text
Accessible forms start with clear, descriptive labels for each field. All HeroUI form components support labeling using the Label component, which is automatically associated with the field via the id and for attributes on your behalf.
In addition, HeroUI components support help text, which associates additional context with a field such as a **description** or **error message**. The label and help text are announced by assistive technology such as screen readers when the user focuses the field.
Most fields should have a visible label. In rare exceptions, the `aria-label` or `aria-labelledby` attribute must be provided instead to identify the element to screen readers.
## Submitting data
How you submit form data depends on your framework, application, and server. By default, **HTML** forms are submitted via a full-page refresh in the browser. You can call `preventDefault` in the `onSubmit` event to handle form data submission via an API.
Frameworks like Next.js, Remix, and React Router provide their own ways to handle form submission.
#### Uncontrolled forms
A simple way to get form data is to use the browser's FormData API during the `onSubmit` event. You can send this data to a backend API or convert it into a JavaScript object using Object.fromEntries. Each field should have a `name` prop to identify it, and the values will be serialized as strings by the browser.
#### Controlled forms
HeroUI form components are uncontrolled by default, but if you need to manage state in real-time, you can use the `useState` hook to make the component controlled.
#### Customizing error messages
By default, error messages are provided by the browser. You can customize these messages by providing a function to the `errorMessage` prop.
> **Note** : The default error messages are localized by the browser based on the browser/operating system language settings. The locale setting in HeroUI Provider does not affect validation errors.
## Validation
Form validation is crucial for ensuring that users enter the correct data. HeroUI supports native HTML constraint validation and allows for custom validation and real-time validation.
#### Built-in validation
HeroUI form components support native HTML validation attributes like `isRequired` and `minLength`. These constraints are checked by the browser when the user commits changes (e.g., on blur) or submits the form. You can display validation errors with custom styles instead of the browser's default UI.
To enable ARIA validation, set `validationBehavior="aria"`. When`validationBehavior="aria"` is set, fields are only marked as required or invalid for assistive technologies, without preventing form submission. You can change the form defaults for your entire app using HeroUI Provider.
Supported constraints include:
  * `isRequired` indicates that a field must have a value before the form can be submitted.
  * `minValue` and `maxValue` specify the minimum and maximum value in a date picker or number input.
  * `minLength` and `maxLength` specify the minimum and length of text input.
  * `pattern` provides a custom regular expression that a text input must conform to.
  * `type="email"` and `type="url"` provide built-in validation for email addresses and URLs.


See each component's documentation for more details on the supported validation props.
#### Custom validation
In addition to built-in constraints, you can provide a function to the `validate` prop to support custom validation.
#### Realtime validation
If you want to display validation errors while the user is typing, you can control the field value and use the `isInvalid` prop along with the `errorMessage` prop.
Use `validationBehavior="aria"` to allow form submission even when fields are invalid, while maintaining accessibility.
#### Server validation
Client-side validation provides immediate feedback, but you should also validate data on the server to ensure accuracy and security. HeroUI allows you to display server-side validation errors by using the `validationErrors` prop in the `Form` component. This prop should be an object where each key is the field `name` and the value is the error message.
#### Schema validation
HeroUI supports errors from schema validation libraries like Zod. You can use Zod's `flatten` method to get error messages for each field and return them as part of the server response.
### React Server Actions
Server Actions that allows seamless form submission to the server and retrieval of results. The useActionState hook can be used to get the result of server actions (such as errors) after submitting a form.
### Remix
Remix actions handle form submissions on the server. You can use the useSubmit hook to submit form data to the server and the useActionData hook to retrieve validation errors from the server.
## Form libraries
In most cases, the built-in validation features of HeroUI are sufficient. However, if you're building more complex forms or integrating HeroUI components into an existing form, you can use a form library like React Hook Form or Formik.
#### React Hook Form
You can integrate HeroUI components using Controller. Controller allows you to manage field values and validation errors, and reflect the validation result in HeroUI components.
> For more information about forms in HeroUI, visit the React Aria Forms Guide.
RoutingNextUI to HeroUI
On this page
  * Labels and help text
  * Submitting data
  * Uncontrolled forms
  * Controlled forms
  * Customizing error messages
  * Validation
  * Built-in validation
  * Custom validation
  * Realtime validation
  * Server validation
  * Schema validation
  * React Server Actions
  * Remix
  * Form libraries
  * React Hook Form
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
