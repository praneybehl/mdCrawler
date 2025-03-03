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


# Layout
HeroUI provides layout customization options for spacing, fonts, and other visual properties. Layout tokens help maintain consistency across components without modifying Tailwind CSS defaults.
```

```

```

module.exports={
plugins:[
heroui({
layout:{},// common layout options
themes:{
light:{
layout:{},// light theme layout options
// ...
},
dark:{
layout:{},// dark theme layout options
// ...
},
// ... custom themes
},
}),
],
};

```


```


```

> Layout options are applied to all components.
## Default Layout
Default values for the layout tokens are:
### CSS Variables
HeroUI creates CSS variables using the format `--prefix-prop-name-scale` for each layout token. By default the prefix is `heroui`, but you can change it with the `prefix` option.
Then you can use the CSS variables in your CSS files.
#### API Reference
Attribute| Type| Description  
---|---|---  
hoverOpacity| string, number| A number between 0 and 1 that is applied as opacity-[value] when the component is hovered.  
disabledOpacity| string, number| A number between 0 and 1 that is applied as opacity-[value] when the component is disabled.  
dividerWeight| string| The default height applied to the divider component. We recommend to use `px` units.  
fontSize| FontThemeUnit| The default font size applied across the components.  
lineHeight| FontThemeUnit| The default line height applied across the components.  
radius| BaseThemeUnit| The default radius applied across the components. We recommend to use `rem` units.  
borderWidth| BaseThemeUnit| The border width applied across the components.  
boxShadow| BaseThemeUnit| The box shadow applied across the components.  
#### BaseThemeUnit
#### FontThemeUnit
ThemeColors
On this page
  * Default Layout
  * CSS Variables
  * API Reference
  * BaseThemeUnit
  * FontThemeUnit
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
