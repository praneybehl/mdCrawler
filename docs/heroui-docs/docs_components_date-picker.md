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


# DatePicker
DatePickers combine a DateInput and a Calendar popover to allow users to enter or select a date and time value.
Storybook@heroui/date-pickerSourceStyles source
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
### With Description
You can add a description to the date-picker by passing the `description` property.
Preview
Code
### With Error Message
You can combine the `isInvalid` and `errorMessage` properties to show an invalid input.
Preview
Code
You can also pass an error message as a function. This allows for dynamic error message handling based on the ValidationResult.
Preview
Code
### With Month and Year Pickers
You can show month and year pickers in the calendar popover by setting the `showMonthAndYearPickers` property to `true`. However, passing a number greater than 1 to the `visibleMonths` prop will disable this feature.
Preview
Code
### With Time Fields
Preview
Code
### Selector Icon
You can use the `selector` to add content to the start and end of the date-picker.
Preview
Code
### Selector Button Placement
You can change the position of the selector button by setting the `selectorButtonPlacement` property to `start` or `end`.
Preview
Code
### Controlled
You can use the `value` and `onChange` properties to control the input value.
Preview
Code
### Time Zones
DatePicker is time zone aware when a `ZonedDateTime` object is provided as the value. In this case, the time zone abbreviation is displayed, and time zone concerns such as daylight saving time are taken into account when the value is manipulated.
@internationalized/date includes functions for parsing strings in multiple formats into `ZonedDateTime` objects.
npm
yarn
pnpm
Preview
Code
### Granularity
The granularity prop allows you to control the smallest unit that is displayed by DatePicker By default, the value is displayed with "day" granularity (year, month, and day), and `CalendarDateTime` and `ZonedDateTime` values are displayed with "minute" granularity.
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
DatePicker supports selecting dates in many calendar systems used around the world, including Gregorian, Hebrew, Indian, Islamic, Buddhist, and more. Dates are automatically displayed in the appropriate calendar system for the user's locale. The calendar system can be overridden using the Unicode calendar locale extension, passed to the I18nProvider component.
@internationalized/date includes functions for parsing strings in multiple formats into `ZonedDateTime` objects.
npm
yarn
pnpm
Preview
Code
### Unavailable Dates
DatePicker supports marking certain dates as unavailable. These dates cannot be selected by the user and are displayed with a crossed out appearance in the calendar. In the date field, an invalid state is displayed if a user enters an unavailable date.
@internationalized/date includes functions for parsing strings in multiple formats into `ZonedDateTime` objects.
npm
yarn
pnpm
Preview
Code
### Visible Months
By default, the calendar popover displays a single month. The `visibleMonths` prop allows displaying up to 3 months at a time, if screen space permits.
Preview
Code
### Custom first day of week
By default, the first day of the week is automatically set based on the current locale. This can be changed by setting the `firstDayOfWeek` prop to `'sun'`, `'mon'`, `'tue'`, `'wed'`, `'thu'`, `'fri'`, or `'sat'`.
Preview
Code
### Page Behavior
By default, when pressing the next or previous buttons, pagination will advance by the `visibleMonths` value. This behavior can be changed to page by single months instead, by setting `pageBehavior` to `single`.
Preview
Code
### Preset
@internationalized/date includes functions for parsing strings in multiple formats into `ZonedDateTime` objects.
npm
yarn
pnpm
Preview
Code
## Slots
  * **base** : Input wrapper, it handles alignment, placement, and general appearance.
  * **selectorButton** : Selector button element.
  * **selectorIcon** : Selector icon element.
  * **popoverContent** : The calendar popover element.
  * **calendar** : The calendar element.
  * **calendarContent** : The calendar's content element.
  * **timeInputLabel** : The time-input component's label element.
  * **timeInput** : The time-input component element.


## Data Attributes
`DatePicker` has the following attributes on the `base` element:
  * **data-slot** : All slots have this prop. which slot the element represents(e.g. `calendar`).
  * **data-open** : Indicates if the calendar popover is open.
  * **data-invalid** : When the date-picker is invalid. Based on `isInvalid` prop.
  * **data-required** : When the date-picker is required. Based on `isRequired` prop.
  * **data-readonly** : When the date-picker is readonly. Based on `isReadOnly` prop.
  * **data-disabled** : When the date-picker is disabled. Based on `isDisabled` prop.


