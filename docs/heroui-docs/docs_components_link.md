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


# Link
Links allow users to click their way from page to page. This component is styled to resemble a hyperlink and semantically renders an `<a>`
Storybook@heroui/linkReact AriaSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest addlink

```


```

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
### Sizes
Preview
Code
### Colors
Preview
Code
### Underline
Preview
Code
### External
If you pass the `isExternal` prop, the link will have the `target="_blank"` and `rel="noopener noreferrer"` attributes.
Preview
Code
### Custom Anchor Icon
Preview
Code
### Block Link
If you pass the `isBlock` prop, the link will be rendered as a block element with a `hover` effect.
Preview
Code
### Polymorphic Component
HeroUI's components expose a `as` prop that allows you to customize the React element type that is used to render the component.
Preview
Code
### Routing
The `<Link>` component works with frameworks and client side routers like Next.js and React Router. See the Routing guide to learn how to set this up.
### Custom Implementation
In case you need to customize the link even further, you can use the `useLink` hook to create your own implementation.
## Data Attributes
`Link` has the following attributes on the `base` element:
  * **data-focus** : When the link is being focused. Based on useFocusRing
  * **data-focus-visible** : When the link is being focused with the keyboard. Based on useFocusRing
  * **data-disabled** : When the link is disabled. Based on `isDisabled` prop.


## Accessibility
  * Support for mouse, touch, and keyboard interactions.
  * Support for navigation links via `<a>` elements or custom element types via ARIA.
  * Support for disabled links.
  * Keyboard users may activate links using the `Enter` key.


## API
### Link Props
Prop| Type| Default  
---|---|---  
`size`| `sm | md | lg`| `"md"`  
`color`| `foreground | primary | secondary | success | warning | danger`| `"primary"`  
`underline`| `none | hover | always | active | focus`| `"none"`  
`href`| `string`  
`target`| `HTMLAttributeAnchorTarget`  
`rel`| `string`  
`download`| `boolean | string`  
`ping`| `string`  
`referrerPolicy`| `HTMLAttributeReferrerPolicy`  
`isExternal`| `boolean`| `false`  
`showAnchorIcon`| `boolean`| `false`  
`anchorIcon`| `ReactNode`  
`isBlock`| `boolean`| `false`  
`isDisabled`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
### Link Events
Prop| Type| Default  
---|---|---  
`onPress`| `(e: PressEvent) => void`  
`onPressStart`| `(e: PressEvent) => void`  
`onPressEnd`| `(e: PressEvent) => void`  
`onPressChange`| `(isPressed: boolean) => void`  
`onPressUp`| `(e: PressEvent) => void`  
`onKeyDown`| `(e: KeyboardEvent) => void`  
`onKeyUp`| `(e: KeyboardEvent) => void`  
`onClick`| `MouseEventHandler`  
KbdListbox
On this page
  * Installation
  * Import
  * Usage
  * Disabled
  * Sizes
  * Colors
  * Underline
  * External
  * Custom Anchor Icon
  * Block Link
  * Polymorphic Component
  * Routing
  * Custom Implementation
  * Data Attributes
  * Accessibility
  * API
  * Link Props
  * Link Events
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
