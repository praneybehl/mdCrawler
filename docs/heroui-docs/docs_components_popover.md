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


# Popover
Popover is a **non-modal** dialog that floats around its disclosure. It's commonly used for displaying additional rich content on top of something.
Storybook@heroui/popoverReact AriaSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add popover

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
HeroUI exports 3 popover-related components:
  * **Popover** : The main component to display a popover.
  * **PopoverTrigger** : The component that triggers the popover.
  * **PopoverContent** : The component that contains the popover content.


Individual
Global
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
### Title Props
To be sure that the popover exposes the correct title to assistive technologies, you should use the `titleProps` prop on the `PopoverContent` component. To use this prop, you must pass a function as a child.
Preview
Code
### With Form
The `Popover` handles the focus within the popover content. It means that you can use the popover with form elements without any problem. the focus returns to the trigger when the popover closes.
Preview
Code
> **Note** : You can add the `autoFocus` prop to the first `Input` component to focus it when the popover opens.
### Backdrop
The `Popover` component has a `backdrop` prop to show a backdrop behind the popover. The backdrop can be either `transparent`, `opaque` or `blur`. The default value is `transparent`.
Preview
Code
### Custom Motion
Popover offers a `motionProps` property to customize the `enter` / `exit` animation.
Preview
Code
> Learn more about Framer motion variants here.
### Custom Trigger
Preview
Code
## Slots
  * **base** : The main popover slot, it wraps the popover content and contains the arrow as a pseudo-element (::before).
  * **trigger** : The popover trigger slot, it has small styles to ensure the trigger works correctly.
  * **backdrop** : The backdrop slot, it contains the backdrop styles.
  * **content** : The content slot, it contains the popover content.


### Custom Styles
You can customize the `Popover` component by passing custom Tailwind CSS classes to the component slots.
Preview
Code
## Data Attributes
`Popover` has the following attributes on the `PopoverContent` element:
  * **data-open** : When the popover is open. Based on popover state.
  * **data-placement** : The placement of the popover. Based on `placement` prop. The arrow element is positioned based on this attribute.
  * **data-focus** : When the popover is being focused. Based on useFocusRing.
  * **data-focus-visible** : When the popover is being focused with the keyboard. Based on useFocusRing.


## Accessibility
  * The trigger and popover are automatically associated semantically via ARIA.
  * Content outside the popover is hidden from assistive technologies while it is open.
  * The popover closes when interacting outside, or pressing the `Escape` key.
  * Focus is moved into the popover on mount, and restored to the trigger element on unmount.
  * The popover is positioned relative to the trigger element, and automatically flips and adjusts to avoid overlapping with the edge of the browser window.
  * Scrolling is prevented outside the popover to avoid unintentionally repositioning or closing it.


## API
### Popover Props
Prop| Type| Default  
---|---|---  
`children*`| `ReactNode[]`  
`size`| `sm | md | lg`| `"md"`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`radius`| `none | sm | md | lg | full`| `"lg"`  
`shadow`| `none | sm | md | lg`| `"lg"`  
`backdrop`| `transparent | opaque | blur`| `"transparent"`  
`placement`| `PopoverPlacement`| `"bottom"`  
`state`| `OverlayTriggerState`  
`isOpen`| `boolean`  
`defaultOpen`| `boolean`  
`offset`| `number`| `"7"`  
`containerPadding`| `number`| `"12"`  
`crossOffset`| `number`| `"0"`  
`triggerType`| `dialog | menu | listbox | tree | grid`| `"dialog"`  
`showArrow`| `boolean`| `false`  
`shouldFlip`| `boolean`| `true`  
`triggerScaleOnOpen`| `boolean`| `true`  
`shouldBlockScroll`| `boolean`| `false`  
`shouldCloseOnScroll`| `boolean`| `false`  
`isKeyboardDismissDisabled`| `boolean`| `false`  
`shouldCloseOnBlur`| `boolean`| `false`  
`motionProps`| `MotionProps`  
`portalContainer`| `HTMLElement`| `"document.body"`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<'base' | 'trigger' | 'backdrop' | 'content', string>>`  
### Popover Events
Prop| Type| Default  
---|---|---  
`onOpenChange`| `(isOpen: boolean) => void`  
`shouldCloseOnInteractOutside`| `(e: HTMLElement) => void`  
`onClose`| `() => void`  
### PopoverTrigger Props
Prop| Type| Default  
---|---|---  
`children*`| `ReactNode`  
### PopoverContent Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode`  
### Popover types
#### Popover Placement
#### Motion Props
PaginationProgress
On this page
  * Installation
  * Import
  * Usage
  * With Arrow
  * Colors
  * Placements
  * Offset
  * Controlled
  * Title Props
  * With Form
  * Backdrop
  * Custom Motion
  * Custom Trigger
  * Slots
  * Custom Styles
  * Data Attributes
  * Accessibility
  * API
  * Popover Props
  * Popover Events
  * PopoverTrigger Props
  * PopoverContent Props
  * Popover types
  * Popover Placement
  * Motion Props
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
