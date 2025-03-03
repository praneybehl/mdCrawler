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


# Autocomplete
An autocomplete combines a text input with a listbox, allowing users to filter a list of options to items matching a query.
Storybook@heroui/autocompleteReact AriaSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
HeroUI exports 3 autocomplete-related components:
  * **Autocomplete** : The main component, which is a wrapper for the other components.
  * **AutocompleteSection** : The component that contains a group of autocomplete items.
  * **AutocompleteItem** : The component that represents a autocomplete item.


Individual
Global
## Usage
Preview
Code
### Dynamic items
Autocomplete follows the Collection Components API, accepting both static and dynamic collections.
  * **Static** : The usage example above shows the static implementation, which can be used when the full list of options is known ahead of time.
  * **Dynamic** : The example below can be used when the options come from an external data source such as an API call, or update over time.


Preview
Code
### Disabled
Preview
Code
### Disabled Items
You can disable specific items by using the `disabledKeys` property.
Preview
Code
### Required
If you pass the `isRequired` property to the autocomplete, it will have a `danger` asterisk at the end of the label and the autocomplete will be required.
Preview
Code
### Read Only
If you pass the `isReadOnly` property to the Autocomplete, the Listbox will open to display all available options, but users won't be able to select any of the listed options.
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
### Label Placements
You can change the position of the label by setting the `labelPlacement` property to `inside`, `outside` or `outside-left`.
Preview
Code
> **Note** : If the `label` is not passed, the `labelPlacement` property will be `outside` by default.
### Start Content
You can use the `startContent` and `endContent` properties to add content to the start and end of the autocomplete.
Preview
Code
### Item Start & End Content
Since the `Autocomplete` component uses the Listbox component under the hood, you can use the `startContent` and `endContent` properties of the `AutocompleteItem` component to add content to the start and end of the autocomplete item.
Preview
Code
### Custom Value
By default, `Autocomplete` doesn't allow users to specify a value that doesn't exist in the list of options and will revert the input value to the current selected value on blur. By specifying `allowsCustomValue`, this behavior is suppressed and the user is free to enter any value within the field.
Preview
Code
### Custom Selector Icon
By default, `Autocomplete` uses a `chevron-down` icon as the selector icon which rotates when the autocomplete is open. You can customize this icon by passing a custom one to the `selectorIcon` property.
Preview
Code
> **Note** : Use the `disableSelectorIconRotation` property to disable the rotation of the icon.
### Without Scroll Shadow
Autocomplete component uses the ScrollShadow under the hood to show a shadow when the autocomplete content is scrollable. You can disable this shadow by passing using the `scrollShadowProps` property.
Preview
Code
> **Note** : You can also use the `showScrollIndicators` property to disable the scroll indicators.
### With Description
You can add a description to the autocomplete by passing the `description` property.
Preview
Code
### With Error Message
You can combine the `isInvalid` and `errorMessage` properties to show an invalid autocomplete.
Preview
Code
### Events
The `Autocomplete` component supports selection via mouse, keyboard, and touch. You can handle all of these via the `onSelectionChange` prop. `Autocomplete` will pass the selected key to the onSelectionChange handler. Additionally, ComboBox accepts an `onInputChange` prop which is triggered whenever the value is edited by the user, whether through typing or option selection.
The example below uses `onSelectionChange` and `onInputChange` to update the selection and input value stored in React state.
Preview
Code
### Controlled
You can use the `selectedKey` and `onSelectionChange` properties to control the select value.
Preview
Code
### Fully Controlled
By passing in `inputValue`, `selectedKey`, and `items` to the `Autocomplete` you can control exactly what your `Autocomplete` should display.
The following example shows how you would create a controlled `Autocomplete`, controlling everything from the selected value `selectedKey` to the combobox options `items`.
We recommend using the `useFilter` hook from @react-aria/i18n to manage the filtering of the items.
npm
yarn
pnpm
> **Note** : It is important to note that you don't have to control every single aspect of a `Autocomplete`. If you decide to only control a single property of the `Autocomplete`, be sure to provide the change handler for that prop as well e.g. controlling `selectedKey` would require `onSelectionChange`.
### Custom Items
You can customize the autocomplete items by modifying the `AutocompleteItem` children.
Preview
Code
### Custom Empty Content Message
By default, a message `No results found.` will be shown if there is no result matching a query with your filter. You can customize the empty content message by modifying the `emptyContent` in `listboxProps`.
Preview
Code
### Custom Filtering
By default, `Autocomplete` uses a `"contains"` function from useFilter to filter the list of options. This can be overridden using the `defaultFilter` prop, or by using the `items` prop to control the filtered list. When `items` is provided rather than `defaultItems`, `Autocomplete` does no filtering of its own.
The following example uses the `defaultFilter` prop to filter the list of options using a custom filter function.
Preview
Code
### Asynchronous Filtering
Autocomplete supports asynchronous filtering, in the example below we are using the useAsyncList function from react-aria to handle asynchronous loading and filtering of data from a server.
npm
yarn
pnpm
### Asynchronous Loading
Autocomplete supports asynchronous loading, in the example below we are using a custom hook to fetch the Pokemon API data in combination with the `useInfiniteScroll` hook to load more data when the user reaches the end of the list.
The `isLoading` prop is used to show a loading indicator instead of the selector icon when the data is being fetched.
npm
yarn
pnpm
### Virtualization
Autocomplete supports virtualization, in the example below we are using the `isVirtualized` prop to enable virtualization.
Preview
Code
> **Note** : The virtualization strategy is based on the @tanstack/react-virtual package, which provides efficient rendering of large lists by only rendering items that are visible in the viewport.
#### Ten Thousand Items
Virtualization with 10,000 items.
Preview
Code
#### Max Listbox Height
The `maxListboxHeight` prop is used to set the maximum height of the listbox. This is required when using virtualization. By default, it's set to `256`.
Preview
Code
#### Custom Item Height
The `itemHeight` prop is used to set the height of each item in the listbox. This is required when using virtualization. By default, it's set to `32`.
> **Note** : If the height of the list items differs from the default due to `startContent` or other custom content, be sure to pass the correct value to `itemHeight` to prevent layout issues.
Preview
Code
### With Sections
You can use the `AutocompleteSection` component to group autocomplete items.
Preview
Code
### Custom Sections Style
You can customize the sections style by using the `classNames` property of the `AutocompleteSection` component.
Preview
Code
### Customizing the Autocomplete
You can customize any slot of the autocomplete by using the `classNames` property. Autocomplete component also provides the popoverProps, listboxProps, inputProps properties to customize the popover, listbox and input components.
Preview
Code
## Slots
  * **base** : The main wrapper of the autocomplete. This wraps the input and popover components.
  * **listboxWrapper** : The wrapper of the listbox. This wraps the listbox component, this slot is used on top of the scroll shadow component.
  * **listbox** : The listbox component. This is the component that wraps the autocomplete items.
  * **popoverContent** : The popover content slot. Use this to modify the popover content styles.
  * **endContentWrapper** : The wrapper of the end content. This wraps the clear button and selector button.
  * **clearButton** : The clear button slot.
  * **selectorButton** : The selector button slot.


