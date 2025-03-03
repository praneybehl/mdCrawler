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


# Create theme
Create a new theme by adding it to your `tailwind.config.js` file. For color palettes (50-900), you can use tools like Eva Design System or Smart Watch to generate them.
### Add the new theme to the plugin
```

```

```

// tailwind.config.js
const{heroui}=require("@heroui/react");
/** @type {import('tailwindcss').Config} */
module.exports={
plugins:[
heroui({
themes:{
"purple-dark":{
extend:"dark",// <- inherit default values from dark theme
colors:{
background:"#0D001A",
foreground:"#ffffff",
primary:{
50:"#3B096C",
100:"#520F83",
200:"#7318A2",
300:"#9823C2",
400:"#c031e2",
500:"#DD62ED",
600:"#F182F6",
700:"#FCADF9",
800:"#FDD5F9",
900:"#FEECFE",
DEFAULT:"#DD62ED",
foreground:"#ffffff",
},
focus:"#F182F6",
},
layout:{
disabledOpacity:"0.3",
radius:{
small:"4px",
medium:"6px",
large:"8px",
},
borderWidth:{
small:"1px",
medium:"2px",
large:"3px",
},
},
},
},
}),
],
};

```


```


```

### Apply the new theme
Now, applying the new theme is as simple as adding the theme name `purple-dark` to the `className` of the `html` / `body` or `main` element.
### Use the new theme
All components that use the `primary` color will be affected by this change.
SolidFadedBorderedLightFlatGhostShadowDisabled
Customize themeDark mode
On this page
  * Add the new theme to the plugin
  * Apply the new theme
  * Use the new theme
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
