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


# Date Range Picker
Date Range Picker combines two DateInputs and a RangeCalendar popover to allow users to enter or select a date and time range.
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
If you pass the `isRequired` property to the input, it will have a `danger` asterisk at the end of the label and the input will be required.
Preview
Code
### Variants
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
### Label Placements
You can change the position of the label by setting the `labelPlacement` property to `inside`, `outside` or `outside-left`.
Preview
Code
> **Note** : If the `label` is not passed, the `labelPlacement` property will be `outside` by default.
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
### With Month and Year Pickers
You can show month and year pickers in the calendar popover by setting the `showMonthAndYearPickers` property to `true`. However, passing a number greater than 1 to the `visibleMonths` prop will disable this feature.
Preview
Code
### With Time Fields
DateRangePicker automatically includes time fields when a `CalendarDateTime` or `ZonedDateTime` object is provided as the value.
Preview
Code
### Selector Icon
You can use the `selector` to add content to the start and end of the date-range-picker.
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
DateRangePicker is time zone aware when a `ZonedDateTime` object is provided as the value. In this case, the time zone abbreviation is displayed, and time zone concerns such as daylight saving time are taken into account when the value is manipulated.
@internationalized/date includes functions for parsing strings in multiple formats into `ZonedDateTime` objects.
npm
yarn
pnpm
Preview
Code
### Granularity
The granularity prop allows you to control the smallest unit that is displayed by DateRangePicker By default, the value is displayed with "day" granularity (year, month, and day), and `CalendarDateTime` and `ZonedDateTime` values are displayed with "minute" granularity.
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
DateRangePicker supports selecting dates in many calendar systems used around the world, including Gregorian, Hebrew, Indian, Islamic, Buddhist, and more. Dates are automatically displayed in the appropriate calendar system for the user's locale. The calendar system can be overridden using the Unicode calendar locale extension, passed to the I18nProvider component.
@internationalized/date includes functions for parsing strings in multiple formats into `ZonedDateTime` objects.
npm
yarn
pnpm
Preview
Code
### Unavailable Dates
DateRangePicker supports marking certain dates as unavailable. These dates cannot be selected by the user and are displayed with a crossed out appearance in the calendar. In the date field, an invalid state is displayed if a user enters an unavailable date.
@internationalized/date includes functions for parsing strings in multiple formats into `ZonedDateTime` objects.
npm
yarn
pnpm
Preview
Code
### Non Contiguous
The allowsNonContiguousRanges prop enables a range to be selected even if there are unavailable dates in the middle. The value emitted in the onChange event will still be a single range with a start and end property, but unavailable dates will not be displayed as selected. It is up to applications to split the full selected range into multiple as needed for business logic.
@internationalized/date includes functions for parsing strings in multiple formats into `ZonedDateTime` objects.
npm
yarn
pnpm
Preview
Code
### Presets
@internationalized/date includes functions for parsing strings in multiple formats into `ZonedDateTime` objects.
npm
yarn
pnpm
Preview
Code
## Slots
  * **base** : base element. it handles alignment, placement, and general appearance.
  * **label** : Label of the date-range-picker, it is the one that is displayed above, inside or left of the date-input.
  * **calendar** : The calendar element.
  * **selectorButton** : Selector button element.
  * **selectorIcon** : Selector icon element.
  * **popoverContent** : The calendar popover element.
  * **calendarContent** : The calendar's content element.
  * **inputWrapper** : Wraps the `label` (when it is inside) and the `innerWrapper`.
  * **input** : The input element.
  * **segment** : The segment element.
  * **separator** : The separator element.
  * **bottomContent** : The bottom content element.
  * **timeInputWrapper** : The wrapper element for the input element.
  * **helperWrapper** : Wraps the `description` and the `errorMessage`.
  * **description** : The description of the date-input.
  * **errorMessage** : The error message of the date-input.


### Custom Styles
You can customize the `DateRangePicker` component by passing custom Tailwind CSS classes to the component slots.
Preview
Code
## Data Attributes
`DateRangePicker` has the following attributes on the `base` element:
  * **data-slot** : All slots have this prop. which slot the element represents(e.g. `canlendar`).
  * **data-open** : Indicates if the calendar popover is open.
  * **data-invalid** : When the date-range-picker is invalid. Based on `isInvalid` prop.
  * **data-required** : When the date-range-picker is required. Based on `isRequired` prop.
  * **data-readonly** : When the date-range-picker is readonly. Based on `isReadOnly` prop.
  * **data-disabled** : When the date-range-picker is disabled. Based on `isDisabled` prop.
  * **data-has-start-content** : When the date-range-picker has a start content. Base on those `startContent` prop.
  * **data-has-end-content** : When the date-range-picker has a end content. Base on those `endContent` prop.
  * **data-has-multiple-months** : When the date-range-picker's `visibleMonth` is more than 2.


