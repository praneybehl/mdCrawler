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


# Range Calendar
A range calendar consists of a grouping element containing one or more date grids (e.g. months), and a previous and next button for navigating through time. Each calendar grid consists of cells containing button elements that can be pressed and navigated to using the arrow keys to select a date range. Once a start date is selected, the user can navigate to another date using the keyboard or by hovering over it, and clicking it or pressing the Enter key commits the selected date range.
Storybook@heroui/calendarReact AriaSourceStyles source
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
A RangeCalendar has no selection by default. An initial, uncontrolled value can be provided to the RangeCalendar using the `defaultValue` prop. Alternatively, a controlled value can be provided using the `value` prop.
Date values are provided using objects in the @internationalized/date package. This library handles correct international date manipulation across calendars, time zones, and other localization concerns.
Preview
Code
### Disabled
The `isDisabled` boolean prop makes the Calendar disabled. Cells cannot be focused or selected.
Preview
Code
### Read Only
The `isReadOnly` boolean prop makes the Calendar's value immutable. Unlike `isDisabled`, the Calendar remains focusable.
Preview
Code
### Controlled
A Calendar has no selection by default. An initial, uncontrolled value can be provided to the Calendar using the `defaultValue` prop. Alternatively, a controlled value can be provided using the value prop.
Preview
Code
### Min Date Value
By default, Calendar allows selecting any date. The `minValue` can also be used to prevent the user from selecting dates outside a certain range.
This example only accepts dates after today.
Preview
Code
### Max Date Value
By default, Calendar allows selecting any date. The `maxValue` can also be used to prevent the user from selecting dates outside a certain range.
This example only accepts dates before today.
Preview
Code
### Unavailable Dates
Calendar supports marking certain dates as unavailable. These dates remain focusable with the keyboard so that navigation is consistent, but cannot be selected by the user. In this example, they are displayed in red. The `isDateUnavailable` prop accepts a callback that is called to evaluate whether each visible date is unavailable.
Preview
Code
### Non-Contiguous Ranges
The `allowsNonContiguousRanges` prop enables a range to be selected even if there are unavailable dates in the middle. The value emitted in the onChange event will still be a single range with a start and end property, but unavailable dates will not be displayed as selected. It is up to applications to split the full selected range into multiple as needed for business logic.
This example prevents selecting weekends, but allows selecting ranges that span multiple weeks.
Preview
Code
### Controlled Focused Value
Calendar tries to avoid allowing the user to select invalid dates in the first place. However, if according to application logic a selected date is invalid, the isInvalid prop can be set. This alerts assistive technology users that the selection is invalid, and can be used for styling purposes as well. In addition, the errorMessage slot may be used to help the user fix the issue.
By default, the selected date is focused when a Calendar first mounts. If no `value` or `defaultValue` prop is provided, then the current date is focused. However, Calendar supports controlling which date is focused using the `focusedValue` and `onFocusChange` props. This also determines which month is visible. The `defaultFocusedValue` prop allows setting the initial focused date when the Calendar first mounts, without controlling it.
Preview
Code
### Invalid Date
This example validates that the selected date is a weekday and not a weekend according to the current locale.
Preview
Code
### With Month And Year Picker
Calendar supports month and year picker for rapid selection. You can enable this feature by setting `showMonthAndYearPickers` to `true`. However, if `visibleMonths` is set to a number greater than 1, this feature will be disabled.
Preview
Code
### International Calendars
Calendar supports selecting dates in many calendar systems used around the world, including Gregorian, Hebrew, Indian, Islamic, Buddhist, and more. Dates are automatically displayed in the appropriate calendar system for the user's locale. The calendar system can be overridden using the Unicode calendar locale extension, passed to the `Provider` component.
Preview
Code
### Visible Months
By default, the Calendar displays a single month. The `visibleMonths` prop allows displaying up to 3 months at a time.
Preview
Code
### Custom first day of week
By default, the first day of the week is automatically set based on the current locale. This can be changed by setting the `firstDayOfWeek` prop to `'sun'`, `'mon'`, `'tue'`, `'wed'`, `'thu'`, `'fri'`, or `'sat'`.
Preview
Code
### Page Behaviour
By default, when pressing the next or previous buttons, pagination will advance by the `visibleMonths` value. This behavior can be changed to page by single months instead, by setting `pageBehavior` to `single`.
Preview
Code
### Presets
Here's the example to customize `topContent` and `bottomContent` to have some preset values.
Preview
Code
## Slots
  * **base** : Calendar wrapper, it handles alignment, placement, and general appearance.
  * **prevButton** : The previous button of the calendar.
  * **nextButton** : The next button of the calendar.
  * **headerWrapper** : Wraps the picker (month / year).
  * **header** : The header element.
  * **title** : A description of the visible date range, for use in the calendar title.
  * **gridWrapper** : The wrapper for the calendar grid.
  * **grid** : The date grid element (e.g. `<table>`).
  * **gridHeader** : The date grid header element (e.g. `<th>`).
  * **gridHeaderRow** : The date grid header row element (e.g. `<tr>`).
  * **gridHeaderCell** : The date grid header cell element (e.g. `<td>`).
  * **gridBody** : The date grid body element (e.g. `<tbody>`).
  * **gridBodyRow** : The date grid body row element (e.g. `<tr>`).
  * **cell** : The date grid cell element (e.g. `<td>`).
  * **cellButton** : The button element within the cell.
  * **pickerWrapper** : The wrapper for the picker
  * **pickerMonthList** : The month list picker.
  * **pickerYearList** : The year list picker.
  * **pickerHighlight** : The highlighted item of the picker.
  * **pickerItem** : The item of the picker.
  * **helperWrapper** : The helper message of the calendar.
  * **errorMessage** : The error message of the calendar.


