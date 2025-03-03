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


# Alert
Alerts are temporary notifications that provide concise feedback about an action or event.
Storybook@heroui/alertSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add alert

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
Individual
Global
## Usage
Preview
Code
This is an alert
Thanks for subscribing to our newsletter!
### Colors
Alert comes with 6 color variants to convey different meanings.
Preview
Code
This is a default alert
This is a primary alert
This is a secondary alert
This is a success alert
This is a warning alert
This is a danger alert
### Variants
Preview
Code
### Radius
Preview
Code
### Custom Icon
By default, Alert displays an appropriate icon based on the `color` prop. You can override this by providing a custom icon using the `icon` prop.
Preview
Code
### Without Icon
You can hide the icon by setting the `hideIcon` prop to `true`.
Preview
Code
### Without Icon Wrapper
You can hide the icon wrapper by setting the `hideIconWrapper` prop to `true`.
Preview
Code
### With Action
Alert supports an `endContent` prop for additional actions.
Preview
Code
### Controlled Visibility
You can control the alert visibility using the `isVisible` and `onVisibleChange` props.
Preview
Code
### Custom Styles
You can customize the alert by passing custom Tailwind CSS classes to the component slots.
Preview
Code
### Custom Implementation
You can use the `useAlert` hook to create your own alert component.
## Data Attributes
Alert has the following attributes on the `base` element:
  * **data-visible** : When the alert is visible
  * **data-closeable** : When the alert can be closed
  * **data-has-title** : When the alert has a title
  * **data-has-description** : When the alert has a description


### Slots
Alert has the following slots:
  * `base`: The main alert container element
  * `title`: The title element
  * `description`: The description element
  * `mainWrapper`: The wrapper for the title and description content
  * `closeButton`: The close button element
  * `iconWrapper`: The wrapper for the alert icon
  * `alertIcon`: The alert icon element


## Accessibility
  * Alert has role of `alert`
  * Close button has aria-label="Close" by default
  * When closed, alert is removed from the DOM


## API
### Alert Props
Prop| Type| Default  
---|---|---  
`title`| `ReactNode`  
`icon`| `ReactNode`  
`description`| `ReactNode`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`variant`| `solid | bordered | flat | faded`| `"flat"`  
`radius`| `none | sm | md | lg | full`| `"md"`  
`startContent`| `ReactNode`  
`endContent`| `ReactNode`  
`isVisible`| `boolean`  
`isClosable`| `boolean`| `false`  
`hideIcon`| `boolean`| `false`  
`hideIconWrapper`| `boolean`| `false`  
`closeButtonProps`| `ButtonProps`  
### Alert Events
Prop| Type| Default  
---|---|---  
`onClose`| `() => void`  
`onVisibleChange`| `(isVisible: boolean) => void`  
AutocompleteAvatar
On this page
  * Installation
  * Import
  * Usage
  * Colors
  * Variants
  * Radius
  * Custom Icon
  * Without Icon
  * Without Icon Wrapper
  * With Action
  * Controlled Visibility
  * Custom Styles
  * Custom Implementation
  * Data Attributes
  * Slots
  * Accessibility
  * API
  * Alert Props
  * Alert Events
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
