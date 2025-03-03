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


# Select
A select displays a collapsible list of options and allows a user to select one or more of them.
Storybook@heroui/selectReact AriaSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
HeroUI exports 3 select-related components:
  * **Select** : The main component, which is a wrapper for the other components.
  * **SelectSection** : The component that contains a group of select items.
  * **SelectItem** : The component that represents a select item.


Individual
Global
## Usage
Preview
Code
### Dynamic items
Select follows the Collection Components API, accepting both static and dynamic collections.
  * **Static** : The usage example above shows the static implementation, which can be used when the full list of options is known ahead of time.
  * **Dynamic** : The example below can be used when the options come from an external data source such as an API call, or update over time.


Preview
Code
### Multiple Selection
You can use the `selectionMode="multiple"` property to allow multiple selection.
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
If you pass the `isRequired` property to the select, it will have a `danger` asterisk at the end of the label and the select will be required.
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
### Start Content
You can use the `startContent` and `endContent` properties to add content to the start and end of the select.
Preview
Code
### Item Start & End Content
Since the `Select` component uses the Listbox component under the hood, you can use the `startContent` and `endContent` properties of the `SelectItem` component to add content to the start and end of the select item.
Preview
Code
### Custom Selector Icon
By default the select uses a `chevron-down` icon as the selector icon which rotates when the select is open. You can customize this icon by passing a custom one to the `selectorIcon` property.
Preview
Code
> **Note** : Use the `disableSelectorIconRotation` property to disable the rotation of the icon.
### Without Scroll Shadow
Select component uses the ScrollShadow under the hood to show a shadow when the select content is scrollable. You can disable this shadow by passing using the `scrollShadowProps` property.
Preview
Code
> **Note** : You can also use the `showScrollIndicators` property to disable the scroll indicators.
### With Description
You can add a description to the select by passing the `description` property.
Preview
Code
### With Error Message
You can combine the `isInvalid` and `errorMessage` properties to show an invalid select.
Preview
Code
### Controlled
You can use the `selectedKeys` and `onSelectionChange` / `onChange` properties to control the select value.
Using `onSelectionChange`:
Preview
Code
Using `onChange`:
Preview
Code
### Controlling the open state
You can control the open state of the select by using the `isOpen` and `onOpenChange` / `onClose` properties.
Preview
Code
### Custom Items
You can customize the select items by modifying the `SelectItem` children.
Preview
Code
### Custom Render Value
By default the select will render the selected item's text value, but you can customize this by passing a `renderValue` function.
Preview
Code
The `renderValue` function receives the selected items as a parameter and must return a `ReactNode`. Check the Render Value Function section for more details.
### Asynchronous Loading
Select supports asynchronous loading, in the example below we are using a custom hook to fetch the Pokemon API data in combination with the `useInfiniteScroll` hook to load more data when the user reaches the end of the list.
The `isLoading` prop is used to show a loading indicator instead of the selector icon when the data is being fetched.
npm
yarn
pnpm
Preview
Code
### Virtualization
Select supports virtualization, which allows efficient rendering of large lists by only rendering items that are visible in the viewport. You can enable virtualization by setting the `isVirtualized` prop to `true`.
Preview
Code
> **Note** : The virtualization strategy is based on the @tanstack/react-virtual package, which provides efficient rendering of large lists by only rendering items that are visible in the viewport.
#### Ten Thousand Items
Here's an example of using virtualization with 10,000 items.
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
You can use the `SelectSection` component to group select items.
Preview
Code
### Custom Sections Style
You can customize the sections style by using the `classNames` property of the `SelectSection` component.
Preview
Code
### Multiple Select Controlled
You can use the same properties as the single select to control the multiple select, `selectedKeys` and `onSelectionChange` / `onChange`.
Using `onSelectionChange`:
Preview
Code
Using `onChange`:
Preview
Code
### Multiple With Chips
You can render any component as the select value by using the `renderValue` property. In this example we are using the Chip component to render the selected items.
Preview
Code
> **Note** : Make sure to pass the `isMultiline` property to the `Select` component to allow the chips to wrap.
The `renderValue` function receives the selected items as a parameter and must return a `ReactNode`. Check the Render Value Function section for more details.
### Customizing the select
You can customize any slot of the select by using the `classNames` property. Select component also provides the popoverProps and listboxProps properties to customize the popover and listbox components.
Preview
Code
### Using `value` attribute in option
The `value` attribute is not directly supported in `SelectItem`. Instead, the `key` property should be used to set the `value` to be submitted in forms.
If you need to submit a specific `value` instead of the `key` during form submission, consider implementing a lookup map in your application.
## Slots
  * **base** : The main wrapper of the select. This wraps the rest of the slots.
  * **label** : The label of the select.
  * **mainWrapper** : Wraps the `helperWrapper` and the `trigger` slots.
  * **trigger** : The trigger of the select. This wraps the label the inner wrapper and the selector icon.
  * **innerWrapper** : The wrapper of the select content. This wraps the start/end content and the select value.
  * **selectorIcon** : The selector icon of the select. This is the icon that rotates when the select is open (`data-open`).
  * **value** : The select value. This is also the slot that wraps the `renderValue` function result.
  * **listboxWrapper** : The wrapper of the listbox. This wraps the listbox component, this slot is used on top of the scroll shadow component.
  * **listbox** : The listbox component. This is the component that wraps the select items.
  * **popoverContent** : The popover content slot. Use this to modify the popover content styles.
  * **helperWrapper** : The wrapper of the helper text. This wraps the helper text and the error message.
  * **description** : The description of the select.
  * **errorMessage** : The error message of the select.


