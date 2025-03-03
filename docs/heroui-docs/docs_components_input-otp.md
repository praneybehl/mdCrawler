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


# Input OTP
The InputOtp component enables users to enter one-time passwords (OTP). It is built on top of the input-otp library by @guilherme_rodz.
Storybook@heroui/input-otpSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add input-otp

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
Individual
Global
## Usage
Preview
Code
## Disabled
The `isDisabled` prop disables user interaction with the `InputOtp` component.
Preview
Code
## Read Only
The `isReadOnly` prop makes the `InputOtp` component read-only while maintaining its visual appearance.
Preview
Code
## Required
The `isRequired` prop marks the `InputOtp` as a required field.
Preview
Code
## Sizes
The size of the `InputOtp` can be customized using the `size` prop. The default value is `md`.
Preview
Code
## Colors
Color of the `InputOtp` can be changed by `color` property.
Preview
Code
## Variants
Styling/Variant of the `InputOtp` can be changed by `variant` property. By default, `variant` property is set to `flat`.
Preview
Code
## Radius
Radius of the `InputOtp` can be changed by `radius` property. By default, `radius` property is set to `md`.
Preview
Code
## Password
`InputOtp` can be used as password/secured-pin input by setting `type` as `password`.
Preview
Code
## Description
Description of the `InputOtp` can be set by `description` property.
Preview
Code
## Error Message
Custom error message of the `InputOtp` can be set by `errorMessage` property.
Preview
Code
## Allowed Keys
  * The `InputOtp` component only accepts specified input keys. Any other input is ignored.
  * You can customize the allowed keys using the `allowedKeys` prop, which accepts a regex pattern.
  * By default, `allowedKeys` is set to `^[0-9]*$` (only numerical digits).


Preview
Code
## Controlled
Preview
Code
## React Hook Form
You can use `InputOtp` with React Hook Form for form validation and submission handling.
Preview
Code
## Different Lengths & Validation
The `InputOtp` component supports different lengths through the `length` property. You can set the number of input segments by passing a number value to the `length` prop. Common use cases include 4-digit PINs and 6-digit authentication codes.
Preview
Code
## Custom Styles
You can customize the styles of the `InputOtp` component using the `classNames` prop.
Preview
Code
## Slots
  * **base** : InputOtp wrapper, it handles alignment, placement, and general appearance.
  * **wrapper** : Wraps the underlying input-otp component. Sent as `containerClassName` prop to underlying input-otp component.
  * **input** : The input element.
  * **segmentWrapper** : Wraps all the segment elements.
  * **segment** : The segment element.
  * **caret** : The caret represents the typing indicator of the input-otp component.
  * **passwordChar** : The passwordChar represents the text styling when input-type is password.
  * **helperWrapper** : Wraps the `description` and the `errorMessage`.
  * **description** : The description of the input-otp.
  * **errorMessage** : The error message of the input-otp.


## Data Attributes
`InputOtp` has the following attributes on the `base` element:
  * **data-invalid** : When the input-otp is invalid. Based on `isInvalid` prop.
  * **data-required** : When the input-otp is required. Based on `isRequired` prop.
  * **data-readonly** : When the input-otp is readonly. Based on `isReadOnly` prop.
  * **data-filled** : When the input-otp is completely filled.
  * **data-disabled** : When the input-otp is disabled. Based on `isDisabled` prop.


`InputOtp` also has the following attributes on the `segment` element:
  * **data-active** : When the segment is active.
  * **data-focus** : When the segment is focused.
  * **data-focus-visible** : When the segment is focused visible.
  * **data-has-value** : When the segment has value.


## Accessibility
  * Built on top of input-otp.
  * Required and invalid states exposed to assistive technology via ARIA.
  * Support for description and error message help text linked to the input-otp via ARIA.
  * Keyboard navigation: 
    * Tab: Moves focus between input segments
    * Arrow keys: Navigate between segments
    * Backspace: Clears current segment and moves focus to previous segment
  * ARIA attributes: 
    * `aria-invalid`: Indicates validation state
    * `aria-required`: Indicates if the input is required


## API
### InputOtp Props
Prop| Type| Default  
---|---|---  
`length`| `number`| `"4"`  
`allowedKeys`| `regEx string`| `"^[0-9]*$"`  
`variant`| `flat | bordered | faded | underlined`| `"flat"`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`size`| `sm | md | lg`| `"md"`  
`radius`| `none | sm | md | lg | full`  
`value`| `string`  
`defaultValue`| `string`  
`description`| `ReactNode`  
`errorMessage`| `ReactNode | ((v: ValidationResult) => ReactNode)`  
`fullWidth`| `boolean`| `false`  
`isRequired`| `boolean`| `false`  
`isReadOnly`| `boolean`| `false`  
`isDisabled`| `boolean`| `false`  
`isInvalid`| `boolean`| `false`  
`baseRef`| `RefObject<HTMLDivElement>`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<'base' | 'inputWrapper' | 'input' | 'segmentWrapper' | 'segment' | 'caret' | 'passwordChar' | 'helperWrapper' | 'description' | 'errorMessage', string>>`  
`autoFocus`| `boolean`| `false`  
`textAlign`| `left | center | right`| `"center"`  
`pushPasswordManagerStrategy`| `'none' | 'hidden' | 'input'`  
`pasteTransformer`| `(text: string) => string`  
`containerClassName`| `string`  
`noScriptCSSFallback`| `string`  
### InputOtp Events
Prop| Type| Default  
---|---|---  
`onChange`| `React.ChangeEvent<HTMLInputElement>`  
`onValueChange`| `(value: string) => void`  
`onComplete`| `(value: string) => void`  
InputKbd
On this page
  * Installation
  * Import
  * Usage
  * Disabled
  * Read Only
  * Required
  * Sizes
  * Colors
  * Variants
  * Radius
  * Password
  * Description
  * Error Message
  * Allowed Keys
  * Controlled
  * React Hook Form
  * Different Lengths & Validation
  * Custom Styles
  * Slots
  * Data Attributes
  * Accessibility
  * API
  * InputOtp Props
  * InputOtp Events
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
