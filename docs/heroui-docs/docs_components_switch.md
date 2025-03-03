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


# Switch
The Switch component is used as an alternative between checked and not checked states.
Storybook@heroui/switchReact AriaSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add switch

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
Individual
Global
## Usage
Preview
Code
### With Label
Preview
Code
### Disabled
Preview
Code
### Sizes
Preview
Code
### Colors
Preview
Code
### With Thumb Icon
Preview
Code
### With Icons
You can also add icons to start and end of the switch by using `startContent` and `endContent` props.
Preview
Code
### Controlled
Preview
Code
> **Note** : HeroUI `Switch` also supports native events like `onChange`, useful for form libraries such as Formik and React Hook Form.
## Slots
  * **base** : Base slot for the switch. It is the main wrapper.
  * **wrapper** : The wrapper of the start icon, end icon and thumb.
  * **hiddenInput** : The hidden input element that is used to handle the switch state.
  * **thumb** : The thumb element of the switch. It is the circle element.
  * **label** : The label slot of the switch.
  * **startContent** : The icon slot at the start of the switch.
  * **endContent** : The icon slot at the end of the switch.
  * **thumbIcon** : The icon slot inside the thumb.


### Custom Styles
You can customize the `Switch` component by passing custom Tailwind CSS classes to the component slots.
Preview
Code
### Custom Implementation
In case you need to customize the switch even further, you can use the `useSwitch` hook to create your own implementation.
Preview
Code
## Data Attributes
`Switch` has the following attributes on the `base` element:
  * **data-selected** : When the switch is checked. Based on `isSelected` prop.
  * **data-pressed** : When the switch is pressed. Based on usePress
  * **data-readonly** : When the switch is readonly. Based on `isReadOnly` prop.
  * **data-hover** : When the switch is being hovered. Based on useHover
  * **data-focus** : When the switch is being focused. Based on useFocusRing.
  * **data-focus-visible** : When the switch is being focused with the keyboard. Based on useFocusRing.
  * **data-disabled** : When the switch is disabled. Based on `isDisabled` prop.


## Accessibility
  * Built with a native HTML `<input>` element.
  * Full support for browser features like form autofill.
  * Keyboard focus management and cross browser normalization.
  * Keyboard event support for `Tab` and `Space` keys.
  * Labeling support for assistive technology.
  * Exposed as a switch to assistive technology via ARIA


## API
### Switch Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode`  
`value`| `string`  
`name`| `string`  
`size`| `sm | md | lg`| `"md"`  
`color`| `default | primary | secondary | success | warning | danger`| `"primary"`  
`thumbIcon`| `ThumbIconProps`  
`startContent`| `ReactNode`  
`endContent`| `ReactNode`  
`isSelected`| `boolean`  
`defaultSelected`| `boolean`  
`isReadOnly`| `boolean`  
`isDisabled`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<"base"｜ "wrapper"｜ "thumb"｜ "label" ｜ "startContent" ｜ "endContent" ｜ "thumbIcon" , string>>`  
### Switch Events
Prop| Type| Default  
---|---|---  
`onChange`| `React.ChangeEvent<HTMLInputElement>`  
`onValueChange`| `(isSelected: boolean) => void`  
### Types
#### Switch Icon Props
SpinnerTable
On this page
  * Installation
  * Import
  * Usage
  * With Label
  * Disabled
  * Sizes
  * Colors
  * With Thumb Icon
  * With Icons
  * Controlled
  * Slots
  * Custom Styles
  * Custom Implementation
  * Data Attributes
  * Accessibility
  * API
  * Switch Props
  * Switch Events
  * Types
  * Switch Icon Props
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
