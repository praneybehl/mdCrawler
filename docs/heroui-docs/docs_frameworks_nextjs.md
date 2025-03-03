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


# Next.js
Requirements:
  * Next.js 12 or later
  * React 18 or later
  * Tailwind CSS 3.4 or later
  * Framer Motion 11.9 or later


To use HeroUI in your Next.js project, you need to follow the steps below, depending on your project structure.
## App Directory Setup
Next.js 13's `app/` directory uses Server Components by default. HeroUI components can be imported directly in Server Components since we add `use client` at build time.
### HeroUI CLI (recommended)
If you are starting a new project, you can use the HeroUI CLI to create a new project with HeroUI pre-configured:
or
npm
yarn
pnpm
bun
### create-next-app
If you are starting a new project, you can run one of the following commands to create a Next.js project pre-configured with HeroUI:
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
In your Next.js project, run one of the following commands to install HeroUI:
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
### Setup Provider
Go to your `app/providers.tsx` or `app/providers.jsx` (create it if it doesn't exist) and wrap the Component with the `HeroUIProvider`:
### Add Provider to Root
Now, Go to your `root` layout page and wrap it with the `Providers`:
> **Note** : HeroUI automatically adds two themes, `light` and `dark`, to your application. You can use any of them by adding the `dark`/`light` class to the `html` tag. See the theme docs for more details.
### Use HeroUI Components
Now you can import any HeroUI component directly in your Server Components without needing to use the `use client;` directive:
> **Important 🚨** : Note that you need to import the component from the individual package, not from `@heroui/react`.
## Pages Directory Setup
### HeroUI CLI (recommended)
If you are starting a new project, you can use the HeroUI CLI to create a new project with HeroUI pre-configured:
If you are using the `/pages` Next.js project structure, you need to follow the steps below.
### create-next-app
If you are starting a new project, you can run one of the following commands to create a Next.js project pre-configured with HeroUI:
npm
yarn
pnpm
### Automatic Installation
You can add individual components using the CLI. For example, to add a button component:
This command adds the Button component to your project and manages all related dependencies.
You can also add multiple components at once:
Or you can add the main library `@heroui/react` by running the following command:
If you leave out the component name, the CLI will prompt you to select the components you want to add.
You still need to add the provider to your app manually (we are working on automating this step).
### Manual Installation
### Add dependencies
In your Next.js project, run one of the following commands to install HeroUI:
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
### Setup Provider
Go to pages`/_app.js` or `pages/_app.tsx` (create it if it doesn't exist) and wrap the Component with the `HeroUIProvider`:
### Use HeroUI Components
Now you can import any HeroUI component wherever you want:
Getting Started: FigmaVite
On this page
  * App Directory Setup
  * HeroUI CLI (recommended)
  * create-next-app
  * Automatic Installation
  * Manual Installation
  * Add dependencies
  * Hoisted Dependencies Setup
  * Tailwind CSS Setup
  * Setup Provider
  * Add Provider to Root
  * Use HeroUI Components
  * Pages Directory Setup
  * HeroUI CLI (recommended)
  * create-next-app
  * Automatic Installation
  * Manual Installation
  * Add dependencies
  * Hoisted Dependencies Setup
  * Tailwind CSS Setup
  * Setup Provider
  * Use HeroUI Components
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
