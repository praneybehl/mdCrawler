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


# Listbox
A listbox displays a list of options and allows a user to select one or more of them.
Storybook@heroui/listboxReact AriaSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
HeroUI exports 3 listbox-related components:
  * **Listbox** : The main component, which is a wrapper for the other components.
  * **ListboxSection** : The component that contains a group of listbox items.
  * **ListboxItem** : The component that represents a listbox item.


Individual
Global
## Usage
Preview
Code
### Dynamic items
Listbox follows the Collection Components API, accepting both static and dynamic collections.
  * **Static** : The usage example above shows the static implementation, which can be used when the full list of options is known ahead of time.
  * **Dynamic** : The example below can be used when the options come from an external data source such as an API call, or update over time.


Preview
Code
### Disabled Keys
Listbox items can be disabled using the `disabledKeys` prop to the `Listbox` component.
Preview
Code
> **Note** : It's important to have a unique key for each item, otherwise the disabled keys will not work.
### Variants
You can use the `variant` in the `Listbox` component to change the `hover` style of the listbox items.
Preview
Code
### Single Selection
You can set the `selectionMode` property as `single` to allow the user to select only one item at a time.
Preview
Code
### Multiple Selection
You can set the `selectionMode` property as `multiple` to allow the user to select multiple items at a time.
Preview
Code
> **Note** : To allow empty selection, you can set the `disallowEmptySelection` property as `false`.
### With Icons
It is possible to add icons to the listbox items using the `startContent` / `endContent` props.
Preview
Code
> **Note** : If you use `currentColor` as the icon color, the icon will have the same color as the item text.
### With Description
You can use the `description` prop to add a description to the listbox item.
Preview
Code
### With Top & Bottom Content
You can use the `topContent` and `bottomContent` props to add content above and below the listbox items.
Preview
Code
### With Sections
You can use the `ListboxSection` component to group listbox items.
Preview
Code
> **Note** : Sections without a `title` must provide an `aria-label` for accessibility.
### Routing
The `<ListboxItem>` component works with frameworks and client side routers like Next.js and React Router. See the Routing guide to learn how to set this up.
### Virtualization
Listbox supports virtualization, which allows efficient rendering of large lists by only rendering items that are visible in the viewport. You can enable virtualization by setting the `isVirtualized` prop to `true`.
Preview
Code
> **Note** : The virtualization strategy is based on the @tanstack/react-virtual package, which provides efficient rendering of large lists by only rendering items that are visible in the viewport.
#### Ten Thousand Items
Here's an example of using virtualization with 10,000 items.
Preview
Code
## Slots
Listbox has 3 components with slots the base one `Listbox`, `ListboxItem` and `ListboxSection` components.
### Listbox
  * **base** : The main wrapper for the listbox component. This slot wraps the `topContent`, `bottomContent` and the `list` slot.
  * **list** : The slot for the listbox component. You can see this slot as the `ul` slot.
  * **emptyContent** : The slot content to display when the collection is empty.


### ListboxItem
  * **base** : The main slot for the listbox item. It wraps all the other slots.
  * **wrapper** : The `title` and `description` wrapper.
  * **title** : The title of the listbox item.
  * **description** : The description of the listbox item.
  * **selectedIcon** : The selected icon slot. This is only visible when the item is selected.


### ListboxSection
  * **base** : The main slot for the listbox section. It wraps all the other slots.
  * **heading** : The title that is render on top of the section group.
  * **group** : The group of listbox items.
  * **divider** : The divider that is render between the groups. This is only visible when `showDivider` is `true`.


### Customizing the listbox
You can customize the `Listbox` items style by using the `itemClasses` prop and passing custom Tailwind CSS classes.
Preview
Code
> **Note** : In the above example, we've utilized the Boxicons icons collection.
### Keyboard Interactions
Key| Description  
---|---  
`Home`| Moves focus to the first item.  
`End`| Moves focus to the last item.  
`ArrowDown`| When focus is on an item, moves focus to the next item.  
`ArrowUp`| When focus is on an item, moves focus to the previous item.  
`Enter` or `Space`| When focus is on an item, selects the item.  
`A-Z` or `a-z`| Moves focus to the next menu item with a label that starts with the typed character if such an menu item exists.  
## Data Attributes
`ListboxItem` has the following attributes on the `base` element:
  * **data-disabled** : When the listbox item is disabled. Based on listbox `disabledKeys` prop.
  * **data-selected** : When the listbox item is selected. Based on listbox `selectedKeys` prop.
  * **data-selectable** : When the listbox item is selectable. Based on listbox `selectionMode` prop.
  * **data-hover** : When the listbox item is being hovered. Based on useHover
  * **data-pressed** : When the listbox item is pressed. Based on usePress
  * **data-focus** : When the listbox item is being focused. Based on useFocusRing.
  * **data-focus-visible** : When the listbox item is being focused with the keyboard. Based on useFocusRing.


