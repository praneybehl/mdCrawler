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


# Keyboard Key
Keyboard key is a component to display which key or combination of keys performs a given action.
Storybook@heroui/kbdServer componentSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add kbd

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
Individual
Global
## Usage
Preview
Code
`⌘K`
### Keys
Preview
Code
`⌘K``⌘⇧N``⌥⌘P`
> **Note** : Check the API section to see all available keys.
## Slots
  * **base** : Kbd wrapper, it handles alignment, placement, and general appearance.
  * **abbr** : The `keys` wrapper that handles the appearance of the keys.
  * **content** : The children wrapper that handles the appearance of the content.


## Accessibility
  * Each command `key` has a `title` attribute that describes the action that the key performs.


## API
### Keyboard Key Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode`  
`keys`| `KbdKey | KbdKey[]`  
`classNames`| `Partial<Record<"base" | "abbr" | "content", string>>`  
### Keyboard Keys
List of supported keys.
Input OTPLink
On this page
  * Installation
  * Import
  * Usage
  * Keys
  * Slots
  * Accessibility
  * API
  * Keyboard Key Props
  * Keyboard Keys
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
  *[⌘]: Command
  *[⇧]: Shift
  *[⌥]: Option
