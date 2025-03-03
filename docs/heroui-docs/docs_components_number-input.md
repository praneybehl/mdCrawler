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


# Number Input
The numeric input component is designed for users to enter a number, and increase or decrease the value using stepper buttons
Storybook@heroui/number-inputReact AriaSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
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
If you pass the `isRequired` property to the input, it will have a `danger` asterisk at the end of the label and the input will be required.
Preview
Code
### Sizes
Preview
Code
### Colors
Preview
Code
### Variants
Preview
Code
### Radius
Preview
Code
### Label Placements
You can change the position of the label by setting the `labelPlacement` property to `inside`, `outside` or `outside-left`.
Preview
Code
> **Note** : If the `label` is not passed, the `labelPlacement` property will be `outside` by default.
### Clear Button
If you pass the `isClearable` property to the input, it will have a clear button at the end of input, it will be visible when input has a value.
Preview
Code
### Hide Stepper
You can hide the stepper buttons by passing the `hideStepper` property.
Preview
Code
### Start & End Content
You can use the `startContent` and `endContent` properties to add content to the start and end of NumberInput.
Preview
Code
### With Label
You can add a label to the input by passing the `label` property.
Preview
Code
### With Description
You can add a description to the input by passing the `description` property.
Preview
Code
### With Min Value
You can set the minimum value of the input by passing the `minValue` property.
Preview
Code
### With Max Value
You can set the maximum value of the input by passing the `maxValue` property.
Preview
Code
### With Wheel Disabled
By default, you can increase or decrease the value with scroll wheel. You can disable changing the vaule with scroll in NumberInput by passing the `isWheelDisabled` property.
Preview
Code
### With Format Options
You can format the value of the input by passing the `formatOptions` property.
Preview
Code
### With Error Message
You can combine the `isInvalid` and `errorMessage` properties to show an invalid input. `errorMessage` is only shown when `isInvalid` is set to `true`.
Preview
Code
### Controlled
You can use the `value` and `onValueChange` properties to control the input value.
Preview
Code
> **Note** : HeroUI `NumberInput` also supports native events like `onChange`, useful for form libraries such as Formik and React Hook Form.
### With Form
`NumberInput` can be used with a `Form` component to leverage form state management. For more on form and validation behaviors, see the Forms guide.
#### Custom Validation
In addition to built-in constraints, you can provide a function to the `validate` property for custom validation.
Preview
Code
#### Realtime Validation
If you want to display validation errors while the user is typing, you can control the field value and use the `isInvalid` prop along with the `errorMessage` prop.
Preview
Code
#### Server Validation
Client-side validation provides immediate feedback, but you should also validate data on the server to ensure accuracy and security. HeroUI allows you to display server-side validation errors by using the `validationErrors` prop in the `Form` component. This prop should be an object where each key is the field `name` and the value is the error message.
Preview
Code
## Slots
  * **base** : Input wrapper, it handles alignment, placement, and general appearance.
  * **label** : Label of the input, it is the one that is displayed above, inside or left of the input.
  * **mainWrapper** : Wraps the `inputWrapper`
  * **inputWrapper** : Wraps the `label` (when it is inside) and the `innerWrapper`.
  * **innerWrapper** : Wraps the `input`, the `startContent` and the `endContent`.
  * **input** : The input element.
  * **clearButton** : The clear button, it is at the end of the input.
  * **stepperButton** : The stepper button to increase or decrease the value.
  * **stepperWrapper** : The wrapper for the stepper.
  * **description** : The description of NumberInput.
  * **errorMessage** : The error message of NumberInput.


### Custom Styles
You can customize the `NumberInput` component by passing custom Tailwind CSS classes to the component slots.
Preview
Code
## Data Attributes
`NumberInput` has the following attributes on the `base` element:
  * **data-invalid** : When the input is invalid. Based on `isInvalid` prop.
  * **data-required** : When the input is required. Based on `isRequired` prop.
  * **data-readonly** : When the input is readonly. Based on `isReadOnly` prop.
  * **data-hover** : When the input is being hovered. Based on useHover
  * **data-focus** : When the input is being focused. Based on useFocusRing.
  * **data-focus-within** : When the input is being focused or any of its children. Based on useFocusWithin.
  * **data-focus-visible** : When the input is being focused with the keyboard. Based on useFocusRing.
  * **data-disabled** : When the input is disabled. Based on `isDisabled` prop.
  * **data-filled** : When the input has content, placeholder, start content or the placeholder is shown.
  * **data-has-elements** : When the input has any element (label, helper text, description, error message).
  * **data-has-helper** : When the input has helper text.
  * **data-has-description** : When the input has a description.
  * **data-has-label** : When the input has a label.
  * **data-has-value** : When the input has a value (placeholder is not shown).


## Accessibility
  * Built with a native `<input>` element with `type="number"`.
  * Visual and ARIA labeling support.
  * Change, clipboard, composition, selection, and input event support.
  * Required and invalid states exposed to assistive technology via ARIA.
  * Support for description, helper text, and error message linked to the input via ARIA.


## API
### NumberInput Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode`  
`variant`| `flat | bordered | faded | underlined`| `"flat"`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`size`| `sm | md | lg`| `"md"`  
`radius`| `none | sm | md | lg | full`  
`name`| `string`  
`label`| `ReactNode`  
`description`| `ReactNode`  
`value`| `string`  
`defaultValue`| `string`  
`placeholder`| `string`  
`errorMessage`| `ReactNode | ((v: ValidationResult) => ReactNode)`  
`validate`| `(value: string) => ValidationError | true | null | undefined`  
`validationBehavior`| `native | aria`| `"native"`  
`minValue`| `number`  
`maxValue`| `number`  
`formatOptions`| `Intl.NumberFormatOptions`  
`step`| `number`| `"1"`  
`hideStepper`| `boolean`  
`isWheelDisabled`| `boolean`  
`startContent`| `ReactNode`  
`endContent`| `ReactNode`  
`labelPlacement`| `inside | outside | outside-left`| `"inside"`  
`fullWidth`| `boolean`| `true`  
`isClearable`| `boolean`| `false`  
`isRequired`| `boolean`| `false`  
`isReadOnly`| `boolean`| `false`  
`isDisabled`| `boolean`| `false`  
`isInvalid`| `boolean`| `false`  
`incrementAriaLabel`| `string`  
`decrementAriaLabel`| `string`  
`baseRef`| `RefObject<HTMLDivElement>`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<'base' | 'label' | 'inputWrapper' | 'innerWrapper' | 'mainWrapper' | 'input' | 'clearButton' | 'stepperButton' | 'helperWrapper' | 'stepperWrapper' | 'description' | 'errorMessage', string>>`  
### NumberInput Events
Prop| Type| Default  
---|---|---  
`onChange`| `React.ChangeEvent<HTMLInputElement>`  
`onValueChange`| `(value: number) => void`  
`onClear`| `() => void`  
NavbarPagination
On this page
  * Installation
  * Usage
  * Disabled
  * Read Only
  * Required
  * Sizes
  * Colors
  * Variants
  * Radius
  * Label Placements
  * Clear Button
  * Hide Stepper
  * Start & End Content
  * With Label
  * With Description
  * With Min Value
  * With Max Value
  * With Wheel Disabled
  * With Format Options
  * With Error Message
  * Controlled
  * With Form
  * Custom Validation
  * Realtime Validation
  * Server Validation
  * Slots
  * Custom Styles
  * Data Attributes
  * Accessibility
  * API
  * NumberInput Props
  * NumberInput Events
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
