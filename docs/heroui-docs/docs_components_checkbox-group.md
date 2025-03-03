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


# Checkbox Group
A CheckboxGroup allows users to select one or more items from a list of choices.
Storybook@heroui/checkboxReact AriaSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add checkbox

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
HeroUI exports 2 checkbox-related components:
  * **CheckboxGroup** : The root component, it wraps the label and the wrapper.
  * **Checkbox** : The checkbox component.


Individual
Global
## Usage
Preview
Code
Select cities
Buenos AiresSydneySan FranciscoLondonTokyo
### Disabled
Preview
Code
### Horizontal
Preview
Code
### Controlled
You can use the `value` and `onValueChange` properties to control the checkbox input value.
Preview
Code
### Invalid
Preview
Code
## Slots
  * **base** : Checkbox group root wrapper, it wraps the label and the wrapper.
  * **wrapper** : Checkbox group wrapper, it wraps all checkboxes.
  * **label** : Checkbox group label, it is placed before the wrapper.
  * **description** : The description of the checkbox group.
  * **errorMessage** : The error message of the checkbox group.


### Custom Styles
You can customize the `CheckboxGroup` component by passing custom Tailwind CSS classes to the component slots.
Preview
Code
### Custom Implementation
In case you need to customize the checkbox even further, you can use the `useCheckboxGroup` hook to create your own implementation.
Preview
Code
> **Note** : We used Tailwind Variants to implement the styles above, you can use any other library such as clsx to achieve the same result.
## API
### Checkbox Group Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode[] | ReactNode[]`  
`orientation`| `vertical | horizontal`| `"vertical"`  
`color`| `default | primary | secondary | success | warning | danger`| `"primary"`  
`size`| `xs | sm | md | lg | xl`| `"md"`  
`radius`| `none | base | xs | sm | md | lg | xl | full`| `"md"`  
`name`| `string`  
`label`| `string`  
`value`| `string[]`  
`lineThrough`| `boolean`| `false`  
`defaultValue`| `string[]`  
`isInvalid`| `boolean`| `false`  
`validationState`| `valid | invalid`  
`description`| `ReactNode`  
`errorMessage`| `ReactNode | ((v: ValidationResult) => ReactNode)`  
`validate`| `(value: string[]) => ValidationError | true | null | undefined`  
`validationBehavior`| `native | aria`| `"native"`  
`isDisabled`| `boolean`| `false`  
`isRequired`| `boolean`| `false`  
`isReadOnly`| `boolean`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<"base" | "wrapper" | "label", string>>`  
### Checkbox Group Events
Prop| Type| Default  
---|---|---  
`onChange`| `(value: string[]) => void`  
CheckboxChip
On this page
  * Installation
  * Import
  * Usage
  * Disabled
  * Horizontal
  * Controlled
  * Invalid
  * Slots
  * Custom Styles
  * Custom Implementation
  * API
  * Checkbox Group Props
  * Checkbox Group Events
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
