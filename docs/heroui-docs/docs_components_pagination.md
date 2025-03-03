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


# Pagination
The Pagination component allows you to display active page and navigate between multiple pages.
Storybook@heroui/paginationSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add pagination

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
HeroUI exports 3 pagination-related components:
  * **Pagination** : The main component to display a pagination.
  * **PaginationItem** : The internal component to display a pagination item.
  * **PaginationCursor** : The internal item component to display the current page.


Individual
Global
## Usage
Preview
Code
### Disabled
Preview
Code
### Sizes
Preview
Code
### Colors
Preview
Code
### Variants
You can use the `variant` property to change the pagination items style.
Preview
Code
### With Controls
You can set the `showControls` to `true` to display the `next` and `previous` buttons.
Preview
Code
### Pagination Loop
In case you want to loop the pagination, you can set the `loop` property to `true`. The cursor will go back to the first page when it reaches the last page and vice versa.
Preview
Code
### Changing the initial page
You can change the initial page by setting the `initialPage` property.
Preview
Code
### Compact Pagination
You can set the `isCompact` property to `true` to display reduced version of the pagination.
Preview
Code
### With Shadow
You can use the `showShadow` property to display a shadow below the active page item.
Preview
Code
### Controlled
Preview
Code
### Siblings
You can control the number of pages to show before and after the current page by setting the `siblings` property.
Preview
Code
### Boundaries
You can control the number of pages to show at the beginning and end of the pagination by setting the `boundaries` property.
Preview
Code
### Custom items
You can use the `renderItem` property to customize the pagination items.
Preview
Code
## Slots
  * **base** : The main pagination slot.
  * **wrapper** : The pagination wrapper slot. This wraps the pagination items.
  * **prev** : The previous button slot.
  * **next** : The next button slot.
  * **item** : The pagination item slot, applied to the middle items.
  * **cursor** : The current page slot. Available only when `disableCursorAnimation` is `false` and `disableAnimation` is `false`.
  * **forwardIcon** : The forward icon slot. The one that appears when hovering the ellipsis button.
  * **ellipsis** : The ellipsis slot.
  * **chevronNext** : The chevron next icon slot.


### Custom Styles
You can customize the `Pagination` component by passing custom Tailwind CSS classes to the component slots.
Preview
Code
### Custom Implementation
In case you need to customize the pagination even further, you can use the `usePagination` hook to create your own implementation.
Preview
Code
## Data Attributes
`Pagination` has the following attributes on the `base` element:
  * **data-controls** : Indicates whether the pagination has controls. Based on `showControls` prop.
  * **data-loop** : When the pagination is looped. Based on `loop` prop.
  * **data-dots-jump** : Indicates whether the pagination has dots jump. Based on `dotsJump` prop.
  * **data-total** : The total number of pages. Based on `total` prop.
  * **data-active-page** : The active page. Based on `activePage` prop.


## Accessibility
  * The root node has a role of `navigation` by default.
  * The pagination items have an aria-label that identifies the item purpose ("next page button", "previous page button", etc.), you can override this label by using the `getItemAriaLabel` function.
  * The pagination items are in tab order, with a tabindex of "0".


## API
### Pagination Props
Prop| Type| Default  
---|---|---  
`variant`| `flat | bordered | light | faded`| `"flat"`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`size`| `sm | md | lg`| `"md"`  
`radius`| `none | sm | md | lg | full`| `"xl"`  
`total`| `number`| `"1"`  
`dotsJump`| `number`| `"5"`  
`initialPage`| `number`| `"1"`  
`page`| `number`  
`siblings`| `number`| `"1"`  
`boundaries`| `number`| `"1"`  
`loop`| `boolean`| `false`  
`isCompact`| `boolean`| `false`  
`isDisabled`| `boolean`| `false`  
`showShadow`| `boolean`| `false`  
`showControls`| `boolean`| `false`  
`disableCursorAnimation`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
`renderItem`| `PaginationItemProps`  
`getItemAriaLabel`| `(page: string) => string`  
`classNames`| `Partial<Record<'base' | 'wrapper' | 'prev' | 'next' | 'item' | 'cursor' | 'forwardIcon' | 'ellipsis' | 'chevronNext', string>>`  
### Pagination Events
Prop| Type| Default  
---|---|---  
`onChange`| `(page: number) => void`  
### Types
#### Pagination Item Props
Number InputPopover
On this page
  * Installation
  * Import
  * Usage
  * Disabled
  * Sizes
  * Colors
  * Variants
  * With Controls
  * Pagination Loop
  * Changing the initial page
  * Compact Pagination
  * With Shadow
  * Controlled
  * Siblings
  * Boundaries
  * Custom items
  * Slots
  * Custom Styles
  * Custom Implementation
  * Data Attributes
  * Accessibility
  * API
  * Pagination Props
  * Pagination Events
  * Types
  * Pagination Item Props
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