## Data Attributes
`Autocomplete` has the following attributes on the `base` element:
  * **data-invalid** : When the autocomplete is invalid. Based on `isInvalid` prop.
  * **data-open** : Indicates if the autocomplete's popover is open.


`Autocomplete` has the following attributes on the `selectorButton` element:
  * **data-open** : Indicates if the autocomplete's popover is open.


`Autocomplete` has the following attributes on the `clearButton` element:
  * **data-visible** : Indicates if the autocomplete's clear button is visible. By default it is visible when hovering the autocomplete and when the autocomplete has a value (desktop), or when the autocomplete has a value (mobile).


`AutocompleteItem` has the following attributes on the `base` element:
  * **data-disabled** : When the autocomplete item is disabled. Based on autocomplete `disabledKeys` prop.
  * **data-selected** : When the autocomplete item is selected. Based on autocomplete `selectedKey` prop.
  * **data-hover** : When the autocomplete item is being hovered. Based on useHover
  * **data-pressed** : When the autocomplete item is pressed. Based on usePress
  * **data-focus** : When the autocomplete item is being focused. Based on useFocusRing.
  * **data-focus-visible** : When the autocomplete item is being focused with the keyboard. Based on useFocusRing.


## Accessibility
  * Support for filtering a list of options by typing
  * Support for selecting a single option
  * Support for disabled options
  * Support for groups of items in sections
  * Support for custom user input values
  * Support for controlled and uncontrolled options, selection, input value, and open state
  * Support for custom filter functions
  * Async loading and infinite scrolling support
  * Support for virtualized scrolling for performance with long lists
  * Exposed to assistive technology as a combobox with ARIA
  * Labeling support for accessibility
  * Required and invalid states exposed to assistive technology via ARIA
  * Support for mouse, touch, and keyboard interactions
  * Keyboard support for opening the combo box list box using the arrow keys, including automatically focusing the first or last item accordingly
  * Support for opening the list box when typing, on focus, or manually
  * Handles virtual clicks on the input from touch screen readers to toggle the list box
  * Virtual focus management for combo box list box option navigation
  * Hides elements outside the input and list box from assistive technology while the list box is open in a portal
  * Custom localized announcements for option focusing, filtering, and selection using an ARIA live region to work around VoiceOver bugs
  * Support for description and error message help text linked to the input via ARIA


