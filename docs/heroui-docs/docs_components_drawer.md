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


# Drawer
Displays a panel that slides in from the edge of the screen, containing supplementary content.
Storybook@heroui/drawerReact AriaSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add drawer

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
HeroUI exports 5 drawer-related components:
  * **Drawer** : The main component to display a drawer.
  * **DrawerContent** : The wrapper of the other drawer components.
  * **DrawerHeader** : The header of the drawer.
  * **DrawerBody** : The body of the drawer.
  * **DrawerFooter** : The footer of the drawer.


Individual
Global
## Usage
When the drawer opens:
  * Focus is bounded within the drawer and set to the first tabbable element.
  * Content behind a drawer is inert, meaning that users cannot interact with it.


Preview
Code
### Sizes
Preview
Code
### Non-dismissible
By default, the drawer can be closed by clicking on the overlay or pressing the `Esc` key. You can disable this behavior by setting the following properties:
  * Set the `isDismissable` property to `false` to prevent the drawer from closing when clicking on the overlay.
  * Set the `isKeyboardDismissDisabled` property to `true` to prevent the drawer from closing when pressing the Esc key.


Preview
Code
### Drawer placement
The drawer can be placed on any edge of the screen using the `placement` prop:
  * `left`
  * `right` (default)
  * `top`
  * `bottom`


Preview
Code
### With Form
The `Drawer` handles the focus within the drawer content. It means that you can use the drawer with form elements without any problem. The focus returns to the trigger when the drawer closes.
Preview
Code
> **Note** : You can add the `autoFocus` prop to the first `Input` component to focus it when the drawer opens.
### Backdrop
The `Drawer` component has a `backdrop` prop to show a backdrop behind the drawer. The backdrop can be either `transparent`, `opaque` or `blur`. The default value is `opaque`.
Preview
Code
### Custom Motion
Drawer offers a `motionProps` property to customize the `enter` / `exit` animation.
Preview
Code
> Learn more about Framer motion variants here.
### Custom Styles
Preview
Code
**Credits**
The Drawer component design is inspired by Luma.
## Slots
  * **wrapper** : The wrapper slot of the drawer. It wraps the `base` and the `backdrop` slots.
  * **base** : The main slot of the drawer content.
  * **backdrop** : The backdrop slot, it is displayed behind the drawer.
  * **header** : The header of the drawer, it is displayed at the top of the drawer.
  * **body** : The body of the drawer, it is displayed in the middle of the drawer.
  * **footer** : The footer of the drawer, it is displayed at the bottom of the drawer.
  * **closeButton** : The close button of the drawer.


## Data Attributes
`Drawer` has the following attributes on the `base` element:
  * **data-open** : When the drawer is open. Based on drawer state.
  * **data-dismissable** : When the drawer is dismissable. Based on `isDismissable` prop.


## Accessibility
  * Content outside the drawer is hidden from assistive technologies while it is open.
  * The drawer optionally closes when interacting outside, or pressing the `Esc` key.
  * Focus is moved into the drawer on mount, and restored to the trigger element on unmount.
  * While open, focus is contained within the drawer, preventing the user from tabbing outside.
  * Scrolling the page behind the drawer is prevented while it is open, including in mobile browsers.


## API
### Drawer Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode`  
`size`| `xs | sm | md | lg | xl | 2xl | 3xl | 4xl | 5xl | full`| `"md"`  
`radius`| `none | sm | md | lg`| `"lg"`  
`placement`| `left | right | top | bottom`| `"right"`  
`isOpen`| `boolean`  
`defaultOpen`| `boolean`  
`isDismissable`| `boolean`| `true`  
`isKeyboardDismissDisabled`| `boolean`| `false`  
`shouldBlockScroll`| `boolean`| `true`  
`hideCloseButton`| `boolean`| `false`  
`closeButton`| `ReactNode`  
`motionProps`| `MotionProps`  
`portalContainer`| `HTMLElement`| `"document.body"`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<'wrapper' | 'base' | 'backdrop' | 'header' | 'body' | 'footer' | 'closeButton', string>>`  
### Drawer Events
Prop| Type| Default  
---|---|---  
`onOpenChange`| `(isOpen: boolean) => void`  
`onClose`| `() => void`  
### Drawer types
#### Motion Props
DropdownForm
On this page
  * Installation
  * Import
  * Usage
  * Sizes
  * Non-dismissible
  * Drawer placement
  * With Form
  * Backdrop
  * Custom Motion
  * Custom Styles
  * Slots
  * Data Attributes
  * Accessibility
  * API
  * Drawer Props
  * Drawer Events
  * Drawer types
  * Motion Props
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