## Accessibility
  * Each date and time unit is displayed as an individually focusable and editable segment, which allows users an easy way to edit dates using the keyboard, in any date format and locale
  * Users can also open a calendar popover to select date ranges in a standard month grid. Localized screen reader messages are included to announce when the selection and visible date range change.
  * Date segments are editable using an easy to use numeric keypad, date ranges can be selected by dragging over dates in the calendar using a touch screen, and all interactions are accessible using touch-based screen readers.
  * Integrates with HTML forms, supporting required, minimum and maximum values, unavailable dates, custom validation functions, realtime validation, and server-side validation errors


## API
### DateRangePicker Props
Prop| Type| Default  
---|---|---  
`label`| `ReactNode`  
`value`| `RangeValue<CalendarDate | CalendarDateTime | ZonedDateTime> | undefined | null`  
`variant`| `flat | bordered | faded | underlined`| `"flat"`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`size`| `sm | md | lg`| `"md"`  
`radius`| `none | sm | md | lg | full`  
`minValue`| `RangeValue<CalendarDate | CalendarDateTime | ZonedDateTime> | undefined | null`  
`maxValue`| `RangeValue<CalendarDate | CalendarDateTime | ZonedDateTime> | undefined | null`  
`defaultValue`| `string`  
`placeholderValue`| `ZonedDateTime | CalendarDate | CalendarDateTime | undefined | null`  
`description`| `ReactNode`  
`errorMessage`| `ReactNode | (v: ValidationResult) => ReactNode`  
`validate`| `(value: RangeValue<MappedDateValue<DateValue>>) => ValidationError | true | null | undefined`  
`validationBehavior`| `native | aria`| `"native"`  
`startContent`| `ReactNode`  
`endContent`| `ReactNode`  
`startName`| `string`  
`endName`| `string`  
`labelPlacement`| `inside | outside | outside-left`| `"inside"`  
`isOpen`| `boolean`  
`defaultOpen`| `boolean`| `false`  
`isRequired`| `boolean`| `false`  
`isReadOnly`| `boolean`| `false`  
`isDisabled`| `boolean`| `false`  
`isInvalid`| `boolean`| `false`  
`selectorIcon`| `ReactNode`  
`pageBehavior`| `single | visible`| `"visible"`  
`visibleMonths`| `number`| `"1"`  
`firstDayOfWeek`| `sun | mon | tue | wed | thu | fri | sat`  
`autoFocus`| `boolean`| `false`  
`hourCycle`| `12 | 24`  
`granularity`| `day | hour | minute | second`  
`hideTimeZone`| `boolean`| `false`  
`allowsNonContiguousRanges`| `boolean`| `false`  
`shouldForceLeadingZeros`| `boolean`| `true`  
`calendarWidth`| `number`| `"256"`  
`CalendarTopContent`| `ReactNode`  
`CalendarBottomContent`| `ReactNode`  
`showMonthAndYearPickers`| `boolean`| `false`  
`popoverProps`| `PopoverProps`| `"{ placement: "bottom", triggerScaleOnOpen: false, offset: 13 }"`  
`selectorButtonProps`| `ButtonProps`| `"{ size: "sm", variant: "light", radius: "full", isIconOnly: true }"`  
`selectorButtonPlacement`| `start | end`| `"end"`  
`calendarProps`| `CalendarProps`  
`timeInputProps`| `TimeInputProps`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<"base" | "label" | "calendar" | "selectorButton" | "selectorIcon" | "popoverContent" | "calendarContent" | "inputWrapper" | "input" | "segment" | "separator" | "bottomContent" | "timeInputWrapper" | "timeInputLabel" | "timeInput" | "helperWrapper" | "description" | "errorMessage", string>>`  
### DateRangePicker Events
Prop| Type| Default  
---|---|---  
`onChange`| `(value: RangeValue<CalendarDate | CalendarDateTime | ZonedDateTime>) => void`  
`onOpenChange`| `(isOpen: boolean) => void`  
`onFocus`| `(e: FocusEvent<HTMLInputElement>) => void`  
`onBlur`| `(e: FocusEvent<HTMLInputElement>) => void`  
`onFocusChange`| `(isFocused: boolean) => void`  
`onKeyDown`| `(e: KeyboardEvent) => void`  
`onKeyUp`| `(e: KeyboardEvent) => void`  
Date PickerDivider
On this page
  * Installation
  * Import
  * Usage
  * Disabled
  * Read Only
  * Required
  * Variants
  * Visible Months
  * Custom first day of week
  * Page Behavior
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
  * Non Contiguous
  * Presets
  * Slots
  * Custom Styles
  * Data Attributes
  * Accessibility
  * API
  * DateRangePicker Props
  * DateRangePicker Events
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