## Data Attributes
`Select` has the following attributes on the `base` element:
  * **data-filled** : Indicates if the select has a value, is focused, has start/end content or is open.
  * **data-has-value** : Indicates if the select has selected item(s).
  * **data-has-label** : Indicates if the select has a label. Based on `label` prop.
  * **data-has-helper** : Indicates if the select has helper text. Based on `errorMessage` or `description` prop.
  * **data-invalid** : Indicates if the select is invalid. Based on `isInvalid` prop.


`Select` has the following attributes on the `trigger` element:
  * **data-open** : Indicates if the select is open.
  * **data-disabled** : When the select trigger is disabled. Based on select `isDisabled` prop.
  * **data-focus** : When the select trigger is being focused. Based on useFocusRing.
  * **data-focus-visible** : When the select trigger is being focused with the keyboard. Based on useFocusRing.
  * **data-pressed** : When the select trigger is pressed. Based on usePress
  * **data-hover** : When the select trigger is being hovered. Based on useHover


`Select` has the following attributes on the `selectorIcon` element:
  * **data-open** : Indicates if the select is open.


`SelectItem` has the following attributes on the `base` element:
  * **data-disabled** : When the select item is disabled. Based on select `disabledKeys` prop.
  * **data-selected** : When the select item is selected. Based on select `selectedKeys` prop.
  * **data-hover** : When the select item is being hovered. Based on useHover
  * **data-pressed** : When the select item is pressed. Based on usePress
  * **data-focus** : When the select item is being focused. Based on useFocusRing.
  * **data-focus-visible** : When the select item is being focused with the keyboard. Based on useFocusRing.


## Accessibility
  * Exposed to assistive technology as a button with a listbox popup using ARIA (combined with Listbox).
  * Support for selecting a single option.
  * Support for selecting multiple options.
  * Support for disabled options.
  * Support for sections.
  * Labeling support for accessibility.
  * Support for description and error message help text linked to the input via ARIA.
  * Support for mouse, touch, and keyboard interactions.
  * Tab stop focus management.
  * Keyboard support for opening the listbox using the arrow keys, including automatically focusing the first or last item accordingly.
  * Typeahead to allow selecting options by typing text, even without opening the listbox.
  * Browser autofill integration via a hidden native `<select>` element.
  * Mobile screen reader listbox dismissal support.


