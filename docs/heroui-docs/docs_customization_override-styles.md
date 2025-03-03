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


# Override styles
Overriding default component styles is as simple as passing your own class names to the `className` or to the `classNames` prop for components with slots.
### What is a Slot?
A slot is a part of a component that can be styled separately using the `classNames` prop. For example, the CircularProgress component has slots like `track`, `indicator`, and `value` that can each be styled independently.
### Overriding a component
Let's override the default styles of the Button component, which is a component that has no slots.
```

```

```

import{Button}from"@heroui/react";
exportdefaultfunctionApp(){
return(
<Button
disableRipple
className="relative overflow-visible rounded-full hover:-translate-y-1 px-12 shadow-xl bg-background/30 after:content-[''] after:absolute after:rounded-full after:inset-0 after:bg-background/40 after:z-[-1] after:transition after:!duration-500 hover:after:scale-150 hover:after:opacity-0"
size="lg"
>
   Press me
</Button>
);
}

```


```


```

Press me
### Components with slots
Some HeroUI components have slots that can be styled individually using the `classNames` prop. The CircularProgress component has the following slots:
  * **base** : The base slot of the circular progress, it is the main container.
  * **svgWrapper** : The wrapper of the svg circles and the value label.
  * **svg** : The svg element of the circles.
  * **track** : The track is the background circle of the circular progress.
  * **indicator** : The indicator is the one that is filled according to the `value`.
  * **value** : The value content.
  * **label** : The label content.


The example below demonstrates styling these slots to create a custom circular progress:
> **Note** : You will find a `Slots` section in the documentation of each component that has slots.
### CSS Modules
CSS Modules allow for the creation of local scope classes and variables. Here's how you can use it to override styles:
With the corresponding CSS module:
### CSS-in-JS
If you are using a CSS-in-JS library such as styled-components or emotion, you can use the following example to override the styles of a component:
Each styled component combines the original component styles with custom styles defined in the template strings. The `StyledCircularProgress` uses `.attrs` to add classNames.
Dark modeCustom variants
On this page
  * What is a Slot?
  * Overriding a component
  * Components with slots
  * CSS Modules
  * CSS-in-JS
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
