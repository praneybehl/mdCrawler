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


# Radio group
Radio Group allow users to select a single option from a list of mutually exclusive options.
Storybook@heroui/radioReact AriaSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
Individual
Global
## Usage
Preview
Code
### Disabled
Preview
Code
### Default Value
Preview
Code
### With Description
Preview
Code
### Horizontal
Preview
Code
### Controlled
You can use the `value` and `onValueChange` properties to control the radio input value.
Preview
Code
> **Note** : HeroUI `Radio` also supports native events like `onChange`, useful for form libraries such as Formik and React Hook Form.
### Invalid
Preview
Code
## Slots
  * RadioGroup Slots
    * **base** : Radio group root wrapper, it wraps the label and the wrapper.
    * **wrapper** : Radio group wrapper, it wraps all Radios.
    * **label** : Radio group label, it is placed before the wrapper.
    * **description** : Description slot for the radio group.
    * **errorMessage** : Error message slot for the radio group.
  * Radio Slots
    * **base** : Radio root wrapper, it wraps all elements.
    * **wrapper** : Radio wrapper, it wraps the control element.
    * **hiddenInput** : The hidden input element that is used to handle the radio state.
    * **labelWrapper** : Label and description wrapper.
    * **label** : Label slot for the radio.
    * **control** : Control element, it is the circle element.
    * **description** : Description slot for the radio.


### Custom Styles
You can customize the `RadioGroup` and `Radio` component by passing custom Tailwind CSS classes to the component slots.
Preview
Code
### Custom Implementation
In case you need to customize the radio group even further, you can use the `useRadio` hook to create your own implementation.
Preview
Code
## Data Attributes
  * RadioGroup has the following attributes on the `base` element:
    * **data-orientation** : The orientation of the radio group. Based on `orientation` prop.
  * Radio has the following attributes on the `base` element:
    * **data-selected** : When the radio is checked. Based on `isSelected` prop.
    * **data-pressed** : When the radio is pressed. Based on usePress.
    * **data-invalid** : When the radio is invalid. Based on `validationState` prop.
    * **data-readonly** : When the radio is readonly. Based on `isReadOnly` prop.
    * **data-hover-unselected** : When the radio is being hovered and unchecked. Based on useHover.
    * **data-hover** : When the radio is being hovered. Based on useHover.
    * **data-focus** : When the radio is being focused. Based on useFocusRing.
    * **data-focus-visible** : When the radio is being focused with the keyboard. Based on useFocusRing.
    * **data-disabled** : When the radio is disabled. Based on `isDisabled` prop.


## Accessibility
  * Radio groups are exposed to assistive technology via ARIA.
  * Each radio is built with a native HTML `<input>` element, which can be optionally visually hidden to allow custom styling.
  * Full support for browser features like form autofill.
  * Keyboard event support for arrows keys.
  * Keyboard focus management and cross browser normalization.
  * Group and radio labeling support for assistive technology.


## API
### RadioGroup Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode | ReactNode[]`  
`label`| `ReactNode`  
`size`| `sm | md | lg`| `"md"`  
`color`| `default | primary | secondary | success | warning | danger`| `"primary"`  
`orientation`| `horizontal | vertical`| `"vertical"`  
`name`| `string`  
`value`| `string[]`  
`defaultValue`| `string[]`  
`description`| `ReactNode`  
`errorMessage`| `ReactNode | ((v: ValidationResult) => ReactNode)`  
`validate`| `(value: string) => ValidationError | true | null | undefined`  
`validationBehavior`| `native | aria`| `"native"`  
`isDisabled`| `boolean`| `false`  
`isRequired`| `boolean`| `false`  
`isReadOnly`| `boolean`  
`isInvalid`| `boolean`| `false`  
`validationState`| `valid | invalid`| `false`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<"base" | "wrapper" | "label", string>>`  
### RadioGroup Events
Prop| Type| Default  
---|---|---  
`onChange`| `React.ChangeEvent<HTMLInputElement>`  
`onValueChange`| `((value: string) => void)`  
### Radio Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode`  
`label`| `ReactNode`  
`size`| `sm | md | lg`| `"md"`  
`color`| `default | primary | secondary | success | warning | danger`| `"primary"`  
`description`| `ReactNode`  
`isDisabled`| `boolean`| `false`  
`isRequired`| `boolean`| `false`  
`isReadOnly`| `boolean`  
`isInvalid`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<"base" | "wrapper" | "labelWrapper" | "label" | "control" | "description", string>>`  
ProgressRange Calendar
On this page
  * Installation
  * Import
  * Usage
  * Disabled
  * Default Value
  * With Description
  * Horizontal
  * Controlled
  * Invalid
  * Slots
  * Custom Styles
  * Custom Implementation
  * Data Attributes
  * Accessibility
  * API
  * RadioGroup Props
  * RadioGroup Events
  * Radio Props
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
