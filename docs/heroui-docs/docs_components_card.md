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


# Card
Card is a container for text, photos, and actions in the context of a single subject.
Storybook@heroui/cardSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
```

```

npx heroui-cli@latest add card

```


```

> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
HeroUI exports 4 card-related components:
  * **Card** : The main component to display a card.
  * **CardHeader** : Commonly used for the title of a card.
  * **CardBody** : The content of the card.
  * **CardFooter** : Commonly used for actions.


Individual
Global
## Usage
Preview
Code
### With Divider
Preview
Code
> See the Divider component for more details.
### With Image
Preview
Code
### Blurred Footer
You can pass the `isFooterBlurred` prop to the card to blur the footer.
Preview
Code
### Composition
You can use other HeroUI components inside the card to compose a more complex card.
Preview
Code
### Blurred Card
You can pass the `isBlurred` prop to the card to blur the card. Card gets blurred properties based on its ancestor element.
> **Note** : To achieve the blur effect as seen in the preview, you need to provide a suitable background (e.g., `bg-gradient-to-tr from-[#FFB457] to-[#FF705B]`) to an ancestor element of the Card component allowing the Card's blur effect to be visible.
Preview
Code
### Primary Action
If you pass the `isPressable` prop to the card, it will be rendered as a button.
Preview
Code
> **Note** : that the used callback function is `onPress` instead of `onClick`. Please see the usePress component for more details.
### Cover Image
You can use `Image` component as the cover of the card by taking it out of the `CardBody` component.
Preview
Code
## Slots
  * **base** : The main container of the card, where the header, body, and footer are placed.
  * **header** : The header of the card, usually used for the title.
  * **body** : The body of the card, where the main content is placed.
  * **footer** : The footer of the card, usually used for actions.


## Data Attributes
`Card` has the following attributes on the `base` element:
  * **data-hover** : When the card is being hovered. Based on useHover
  * **data-focus** : When the card is being focused. Based on useFocusRing.
  * **data-focus-visible** : When the card is being focused with the keyboard. Based on useFocusRing.
  * **data-disabled** : When the card is disabled. Based on `isDisabled` prop.
  * **data-pressed** : When the card is pressed. Based on usePress


## API
### Card Props
Prop| Type| Default  
---|---|---  
`children`| `ReactNode | ReactNode[]`  
`shadow`| `none | sm | md | lg`| `"md"`  
`radius`| `none | sm | md | lg`| `"lg"`  
`fullWidth`| `boolean`| `false`  
`isHoverable`| `boolean`| `false`  
`isPressable`| `boolean`| `false`  
`isBlurred`| `boolean`| `false`  
`isFooterBlurred`| `boolean`| `false`  
`isDisabled`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
`disableRipple`| `boolean`| `false`  
`allowTextSelectionOnPress`| `boolean`| `false`  
`classNames`| `Partial<Record<'base' | 'header' | 'body' | 'footer', string>>`  
### Card Events
Prop| Type| Default  
---|---|---  
`onPress`| `(e: PressEvent) => void`  
`onPressStart`| `(e: PressEvent) => void`  
`onPressEnd`| `(e: PressEvent) => void`  
`onPressChange`| `(isPressed: boolean) => void`  
`onPressUp`| `(e: PressEvent) => void`  
CalendarCheckbox
On this page
  * Installation
  * Import
  * Usage
  * With Divider
  * With Image
  * Blurred Footer
  * Composition
  * Blurred Card
  * Primary Action
  * Cover Image
  * Slots
  * Data Attributes
  * API
  * Card Props
  * Card Events
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
