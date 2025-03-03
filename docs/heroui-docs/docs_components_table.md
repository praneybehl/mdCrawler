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


# Table
Tables are used to display tabular data using rows and columns. They allow users to quickly scan, sort, compare, and take action on large amounts of data.
Storybook@heroui/tableSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
HeroUI exports 6 table-related components:
  * **Table** : The main component to display a table.
  * **TableHeader** : The header of the table.
  * **TableBody** : The body of the table.
  * **TableColumn** : The column of the table.
  * **TableRow** : The row of the table.
  * **TableCell** : The cell of the table.


Individual
Global
## Usage
Preview
Code
### Dynamic
To render a table dynamically, you can use the `columns` prop to pass the columns and `items` prop to pass the data.
Preview
Code
#### Why not array map?
Using the `items` prop and providing a render function allows react-aria to automatically cache the results of rendering each item and avoid re-rendering all items in the collection when only one of them changes. This has big performance benefits for large collections.
You could also use `Array.map` to render the items, but it will not be as performant as using the `items` and `columns` prop.
Example:
> **Note** : To learn more about React Aria collections and how to use them, please check React Aria Collections.
### Empty State
You can use the `emptyContent` prop to render a custom component when the table is empty.
Preview
Code
### Without Header
In case you don't want to render the header, you can use the `hideHeader` prop.
Preview
Code
### Without Wrapper
By default the table is wrapped in a `div` element with a small shadow effect and a border radius. You can use the `removeWrapper` prop to remove the wrapper and only render the table.
Preview
Code
### Custom Cells
You can render any component inside the table cell. In the example below, we are rendering different components according to the `key` of the column.
Preview
Code
### Striped Rows
You can use the `isStriped` prop to render striped rows.
Preview
Code
### Single Row Selection
It is possible to make the table rows selectable. To do so, you can use the `selectionMode` prop. Use `defaultSelectedKeys` to provide a default set of selected rows.
Preview
Code
> **Note** : The value of the selected keys must match the key prop of the row.
### Multiple Row Selection
You can also select multiple rows by using the `selectionMode="multiple"` prop. Use `defaultSelectedKeys` to provide a default set of selected rows.
Preview
Code
> **Note** : When using multiple selection, selectable checkboxes will be rendered in the first column of the table.
### Disallow Empty Selection
Table also supports a `disallowEmptySelection` prop which forces the user to have at least one row in the Table selected at all times. In this mode, if a single row is selected and the user presses it, it will not be deselected.
Preview
Code
### Controlled Selection
To programmatically control row selection, use the `selectedKeys` prop paired with the `onSelectionChange` callback. The key prop from the selected rows will be passed into the callback when the row is pressed, allowing you to update state accordingly.
Preview
Code
> **Note** : The `selectedKeys` property must be a `Set` object.
### Disabled Rows
You can disable rows by using the `disabledKeys` prop. This will prevent rows from being selectable as shown in the example below.
Preview
Code
### Selection Behavior
By default, Table uses the `toggle` selection behavior, which behaves like a checkbox group: clicking, tapping, or pressing the `Space` or `Enter` keys toggles selection for the focused row.
When the `selectionBehavior` prop is set to `replace`, clicking a row with the mouse replaces the selection with only that row. Using the arrow keys moves both focus and selection. To select multiple rows, modifier keys such as `Ctrl`, `Cmd`, and `Shift` can be used.
Preview
Code
### Rows Actions
Table supports rows via the `onRowAction` callback. In the default `toggle` selection behavior, when nothing is selected, clicking or tapping the row triggers the row action.
This behavior is slightly different in the `replace` selection behavior, where single clicking selects the row and actions are performed via double click.
Preview
Code
### Sorting Rows
Table supports sorting its data when a column header is pressed. To designate that a `Column` should support sorting, provide it with the `allowsSorting` prop.
Table accepts a `sortDescriptor` prop that defines the current column key to sort by and the sort direction (ascending/descending). When the user presses a sortable column header, the column's key and sort direction is passed into the `onSortChange` callback, allowing you to update the `sortDescriptor` appropriately.
We recommend using the `useAsyncList` hook from @react-stately/data to manage the data sorting. So make sure to install it before using the sorting feature.
npm
yarn
pnpm
bun
Preview
Code
> Note that we passed the `isLoading` and `loadingContent` props to `TableBody` to render a loading state while the data is being fetched.
### Loading more data
Table allows you to add a custom component at the end of the table, on the example below we are using a button to load more data.
Preview
Code
> **Note** : We passed the `isHeaderSticky` to the `Table` component to make the header sticky.
### Paginated Table
You can use the Pagination component to paginate the table.
Preview
Code
### Async Pagination
It is also possible to use the Pagination component to paginate the table asynchronously. To fetch the data, we are using the `useSWR` hook from SWR.
Preview
Code
### Infinite Pagination
Table also supports infinite pagination. To do so, you can use the `useAsyncList` hook from @react-stately/data and @heroui/use-infinite-scroll hook.
npm
yarn
pnpm
bun
Preview
Code
### Virtualization
Table supports virtualization, which allows efficient rendering of large lists by only rendering items that are visible in the viewport. You can enable virtualization by setting the `isVirtualized` prop to `true`.
Preview
Code
> **Note** : The virtualization strategy is based on the @tanstack/react-virtual package, which provides efficient rendering of large lists by only rendering items that are visible in the viewport.
#### Ten Thousand Items
Here's an example of using virtualization with 10,000 items.
Preview
Code
#### Max Table Height
The `maxTableHeight` prop is used to set the maximum height of the table. This is required when using virtualization. By default, it's set to `600`.
Preview
Code
#### Custom Row Height
The `rowHeight` prop is used to set the height of each row in the table. This is required when using virtualization. By default, it's set to `40`.
Preview
Code
### Use Case Example
When creating a table, you usually need core functionalities like sorting, pagination, and filtering. In the example below, we combined all these functionalities to create a complete table.
Preview
Code
## Slots
  * **base** : Defines a flexible column layout and relative positioning for the table component.
  * **wrapper** : Applies to the outermost wrapper, providing padding, flexible layout, relative positioning, visual styles, and scrollable overflow handling.
  * **table** : Sets the table to have a full minimum width and auto-adjusting height.
  * **thead** : Specifies rounded corners for the first child row in the table header.
  * **tbody** : No specific styles are applied to the body of the table.
  * **tr** : Styles for table rows including group focus, outline properties, and a set of undefined focus-visible classes.
  * **th** : Styles for table headers, including padding, text alignment, font properties, and special styles for sortable columns.
  * **td** : Applies to table cells, with properties for padding, alignment, and relative positioning, plus special styles for first child elements, selection indication, and disabled cells.
  * **tfoot** : No specific styles are applied to the footer of the table.
  * **sortIcon** : Styles for sorting icons, with properties for margin, opacity, and transition effects based on sorting direction and hover state.
  * **emptyWrapper** : Defines style for an empty table, with text alignment, color, and a specified height.
  * **loadingWrapper** : Style applied when the table is loading, positioning it centrally in its container.


