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


# Colors
HeroUI's plugin enables you to personalize the semantic colors of the theme such as `primary`, `secondary`, `success`, etc.
```

```

```

module.exports={
plugins:[
heroui({
themes:{
light:{
// ...
colors:{},
},
dark:{
// ...
colors:{},
},
// ... custom themes
},
}),
],
};

```


```


```

> **Note** : Colors configurations apply globally across all components.
## Default Colors
HeroUI offers a default color palette right out of the box, perfect for when you're still undecided about your specific branding colors.
These colors are split into Common Colors and Semantic Colors.
  * Common Colors: Consistent across themes.
  * Semantic Colors: Adjust according to the chosen theme.


### Common Colors
Common colors, like TailwindCSS colors, remain consistent regardless of the theme.
To prevent conflicts with TailwindCSS colors, common colors are initially disabled but can be activated with the `addCommonColors` option.
Enabling this option supplements some TailwindCSS default colors with the following:
## White & Black
#FFFFFF#000000
## Blue
#E6F1FE50#CCE3FD100#99C7FB200#66AAF9300#338EF7400#006FEE500#005BC4600#004493700#002E62800#001731900
## Purple
#F2EAFA50#E4D4F4100#C9A9E9200#AE7EDE300#9353D3400#7828C8500#6020A0600#481878700#301050800#180828900
## Green
#E8FAF050#D1F4E0100#A2E9C1200#74DFA2300#45D483400#17C964500#12A150600#0E793C700#095028800#052814900
## Red
#FEE7EF50#FDD0DF100#FAA0BF200#F871A0300#F54180400#F31260500#C20E4D600#920B3A700#610726800#310413900
## Pink
#FFEDFA50#FFDCF5100#FFB8EB200#FF95E1300#FF71D7400#FF4ECD500#CC3EA4600#992F7B700#661F52800#331029900
## Yellow
#FEFCE850#FDEDD3100#FBDBA7200#F9C97C300#F7B750400#F5A524500#C4841D600#936316700#62420E800#312107900
## Cyan
#F0FCFF50#E6FAFE100#D7F8FE200#C3F4FD300#A5EEFD400#7EE7FC500#06B7DB600#09AACD700#0E8AAA800#053B48900
## Zinc
#FAFAFA50#F4F4F5100#E4E4E7200#D4D4D8300#A1A1AA400#71717A500#52525B600#3F3F46700#27272A800#18181B900
### Semantic Colors
Semantic colors adapt with the theme, delivering meaning and reinforcing your brand identity.
For an effective palette, we recommend using color ranges from `50` to `900`. You can use tools like Eva Design System, Smart Watch, Palette or Color Box to generate your palette.
> Semantic colors should be placed inside the `heroui` plugin options, not inside the TailwindCSS theme object.
> Change the docs theme to see the semantic colors in action.
## Layout
background#000000foreground#ECEDEEdividerrgba(255, 255, 255, 0.15)focus#006FEE
## Content
content1#18181bcontent2#27272acontent3#3f3f46content4#52525b
## Base
default#3f3f46primary#006FEEsecondary#9353d3success#17c964warning#f5a524danger#f31260
## Default
default-50#18181bdefault-100#27272adefault-200#3f3f46default-300#52525bdefault-400#71717adefault-500#a1a1aadefault-600#d4d4d8default-700#e4e4e7default-800#f4f4f5default-900#fafafa
## Primary
primary-50#001731primary-100#002e62primary-200#004493primary-300#005bc4primary-400#006FEEprimary-500#338ef7primary-600#66aaf9primary-700#99c7fbprimary-800#cce3fdprimary-900#e6f1fe
## Secondary
secondary-50#180828secondary-100#301050secondary-200#481878secondary-300#6020a0secondary-400#7828c8secondary-500#9353d3secondary-600#ae7edesecondary-700#c9a9e9secondary-800#e4d4f4secondary-900#f2eafa
## Success
success-50#052814success-100#095028success-200#0e793csuccess-300#12a150success-400#17c964success-500#45d483success-600#74dfa2success-700#a2e9c1success-800#d1f4e0success-900#e8faf0
## Warning
warning-50#312107warning-100#62420ewarning-200#936316warning-300#c4841dwarning-400#f5a524warning-500#f7b750warning-600#f9c97cwarning-700#fbdba7warning-800#fdedd3warning-900#fefce8
## Danger
danger-50#310413danger-100#610726danger-200#920b3adanger-300#c20e4ddanger-400#f31260danger-500#f54180danger-600#f871a0danger-700#faa0bfdanger-800#fdd0dfdanger-900#fee7ef
### Using Semantic Colors
Semantic colors can be applied anywhere in your project where colors are used, such as text color, border color, background color utilities, and more.
### Javascript Variables
Import semantic and common colors into your JavaScript files as follows:
### CSS Variables
HeroUI creates CSS variables using the format `--prefix-colorname-shade` for each semantic color. By default the prefix is `heroui`, but you can change it with the `prefix` option.
Then you can use the CSS variables in your CSS files.
LayoutCustomize theme
On this page
  * Default Colors
  * Common Colors
  * Semantic Colors
  * Using Semantic Colors
  * Javascript Variables
  * CSS Variables
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
