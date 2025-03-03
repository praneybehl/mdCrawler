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


# Customize theme
HeroUI provides `light` and `dark` themes that can be customized to match your needs. You can also create custom themes based on these defaults, using Layout and Color tokens.
## Customizing Layout
Layout tokens let you customize spacing, typography, borders and more - either globally or per theme.
### Global Layout Customization
You can customize border radius, border width, and disabled opacity across all themes by modifying your `tailwind.config.js` file:
```

```

```

// tailwind.config.js
const{heroui}=require("@heroui/react");
/** @type {import('tailwindcss').Config} */
module.exports={
plugins:[
heroui({
layout:{
disabledOpacity:"0.3",// opacity-[0.3]
radius:{
small:"2px",// rounded-small
medium:"4px",// rounded-medium
large:"6px",// rounded-large
},
borderWidth:{
small:"1px",// border-small
medium:"1px",// border-medium
large:"2px",// border-large
},
},
themes:{
light:{},
dark:{},
},
}),
],
};

```


```


```

Layout tokens are used across all HeroUI components. For example, the Button component uses `radius` and `borderWidth` tokens for its styling. Here's how it looks with the customized values:
ButtonDisabled
> See the Layout section for more details about the available tokens.
### Customizing Colors
Now, Let's say you wish to modify the primary and focus colors of the dark theme. This can be achieved by adding the following code to your `tailwind.config.js` file.
This modification will impact all components using the `primary` color. For instance, the Button component uses the `primary` color as background color when the variant is `solid` or `ghost`.
SolidGhost
> 🎉 That's it! You have successfully customized the default theme. See the Colors section for more details about the available semantic colors and color tokens.
ColorsCreate theme
On this page
  * Customizing Layout
  * Global Layout Customization
  * Customizing Colors
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
