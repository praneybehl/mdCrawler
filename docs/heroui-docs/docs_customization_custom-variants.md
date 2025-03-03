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


# Custom Variants
HeroUI allows you to create new variants for components by extending and customizing their styles. You can override the component's `variants`, `defaultVariants` and `compoundVariants`.
> **Note** : For one-off customizations, refer to the Override Styles documentation.
## Creating new variants for non-slots components
Let's use the Button component as an example. It's a non-slots component, and you can view its source styles here.
> **Note** : If you are not familiar with the variants concept, please refer to the Tailwind Variants documentation.
### Extend the original component variants
Use the `extendVariants` function to create a new component with customized variants based on an existing component.
### Use your custom component in your application
Then, you can now use your custom component in your application. Here, `MyButton` is used with the color set to `olive` and the size set to `xl`.
The new component will include the original props of the `Button` component, plus the new variants that you have created.
Press Me
## Creating new variants for slots components
The `extendVariants` function can also be used with slot-based components like Input to add or override variants. You can view the Input component's source styles here.
> **Note** : If you are not familiar with the variants/slots concept, please refer to the Tailwind Variants documentation.
### Extend the original component variants
Use the `extendVariants` function to create a new component with custom variants based on the original component.
### Use your custom component in your application
Then, you can now use your custom component in your application. Here, `MyInput` is used with the color set to `slate` and the size set to `xl`.
The new component will include the original props of the Input component, plus the new variants that you have created.
> Use the `Styles source` link at the top of each component page to view its source code as a reference for customization.
### Types
### Main Function
### Options
### Config
> **Note** : See the Tailwind Merge Config to learn more about it.
Override stylesComponents: Accordion
On this page
  * Creating new variants for non-slots components
  * Extend the original component variants
  * Use your custom component in your application
  * Creating new variants for slots components
  * Extend the original component variants
  * Use your custom component in your application
  * Types
  * Main Function
  * Options
  * Config
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
