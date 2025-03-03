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


# Navbar
A responsive navigation header positioned on top side of your page that includes support for branding, links, navigation, collapse menu and more.
Storybook@heroui/navbarSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add navbar

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
HeroUI exports 7 navbar-related components:
  * **Navbar** : The main component of navbar.
  * **NavbarBrand** : The component for branding.
  * **NavbarContent** : The component for wrapping navbar items.
  * **NavbarItem** : The component for navbar item.
  * **NavbarMenuToggle** : The component for toggling navbar menu.
  * **NavbarMenu** : The component for wrapping navbar menu items.
  * **NavbarMenuItem** : The component for navbar menu item.


Individual
Global
## Usage
Preview
Code
### Static
You can use the `position` prop to make the navbar static positioned (the default behavior is `sticky`).
Preview
Code
### Hide on scroll
It is possible to hide the navbar on scroll by using the `shouldHideOnScroll` prop.
Preview
Code
### With Menu
You can use the `NavbarMenuToggle` and `NavbarMenu` components to display a togglable menu.
Preview
Code
If you want to remove the `open` / `close` animation, you can pass the `disableAnimation={true}` prop to `Navbar` component.
Preview
Code
### Controlled Menu
You can use the `isMenuOpen` and `onMenuOpenChange` props to control the navbar menu state.
Preview
Code
### With Border
You can use the `isBordered` prop to add a bottom border to the navbar.
Preview
Code
### Disabling Blur
Navbar has a blur effect by default. You can disable it by using the `isBlurred=false` prop.
Preview
Code
### With Dropdown Menu
It is possible to use the Dropdown component to display a dropdown menu as navbar item.
Preview
Code
### With Avatar
Example of a navbar with avatar and dropdown menu.
Preview
Code
### With Search Input
Example of a navbar with search input.
Preview
Code
### Customizing the active item
When the `NavbarItem` is active, it will have a `data-active` attribute. You can use this attribute to customize it.
Preview
Code
## Slots
  * **base** : The main slot for the navbar. It takes the full width of the parent and wraps the navbar elements including the menu.
  * **wrapper** : The slot that contains the navbar elements such as `brand`, `content` and `toggle`.
  * **brand** : The slot for the `NavbarBrand` component.
  * **content** : The slot for the `NavbarContent` component.
  * **item** : The slot for the `NavbarItem` component.
  * **toggle** : The slot for the `NavbarMenuToggle` component.
  * **toggleIcon** : The slot for the `NavbarMenuToggle` icon.
  * **menu** : The slot for the `NavbarMenu` component.
  * **menuItem** : The slot for the `NavbarMenuItem` component.


## Data Attributes
`Navbar` has the following attributes on the `base` element:
  * **data-menu-open** : Indicates if the navbar menu is open.
  * **data-hidden** : Indicates if the navbar is hidden. It is used when the `shouldHideOnScroll` prop is `true`.


`NavbarContent`
  * **data-justify** : The justify content of the navbar content. It takes into account the correct space distribution.


`NavbarItem` has the following attributes on the `base` element:
  * **data-active** : Indicates if the navbar item is active. It is used when the `isActive` prop is `true`.


`NavbarMenuToggle` has the following attributes on the `base` element:
  * **data-open** : Indicates if the navbar menu is open. It is used when the `isMenuOpen` prop is `true`.
  * **data-pressed** : When the navbar menu toggle is pressed. Based on usePress
  * **data-hover** : When the navbar menu toggle is being hovered. Based on useHover
  * **data-focus-visible** : When the navbar menu toggle is being focused with the keyboard. Based on useFocusRing.


`NavbarMenuItem` has the following attributes on the `base` element:
  * **data-active** : Indicates if the menu item is active. It is used when the `isActive` prop is `true`.


## API
### Navbar Props
Prop| Type| Default  
---|---|---  
`children*`| `ReactNode[]`  
`height`| `string | number`| `"4rem (64px)"`  
`position`| `static | sticky`| `"sticky"`  
`maxWidth`| `sm | md | lg | xl | 2xl | full`| `"lg"`  
`parentRef`| `React.RefObject<HTMLElement>`| `"window"`  
`isBordered`| `boolean`| `false`  
`isBlurred`| `boolean`| `true`  
`isMenuOpen`| `boolean`| `false`  
`isMenuDefaultOpen`| `boolean`| `false`  
`shouldHideOnScroll`| `boolean`| `false`  
`motionProps`| `MotionProps`  
`disableScrollHandler`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
`classNames`| `Partial<Record<'base' | 'wrapper' | 'brand' | 'content' | 'item' | 'toggle' | 'toggleIcon' | 'menu' | 'menuItem', string>>`  
### Navbar Events
Prop| Type| Default  
---|---|---  
`onMenuOpenChange`| `(isOpen: boolean) => void`  
`onScrollPositionChange`| `(position: number) => void`  
### NavbarContent Props
Prop| Type| Default  
---|---|---  
`children*`| `ReactNode[]`  
`justify`| `start | center | end`| `"start"`  
### NavbarItem Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode`  
`isActive`| `boolean`| `false`  
### NavbarMenuToggle Props
Prop| Type| Default  
---|---|---  
`icon`| `ReactNode | ((isOpen: boolean | undefined) => ReactNode)`  
`isSelected`| `boolean`| `false`  
`defaultSelected`| `boolean`| `false`  
`srOnlyText`| `string`| `"open/close navigation menu"`  
### NavbarMenuToggle Events
Prop| Type| Default  
---|---|---  
`onChange`| `(isOpen: boolean) => void`  
### NavbarMenu Props
Prop| Type| Default  
---|---|---  
`children*`| `ReactNode[]`  
`portalContainer`| `HTMLElement`| `"document.body"`  
`motionProps`| `MotionProps`  
### NavbarMenuItem Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode`  
`isActive`| `boolean`| `false`  
### Types
ModalNumber Input
On this page
  * Installation
  * Import
  * Usage
  * Static
  * Hide on scroll
  * With Menu
  * Controlled Menu
  * With Border
  * Disabling Blur
  * With Dropdown Menu
  * With Avatar
  * With Search Input
  * Customizing the active item
  * Slots
  * Data Attributes
  * API
  * Navbar Props
  * Navbar Events
  * NavbarContent Props
  * NavbarItem Props
  * NavbarMenuToggle Props
  * NavbarMenuToggle Events
  * NavbarMenu Props
  * NavbarMenuItem Props
  * Types
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
