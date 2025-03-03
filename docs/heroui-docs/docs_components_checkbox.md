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


# Checkbox
Checkboxes allow users to select multiple items from a list of individual items, or to mark one individual item as selected.
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
Individual
Global
## Usage
Preview
Code
Option
### Disabled
Preview
Code
OptionOption
### Sizes
Preview
Code
### Colors
Preview
Code
### Radius
Preview
Code
### Indeterminate
The `isIndeterminate` prop sets a `Checkbox` to an indeterminate state, overriding its appearance and maintaining it until set to `false`, regardless of user interaction.
Preview
Code
### Line Through
Preview
Code
### Custom Check Icon
> By default, `IconProps` will be passed to your icon component. Please make sure that `isSelected`, `isIndeterminate`, and `disableAnimation` are not passed to a DOM element.
Preview
Code
### Controlled
Preview
Code
> **Note** : HeroUI `Checkbox` also supports native events like `onChange`, useful for form libraries such as Formik and React Hook Form.
## Slots
  * **base** : Checkbox wrapper, it handles alignment, placement, and general appearance.
  * **wrapper** : An inner container that includes styles for relative positioning, flex properties, overflow handling and managing hover and selected states.
  * **hiddenInput** : The hidden input element that is used to handle the checkbox state.
  * **icon** : Icon within the checkbox, controlling size, visibility, and changes when checked.
  * **label** : The text associated with the checkbox.


### Custom Styles
You can customize the `Checkbox` component by passing custom Tailwind CSS classes to the component slots.
Preview
Code
### Custom Implementation
In case you need to customize the checkbox even further, you can use the `useCheckbox` hook to create your own implementation.
Preview
Code
> **Note** : We used Tailwind Variants to implement the styles above, you can use any other library such as clsx to achieve the same result.
## Data Attributes
`Checkbox` has the following attributes on the `base` element:
  * **data-selected** : When the checkbox is checked. Based on `isSelected` prop.
  * **data-pressed** : When the checkbox is pressed. Based on usePress
  * **data-invalid** : When the checkbox is invalid. Based on `validationState` prop.
  * **data-readonly** : When the checkbox is readonly. Based on `isReadOnly` prop.
  * **data-indeterminate** : When the checkbox is indeterminate. Based on `isIndeterminate` prop.
  * **data-hover** : When the checkbox is being hovered. Based on useHover
  * **data-focus** : When the checkbox is being focused. Based on useFocusRing.
  * **data-focus-visible** : When the checkbox is being focused with the keyboard. Based on useFocusRing.
  * **data-disabled** : When the checkbox is disabled. Based on `isDisabled` prop.
  * **data-loading** : When the checkbox is loading. Based on `isLoading` prop.


## Accessibility
  * Built with a native HTML `<input>` element.
  * Full support for browser features like form autofill.
  * Keyboard focus management and cross browser normalization.
  * Keyboard event support for `Tab` and `Space` keys.
  * Labeling support for assistive technology.
  * Indeterminate state support.


## API
### Checkbox Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode`  
`icon`| `CheckboxIconProps`  
`value`| `string`  
`name`| `string`  
`size`| `sm | md | lg`| `"md"`  
`color`| `default | primary | secondary | success | warning | danger`| `"primary"`  
`radius`| `none | sm | md | lg | full`  
`lineThrough`| `boolean`| `false`  
`isSelected`| `boolean`  
`defaultSelected`| `boolean`  
`isRequired`| `boolean`| `false`  
`isReadOnly`| `boolean`  
`isDisabled`| `boolean`| `false`  
`isIndeterminate`| `boolean`  
`isInvalid`| `boolean`| `false`  
`validationState`| `valid | invalid`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<"base"｜ "wrapper"｜ "icon"｜ "label", string>>`  
### Checkbox Events
Prop| Type| Default  
---|---|---  
`onChange`| `React.ChangeEvent<HTMLInputElement>`  
`onValueChange`| `(isSelected: boolean) => void`  
### Types
#### Checkbox Icon Props
CardCheckbox Group
On this page
  * Installation
  * Import
  * Usage
  * Disabled
  * Sizes
  * Colors
  * Radius
  * Indeterminate
  * Line Through
  * Custom Check Icon
  * Controlled
  * Slots
  * Custom Styles
  * Custom Implementation
  * Data Attributes
  * Accessibility
  * API
  * Checkbox Props
  * Checkbox Events
  * Types
  * Checkbox Icon Props
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
