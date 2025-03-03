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


# Time Input
The `TimeInput` component consists of a label, and a group of segments representing each unit of a time (e.g. hours, minutes, and seconds). Each segment is individually focusable and editable by the user, by typing or using the arrow keys to increment and decrement the value. This approach allows values to be formatted and parsed correctly regardless of the locale or time format, and offers an easy and error-free way to edit times using the keyboard.
Storybook@heroui/date-inputReact AriaSourceStyles source
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
A `TimeInput` displays a placeholder by default. An initial, uncontrolled value can be provided to the TimeField using the defaultValue prop. Alternatively, a controlled value can be provided using the value prop.
Time values are provided using objects in the `@internationalized/date` package. This library handles correct international date and time manipulation across calendars, time zones, and other localization concerns.
`TimeInput` only supports selecting times, but values with date components are also accepted. By default, `TimeInput` will emit `Time` objects in the onChange event, but if a `CalendarDateTime` or `ZonedDateTime` object is passed as the `value` or `defaultValue`, values of that type will be emitted, changing only the time and preserving the date components.
Preview
Code
### Required
`TimeInput` supports the `isRequired` prop to ensure the user enters a value, as well as minimum and maximum values, and custom client and server-side validation.
Preview
Code
### Disabled
The `isDisabled` boolean prop makes `TimeInput` disabled. Inputs cannot be focused or selected.
Preview
Code
### Read Only
The `isReadOnly` boolean prop makes `TimeInput`'s value immutable. Unlike `isDisabled`, `TimeInput` remains focusable.
Preview
Code
### Without Label
`TimeInput` supports the `label` prop to show or not show the label.
Preview
Code
### With Description
A description for the field. Provides a hint such as specific requirements for what to choose.
Preview
Code
### With Error Message
You can combine the `isInvalid` and `errorMessage` properties to show an invalid input.
Preview
Code
You can also pass an error message as a function. This allows for dynamic error message handling based on the ValidationResult.
Preview
Code
### Label Placement
The label's overall position relative to the element it is labeling.
Preview
Code
### Start Content
If you want to display some content before the time inputs, you can set the `startContent` property.
Preview
Code
### End Content
If you want to display some content after the time inputs, you can set the `endContent` property.
Preview
Code
### Controlled
An initial, uncontrolled value can be provided to the `TimeInput` using the `defaultValue` prop. A controlled value can be provided using the `value` prop.
Preview
Code
### Time Zones
`TimeInput` is time zone aware when a `ZonedDateTime` object is provided as the value. In this case, the time zone abbreviation is displayed, and time zone concerns such as daylight saving time are taken into account when the value is manipulated.
In most cases, your data will come from and be sent to a server as an ISO 8601 formatted string. @internationalized/date includes functions for parsing strings in multiple formats into ZonedDateTime objects. Which format you use will depend on what information you need to store.
  * `parseZonedDateTime` – This function parses a date with an explicit time zone and optional UTC offset attached (e.g. `2021-11-07T00:45[America/Los_Angeles]` or `2021-11-07T00:45-07:00[America/Los_Angeles]`). This format preserves the maximum amount of information. If the exact local time and time zone that a user selected is important, use this format. Storing the time zone and offset that was selected rather than converting to UTC ensures that the local time is correct regardless of daylight saving rule changes (e.g. if a locale abolishes DST). Examples where this applies include calendar events, reminders, and other times that occur in a particular location.
  * `parseAbsolute` – This function parses an absolute date and time that occurs at the same instant at all locations on Earth. It can be represented in UTC (e.g. `2021-11-07T07:45:00Z`), or stored with a particular offset (e.g. `2021-11-07T07:45:00-07:00`). A time zone identifier, e.g. America/Los_Angeles, must be passed, and the result will be converted into that time zone. Absolute times are the best way to represent events that occurred in the past, or future events where an exact time is needed, regardless of time zone.
  * `parseAbsoluteToLocal` – This function parses an absolute date and time into the current user's local time zone. It is a shortcut for parseAbsolute, and accepts the same formats.


