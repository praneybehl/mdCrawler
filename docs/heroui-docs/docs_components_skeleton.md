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


# Skeleton
Skeleton is a placeholder to show a loading state and the expected shape of a component.
Storybook@heroui/skeletonSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add skeleton

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
Individual
Global
## Usage
Preview
Code
### Standalone
Skeleton takes the shape of its `children` component by default, but you can also use it as a standalone component.
Preview
Code
### Loaded State
You can use the `isLoaded` prop to stop the skeleton animation and show the children component.
Preview
Code
## Slots
  * **base** : The base slot of the skeleton, it contains the `before` and `after` pseudo elements to create the animation.
  * **content** : The wrapped component to show the skeleton shape. It is visible only when the `isLoaded` prop is `true`.


## Data Attributes
`Skeleton` has the following attributes on the `base` element:
  * **data-loaded** : Indicates the loaded state of the skeleton. Based on the `isLoaded` prop.


## API
### Skeleton Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode`  
`isLoaded`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<"base" | "content", string>>`  
SelectSlider
On this page
  * Installation
  * Import
  * Usage
  * Standalone
  * Loaded State
  * Slots
  * Data Attributes
  * API
  * Skeleton Props
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
