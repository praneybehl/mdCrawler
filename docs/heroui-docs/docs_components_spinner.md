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


# Spinner
Spinner express an unspecified wait time or display the length of a process.
Storybook@heroui/spinnerServer componentSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add spinner

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
Individual
Global
## Usage
Preview
Code
> **Note** : Spinner adds `Loading` as `aria-label` by default. This is required for accessibility. You can change it by passing a `label` or `aria-label` prop.
### Sizes
Preview
Code
### Colors
Preview
Code
### With Label
Preview
Code
### Label colors
Preview
Code
### Variants
Preview
Code
## Slots
  * **base** : The base slot of the spinner, it wraps the circles and the label.
  * **wrapper** : The wrapper of the circles.
  * **circle1** : The first circle of the spinner component. (Effective only when variant is `default` or `gradient`)
  * **circle2** : The second circle of the spinner component. (Effective only when variant is `default` or `gradient`)
  * **dots** : Dots of the spinner component. (Effective only when variant is `wave` or `dots`)
  * **spinnerBars** : Bars of the spinner component. (Effective only when variant is `spinner`)
  * **label** : The label content.


## API
### Spinner Props
Prop| Type| Default  
---|---|---  
`label`| `string`  
`size`| `sm | md | lg`| `"md"`  
`color`| `default | primary | secondary | success | warning | danger`| `"primary"`  
`variant`| `default | simple | gradient | wave | dots | spinner`| `"default"`  
`labelColor`| `default | primary | secondary | success | warning | danger`| `"default"`  
`classNames`| `Partial<Record<'base' | 'wrapper' | 'circle1' | 'circle2' | 'dots' | 'spinnerBars' | 'label', string>>`  
SpacerSwitch
On this page
  * Installation
  * Import
  * Usage
  * Sizes
  * Colors
  * With Label
  * Label colors
  * Variants
  * Slots
  * API
  * Spinner Props
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