## API
### Select Props
Prop| Type| Default  
---|---|---  
`children*`| `ReactNode[]`  
`items`| `Iterable<T>`  
`selectionMode`| `single | multiple`  
`selectedKeys`| `all | Iterable<React.Key>`  
`disabledKeys`| `Iterable<React.Key>`  
`defaultSelectedKeys`| `all | Iterable<React.Key>`  
`variant`| `flat | bordered | faded | underlined`| `"flat"`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`size`| `sm | md | lg`| `"md"`  
`radius`| `none | sm | md | lg | full`  
`placeholder`| `string`| `"Select an option"`  
`labelPlacement`| `inside | outside | outside-left`| `"inside"`  
`label`| `ReactNode`  
`description`| `ReactNode`  
`errorMessage`| `ReactNode | ((v: ValidationResult) => ReactNode)`  
`startContent`| `ReactNode`  
`endContent`| `ReactNode`  
`selectorIcon`| `ReactNode`  
`scrollRef`| `React.RefObject<HTMLElement>`  
`spinnerRef`| `React.RefObject<HTMLElement>`  
`maxListboxHeight`| `number`| `"256"`  
`itemHeight`| `number`| `"32"`  
`isVirtualized`| `boolean`| `"undefined"`  
`fullWidth`| `boolean`| `true`  
`isOpen`| `boolean`  
`defaultOpen`| `boolean`  
`isRequired`| `boolean`| `false`  
`isDisabled`| `boolean`| `false`  
`isMultiline`| `boolean`| `false`  
`isInvalid`| `boolean`| `false`  
`validationState`| `valid | invalid`  
`showScrollIndicators`| `boolean`| `true`  
`autoFocus`| `boolean`| `false`  
`disallowEmptySelection`| `boolean`| `false`  
`disableAnimation`| `boolean`| `true`  
`disableSelectorIconRotation`| `boolean`| `false`  
`hideEmptyContent`| `boolean`| `false`  
`popoverProps`| `PopoverProps`  
`listboxProps`| `ListboxProps`  
`scrollShadowProps`| `ScrollShadowProps`  
`classNames`| `Partial<Record<"base"｜ "label"｜ "trigger"｜ "mainWrapper" ｜ "innerWrapper"｜ "selectorIcon" ｜ "value" ｜ "listboxWrapper"｜ "listbox" ｜ "popoverContent" ｜ "helperWrapper" ｜ "description" ｜ "errorMessage", string>>`  
### Select Events
Prop| Type| Default  
---|---|---  
`onClose`| `() => void`  
`onOpenChange`| `(isOpen: boolean) => void`  
`onSelectionChange`| `(keys: "all" | Set<React.Key> & {anchorKey?: string; currentKey?: string}) => void`  
`onChange`| `React.ChangeEvent<HTMLSelectElement>`  
`renderValue`| `RenderValueFunction`  
### SelectItem Props
Check the ListboxItem props.
### SelectItem Events
Check the ListboxItem events.
### SelectSection Props
Check the ListboxSection props.
### Types
#### Render Value Function
The `T` type is the type of the data passed to the select `items`.
Scroll ShadowSkeleton
On this page
  * Installation
  * Import
  * Usage
  * Dynamic items
  * Multiple Selection
  * Disabled
  * Disabled Items
  * Required
  * Sizes
  * Colors
  * Variants
  * Radius
  * Label Placements
  * Start Content
  * Item Start & End Content
  * Custom Selector Icon
  * Without Scroll Shadow
  * With Description
  * With Error Message
  * Controlled
  * Controlling the open state
  * Custom Items
  * Custom Render Value
  * Asynchronous Loading
  * Virtualization
  * Ten Thousand Items
  * Max Listbox Height
  * Custom Item Height
  * With Sections
  * Custom Sections Style
  * Multiple Select Controlled
  * Multiple With Chips
  * Customizing the select
  * Using `value` attribute in option
  * Slots
  * Data Attributes
  * Accessibility
  * API
  * Select Props
  * Select Events
  * SelectItem Props
  * SelectItem Events
  * SelectSection Props
  * Types
  * Render Value Function
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
