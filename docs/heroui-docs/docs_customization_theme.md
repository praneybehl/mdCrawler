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


# Theme
Theming allows you to maintain a consistent look and feel across your application. HeroUI provides theme customization through a TailwindCSS plugin based on tw-colors, enabling you to easily customize colors, layouts and other UI elements.
## What is a Theme?
A theme is a predefined set of colors and layout attributes that ensure visual consistency across your application. It simplifies managing and updating your app's appearance.
## Setup
The first step to using HeroUI's theming capability is adding the `heroui` plugin to your `tailwind.config.js` file. Below is an example of how to do this:
> **Note** : If you are using pnpm and monorepo architecture, please make sure you are pointing to the ROOT `node_modules`
### Usage
After adding the plugin to your `tailwind.config.js` file, you can utilize any of the default themes (light/dark) or a custom one. Here's how you can apply these themes in your `main.jsx` or `main.tsx`:
Go to the src directory and inside `main.jsx` or `main.tsx`, apply the following class names to the root element:
  * `light` for the light theme.
  * `dark` for the dark theme.
  * `text-foreground` to set the text color.
  * `bg-background` to set the background color.


> **Note** : See the Colors section to learn more about the color classes.
### Default Plugin Options
The `heroui` plugin provides a default structure. It is outlined as follows:
### Themes Options
These are the options that you can use to apply custom configurations to your themes.
### Nested themes
HeroUI supports nested themes, allowing you to apply different themes to different sections of your application:
### Theme based variants
HeroUI enables you to apply TailwindCSS styles based on the currently active theme. Below are examples of how to do this:
### API Reference
The following table provides an overview of the various attributes you can use when working with themes in HeroUI:
Attribute| Type| Description| Default  
---|---|---|---  
prefix| `string`| The prefix for the css variables.| `heroui`  
addCommonColors| `boolean`| If true, the common heroui colors (e.g. "blue", "green", "purple") will replace the TailwindCSS default colors.| `false`  
defaultTheme| `light` | `dark`| The default theme to use.| `light`  
defaultExtendTheme| `light` | `dark`| The default theme to extend.| `light`  
layout| LayoutTheme| The layout definitions.| -  
themes| ConfigThemes| The theme definitions.| -  
### Types
#### ConfigThemes
#### LayoutTheme
#### ThemeColors
Frameworks: LaravelLayout
On this page
  * What is a Theme?
  * Setup
  * Usage
  * Default Plugin Options
  * Themes Options
  * Nested themes
  * Theme based variants
  * API Reference
  * Types
  * ConfigThemes
  * LayoutTheme
  * ThemeColors
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