Preview
Code
### Granularity
The `granularity` prop allows you to control the smallest unit that is displayed by TimeInput. By default, times are displayed with "minute" granularity. More granular time values can be displayed by setting the granularity prop to "second".
Preview
Code
### Min Time Value
The `minValue` prop allows you to validate time value before a certain time.
Preview
Code
### Max Time Value
The `maxValue` prop allows you to validate time value before a certain time.
Preview
Code
### Placeholder Value
When no value is set, a placeholder is shown. The format of the placeholder is influenced by the `granularity` and `placeholderValue` props. placeholderValue also controls the default values of each segment when the user first interacts with them, e.g. using the up and down arrow keys. By default, the placeholderValue is midnight, but you can set it to a more appropriate value if needed.
Preview
Code
### Hide Time Zone
When a `ZonedDateTime` object is provided as the value to `TimeInput`, the time zone abbreviation is displayed by default. However, if this is displayed elsewhere or implicit based on the usecase, it can be hidden using the `hideTimeZone` option.
Preview
Code
### Hour Cycle
By default, `TimeInput` displays times in either 12 or 24 hour hour format depending on the user's locale. However, this can be overridden using the `hourCycle` prop if needed for a specific usecase. This example forces `TimeInput` to use 24-hour time, regardless of the locale.
Preview
Code
## Slots
  * **base** : Input wrapper, it handles alignment, placement, and general appearance.
  * **label** : Label of the time input, it is the one that is displayed above, inside or left of the time input.
  * **inputWrapper** : Wraps the `label` (when it is inside) and the `innerWrapper`.
  * **input** : The time input element.
  * **innerWrapper** : Wraps the segments, the `startContent` and the `endContent`.
  * **segment** : The segment of input elements.
  * **helperWrapper** : The wrapper of the helper text. This wraps the helper text and the error message.
  * **description** : The description of the time input.
  * **errorMessage** : The error message of the time input.


## Data Attributes
`TimeInput` has the following attributes on the `base` element:
  * **data-has-helper** : When the time input has description or error message. Based on `description` or `errorMessage` props.
  * **data-required** : When the time input is required. Based on `isRequired` prop.
  * **data-disabled** : When the time input is disabled. Based on `isDisabled` prop.
  * **data-readonly** : When the time input is readonly. Based on `isReadOnly` prop.
  * **data-invalid** : When the time input is invalid. Based on `isInvalid` prop.
  * **data-has-start-content** : When the time input has start content. Based on `startContent` prop.
  * **data-has-end-content** : When the time input has end content. Based on `endContent` prop.


## Accessibility
  * Support for locale-specific formatting, number systems, hour cycles, and right-to-left layout.
  * Times can optionally include a time zone. All modifications follow time zone rules such as daylight saving time.
  * Each time unit is displayed as an individually focusable and editable segment, which allows users an easy way to edit times using the keyboard, in any format and locale.
  * Time segments are editable using an easy to use numeric keypad, and all interactions are accessible using touch-based screen readers.


## API
### TimeInput Props
Prop| Type| Default  
---|---|---  
`label`| `ReactNode`  
`name`| `string`  
`value`| `TimeValue | null`  
`defaultValue`| `TimeValue | null`  
`variant`| `flat | bordered | faded | underlined`| `"flat"`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`size`| `sm | md | lg`| `"md"`  
`radius`| `none | sm | md | lg | full`  
`hourCycle`| `12 | 24`  
`granularity`| `hour | minute | second`| `"minute"`  
`hideTimeZone`| `boolean`  
`labelPlacement`| `inside | outside | outside-left`| `"inside"`  
`shouldForceLeadingZeros`| `boolean`| `true`  
`placeholderValue`| `TimeValue`  
`minValue`| `TimeValue`  
`maxValue`| `TimeValue`  
`isDisabled`| `boolean`  
`isReadOnly`| `boolean`  
`isRequired`| `boolean`  
`isInvalid`| `boolean`  
`autoFocus`| `boolean`  
`description`| `ReactNode`  
`errorMessage`| `ReactNode | (v: ValidationResult) => ReactNode`  
`validate`| `(value: MappedTimeValue<TimeValue>) => ValidationError | true | null | undefined`  
`validationBehavior`| `native | aria`| `"native"`  
`disableAnimation`| `boolean`  
`classNames`| `Partial<Record<"base" | "label" | "inputWrapper" | "innerWrapper" | "segment" | "helperWrapper" | "input" | "description" | "errorMessage", string>>`  
### TimeInput Events
Prop| Type| Default  
---|---|---  
`onFocus`| `(e: FocusEvent<Target>) => void`  
`onBlur`| `(e: FocusEvent<Target>) => void`  
`onFocusChange`| `(isFocused: boolean) => void`  
`onKeyDown`| `(e: KeyboardEvent) => void`  
`onKeyUp`| `(e: KeyboardEvent) => void`  
`onChange`| `(value: MappedTimeValue<TimeValue>) => void`  
TextareaTooltip
On this page
  * Installation
  * Import
  * Usage
  * Required
  * Disabled
  * Read Only
  * Without Label
  * With Description
  * With Error Message
  * Label Placement
  * Start Content
  * End Content
  * Controlled
  * Time Zones
  * Granularity
  * Min Time Value
  * Max Time Value
  * Placeholder Value
  * Hide Time Zone
  * Hour Cycle
  * Slots
  * Data Attributes
  * Accessibility
  * API
  * TimeInput Props
  * TimeInput Events
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
