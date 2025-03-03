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


# Tabs
Tabs organize content into multiple sections and allow users to navigate between them.
Storybook@heroui/tabsReact AriaSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add tabs

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
HeroUI exports 2 tabs-related components:
  * **Tabs** : The main component to display a tab list.
  * **Tab** : The component to display a tab item. The children of this component will be displayed as the content of the tab.


Individual
Global
## Usage
Preview
Code
### Dynamic
You can render tabs dynamically by using `items` prop.
Preview
Code
### Disabled
Preview
Code
### Disabled Item
Preview
Code
### Sizes
Preview
Code
### Radius
Preview
Code
### Colors
Preview
Code
### Variants
Preview
Code
### With Icons
Preview
Code
### Controlled
You can use the `onSelectionChange` and `selectedKey` props to control the selected tab.
Preview
Code
### Placement
You can change the position of the tabs by using the `placement` prop. The default value is `top`.
Preview
Code
### Vertical
Change the orientation of the tabs it will invalidate the placement prop when the value is `true`.
Preview
Code
### Links
Tabs items can be rendered as links by passing the `href` prop to the `Tab` component. By default, links perform native browser navigation. However, you'll usually want to synchronize the selected tab with the current URL from your client side router. You can do this by doing the following:
  1. Set up your router at the root of your app. See Routing guide to learn how to do this.
  2. Use the `selectedKey` prop to set the selected tab based on the current URL.


#### Next.js
This example uses Next.js App router to set up routes for each tab and synchronize the selected tab with the current URL.
#### React Router
This example uses React Router to setup routes for each tab and synchronize the selection with the URL.
> **Note** : See the Routing guide to learn how to set up the router for your framework.
### With Form
Preview
Code
## Slots
  * **base** : The main tabs slot, it wraps the items and the panels.
  * **tabList** : The tab list slot, it wraps the tab items.
  * **tab** : The tab slot, it wraps the tab item.
  * **tabContent** : The tab content slot, it wraps the tab content.
  * **cursor** : The cursor slot, it wraps the cursor. This is only visible when `disableAnimation=false`
  * **panel** : The panel slot, it wraps the tab panel (content).
  * **tabWrapper** : The tab wrapper slot, it wraps the tab and the tab content.


### Custom Styles
You can customize the `Tabs` component by passing custom Tailwind CSS classes to the component slots.
Preview
Code
## Data Attributes
`Tab` has the following attributes on the `base` element:
  * **data-selected** : When the tab is selected.
  * **data-disabled** : When the tab is disabled.
  * **data-hover** : When the tab is being hovered. Based on useHover.
  * **data-hover-selected** : When the tab is being hovered and is not selected. Based on useHover and `selected` state.
  * **data-focus** : When the tab is being focused. Based on useFocusRing.
  * **data-focus-visible** : When the tab is being focused with the keyboard. Based on useFocusRing.
  * **data-pressed** : When the tab is pressed. Based on usePress.


## Accessibility
  * Support for mouse, touch, and keyboard interactions on tabs.
  * Keyboard event support for arrows keys.
  * Support for disabled tabs.
  * Follows the tabs ARIA pattern, semantically linking tabs and their associated tab panels.
  * Focus management for tab panels without any focusable children.


## API
### Tabs Props
Prop| Type| Default  
---|---|---  
`children*`| `ReactNode | ((item: T) => ReactElement)`  
`variant`| `solid | bordered | light | underlined`| `"solid"`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`size`| `sm | md | lg`| `"md"`  
`radius`| `none | sm | md | lg | full`  
`fullWidth`| `boolean`| `false`  
`items`| `Iterable<T>`  
`disabledKeys`| `React.Key[]`  
`selectedKey`| `React.Key`  
`defaultSelectedKey`| `React.Key`  
`shouldSelectOnPressUp`| `boolean`| `true`  
`keyboardActivation`| `automatic | manual`| `"automatic"`  
`motionProps`| `MotionProps`  
`disableCursorAnimation`| `boolean`| `false`  
`isDisabled`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<"base"｜ "tabList"｜ "tab"｜ "tabContent"｜ "cursor" ｜ "panel" ｜ "tabWrapper", string>>`  
`placement`| `top | bottom | start | end`| `"top"`  
`isVertical`| `boolean`| `false`  
`destroyInactiveTabPanel`| `boolean`| `true`  
### Tabs Events
Prop| Type| Default  
---|---|---  
`onSelectionChange`| `(key: React.Key) => any`  
### Tab Props
Prop| Type| Default  
---|---|---  
`tabRef`| `RefObject<HTMLButtonElement>`  
`children*`| `ReactNode`  
`title`| `ReactNode`  
`titleValue`| `string`  
`href`| `string`  
`target`| `HTMLAttributeAnchorTarget`  
`rel`| `string`  
`download`| `boolean | string`  
`ping`| `string`  
`referrerPolicy`| `HTMLAttributeReferrerPolicy`  
`shouldSelectOnPressUp`| `boolean`  
TableToast
On this page
  * Installation
  * Import
  * Usage
  * Dynamic
  * Disabled
  * Disabled Item
  * Sizes
  * Radius
  * Colors
  * Variants
  * With Icons
  * Controlled
  * Placement
  * Vertical
  * Links
  * Next.js
  * React Router
  * With Form
  * Slots
  * Custom Styles
  * Data Attributes
  * Accessibility
  * API
  * Tabs Props
  * Tabs Events
  * Tab Props
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
