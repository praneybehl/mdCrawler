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


# Slider
A slider allows a user to select one or more values within a range.
Storybook@heroui/sliderSourceStyles source
## Installation
CLI
npm
yarn
pnpm
bun
> The above command is for individual installation only. You may skip this step if `@heroui/react` is already installed globally.
## Import
Individual
Global
## Usage
Preview
Code
### Disabled
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
### Vertical Slider
It is possible to change the orientation of the slider by using the `orientation="vertical"` prop.
Preview
Code
### With Visible Steps
You can use the `showSteps` prop to display small dots on each step.
Preview
Code
### With Marks
You can use the `marks` prop to display a label on each step.
Preview
Code
### Range Slider
If you pass an array of values to the `value` prop or to the `defaultValue` prop, the slider will become a range slider.
Preview
Code
### Fill Offset
The `fillOffset` prop allows you to set where the fill should start.
Preview
Code
### With Tooltip
The `showTooltip` prop allows you to show a tooltip with the current thumb value when the user hovers or drags the thumb.
Preview
Code
> **Note:** You can change any of the tooltip props by passing the `tooltipProps` to the `Slider` component.
### With Outline
It is possible to add a small outline to the slider's thumbs by passing the `showOutline` prop.
Preview
Code
### Start & End Content
Slider component provides `startContent` and `endContent` props that allows you to add any `ReactNode` to the start and end of the slider.
Preview
Code
### Value Formatting
Values are formatted as a percentage by default, but this can be modified by using the `formatOptions` prop to specify a different format. `formatOptions` is compatible with the option parameter of Intl.NumberFormat and is applied based on the current locale.
Preview
Code
> **Note:** Use the `tooltipValueFormatOptions` prop to format the tooltip value.
It is also possible to format the value using the `getValue` prop.
Preview
Code
### Hiding the Value
The Slider value is shown by default, but can be hidden by passing the `hideValue` prop.
Preview
Code
### Hiding the Thumbs
The Slider thumbs are shown by default, but can be hidden by passing the `hideThumb` prop.
Preview
Code
### Controlled
You can control the slider by passing the `value` and `onChange` props.
Preview
Code
If you want to capture the slider value only when the user stops dragging the thumb, you can use the `onChangeEnd` prop.
Preview
Code
### Controlled Range
You can also control the range slider by using an array of values in the `value` and `onChange` props.
Preview
Code
### Custom Thumb
The Slider component provides a `renderThumb` prop that allows you to customize the thumb in any way you want.
Preview
Code
### Custom Range Thumbs
You can also use the `renderThumb` prop to customize the thumbs of a range slider. The `index` prop will tell you which thumb is being rendered.
Preview
Code
### Custom Label
The Slider component provides a `renderLabel` prop that allows you to customize the label in any way you want.
Preview
Code
### Custom Value
The Slider component provides a `renderValue` prop that allows you to customize the value label element.
Preview
Code
### Disabling Thumb Scale
In case you want to disable the thumb scale animation, you can pass the `disableThumbScale` prop.
Preview
Code
## Slots
  * **base** : The foundational slot, encompassing all other slots and elements. It serves as the primary container.
  * **labelWrapper** : The container for the Slider's label and value. It aligns these elements and ensures a consistent layout.
  * **label** : A dedicated slot to display the Slider's label.
  * **value** : Displays the current value of the Slider. Located within the `labelWrapper`.
  * **step** : Represents individual steps or intervals on the Slider.
  * **mark** : Denotes specific values or intervals along the Slider.
  * **trackWrapper** : A container for the slider's track, ensuring it is consistently aligned and positioned.
  * **track** : The base bar of the Slider, along which the thumb moves.
  * **filler** : A visual representation of the selected value, filling the track from the start point to the current thumb position.
  * **thumb** : The interactive element that users drag along the track to select a value on the Slider.
  * **startContent** : A slot for additional content or icons at the beginning of the Slider.
  * **endContent** : A slot for additional content or icons at the end of the Slider.


### Custom Styles
You can customize the `Slider` component by passing custom Tailwind CSS classes to the component slots.
Preview
Code
## Data Attributes
`Slider` has the following attributes:
  * **data-hover** : When the slider is being hovered. Based on useHover
  * **data-orientation** : The orientation of the slider. Based on `orientation` prop.


