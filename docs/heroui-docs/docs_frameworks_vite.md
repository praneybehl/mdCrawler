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


# Vite
Requirements:
  * Vite 2 or later
  * React 18 or later
  * Tailwind CSS 3.4 or later
  * Framer Motion 11.9 or later


To use HeroUI in your Vite project, you need to follow the following steps:
### HeroUI CLI (recommended)
If you are starting a new project, you can use the HeroUI CLI to create a new project with HeroUI pre-configured:
npm
yarn
pnpm
bun
### Using HeroUI + Vite template
If you are starting a new project, you can run one of the following commands to create a Vite project pre-configured with HeroUI:
npm
yarn
pnpm
bun
### Automatic Installation
You can add individual components using the CLI. For example, to add a button component:
This command adds the Button component to your project and manages all related dependencies.
You can also add multiple components at once:
Or you can add the main library `@heroui/react` by running the following command:
If you leave out the component name, the CLI will prompt you to select the components you want to add.
You still need to add the provider to your app manually (we are working on automating this step).
### Manual Installation
### Add dependencies
In your Vite React project, run one of the following command to install HeroUI:
npm
yarn
pnpm
bun
### Hoisted Dependencies Setup
> **Note** : This step is only for those who use `pnpm` to install. If you install HeroUI using other package managers, you may skip this step.
If you are using pnpm, you need to add the following line to your `.npmrc` file to hoist our packages to the root `node_modules`.
After modifying the `.npmrc` file, you need to run `pnpm install` again to ensure that the dependencies are installed correctly.
### Tailwind CSS Setup
HeroUI is built on top of Tailwind CSS, so you need to install Tailwind CSS first. You can follow the official installation guide to install Tailwind CSS. Then you need to add the following code to your `tailwind.config.js` file:
> **Note** : If you are using pnpm and monorepo architecture, please make sure you are pointing to the ROOT `node_modules`
### Provider Setup
After installing HeroUI, you need to set up the `HeroUIProvider` at the `root` of your application.
Go to the src directory and inside `main.jsx` or `main.tsx`, wrap `HeroUIProvider` around App:
Next.jsRemix
On this page
  * HeroUI CLI (recommended)
  * Using HeroUI + Vite template
  * Automatic Installation
  * Manual Installation
  * Add dependencies
  * Hoisted Dependencies Setup
  * Tailwind CSS Setup
  * Provider Setup
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
