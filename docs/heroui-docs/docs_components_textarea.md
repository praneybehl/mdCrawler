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


# Textarea
Textarea component is a multi-line Input which allows you to write large texts.
Storybook@heroui/inputReact AriaSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add input

```


```

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
### Read Only
Preview
Code
### Required
If you pass the `isRequired` property to the input, it will have a `danger` asterisk at the end of the label and the textarea will be required.
Preview
Code
### Clear Button
If you pass the `isClearable` property to the textarea, it will have a clear button at the end of the textarea, it will be visible when the textarea has a value.
Preview
Code
### Autosize
Textarea grows automatically based on the content, but you can also set a min and max height to it using the `minRows` and `maxRows` properties. It is based on react-textarea-autosize.
Preview
Code
### Without Autosize
In case you want to disable the autosize feature, you can use the `disableAutosize` property.
Preview
Code
### Variants
Preview
Code
### With Error Message
You can combine the `isInvalid` and `errorMessage` properties to show an invalid textarea.
Preview
Code
### Description
Preview
Code
### Controlled
You can use the `value` and `onValueChange` properties to control the input value.
Preview
Code
> **Note** : HeroUI `Textarea` also supports native events like `onChange`, useful for form libraries such as Formik and React Hook Form.
## Slots
  * **base** : Input wrapper, it handles alignment, placement, and general appearance.
  * **label** : Label of the textarea, it is the one that is displayed above, inside or left of the textarea.
  * **inputWrapper** : Wraps the `label` (when it is inside) and the `innerWrapper`.
  * **input** : The textarea input element.
  * **description** : The description of the textarea.
  * **errorMessage** : The error message of the textarea.
  * **headerWrapper** : Wraps the `label` and the `clearButton`.


## Data Attributes
`Textarea` has the following attributes on the `base` element:
  * **data-invalid** : When the textarea is invalid. Based on `isInvalid` prop.
  * **data-required** : When the textarea is required. Based on `isRequired` prop.
  * **data-readonly** : When the textarea is readonly. Based on `isReadOnly` prop.
  * **data-hover** : When the textarea is being hovered. Based on useHover
  * **data-focus** : When the textarea is being focused. Based on useFocusRing.
  * **data-focus-visible** : When the textarea is being focused with the keyboard. Based on useFocusRing.
  * **data-disabled** : When the textarea is disabled. Based on `isDisabled` prop.


## Accessibility
  * Built with a native `<input>` element.
  * Visual and ARIA labeling support.
  * Change, clipboard, composition, selection, and input event support.
  * Required and invalid states exposed to assistive technology via ARIA.
  * Support for description and error message help text linked to the input via ARIA.


## API
### Textarea Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode`  
`minRows`| `number`| `"3"`  
`maxRows`| `number`| `"8"`  
`cacheMeasurements`| `boolean`| `false`  
`variant`| `flat | bordered | faded | underlined`| `"flat"`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`size`| `sm | md | lg`| `"md"`  
`radius`| `none | sm | md | lg | full`  
`label`| `ReactNode`  
`value`| `string`  
`defaultValue`| `string`  
`placeholder`| `string`  
`startContent`| `ReactNode`  
`endContent`| `ReactNode`  
`description`| `ReactNode`  
`errorMessage`| `ReactNode | ((v: ValidationResult) => ReactNode)`  
`validate`| `(value: string) => ValidationError | true | null | undefined`  
`validationBehavior`| `native | aria`| `"native"`  
`labelPlacement`| `inside | outside | outside-left`| `"inside"`  
`fullWidth`| `boolean`| `true`  
`isRequired`| `boolean`| `false`  
`isReadOnly`| `boolean`  
`isDisabled`| `boolean`| `false`  
`isClearable`| `boolean`| `false`  
`isInvalid`| `boolean`| `false`  
`validationState`| `valid | invalid`  
`disableAutosize`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<"base" | "label" | "inputWrapper" | "innerWrapper" | "input" | "description" | "errorMessage", string>>`  
### Input Events
Prop| Type| Default  
---|---|---  
`onChange`| `React.ChangeEvent<HTMLInputElement>`  
`onValueChange`| `(value: string) => void`  
`onClear`| `() => void`  
`onHeightChange`| `(height: number, meta: { rowHeight: number }) => void`  
ToastTime Input
On this page
  * Installation
  * Import
  * Usage
  * Disabled
  * Read Only
  * Required
  * Clear Button
  * Autosize
  * Without Autosize
  * Variants
  * With Error Message
  * Description
  * Controlled
  * Slots
  * Data Attributes
  * Accessibility
  * API
  * Textarea Props
  * Input Events
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
