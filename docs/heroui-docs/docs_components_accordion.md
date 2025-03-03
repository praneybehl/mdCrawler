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


# Accordion
Accordion display a list of high-level options that can expand/collapse to reveal more information.
Storybook@heroui/accordionSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
HeroUI exports 2 accordion-related components:
  * **Accordion** : The main component to display a list of accordion items.
  * **AccordionItem** : The item component to display a single accordion item.


Individual
Global
## Usage
Preview
Code
### With Subtitle
Preview
Code
### Expand multiple items
If you set `selectionMode` to `multiple`, then the `Accordion` will allow multiple items to be expanded at the same time.
Preview
Code
### Compact
If you set `isCompact` to `true`, the `Accordion` will be displayed in a compact style.
Preview
Code
### Variants
Accordion has 4 variants: `light`, `shadow`, `bordered` and `splitted`.
#### Light variant
Preview
Code
#### Shadow variant
Preview
Code
#### Bordered variant
Preview
Code
#### Splitted variant
Preview
Code
### Default expanded keys
If you want to expand some items by default, you can set the `defaultExpandedKeys` property to an array of keys.
Preview
Code
### Disabled keys
If you want to disable some items, you can set the `disabledKeys` property to an array of keys.
Preview
Code
### Start content
If you want to display some content before the accordion items, you can set the `startContent` property.
Preview
Code
### Custom Indicator
Accordion items have a property called `indicator`. You can use it to customize the open/close indicator.
Preview
Code
The indicator can be also a `function`, which receives the `isOpen`, `isDisabled` and the default `indicator` as parameters.
Preview
Code
### Custom Motion
Accordion offers a `motionProps` property to customize the `enter` / `exit` animation.
Preview
Code
> Learn more about Framer motion variants here.
### Controlled
Accordion is a controlled component, which means you need to control the `selectedKeys` property by yourself.
Preview
Code
## Accordion Item Slots
  * **base** : The accordion item wrapper.
  * **heading** : The accordion item heading. It contains the `indicator` and the `title`.
  * **trigger** : The button that open/close the accordion item.
  * **titleWrapper** : The wrapper of the `title` and `subtitle`.
  * **title** : The accordion item title.
  * **subtitle** : The accordion item subtitle.
  * **startContent** : The content before the accordion item.
  * **indicator** : The element that indicates the open/close state of the accordion item.
  * **content** : The accordion item content.


### Custom Accordion Styles
You can customize the accordion and accordion items styles by using any of the following properties:
  * `className`: The class name of the accordion. Modify the accordion wrapper styles.(Accordion)
  * `itemClasses`: The class names of the accordion items. Modify all accordion items styles at once. (Accordion)
  * `classNames`: The class names of the accordion items. Modify each accordion item styles separately. (AccordionItem)


Here's an example of how to customize the accordion styles:
Preview
Code
## Data Attributes
`AccordionItem` has the following attributes on the `base` element:
  * **data-open** : Whether the accordion item is open.
  * **data-disabled** : When the accordion item is disabled.
  * **data-hover** : When the accordion item is being hovered. Based on useHover.
  * **data-focus** : When the accordion item is being focused. Based on useFocusRing.
  * **data-focus-visible** : When the accordion item is being focused with the keyboard. Based on useFocusRing.
  * **data-disabled** : When the accordion item is disabled. Based on `isDisabled` prop.
  * **data-pressed** : When the accordion item is pressed. Based on usePress.


## Accessibility
  * Keyboard event support for `Space`, `Enter`, `Arrow Up`, `Arrow Down` and `Home` / `End` keys.
  * Keyboard focus management and cross browser normalization.
  * `aria-expanded` attribute for the accordion item.
  * `aria-disabled` attribute for the accordion item.
  * `aria-controls` attribute for the accordion item.


## API
### Accordion Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode | ReactNode[]`  
`variant`| `light | shadow | bordered | splitted`| `"light"`  
`selectionMode`| `none | single | multiple`  
`selectionBehavior`| `toggle | replace`| `"toggle"`  
`isCompact`| `boolean`| `false`  
`isDisabled`| `boolean`| `false`  
`showDivider`| `boolean`| `true`  
`dividerProps`| `DividerProps`  
`hideIndicator`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
`disableIndicatorAnimation`| `boolean`| `false`  
`disallowEmptySelection`| `boolean`| `false`  
`keepContentMounted`| `boolean`| `false`  
`fullWidth`| `boolean`| `true`  
`motionProps`| `MotionProps`  
`disabledKeys`| `React.Key[]`  
`itemClasses`| `AccordionItemClassnames`  
`selectedKeys`| `all | React.Key[]`  
`defaultSelectedKeys`| `all | React.Key[]`  
### Accordion Events
Prop| Type| Default  
---|---|---  
`onSelectionChange`| `(keys: "all" | Set<React.Key>) => any`  
### Accordion Item Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode`  
`title`| `ReactNode`  
`subtitle`| `ReactNode`  
`indicator`| `IndicatorProps`  
`startContent`| `ReactNode`  
`motionProps`| `MotionProps`  
`isCompact`| `boolean`| `false`  
`isDisabled`| `boolean`| `false`  
`keepContentMounted`| `boolean`| `false`  
`hideIndicator`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
`disableIndicatorAnimation`| `boolean`| `false`  
`HeadingComponent`| `React.ElementType`| `"h2"`  
`classNames`| `AccordionItemClassnames`  
### Accordion Item Events
Prop| Type| Default  
---|---|---  
`onFocus`| `(e: FocusEvent) => void`  
`onBlur`| `(e: FocusEvent) => void`  
`onFocusChange`| `(isFocused: boolean) => void`  
`onKeyDown`| `(e: KeyboardEvent) => void`  
`onKeyUp`| `(e: KeyboardEvent) => void`  
`onPress`| `(e: PressEvent) => void`  
`onPressStart`| `(e: PressEvent) => void`  
`onPressEnd`| `(e: PressEvent) => void`  
`onPressChange`| `(isPressed: boolean) => void`  
`onPressUp`| `(e: PressEvent) => void`  
`onClick`| `MouseEventHandler`  
### Types
#### Accordion Item Indicator Props
### Accordion Item classNames
#### Motion Props
Customization: Custom variantsAutocomplete
On this page
  * Installation
  * Import
  * Usage
  * With Subtitle
  * Expand multiple items
  * Compact
  * Variants
  * Light variant
  * Shadow variant
  * Bordered variant
  * Splitted variant
  * Default expanded keys
  * Disabled keys
  * Start content
  * Custom Indicator
  * Custom Motion
  * Controlled
  * Accordion Item Slots
  * Custom Accordion Styles
  * Data Attributes
  * Accessibility
  * API
  * Accordion Props
  * Accordion Events
  * Accordion Item Props
  * Accordion Item Events
  * Types
  * Accordion Item Indicator Props
  * Accordion Item classNames
  * Motion Props
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