## Accessibility
  * Exposed to assistive technology as a `listbox` using ARIA.
  * Support for single, multiple, or no selection.
  * Support for disabled items.
  * Support for sections.
  * Labeling support for accessibility.
  * Support for mouse, touch, and keyboard interactions.
  * Tab stop focus management.
  * Keyboard navigation support including arrow keys, home/end, page up/down, select all, and clear.
  * Automatic scrolling support during keyboard navigation.
  * Typeahead to allow focusing options by typing text.


## API
### Listbox Props
Prop| Type| Default  
---|---|---  
`children*`| `ReactNode[]`  
`items`| `Iterable<T>`  
`variant`| `solid | bordered | light | flat | faded | shadow`| `"solid"`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`selectionMode`| `none | single | multiple`  
`selectedKeys`| `React.Key[]`  
`disabledKeys`| `React.Key[]`  
`defaultSelectedKeys`| `all | React.Key[]`  
`disallowEmptySelection`| `boolean`| `false`  
`shouldHighlightOnFocus`| `boolean`| `false`  
`autoFocus`| `boolean | first | last`| `false`  
`topContent`| `ReactNode`  
`bottomContent`| `ReactNode`  
`emptyContent`| `ReactNode`| `"No items."`  
`shouldFocusWrap`| `boolean`| `false`  
`isVirtualized`| `boolean`| `false`  
`virtualization`| `Record<"maxListboxHeight" & "itemHeight", number>`  
`hideEmptyContent`| `boolean`| `false`  
`hideSelectedIcon`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<"base" | "list" | "emptyContent", string>>`  
`itemClasses`| `Partial<Record<"base" | "wrapper" | "title" | "description" | "selectedIcon", string>>`  
### Listbox Events
Prop| Type| Default  
---|---|---  
`onAction`| `(key: React.Key) => void`  
`onSelectionChange`| `(keys: React.Key[]) => void`  
### ListboxSection Props
Prop| Type| Default  
---|---|---  
`children*`| `ReactNode`  
`title`| `string`  
`items`| `Iterable<T>`  
`hideSelectedIcon`| `boolean`| `false`  
`showDivider`| `boolean`| `false`  
`dividerProps`| `DividerProps`  
`classNames`| `Partial<Record<"base" | "heading" | "group" | "divider", string>>`  
`itemClasses`| `Partial<Record<"base" | "wrapper" | "title" | "description" | "shortcut" | "selectedIcon", string>>`  
### ListboxItem Props
Prop| Type| Default  
---|---|---  
`children*`| `ReactNode`  
`key`| `React.Key`  
`title`| `string | ReactNode`  
`textValue`| `string`  
`description`| `string | ReactNode`  
`shortcut`| `string | ReactNode`  
`startContent`| `ReactNode`  
`endContent`| `ReactNode`  
`selectedIcon`| `ListboxItemSelectedIconProps`  
`href`| `string`  
`target`| `HTMLAttributeAnchorTarget`  
`rel`| `string`  
`download`| `boolean | string`  
`ping`| `string`  
`referrerPolicy`| `HTMLAttributeReferrerPolicy`  
`shouldHighlightOnFocus`| `boolean`| `false`  
`hideSelectedIcon`| `boolean`| `false`  
`showDivider`| `boolean`| `false`  
`isDisabled`| `boolean`| `false`  
`isSelected`| `boolean`| `false`  
`isReadOnly`| `boolean`| `false`  
`classNames`| `Partial<Record<"base" | "wrapper" | "title" | "description" | "shortcut" | "selectedIcon", string>>`  
### ListboxItem Events
Prop| Type| Default  
---|---|---  
`onAction`| `() => void`  
`onPress`| `(e: PressEvent) => void`  
`onPressStart`| `(e: PressEvent) => void`  
`onPressEnd`| `(e: PressEvent) => void`  
`onPressChange`| `(isPressed: boolean) => void`  
`onPressUp`| `(e: PressEvent) => void`  
`onKeyDown`| `(e: KeyboardEvent) => void`  
`onKeyUp`| `(e: KeyboardEvent) => void`  
`onClick`| `MouseEventHandler`  
### Types
#### Listbox Item Selected Icon Props
LinkModal
On this page
  * Installation
  * Import
  * Usage
  * Dynamic items
  * Disabled Keys
  * Variants
  * Single Selection
  * Multiple Selection
  * With Icons
  * With Description
  * With Top & Bottom Content
  * With Sections
  * Routing
  * Virtualization
  * Ten Thousand Items
  * Slots
  * Listbox
  * ListboxItem
  * ListboxSection
  * Customizing the listbox
  * Keyboard Interactions
  * Data Attributes
  * Accessibility
  * API
  * Listbox Props
  * Listbox Events
  * ListboxSection Props
  * ListboxItem Props
  * ListboxItem Events
  * Types
  * Listbox Item Selected Icon Props
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
