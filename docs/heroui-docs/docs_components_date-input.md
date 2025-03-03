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


# DateInput
DateInput is a component that allows users to enter and edit date and time values using a keyboard. Each part of a date value is displayed in an individually editable segment.
Storybook@heroui/date-inputSourceStyles source
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
### Read Only
Preview
Code
### Required
Preview
Code
### Variants
Preview
Code
### Label Placements
You can change the position of the label by setting the `labelPlacement` property to `inside`, `outside` or `outside-left`.
Preview
Code
> **Note** : If the `label` is not passed, the `labelPlacement` property will be `outside` by default.
### Start & End Content
You can use the `startContent` and `endContent` properties to add content to the start and end of the `DateInput`.
Preview
Code
### With Description
You can add a description to the input by passing the `description` property.
Preview
Code
### With Error Message
You can combine the `isInvalid` and `errorMessage` properties to show an invalid input.
Preview
Code
You can also pass an error message as a function. This allows for dynamic error message handling based on the ValidationResult.
Preview
Code
### Controlled
You can use the `value` and `onChange` properties to control the input value.
Preview
Code
### Time Zones
DateInput is time zone aware when a `ZonedDateTime` object is provided as the value. In this case, the time zone abbreviation is displayed, and time zone concerns such as daylight saving time are taken into account when the value is manipulated.
@internationalized/date includes functions for parsing strings in multiple formats into `ZonedDateTime` objects.
npm
yarn
pnpm
Preview
Code
### Granularity
The granularity prop allows you to control the smallest unit that is displayed by DateInput By default, the value is displayed with "day" granularity (year, month, and day), and `CalendarDateTime` and `ZonedDateTime` values are displayed with "minute" granularity.
@internationalized/date includes functions for parsing strings in multiple formats into `ZonedDateTime` objects.
npm
yarn
pnpm
Preview
Code
### Min Date And Max Date
The minValue and maxValue props can also be used to ensure the value is within a specific range.
@internationalized/date includes functions for parsing strings in multiple formats into `ZonedDateTime` objects.
npm
yarn
pnpm
Preview
Code
### International Calendar
DateInput supports selecting dates in many calendar systems used around the world, including Gregorian, Hebrew, Indian, Islamic, Buddhist, and more. Dates are automatically displayed in the appropriate calendar system for the user's locale. The calendar system can be overridden using the Unicode calendar locale extension, passed to the I18nProvider component.
@internationalized/date includes functions for parsing strings in multiple formats into `ZonedDateTime` objects.
npm
yarn
pnpm
Preview
Code
### Hide Time Zone
When a `ZonedDateTime` object is provided as the value to DateInput, the time zone abbreviation is displayed by default. However, if this is displayed elsewhere or implicit based on the usecase, it can be hidden using the hideTimeZone option.
@internationalized/date includes functions for parsing strings in multiple formats into `ZonedDateTime` objects.
npm
yarn
pnpm
Preview
Code
### Hourly Cycle
By default, DateInput displays times in either 12 or 24 hour hour format depending on the user's locale. However, this can be overridden using the `hourCycle` prop if needed for a specific usecase. This example forces DateInput to use 24-hour time, regardless of the locale.
@internationalized/date includes functions for parsing strings in multiple formats into `ZonedDateTime` objects.
npm
yarn
pnpm
Preview
Code
## Slots
  * **base** : Input wrapper, it handles alignment, placement, and general appearance.
  * **label** : Label of the date-input, it is the one that is displayed above, inside or left of the date-input.
  * **inputWrapper** : Wraps the `label` (when it is inside) and the `innerWrapper`.
  * **input** : The date-input element.
  * **innerWrapper** : Wraps the `input`, the `startContent` and the `endContent`.
  * **clearButton** : The clear button, it is at the end of the input.
  * **helperWrapper** : Wraps the `description` and the `errorMessage`.
  * **description** : The description of the date-input.
  * **errorMessage** : The error message of the date-input.


## Data Attributes
`DateInput` has the following attributes on the `base` element:
  * **data-slot** : All slots have this prop. which slot the element represents(e.g. `slot`).
  * **data-invalid** : When the date-input is invalid. Based on `isInvalid` prop.
  * **data-required** : When the date-input is required. Based on `isRequired` prop.
  * **data-readonly** : When the date-input is readonly. Based on `isReadOnly` prop.
  * **data-disabled** : When the date-input is disabled. Based on `isDisabled` prop.
  * **data-has-helper** : When the date-input has helper text(`errorMessage` or `description`). Base on those two props.
  * **data-has-start-content** : When the date-input has a start content. Base on those `startContent` prop.
  * **data-has-end-content** : When the date-input has a end content. Base on those `endContent` prop.


## Accessibility
  * Built with a native `<input>` element.
  * Visual and ARIA labeling support.
  * Change, clipboard, composition, selection, and input event support.
  * Required and invalid states exposed to assistive technology via ARIA.
  * Support for description and error message help text linked to the input via ARIA.
  * Each date and time unit is displayed as an individually focusable and editable segment, which allows users an easy way to edit dates using the keyboard, in any date format and locale.
  * Date segments are editable using an easy to use numeric keypad, and all interactions are accessible using touch-based screen readers.


## API
### DateInput Props
Prop| Type| Default  
---|---|---  
`label`| `ReactNode`  
`value`| `DateValue`  
`defaultValue`| `DateValue`  
`variant`| `flat | bordered | faded | underlined`| `"flat"`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`size`| `sm | md | lg`| `"md"`  
`radius`| `none | sm | md | lg | full`  
`placeholderValue`| `DateValue`  
`minValue`| `DateValue`  
`maxValue`| `DateValue`  
`locale`| `string`  
`description`| `ReactNode`  
`errorMessage`| `ReactNode | (v: ValidationResult) => ReactNode`  
`labelPlacement`| `inside | outside | outside-left`| `"inside"`  
`isRequired`| `boolean`| `false`  
`isReadOnly`| `boolean`  
`isDisabled`| `boolean`| `false`  
`isInvalid`| `boolean`| `false`  
`autoFocus`| `boolean`| `false`  
`hideTimeZone`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<"base" | "label" | "inputWrapper" | "input" | "segment" | "helperWrapper" | "description" | "errorMessage", string>>`  
### DateInput Events
Prop| Type| Default  
---|---|---  
`onChange`| `(value: ZonedDateTime | CalendarDate | CalendarDateTime) => void`  
`onFocus`| `(e: FocusEvent<HTMLInputElement>) => void`  
`onBlur`| `(e: FocusEvent<HTMLInputElement>) => void`  
`onFocusChange`| `(isFocused: boolean) => void`  
`onKeyDown`| `(e: KeyboardEvent) => void`  
`onKeyUp`| `(e: KeyboardEvent) => void`  
CodeDate Picker
On this page
  * Installation
  * Import
  * Usage
  * Disabled
  * Read Only
  * Required
  * Variants
  * Label Placements
  * Start & End Content
  * With Description
  * With Error Message
  * Controlled
  * Time Zones
  * Granularity
  * Min Date And Max Date
  * International Calendar
  * Hide Time Zone
  * Hourly Cycle
  * Slots
  * Data Attributes
  * Accessibility
  * API
  * DateInput Props
  * DateInput Events
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
