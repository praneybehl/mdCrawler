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


# Chip
A Chip is a small block of essential information that represent an input, attribute, or action.
Storybook@heroui/chipSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add chip

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
Individual
Global
## Usage
Preview
Code
Chip
### Disabled
Preview
Code
Chip
### Sizes
Preview
Code
### Colors
Preview
Code
### Radius
Preview
Code
### Variants
Preview
Code
### Start & End Content
Preview
Code
### With Close Button
If you pass the `onClose` prop, the close button will be visible. You can override the close icon by passing the `endContent` prop.
Preview
Code
### With Avatar
Preview
Code
### List of Chips
Preview
Code
## Slots
  * **base** : The base slot of the chip, it is the container of the chip.
  * **content** : The content slot of the chip, it is the container of the chip children.
  * **dot** : Small dot on the left side of the chip. It is visible when the `variant=dot` prop is passed.
  * **avatar** : Avatar classes of the chip. It is visible when the `avatar` prop is passed.
  * **closeButton** : Close button classes of the chip. It is visible when the `onClose` prop is passed.


### Custom Styles
You can customize the `Chip` component by passing custom Tailwind CSS classes to the component slots.
Preview
Code
## API
### Chip Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode`  
`variant`| `solid | bordered | light | flat | faded | shadow | dot`| `"solid"`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`size`| `sm | md | lg`| `"md"`  
`radius`| `none | sm | md | lg | full`| `"full"`  
`avatar`| `ReactNode`  
`startContent`| `ReactNode`  
`endContent`| `ReactNode`  
`isDisabled`| `boolean`| `false`  
`classNames`| `Partial<Record<"base" | "content" | "dot" | "avatar" | "closeButton", string>>`  
### Chip Events
Prop| Type| Default  
---|---|---  
`onClose`| `(e: PressEvent) => void`  
Checkbox GroupCircular Progress
On this page
  * Installation
  * Import
  * Usage
  * Disabled
  * Sizes
  * Colors
  * Radius
  * Variants
  * Start & End Content
  * With Close Button
  * With Avatar
  * List of Chips
  * Slots
  * Custom Styles
  * API
  * Chip Props
  * Chip Events
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