### Custom Styles
You can customize the `Table` component by passing custom Tailwind CSS classes to the component slots.
Preview
Code
## Data Attributes
`TableBody` has the following attributes:
  * **data-empty** : When the table is empty.
  * **data-loading** : When the table data is loading. Based on `TableBody` `isLoading` and `loadingContent` props.


`TableRow` has the following attributes:
  * **data-selected** : When the row is selected. Based on `Table` `selectedKeys` prop.
  * **data-disabled** : When the row is disabled. Based on `Table` `disabledKeys` prop.
  * **data-hover** : When the row is being hovered. Based on useHover
  * **data-focus-visible** : When the row is being focused with the keyboard. Based on useFocusRing.
  * **data-first** : When the row is the first row.
  * **data-middle** : When the row is in the middle.
  * **data-odd** : When the row is odd.
  * **data-last** : When the row is the last row.


`TableCell` has the following attributes:
  * **data-selected** : When the cell row is selected. Based on `Table` `selectedKeys` prop.
  * **data-focus-visible** : When the cell is being focused with the keyboard. Based on useFocusRing.


## Accessibility
  * Exposed to assistive technology as a grid using ARIA.
  * Keyboard navigation between columns, rows, cells, and in-cell focusable elements via the arrow keys.
  * Single, multiple, or no row selection via mouse, touch, or keyboard interactions.
  * Support for disabled rows, which cannot be selected.
  * Column sorting support.
  * Async loading, infinite scrolling, filtering, and sorting support.
  * Support for both toggle and replace selection behaviors.
  * Labeling support for accessibility.
  * Ensures that selections are announced using an ARIA live region.
  * Support for marking columns as row headers, which will be read when navigating the rows with a screen reader.
  * Optional support for checkboxes in each row for selection, as well as in the header to select all rows.
  * Automatic scrolling support during keyboard navigation.
  * Support for row actions via double click, Enter key, or tapping.
  * Typeahead to allow focusing rows by typing text.
  * Long press to enter selection mode on touch when there is both selection and row actions.


