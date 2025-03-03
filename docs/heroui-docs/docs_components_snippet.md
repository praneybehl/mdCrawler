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


# Snippet
Snippet is a component that can be used to display inline or multiline code snippets.
Storybook@heroui/snippetSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
Individual
Global
## Usage
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
### Custom Symbol
Preview
Code
### Without Copy
You can hide the copy button by setting the `hideCopyButton` property to `true`.
Preview
Code
### Custom Tooltip
You can customize the tooltip by using the `tooltipProps` property.
Preview
Code
> **Note** : For more information about the `Tooltip` props, please visit the Tooltip page.
### Multiline
Preview
Code
### Custom Icons
You can customize the copy and copied icons by using the `copyIcon` and `checkIcon` properties.
Preview
Code
## Slots
  * **base** : The base slot of the snippet, it is the main container.
  * **content** : This is the wrapper of the `<pre/>` slot.
  * **pre** : The `<pre/>` slot of the snippet. It is used to wrap the code.
  * **symbol** : The symbol wrapper slot.
  * **copyButton** : The copy button slot.
  * **copyIcon** : The copy icon slot.
  * **checkIcon** : The check icon slot.


## API
### Snippet Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode | ReactNode[]`  
`size`| `sm | md | lg`| `"md"`  
`radius`| `none | sm | md | lg`| `"lg"`  
`symbol`| `string | ReactNode`| `"$"`  
`timeout`| `number`| `"2000"`  
`codeString`| `string`  
`tooltipProps`| `TooltipProps`  
`copyIcon`| `ReactNode`  
`checkIcon`| `ReactNode`  
`disableTooltip`| `boolean`| `false`  
`disableCopy`| `boolean`| `false`  
`hideCopyButton`| `boolean`| `false`  
`hideSymbol`| `boolean`| `false`  
`copyButtonProps`| `ButtonProps`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<'base' | 'content' | 'pre' | 'symbol' | 'copyButton' | 'checkIcon', string>>`  
### Snippet Events
Prop| Type| Default  
---|---|---  
`onCopy`| `(value: string | string[]) => void`  
SliderSpacer
On this page
  * Installation
  * Import
  * Usage
  * Sizes
  * Colors
  * Variants
  * Custom Symbol
  * Without Copy
  * Custom Tooltip
  * Multiline
  * Custom Icons
  * Slots
  * API
  * Snippet Props
  * Snippet Events
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
