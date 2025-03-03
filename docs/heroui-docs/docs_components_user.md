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


# User
Display user information with avatar and name.
Storybook@heroui/userSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add user

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
Individual
Global
## Usage
Preview
Code
![avatar](https://i.pravatar.cc/150?u=a04258114e29026702d)
Jane DoeProduct Designer
> **Note** : See the Avatar component for more details about `avatarProps`.
### Link Description
Preview
Code
![avatar](https://avatars.githubusercontent.com/u/30373425?v=4)
Junior Garcia@jrgarciadev
## Slots
  * **base** : The base slot of the user, it is the main container.
  * **wrapper** : The name and description wrapper.
  * **name** : The name of the user.
  * **description** : The description of the user.


## Data Attributes
`User` has the following attributes on the `root` element only when `isFocusable` is `true`:
  * **data-focus** : When the user is being focused. Based on useFocusRing
  * **data-focus-visible** : When the user is being focused with the keyboard. Based on useFocusRing


## API
### User Props
Prop| Type| Default  
---|---|---  
`name`| `string`  
`description`| `ReactNode`  
`isFocusable`| `boolean`| `false`  
`avatarProps`| `AvatarProps`  
`classNames`| `Partial<Record<"base" | "wrapper" | "name" | "description", string>>`  
TooltipAPI References: HeroUI CLI
On this page
  * Installation
  * Import
  * Usage
  * Link Description
  * Slots
  * Data Attributes
  * API
  * User Props
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