## API
### Table Props
Prop| Type| Default  
---|---|---  
`children*`| `ReactNode[]`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`layout`| `auto | fixed`| `"auto"`  
`radius`| `none | sm | md | lg`| `"lg"`  
`shadow`| `none | sm | md | lg`| `"sm"`  
`maxTableHeight`| `number`| `"600"`  
`rowHeight`| `number`| `"40"`  
`isVirtualized`| `boolean`| `"undefined"`  
`hideHeader`| `boolean`| `false`  
`isStriped`| `boolean`| `false`  
`isCompact`| `boolean`| `false`  
`isHeaderSticky`| `boolean`| `false`  
`fullWidth`| `boolean`| `true`  
`removeWrapper`| `boolean`| `false`  
`BaseComponent`| `React.ComponentType<any>`| `"div"`  
`topContent`| `ReactNode`  
`bottomContent`| `ReactNode`  
`topContentPlacement`| `inside | outside`| `"inside"`  
`bottomContentPlacement`| `inside | outside`| `"inside"`  
`showSelectionCheckboxes`| `boolean`  
`sortDescriptor`| `SortDescriptor`  
`selectedKeys`| `Selection`  
`defaultSelectedKeys`| `Selection`  
`disabledKeys`| `Selection`  
`disallowEmptySelection`| `boolean`  
`selectionMode`| `single | multiple | none`| `"none"`  
`selectionBehavior`| `toggle | replace`| `"toggle"`  
`disabledBehavior`| `selection | all`| `"selection"`  
`allowDuplicateSelectionEvents`| `boolean`  
`disableAnimation`| `boolean`| `false`  
`checkboxesProps`| `CheckboxProps`  
`classNames`| `Partial<Record<'base' | 'table' | 'thead' | 'tbody' | 'tfoot' | 'emptyWrapper' | 'loadingWrapper' | 'wrapper' | 'tr' | 'th' | 'td' | 'sortIcon', string>>`  
`isKeyboardNavigationDisabled`| `boolean`| `false`  
### Table Events
Prop| Type| Default  
---|---|---  
`onRowAction`| `(key: React.Key) => void`  
`onCellAction`| `(key: React.Key) => void`  
`onSelectionChange`| `(keys: Selection) => any`  
`onSortChange`| `(descriptor: SortDescriptor) => any`  
### TableHeader Props
Prop| Type| Default  
---|---|---  
`children*`| `ReactNode[]`  
`columns`| `T[]`  
### TableColumn Props
Prop| Type| Default  
---|---|---  
`children*`| `ReactNode`  
`align`| `start | center | end`| `"start"`  
`hideHeader`| `boolean`| `false`  
`allowsSorting`| `boolean`  
`isRowHeader`| `boolean`  
`textValue`| `string`  
`width`| `string | number`  
`minWidth`| `string | number`  
`maxWidth`| `string | number`  
### TableBody Props
Prop| Type| Default  
---|---|---  
`children*`| `RowElement | RowElement[] | ((item: T) => RowElement)`  
`items`| `Iterable<T>`  
`isLoading`| `boolean`  
`loadingState`| `LoadingState`  
`loadingContent`| `ReactNode`  
`emptyContent`| `ReactNode`  
### TableBody Events
Prop| Type| Default  
---|---|---  
`onLoadMore`| `() => any`  
### TableRow Props
Prop| Type| Default  
---|---|---  
`children*`| `CellElement | CellElement[] | CellRenderer`  
`textValue`| `string`  
### TableCell Props
Prop| Type| Default  
---|---|---  
`children*`| `ReactNode`  
`textValue`| `string`  
### Table types
#### Sort descriptor
#### Selection
#### Loading state
SwitchTabs
On this page
  * Installation
  * Import
  * Usage
  * Dynamic
  * Why not array map?
  * Empty State
  * Without Header
  * Without Wrapper
  * Custom Cells
  * Striped Rows
  * Single Row Selection
  * Multiple Row Selection
  * Disallow Empty Selection
  * Controlled Selection
  * Disabled Rows
  * Selection Behavior
  * Rows Actions
  * Sorting Rows
  * Loading more data
  * Paginated Table
  * Async Pagination
  * Infinite Pagination
  * Virtualization
  * Ten Thousand Items
  * Max Table Height
  * Custom Row Height
  * Use Case Example
  * Slots
  * Custom Styles
  * Data Attributes
  * Accessibility
  * API
  * Table Props
  * Table Events
  * TableHeader Props
  * TableColumn Props
  * TableBody Props
  * TableBody Events
  * TableRow Props
  * TableCell Props
  * Table types
  * Sort descriptor
  * Selection
  * Loading state
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
