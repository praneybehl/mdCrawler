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


# Image
The Image component is used to display images with support for fallback.
Storybook@heroui/imageSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add image

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
Individual
Global
## Usage
Preview
Code
### Blurred
You can use the `isBlurred` prop to duplicate the image and blur it to create a blurred effect.
Preview
Code
### Zoomed
You can use the `isZoomed` prop make the image zoomed when hovered.
Preview
Code
### Animated Loading
Image component has a built-in `skeleton` animation to indicate the image is loading and an `opacity` animation when the image loads.
Preview
Code
> **Note** : The `URL` uses `https://app.requestly.io/delay` to simulate a slow network.
### Image with fallback
You can use the `fallbackSrc` prop to display a fallback image when:
  * The `fallbackSrc` prop is provided.
  * The image provided in `src` is still loading.
  * The image provided in `src` fails to load.
  * The image provided in `src` is not found.


Preview
Code
### With Next.js Image
Next.js provides an optimized Image component, you can use it with HeroUI `Image` component as well.
> **Note** : HeroUI's `Image` component is `client-side`, using hooks like `useState` for loading states and animations. Use Next.js `Image` alone if these features aren't required.
## Slots
  * **img** : Slot for the image element.
  * **wrapper** : Image wrapper, it handles alignment, placement, and general appearance.
  * **zoomedWrapper** : The wrapper slot for the zoomed image it avoids the image content to overflow the parent container.
  * **blurredImg** : The wrapper slot for the duplicated blurred image.


## API
### Image Props
Prop| Type| Default  
---|---|---  
`src`| `string`  
`srcSet`| `string`  
`sizes`| `string`  
`alt`| `string`  
`width`| `number`  
`height`| `number`  
`radius`| `none | sm | md | lg | full`| `"xl"`  
`shadow`| `none | sm | md | lg`| `"none"`  
`loading`| `eager | lazy`  
`fallbackSrc`| `string`  
`isBlurred`| `boolean`| `false`  
`isZoomed`| `boolean`| `false`  
`removeWrapper`| `boolean`| `false`  
`disableSkeleton`| `boolean`| `false`  
`classNames`| `Partial<Record<"img" | "wrapper" | "zoomedWrapper" | "blurredImg", string>>`  
### Image Events
Prop| Type| Default  
---|---|---  
`onLoad`| `ReactEventHandler<HTMLImageElement>`  
`onError`| `() => void`  
FormInput
On this page
  * Installation
  * Import
  * Usage
  * Blurred
  * Zoomed
  * Animated Loading
  * Image with fallback
  * With Next.js Image
  * Slots
  * API
  * Image Props
  * Image Events
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
