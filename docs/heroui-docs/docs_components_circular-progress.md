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


# Circular Progress
Circular progress indicators are utilized to indicate an undetermined wait period or visually represent the duration of a process.
Storybook@heroui/progressReact AriaSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add progress

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
Individual
Global
## Usage
Preview
Code
> **Note** : Make sure to pass the `aria-label` prop when the `label` prop is not provided. This is required for accessibility.
### Sizes
Preview
Code
### Colors
Preview
Code
### With Label
Preview
Code
### With Value
Preview
Code
### Value Formatting
Values are formatted as a percentage by default, but this can be modified by using the `formatOptions` prop to specify a different format. `formatOptions` is compatible with the option parameter of Intl.NumberFormat and is applied based on the current locale.
Preview
Code
## Slots
  * **base** : The base slot of the circular progress, it is the main container.
  * **svgWrapper** : The wrapper of the svg circles and the value label.
  * **svg** : The svg element of the circles.
  * **track** : The track is the background circle of the circular progress.
  * **indicator** : The indicator is the one that is filled according to the `value`.
  * **value** : The value content.
  * **label** : The label content.


### Custom Styles
You can customize the `CircularProgress` component by passing custom Tailwind CSS classes to the component slots.
Preview
Code
## Data Attributes
`CircularProgress` has the following attributes on the `base` element:
  * **data-indeterminate** : Indicates whether the progress is indeterminate.
  * **data-disabled** : Indicates whether the progress is disabled. Based on `isDisabled` prop.


## Accessibility
  * Exposed to assistive technology as a progress bar via ARIA.
  * Labeling support for accessibility.
  * Internationalized number formatting as a percentage or value.
  * Determinate and indeterminate progress support.
  * Exposes the `aria-valuenow`, `aria-valuemin`, `aria-valuemax` and `aria-valuetext` attributes.


## API
### Circular Progress Props
Prop| Type| Default  
---|---|---  
`label`| `ReactNode`  
`size`| `sm | md | lg`| `"md"`  
`color`| `default | primary | secondary | success | warning | danger`| `"primary"`  
`value`| `number`  
`valueLabel`| `ReactNode`  
`minValue`| `number`| `"0"`  
`maxValue`| `number`| `"100"`  
`formatOptions`| `Intl.NumberFormat`| `"{style: 'percent'}"`  
`isIndeterminate`| `boolean`| `true`  
`showValueLabel`| `boolean`| `true`  
`strokeWidth`| `number`| `"2"`  
`isDisabled`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<'base'｜'svgWrapper'｜'svg'｜'track'｜'indicator'｜'value'｜'label', string>>`  
ChipCode
On this page
  * Installation
  * Import
  * Usage
  * Sizes
  * Colors
  * With Label
  * With Value
  * Value Formatting
  * Slots
  * Custom Styles
  * Data Attributes
  * Accessibility
  * API
  * Circular Progress Props
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