## Accessibility
  * Each date and time unit is displayed as an individually focusable and editable segment, which allows users an easy way to edit dates using the keyboard, in any date format and locale.
  * Users can also open a calendar popover to select dates in a standard month grid.
  * Localized screen reader messages are included to announce when the selection and visible date range change.
  * Date segments are editable using an easy to use numeric keypad, and all interactions are accessible using touch-based screen readers.
  * Integrates with HTML forms, supporting required, minimum and maximum values, unavailable dates, custom validation functions, realtime validation, and server-side validation errors


## API
### DatePicker Props
Prop| Type| Default  
---|---|---  
`label`| `ReactNode`  
`value`| `ZonedDateTime | CalendarDate | CalendarDateTime | undefined | null`  
`variant`| `flat | bordered | faded | underlined`| `"flat"`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`size`| `sm | md | lg`| `"md"`  
`radius`| `none | sm | md | lg | full`  
`defaultValue`| `string`  
`placeholderValue`| `ZonedDateTime | CalendarDate | CalendarDateTime | undefined | null`  
`description`| `ReactNode`  
`errorMessage`| `ReactNode | (v: ValidationResult) => ReactNode`  
`validate`| `(value: MappedDateValue<DateValue>) => ValidationError | true | null | undefined`  
`validationBehavior`| `native | aria`| `"native"`  
`startContent`| `ReactNode`  
`endContent`| `ReactNode`  
`labelPlacement`| `inside | outside | outside-left`| `"inside"`  
`isRequired`| `boolean`| `false`  
`isReadOnly`| `boolean`| `false`  
`isDisabled`| `boolean`| `false`  
`isInvalid`| `boolean`| `false`  
`visibleMonths`| `number`| `"1"`  
`firstDayOfWeek`| `sun | mon | tue | wed | thu | fri | sat`  
`selectorIcon`| `ReactNode`  
`pageBehavior`| `PageBehavior`| `"visible"`  
`calendarWidth`| `number`| `"256"`  
`isDateUnavailable`| `(date: DateValue) => boolean`  
`autoFocus`| `boolean`| `false`  
`hourCycle`| `12 | 24`  
`granularity`| `day | hour | minute | second`  
`hideTimeZone`| `boolean`| `false`  
`shouldForceLeadingZeros`| `boolean`| `true`  
`CalendarBottomContent`| `ReactNode`  
`showMonthAndYearPickers`| `boolean | undefined`| `false`  
`popoverProps`| `PopoverProps | undefined`| `"{ placement: "bottom", triggerScaleOnOpen: false, offset: 13 }"`  
`selectorButtonProps`| `ButtonProps | undefined`| `"{ size: "sm", variant: "light", radius: "full", isIconOnly: true }"`  
`calendarProps`| `CalendarProps | undefined`| `"{ size: "sm", variant: "light", radius: "full", isIconOnly: true }"`  
`timeInputProps`| `TimeInputProps | undefined`| `"{ size: "sm", variant: "light", radius: "full", isIconOnly: true }"`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<"base" | "selectorButton" | "selectorIcon" | "popoverContent" | "calendar" | "calendarContent" | "timeInputLabel" | "timeInput", string>>`  
### DatePicker Events
Prop| Type| Default  
---|---|---  
`onChange`| `(value: ZonedDateTime | CalendarDate | CalendarDateTime) => void`  
`onFocus`| `(e: FocusEvent<HTMLInputElement>) => void`  
`onBlur`| `(e: FocusEvent<HTMLInputElement>) => void`  
`onFocusChange`| `(isFocused: boolean) => void`  
`onKeyDown`| `(e: KeyboardEvent) => void`  
`onKeyUp`| `(e: KeyboardEvent) => void`  
Date InputDate Range Picker
On this page
  * Installation
  * Import
  * Usage
  * Disabled
  * Read Only
  * Required
  * Variants
  * Label Placements
  * With Description
  * With Error Message
  * With Month and Year Pickers
  * With Time Fields
  * Selector Icon
  * Selector Button Placement
  * Controlled
  * Time Zones
  * Granularity
  * Min Date And Max Date
  * International Calendar
  * Unavailable Dates
  * Visible Months
  * Custom first day of week
  * Page Behavior
  * Preset
  * Slots
  * Data Attributes
  * Accessibility
  * API
  * DatePicker Props
  * DatePicker Events
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
