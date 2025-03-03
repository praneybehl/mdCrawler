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


# Toast
Toasts are temporary notifications that provide concise feedback about an action or event.
Storybook@heroui/toastSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add toast

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
Individual
Global
## Requirement
The `ToastProvider` must be added to the application before using the `addToast` function. This is required to initialize the context for managing toasts.
### Usage
Preview
Code
### Colors
Toast comes with 6 color variants to convey different meanings.
Preview
Code
### Variants
Preview
Code
### Radius
Preview
Code
### Toast Placement
Preview
Code
### Custom Styles
You can customize the alert by passing custom Tailwind CSS classes to the component slots.
Preview
Code
### Custom Close Icon
You can pass a custom close icon to the toast by passing the `closeIcon` prop and a custom class name to the `closeButton` slot.
Preview
Code
### Global Toast Props
You can pass global toast props to the `ToastProvider` to apply to all toasts.
## Data Attributes
Toast has the following attributes on the `base` element:
  * **data-has-title** : When the toast has a title
  * **data-has-description** : When the toast has a description
  * **data-animation** : Shows the current animation of toast ("entering", "queued", "exiting", "undefined")
  * **data-placement** : Where the toast is placed on the view-port.
  * **data-drag-value** : Value by which the toast is dragged from it's original position. (This remains "0" in case of disabledAnimation)


### Slots
Toast has the following slots:
  * `base`: The main toast container element
  * `title`: The title element
  * `description`: The description element
  * `icon`: The icon element
  * `loadingIcon`: The icon to be displayed until `promise` is resolved/rejected.
  * `content`: The wrapper for the title, description and icon content.
  * `motionDiv`: The motion.div for the FramerMotion.
  * `progressTrack`: The track of the progressBar.
  * `progressIndicator`: The indicator of the progressBar.
  * `closeButton`: The close button element
  * `closeIcon`: The icon which resides in the close button.


## Accessibility
  * Toast has role of `alert`
  * All Toasts are present in ToastRegion.
  * Close button has aria-label="Close" by default
  * When no toast are present, ToastRegion is removed from the DOM


## API
### Toast Props
Prop| Type| Default  
---|---|---  
`title`| `ReactNode`  
`icon`| `ReactNode`  
`description`| `ReactNode`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`variant`| `solid | bordered | flat`| `"flat"`  
`radius`| `none | sm | md | lg | full`| `"md"`  
`endContent`| `ReactNode`  
`closeIcon`| `ReactNode`  
`timeout`| `number`| `"6000"`  
`promise`| `Promise | undefined`| `"undefined"`  
`loadingIcon`| `ReactNode`  
`priority`| `number | undefined`| `"undefined"`  
`hideIcon`| `boolean`| `false`  
`hideCloseButton`| `boolean`| `false`  
`shouldShowTimeoutProgress`| `boolean`| `false`  
`classNames`| `Partial<Record<"base" | "content" | "wrapper" | "title" | "description" | "icon" | "loadingIcon" | "progressTrack" | "progressIndicator | "motionDiv" | "closeButton" | "closeIcon", string>>`  
### ToastProvider Props
Prop| Type| Default  
---|---|---  
`maxVisibleToasts`| `number`| `"3"`  
`placement`| `bottom-right | bottom-left | bottom-center | top-right | top-left | top-center`| `"bottom-right"`  
`severity`| `default | primary | secondary | success | warning | danger`| `"default"`  
`disableAnimation`| `boolean`| `false`  
`toastOffset`| `number`| `"0"`  
`toastProps`| `ToastProps`  
### Toast Events
Prop| Type| Default  
---|---|---  
`onClose`| `() => void`  
TabsTextarea
On this page
  * Installation
  * Import
  * Requirement
  * Usage
  * Colors
  * Variants
  * Radius
  * Toast Placement
  * Custom Styles
  * Custom Close Icon
  * Global Toast Props
  * Data Attributes
  * Slots
  * Accessibility
  * API
  * Toast Props
  * ToastProvider Props
  * Toast Events
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