## Data Attributes
`Calendar` has the following attributes on the `CalendarCell` element:
  * **data-focused** : Whether the cell is focused.
  * **data-hovered** : Whether the cell is currently hovered with a mouse.
  * **data-pressed** : Whether the cell is currently being pressed.
  * **data-unavailable** : Whether the cell is unavailable, according to the calendar's `isDateUnavailable` prop. Unavailable dates remain focusable, but cannot be selected by the user. They should be displayed with a visual affordance to indicate they are unavailable, such as a different color or a strikethrough.
  * **data-disabled** : Whether the cell is disabled, according to the calendar's `minValue`, `maxValue`, and `isDisabled` props.
  * **data-focus-visible** : Whether the cell is keyboard focused.
  * **data-outside-visible-range** : Whether the cell is outside the visible range of the calendar.
  * **data-outside-month** : Whether the cell is outside the current month.
  * **data-selected** : Whether the cell is selected.
  * **data-selected-start** : Whether the cell is the first date in a range selection.
  * **data-selected-end** : Whether the cell is the last date in a range selection.
  * **data-invalid** : Whether the cell is part of an invalid selection.


## Accessibility
  * Display one or more months at once, or a custom time range for use cases like a week view. Minimum and maximum values, unavailable dates, and non-contiguous selections are supported as well.
  * Support for 13 calendar systems used around the world, including Gregorian, Buddhist, Islamic, Persian, and more. Locale-specific formatting, number systems, and right-to-left support are available as well.
  * Calendar cells can be navigated and selected using the keyboard, and localized screen reader messages are included to announce when the selection and visible date range change.


## API
### RangeCalendar Props
Prop| Type| Default  
---|---|---  
`value`| `RangeValue`| `"null"`  
`defaultValue`| `RangeValue`| `"null"`  
`minValue`| `DateValue`  
`maxValue`| `DateValue`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`visibleMonths`| `number`| `"1"`  
`firstDayOfWeek`| `sun | mon | tue | wed | thu | fri | sat`  
`focusedValue`| `DateValue`  
`defaultFocusedValue`| `DateValue`  
`calendarWidth`| `number | string`| `"256"`  
`pageBehavior`| `PageBehavior`| `"visible"`  
`weekdayStyle`| `narrow | short | long`| `"narrow"`  
`showMonthAndYearPickers`| `boolean`| `false`  
`allowsNonContiguousRanges`| `boolean`| `false`  
`isDisabled`| `boolean`| `false`  
`isReadOnly`| `boolean`| `false`  
`isInvalid`| `boolean`  
`autoFocus`| `boolean`| `false`  
`showHelper`| `boolean`| `false`  
`showShadow`| `boolean`| `false`  
`topContent`| `ReactNode`  
`bottomContent`| `ReactNode`  
`isDateUnavailable`| `(date: DateValue) => boolean`  
`createCalendar`| `(calendar: SupportedCalendars) => Calendar | null`| `"all calendars"`  
`errorMessage`| `ReactNode | (v: ValidationResult) => ReactNode`  
`validate`| `(value: { inputValue: string, selectedKey: React.Key }) => ValidationError | true | null | undefined`  
`hideDisabledDates`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
### RangeCalendar Events
Prop| Type| Default  
---|---|---  
`onFocusChange`| `(date: CalendarDate) => void`  
`onChange`| `(value: RangeValue<DateValue> | null) => void`  
#### Supported Calendars
Radio GroupScroll Shadow
On this page
  * Installation
  * Import
  * Usage
  * Disabled
  * Read Only
  * Controlled
  * Min Date Value
  * Max Date Value
  * Unavailable Dates
  * Non-Contiguous Ranges
  * Controlled Focused Value
  * Invalid Date
  * With Month And Year Picker
  * International Calendars
  * Visible Months
  * Custom first day of week
  * Page Behaviour
  * Presets
  * Slots
  * Data Attributes
  * Accessibility
  * API
  * RangeCalendar Props
  * RangeCalendar Events
  * Supported Calendars
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
