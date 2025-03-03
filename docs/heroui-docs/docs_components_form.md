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


# Form
A form is a group of inputs that allows users to submit data to a server, with support for providing field validation errors.
Storybook@heroui/formSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add form

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
Individual
Global
## Usage
Preview
Code
Email
Submit
## Anatomy
A `Form` is a container for input elements and submit/reset buttons, with support for validation messages. When labeled with `aria-label` or `aria-labelledby`, it becomes a navigable form landmark for assistive technology.
## Events
The `onSubmit` event will be triggered when a user submits the form with the `Enter` key or by pressing a submit button. The onReset event will be triggered when a user presses a reset button.
Preview
Code
## Validation
`Form` supports native HTML constraint validation with customizable UI, custom validation functions, and server-side validation. Server-side validation errors can be provided via the `validationErrors` prop as an object mapping field names to error messages, which are cleared when the user modifies the field.
Preview
Code
See the Forms guide to learn more about form validation, including client-side validation, and integration with other frameworks and libraries.
### Validation Behavior
`Form` validation uses native validation behavior by default, but can be switched to ARIA validation by setting `validationBehavior="aria"`. ARIA validation shows realtime errors without blocking submission. This can be set at the form or field level. To set the default behavior at the app level, you can change the form defaults for your entire app using HeroUI Provider.
Preview
Code
## Accessibility
  * Built with a native HTML `<form>` element, with support for ARIA labelling to create a form landmark.
  * Full support for browser features like form autofill.
  * Support for native HTML constraint validation with customizable UI, custom validation functions, realtime validation, and server-side validation errors.


## API
### Form Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode`  
`validationBehavior`| `'native' | 'aria'`| `"native"`  
`validationErrors`| `Record<string, string | string[]>`  
`action`| `string | FormHTMLAttributes<HTMLFormElement>['action']`  
`encType`| `'application/x-www-form-urlencoded' | 'multipart/form-data' | 'text/plain'`  
`method`| `'get' | 'post' | 'dialog'`  
`target`| `'_blank' | '_self' | '_parent' | '_top'`  
`autoComplete`| `'off' | 'on'`  
`autoCapitalize`| `'off' | 'none' | 'on' | 'sentences' | 'words' | 'characters'`  
`className`| `string`  
`style`| `CSSProperties`  
DrawerImage
On this page
  * Installation
  * Import
  * Usage
  * Anatomy
  * Events
  * Validation
  * Validation Behavior
  * Accessibility
  * API
  * Form Props
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
