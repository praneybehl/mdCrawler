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


# Avatar
The Avatar component is used to represent a user, and displays the profile picture, initials or fallback icon.
Storybook@heroui/avatarSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
HeroUI exports 3 avatar-related components:
  * **Avatar** : The main component to display an avatar.
  * **AvatarGroup** : A wrapper component to display a group of avatars.
  * **AvatarIcon** : The default icon used as fallback when the image fails to load.


Individual
Global
## Usage
Preview
Code
### Sizes
Preview
Code
### Disabled
Preview
Code
### Bordered
Preview
Code
### Radius
Preview
Code
### Colors
Preview
Code
### Avatar Fallbacks
If there is an error loading the `src` of the avatar, there are 2 fallbacks:
  * If there's a `name` prop, we use it to generate the initials and a random, accessible background color.
  * If there's no `name` prop, we use a default avatar.


If the `showFallback` is not passed, the fallbacks will not be displayed.
Preview
Code
### Custom Fallback
You can also provide a custom fallback component to be displayed when the `src` fails to load.
Preview
Code
### Custom Implementation
In case you need to customize the avatar even further, you can use the `useAvatar` hook to create your own implementation.
### Custom initials logic
It is possible to customize the logic used to generate the initials by passing a function to the `getInitials` prop. By default we merge the first characters of each word in the `name` prop.
## Avatar Group
Preview
Code
### Group Disabled
Preview
Code
### Group Max Count
You can limit the number of avatars displayed by passing the `max` prop to the `AvatarGroup` component.
Preview
Code
### Group Total Count
You can display the total number of avatars by passing the `total` prop to the `AvatarGroup` component.
Preview
Code
### Group Custom count
`AvatarGroup` provides a `renderCount` prop to customize the count displayed when the `total` prop is passed.
Preview
Code
### Group Grid
By passing the `isGrid` prop to the `AvatarGroup` component, the avatars will be displayed in a grid layout.
Preview
Code
### Group Custom Implementation
In case you need to customize the avatar group even further, you can use the `useAvatarGroup` hook and the `AvatarGroupProvider` to create your own implementation.
## Slots
  * **base** : Avatar wrapper, it includes styles for focus ring, position, and general appearance.
  * **img** : Image element within the avatar, it includes styles for opacity transition and size.
  * **fallback** : Fallback content when the image fails to load or is not provided, it includes styles for centering the content.
  * **name** : Initials displayed when the image is not provided or fails to load, it includes styles for font, text alignment, and inheritance.
  * **icon** : Icon element within the avatar, it includes styles for centering the content, text inheritance, and size.


### Custom Avatar Styles
You can customize any part of the avatar by using the `classNames` prop, each `slot` has its own `className`.
Preview
Code
## Data Attributes
`Avatar` has the following attributes on the `base` element:
  * **data-hover** : When the avatar is being hovered. Based on useHover
  * **data-focus** : When the avatar is being focused. Based on useFocusRing, it is applied when `isFocusable` is `true` or when the `as` property is assigned as `button`.
  * **data-focus-visible** : When the avatar is being focused with the keyboard. Based on useFocusRing, it is applied when `isFocusable` is `true` or when the `as` property is assigned as `button`.


## API
### Avatar Props
Prop| Type| Default  
---|---|---  
`src`| `string`  
`color`| `default | primary | secondary | success | warning | danger`| `"default"`  
`radius`| `none | sm | md | lg | full`| `"full"`  
`size`| `sm | md | lg`| `"md"`  
`name`| `string`  
`icon`| `ReactNode`  
`fallback`| `ReactNode`  
`isBordered`| `boolean`| `false`  
`isDisabled`| `boolean`| `false`  
`isFocusable`| `boolean`| `false`  
`showFallback`| `boolean`| `false`  
`ImgComponent`| `React.ElementType`| `"img"`  
`imgProps`| `ImgComponentProps`  
`classNames`| `Partial<Record<"base" | "img" | "fallback" | "name" | "icon", string>>`  
### Avatar Group Props
Prop| Type| Default  
---|---|---  
`max`| `number`| `"5"`  
`total`| `number`  
`size`| `AvatarProps['size']`  
`color`| `AvatarProps['color']`  
`radius`| `AvatarProps['radius']`  
`isGrid`| `boolean`| `false`  
`isDisabled`| `boolean`  
`isBordered`| `boolean`  
`renderCount`| `(count: number) => ReactNode`  
`classNames`| `Partial<Record<"base" | "count", string>>`  
AlertBadge
On this page
  * Installation
  * Import
  * Usage
  * Sizes
  * Disabled
  * Bordered
  * Radius
  * Colors
  * Avatar Fallbacks
  * Custom Fallback
  * Custom Implementation
  * Custom initials logic
  * Avatar Group
  * Group Disabled
  * Group Max Count
  * Group Total Count
  * Group Custom count
  * Group Grid
  * Group Custom Implementation
  * Slots
  * Custom Avatar Styles
  * Data Attributes
  * API
  * Avatar Props
  * Avatar Group Props
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
