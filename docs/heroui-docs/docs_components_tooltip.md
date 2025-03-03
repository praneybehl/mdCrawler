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


# Tooltip
Tooltips display a brief, informative message that appears when a user interacts with an element.
Storybook@heroui/tooltipReact AriaSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add tooltip

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
Individual
Global
> For individual installation, please note that you should add `./node_modules/@heroui/theme/dist/components/popover.js` to your `tailwind.config.js` file instead since tooltip reuses popover styles.
## Usage
Preview
Code
### With Arrow
Preview
Code
### Colors
Preview
Code
### Placements
Preview
Code
### Offset
Preview
Code
### Controlled
Preview
Code
### With Delay
You can control the `open` and `close` delay of the tooltip with `delay` and `closeDelay` props.
Preview
Code
Hovering over the second button shows the tooltip immediately. If you wait for a delay before hovering another element, the delay restarts.
Preview
Code
### Custom Content
Preview
Code
### Custom Motion
Tooltip offers a `motionProps` property to customize the `enter` / `exit` animation.
Preview
Code
> Learn more about Framer motion variants here.
## Slots
  * **base** : The main tooltip slot, it wraps the tooltip content.
  * **arrow** : The arrow slot, it wraps the tooltip arrow, the placement of the arrow is based on the tooltip placement, e.g. `data-[placement=top]:...`.


### Custom Styles
You can customize the `Tooltip` component by passing custom Tailwind CSS classes to the component slots.
Preview
Code
## Data Attributes
`Tooltip` has the following attributes on the `base` element:
  * **data-open** : When the tooltip is open. Based on tooltip state.
  * **data-placement** : The placement of the tooltip. Based on `placement` prop. The arrow element is positioned based on this attribute.
  * **data-disabled** : When the tooltip is disabled. Based on `isDisabled` prop.


## Accessibility
  * Keyboard focus management and cross browser normalization.
  * Hover management and cross browser normalization.
  * Labeling support for screen readers (aria-describedby).
  * Exposed as a tooltip to assistive technology via ARIA.
  * Matches native tooltip behavior with delay on hover of first tooltip and no delay on subsequent tooltips.


## API
### Tooltip Props
Prop| Type| Default  
---|---|---  
`children*`| `ReactNode[]`  
`content`| `ReactNode`  
`size`| `sm | md | lg`| `"md"`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`radius`| `none | sm | md | lg | full`| `"md"`  
`shadow`| `none | sm | md | lg`| `"sm"`  
`placement`| `TooltipPlacement`| `"top"`  
`delay`| `number`| `"0"`  
`closeDelay`| `number`| `"500"`  
`isOpen`| `boolean`  
`defaultOpen`| `boolean`  
`offset`| `number`| `"7"`  
`containerPadding`| `number`| `"12"`  
`crossOffset`| `number`| `"0"`  
`showArrow`| `boolean`| `false`  
`shouldFlip`| `boolean`| `true`  
`triggerScaleOnOpen`| `boolean`| `true`  
`isKeyboardDismissDisabled`| `boolean`| `false`  
`isDismissable`| `boolean`| `false`  
`shouldCloseOnBlur`| `boolean`| `true`  
`motionProps`| `MotionProps`  
`portalContainer`| `HTMLElement`| `"document.body"`  
`updatePositionDeps`| `any[]`| `"[]"`  
`isDisabled`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<"base"｜"content", string>>`  
### Tooltip Events
Prop| Type| Default  
---|---|---  
`onOpenChange`| `(isOpen: boolean) => void`  
`shouldCloseOnInteractOutside`| `(e: HTMLElement) => void`  
`onClose`| `() => void`  
### Tooltip types
#### Tooltip Placement
#### Motion Props
Time InputUser
On this page
  * Installation
  * Import
  * Usage
  * With Arrow
  * Colors
  * Placements
  * Offset
  * Controlled
  * With Delay
  * Custom Content
  * Custom Motion
  * Slots
  * Custom Styles
  * Data Attributes
  * Accessibility
  * API
  * Tooltip Props
  * Tooltip Events
  * Tooltip types
  * Tooltip Placement
  * Motion Props
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
