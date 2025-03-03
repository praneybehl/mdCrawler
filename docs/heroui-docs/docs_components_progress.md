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


# Progress
The Progress component allows you to view the progress of any activity.
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
### Indeterminate
You can use the `isIndeterminate` prop to display an indeterminate progress bar. This is useful when you don't know how long an operation will take.
Preview
Code
### Striped
Preview
Code
### With Label
Preview
Code
> **Note** : If you pass the `label` prop you don't need to pass `aria-label` prop anymore.
### With Value
Preview
Code
### Value Formatting
Values are formatted as a percentage by default, but this can be modified by using the `formatOptions` prop to specify a different format. `formatOptions` is compatible with the option parameter of Intl.NumberFormat and is applied based on the current locale.
Preview
Code
## Slots
  * **base** : The base slot of the progress, it is the main container.
  * **labelWrapper** : The label and value label wrapper.
  * **label** : The label of the progress.
  * **value** : The value label of the progress.
  * **track** : The track is the background bar of the progress.
  * **indicator** : The indicator is the bar that is filled according to the `value`.


### Custom Styles
You can customize the `Progress` component by passing custom Tailwind CSS classes to the component slots.
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
### Progress Props
Prop| Type| Default  
---|---|---  
`label`| `ReactNode`  
`size`| `sm | md | lg`| `"md"`  
`color`| `default | primary | secondary | success | warning | danger`| `"primary"`  
`radius`| `none | sm | md | lg | full`| `"full"`  
`value`| `number`  
`valueLabel`| `ReactNode`  
`minValue`| `number`| `"0"`  
`maxValue`| `number`| `"100"`  
`formatOptions`| `Intl.NumberFormat`| `"{style: 'percent'}"`  
`isIndeterminate`| `boolean`| `false`  
`isStriped`| `boolean`| `false`  
`showValueLabel`| `boolean`| `true`  
`isDisabled`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<'base' | 'labelWrapper' | 'label' | 'track' | 'value' | 'indicator', string>>`  
PopoverRadio Group
On this page
  * Installation
  * Import
  * Usage
  * Sizes
  * Colors
  * Indeterminate
  * Striped
  * With Label
  * With Value
  * Value Formatting
  * Slots
  * Custom Styles
  * Data Attributes
  * Accessibility
  * API
  * Progress Props
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