`Thumbs` have the following attributes which are returned by the `renderThumb` prop:
  * **data-dragging** : When the thumb is being dragged.
  * **data-focus-visible** : When the thumb is focused. Based on useFocusVisible
  * **data-hover** : When the thumb is being hovered. Based on useHover
  * **data-pressed** : When the thumb is being pressed. Based on usePress


## Accessibility
  * Support for one or multiple thumbs.
  * Support for mouse, touch, and keyboard via the useMove hook.
  * Multi-touch support for dragging multiple thumbs or multiple sliders at once.
  * Pressing on the track moves the nearest thumb to that position.
  * Supports using the arrow keys, as well as page up/down, home, and end keys.
  * Support for both horizontal and vertical orientations.
  * Support for custom min, max, and step values with handling for rounding errors.
  * Support for disabling the whole slider or individual thumbs.
  * Prevents text selection while dragging.
  * Exposed to assistive technology as a group of slider elements via ARIA.
  * Slider thumbs use hidden native input elements to support touch screen readers.
  * Support for labeling both the slider as a whole and individual thumbs.
  * Support for displaying the current thumb values using an `<output>` element.
  * Internationalized number formatting as a percentage or value.
  * Support for mirroring in RTL locales.


## API
### Slider Props
Prop| Type| Default  
---|---|---  
`label`| `ReactNode`  
`name`| `string`  
`size`| `sm | md | lg`| `"md"`  
`color`| `foreground | primary | secondary | success | warning | danger`| `"primary"`  
`radius`| `none | sm | md | lg | full`| `"full"`  
`step`| `number`| `"1"`  
`value`| `number`  
`defaultValue`| `number`  
`minValue`| `number`| `"0"`  
`maxValue`| `number`| `"100"`  
`orientation`| `horizontal | vertical`| `"horizontal"`  
`fillOffset`| `number`  
`showSteps`| `boolean`| `false`  
`showTooltip`| `boolean`| `false`  
`marks`| `SliderStepMarks`  
`startContent`| `ReactNode`  
`endContent`| `ReactNode`  
`formatOptions`| `Intl.NumberFormat`  
`tooltipValueFormatOptions`| `Intl.NumberFormat`  
`tooltipProps`| `TooltipProps`  
`showOutline`| `boolean`| `false`  
`hideValue`| `boolean`| `false`  
`hideThumb`| `boolean`| `false`  
`disableThumbScale`| `boolean`| `false`  
`isDisabled`| `boolean`| `false`  
`disableAnimation`| `boolean`| `false`  
### Slider Functions
Prop| Type| Default  
---|---|---  
`getValue`| `(value: SliderValue) => string`  
`renderLabel`| `(props: DOMAttributes<HTMLLabelElement>) => ReactNode`  
`renderValue`| `(props: DOMAttributes<HTMLOutputElement>) => ReactNode`  
`renderThumb`| `(props: DOMAttributes<HTMLDivElement> & {index?: number}) => ReactNode`  
### Slider Events
Prop| Type| Default  
---|---|---  
`onChange`| `(value: SliderValue) => void`  
`onChangeEnd`| `(value: SliderValue) => void`  
### Types
#### Slider Value
#### Slider Step Marks
SkeletonSnippet
On this page
  * Installation
  * Import
  * Usage
  * Disabled
  * Sizes
  * Radius
  * Colors
  * Vertical Slider
  * With Visible Steps
  * With Marks
  * Range Slider
  * Fill Offset
  * With Tooltip
  * With Outline
  * Start & End Content
  * Value Formatting
  * Hiding the Value
  * Hiding the Thumbs
  * Controlled
  * Controlled Range
  * Custom Thumb
  * Custom Range Thumbs
  * Custom Label
  * Custom Value
  * Disabling Thumb Scale
  * Slots
  * Custom Styles
  * Data Attributes
  * Accessibility
  * API
  * Slider Props
  * Slider Functions
  * Slider Events
  * Types
  * Slider Value
  * Slider Step Marks
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
