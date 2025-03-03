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


# Badge
Badges are used as a small numerical value or status descriptor for UI elements.
Storybook@heroui/badgeSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add badge

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
Individual
Global
## Usage
Preview
Code
### Sizes
Preview
Code
### Colors
Preview
Code
### Variants
Preview
Code
### Placements
Preview
Code
### Shapes
For a better positioning, you can use the `shape` property to define the shape of the badge.
Preview
Code
### Badge Visibility
You can control the visibility of the badge by using the `isInvisible` property.
Preview
Code
### Content Examples
Preview
Code
### Disable Outline
By default, the badge has an outline, you can disable it by using the `showOutline={false}` property.
Preview
Code
### Accessibility
It's not advisable to depend on the badge's content for accurate announcement. Instead, consider supplying a comprehensive description, such as using `aria-label`.
Preview
Code
## Slots
The Badge component has two slots:
  * **base** : The base slot for the badge, which is the container of the badge.
  * **badge** : The main slot for the badge content, which is the content of the badge.


## API
### Badge Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode`  
`content`| `string | number | ReactNode`  
`variant`| `solid | flat | faded | shadow`| `"solid"`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`size`| `sm | md | lg`| `"md"`  
`shape`| `circle | rectangle`| `"rectangle"`  
`placement`| `top-right | top-left | bottom-right | bottom-left`| `"top-right"`  
`showOutline`| `boolean`| `true`  
`disableOutline`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
`isInvisible`| `boolean`| `false`  
`isOneChar`| `boolean`| `false`  
`isDot`| `boolean`| `false`  
`classNames`| `Partial<Record<"base"｜"badge", string>>`  
AvatarBreadcrumbs
On this page
  * Installation
  * Import
  * Usage
  * Sizes
  * Colors
  * Variants
  * Placements
  * Shapes
  * Badge Visibility
  * Content Examples
  * Disable Outline
  * Accessibility
  * Slots
  * API
  * Badge Props
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