## API
### Autocomplete Props
Prop| Type| Default  
---|---|---  
`children*`| `ReactNode[]`  
`label`| `ReactNode`  
`name`| `string`  
`variant`| `flat | bordered | faded | underlined`| `"flat"`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`size`| `sm | md | lg`| `"md"`  
`radius`| `none | sm | md | lg | full`  
`items`| `Iterable<T>`  
`defaultItems`| `Iterable<T>`  
`inputValue`| `string`  
`defaultInputValue`| `string`  
`allowsCustomValue`| `boolean`| `false`  
`allowsEmptyCollection`| `boolean`| `true`  
`shouldCloseOnBlur`| `boolean`| `true`  
`placeholder`| `string`  
`description`| `ReactNode`  
`menuTrigger`| `focus | input | manual`| `"focus"`  
`labelPlacement`| `inside | outside | outside-left`| `"inside"`  
`selectedKey`| `React.Key`  
`defaultSelectedKey`| `React.Key`  
`disabledKeys`| `all | React.Key[]`  
`errorMessage`| `ReactNode | ((v: ValidationResult) => ReactNode)`  
`validate`| `(value: { inputValue: string, selectedKey: React.Key }) => ValidationError | true | null | undefined`  
`validationBehavior`| `native | aria`| `"native"`  
`startContent`| `ReactNode`  
`endContent`| `ReactNode`  
`autoFocus`| `boolean`| `false`  
`defaultFilter`| `(textValue: string, inputValue: string) => boolean`  
`filterOptions`| `Intl.CollatorOptions`| `"{ sensitivity: 'base'}"`  
`maxListboxHeight`| `number`| `"256"`  
`itemHeight`| `number`| `"32"`  
`isVirtualized`| `boolean`| `"undefined"`  
`isReadOnly`| `boolean`| `false`  
`isRequired`| `boolean`| `false`  
`isInvalid`| `boolean`| `false`  
`isDisabled`| `boolean`| `false`  
`fullWidth`| `boolean`| `true`  
`selectorIcon`| `ReactNode`  
`clearIcon`| `ReactNode`  
`showScrollIndicators`| `boolean`| `true`  
`scrollRef`| `React.RefObject<HTMLElement>`  
`inputProps`| `InputProps`  
`popoverProps`| `PopoverProps`  
`listboxProps`| `ListboxProps`  
`scrollShadowProps`| `ScrollShadowProps`  
`selectorButtonProps`| `ButtonProps`  
`clearButtonProps`| `ButtonProps`  
`isClearable`| `boolean`| `true`  
`disableClearable`| `boolean`| `false`  
`disableAnimation`| `boolean`| `true`  
`disableSelectorIconRotation`| `boolean`| `false`  
`classNames`| `Partial<Record<'base' | 'listboxWrapper' | 'listbox' | 'popoverContent' | 'endContentWrapper' | 'clearButton' | 'selectorButton', string>>`  
### Autocomplete Events
Prop| Type| Default  
---|---|---  
`onOpenChange`| `(isOpen: boolean, menuTrigger?: MenuTriggerAction) => void`  
`onInputChange`| `(value: string) => void`  
`onSelectionChange`| `(key: React.Key) => void`  
`onFocus`| `(e: FocusEvent<HTMLInputElement>) => void`  
`onBlur`| `(e: FocusEvent<HTMLInputElement>) => void`  
`onFocusChange`| `(isFocused: boolean) => void`  
`onKeyDown`| `(e: KeyboardEvent) => void`  
`onKeyUp`| `(e: KeyboardEvent) => void`  
`onClose`| `() => void`  
### AutocompleteItem Props
Check the ListboxItem props.
### AutocompleteItem Events
Check the ListboxItem events.
### AutocompleteSection Props
Check the ListboxSection props.
### Types
#### Menu Trigger Action
AccordionAlert
On this page
  * Installation
  * Import
  * Usage
  * Dynamic items
  * Disabled
  * Disabled Items
  * Required
  * Read Only
  * Sizes
  * Colors
  * Variants
  * Label Placements
  * Start Content
  * Item Start & End Content
  * Custom Value
  * Custom Selector Icon
  * Without Scroll Shadow
  * With Description
  * With Error Message
  * Events
  * Controlled
  * Fully Controlled
  * Custom Items
  * Custom Empty Content Message
  * Custom Filtering
  * Asynchronous Filtering
  * Asynchronous Loading
  * Virtualization
  * Ten Thousand Items
  * Max Listbox Height
  * Custom Item Height
  * With Sections
  * Custom Sections Style
  * Customizing the Autocomplete
  * Slots
  * Data Attributes
  * Accessibility
  * API
  * Autocomplete Props
  * Autocomplete Events
  * AutocompleteItem Props
  * AutocompleteItem Events
  * AutocompleteSection Props
  * Types
  * Menu Trigger Action
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
