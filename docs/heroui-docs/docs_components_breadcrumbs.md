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


# Breadcrumbs
Breadcrumbs display a hierarchy of links to the current page or resource in an application.
Storybook@heroui/breadcrumbsSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add breadcrumbs

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
HeroUI exports 2 breadcrumb-related components:
  * **Breadcumbs** : The main component, which is a wrapper for the other components.
  * **BreadcrumbItem** : The component that represents a breadcrumb item.


Individual
Global
## Usage
Preview
Code
### Disabled
Disabled breadcrumbs display items but prevent navigation, ensuring a consistent layout. The last item, signifying the current page, isn't disabled.
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
### Underlines
Preview
Code
### Radius
Preview
Code
### Routing
The `<BreadcrumbItem>` component works with frameworks and client side routers like Next.js and React Router. See the Routing guide to learn how to set this up.
Preview
Code
### Controlled
You can control the current/active item by using the `isCurrent` and `onAction` props.
Preview
Code
> **Note** : If needed you can use the `onPress` prop to handle the click event on the breadcrumb item.
### Menu Type
It is possible to use the `Breadcrumbs` component as a horizontal menu. This is useful when you want to display a list of possible navigations and let the user choose one of them.
Preview
Code
### Start & End Content
You can add any element to the start or end of the breadcrumbs by using the `startContent` and `endContent` props. The above example uses the `startContent` prop to add icons to the start of the breadcrumbs.
Preview
Code
### Custom Separator
You can customize the separator between breadcrumbs by using the `separator` prop.
Preview
Code
### Custom Items
the `BreadcrumbItem` component accepts any element as its children. This allows you to customize the appearance of the breadcrumb items.
The above example uses the Dropdown component to create a dropdown menu in the breadcrumb.
Preview
Code
The `Breadcrumbs` component picks only the `BreadcrumbItem` components as its children. This means that you cannot place any other component directly inside the `Breadcrumbs` component.
### Collapsing Items
The `Breadcrumb` component provides 3 props to control the collapsing of items:
  * `maxItems`: Specifies the maximum number of breadcrumbs to display. When there are more than the maximum number, only the first `itemsBeforeCollapse` and last `itemsAfterCollapse` will be shown, with an ellipsis in between.
  * `itemsBeforeCollapse`: If max items is exceeded, the number of items to show before the ellipsis.
  * `itemsAfterCollapse`: If max items is exceeded, the number of items to show after the ellipsis.


Preview
Code
> **Note** : The ellipsis item will use the first collapsed item as its `href` prop.
### Customizing the Ellipsis Item
You can customize the ellipsis item by using the `renderEllipsis` prop. This prop accepts a function that returns a React element.
Preview
Code
## Slots
  * Breadcrumbs Slots
  * **base** : The main slot for the breadcrumbs. It wraps the `list` slot.
  * **list** : The list of breadcrumbs wrapper.
  * **ellipsis** : The slot for the ellipsis item. This is only visible when the breadcrumbs are collapsed.
  * **separator** : The slot for the custom separator, the one that can be set using the `separator` prop.
  * BreadcrumbItem Slots
  * **base** : The main slot for the breadcrumb item. It wraps the `item` slot.
  * **item** : The breadcrumb item wrapper.
  * **separator** : The slot for the item separator.


### Customizing the Breadcrumbs Styles
You can customize the `Breadcrumbs` style by using the `classNames` prop and its items by using the `itemClasses` prop.
Preview
Code
## Data Attributes
`BreadcrumbItem` has the following attributes on the `item` element:
  * **data-current** : When the breadcrumb item is the current item. Based on breadcrumb `isCurrent` prop or on whether the item is the last one.
  * **data-disabled** : When the breadcrumb item is disabled. Based on breadcrumb `isDisabled` prop.
  * **data-focus** : When the breadcrumb item is being focused. Based on useFocusRing.
  * **data-focus-visible** : When the breadcrumb item is being focused with the keyboard. Based on useFocusRing.


## Accessibility
  * Implemented as an ordered list of items.
  * Support for mouse, touch, and keyboard interactions on breadcrumbs.
  * Support for navigation links via `<a>` elements or custom element types via ARIA.
  * Localized ARIA labeling support for landmark navigation region.
  * Support for disabled breadcrumbs.
  * The last item is automatically marked as the current page using `aria-current`.


## API
### Breadcrumbs Props
Prop| Type| Default  
---|---|---  
`children*`| `ReactNode`  
`variant`| `solid | bordered | light`| `"solid"`  
`color`| `foreground | primary | secondary | success | warning | danger`| `"foreground"`  
`size`| `sm | md | lg`| `"md"`  
`radius`| `none | sm | md | lg | full`  
`underline`| `none | active | hover | focus | always`| `"none"`  
`separator`| `ReactNode`  
`maxItems`| `number`  
`itemsBeforeCollapse`| `number`  
`itemsAfterCollapse`| `number`  
`hideSeparator`| `boolean`| `false`  
`isDisabled`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
`itemClasses`| `Partial<Record<"base" | "item" | "separator", string>>`  
`classNames`| `Partial<Record<"base" | "list" | "ellipsis" | "separator", string>>`  
### Breadcrumbs Events
Prop| Type| Default  
---|---|---  
`onAction`| `(key: React.Key) => void`  
### BreadcrumbItem Props
Prop| Type| Default  
---|---|---  
`children*`| `ReactNode`  
`color`| `foreground | primary | secondary | success | warning | danger`| `"foreground"`  
`size`| `sm | md | lg`| `"md"`  
`underline`| `none | active | hover | focus | always`| `"none"`  
`startContent`| `ReactNode`  
`endContent`| `ReactNode`  
`separator`| `ReactNode`  
`isCurrent`| `boolean`| `false`  
`isLast`| `boolean`| `false`  
`hideSeparator`| `boolean`| `false`  
`isDisabled`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<"base" | "item" | "separator", string>>`  
### BreadcrumbItem Events
Prop| Type| Default  
---|---|---  
`onPress`| `(e: PressEvent) => void`  
`onPressStart`| `(e: PressEvent) => void`  
`onPressEnd`| `(e: PressEvent) => void`  
`onKeyDown`| `(e: KeyboardEvent) => void`  
`onKeyUp`| `(e: KeyboardEvent) => void`  
### Types
#### Render Ellipsis Function
BadgeButton
On this page
  * Installation
  * Import
  * Usage
  * Disabled
  * Sizes
  * Colors
  * Variants
  * Underlines
  * Radius
  * Routing
  * Controlled
  * Menu Type
  * Start & End Content
  * Custom Separator
  * Custom Items
  * Collapsing Items
  * Customizing the Ellipsis Item
  * Slots
  * Customizing the Breadcrumbs Styles
  * Data Attributes
  * Accessibility
  * API
  * Breadcrumbs Props
  * Breadcrumbs Events
  * BreadcrumbItem Props
  * BreadcrumbItem Events
  * Types
  * Render Ellipsis Function
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
