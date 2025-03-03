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


# Installation
Requirements:
  * React 18 or later
  * Tailwind CSS 3.4 or later
  * Framer Motion 11.9 or later


## Automatic Installation
Using the CLI is now the easiest way to start a HeroUI project. You can initialize your project and add components directly via the CLI:
### Installation
Execute one of the following commands in your terminal:
npm
yarn
pnpm
bun
### Initialization and Starting the App
Initialize the project by using the `init` command.
You will be prompted to configure your project:
Install the dependencies to start the local server:
npm
yarn
pnpm
bun
Start the local server:
npm
yarn
pnpm
bun
### Adding the Components
Once your HeroUI project is ready to develop, you can add individual components using the CLI. For example, to add a button component:
This command adds the Button component to your project and manages all related dependencies.
You can also add multiple components at once:
Or you can add the main library `@heroui/react` by running the following command:
If you leave out the component name, the CLI will prompt you to select the components you want to add.
## Manual Installation
If you prefer not to use the CLI, you may try either global installation or individual installation to set up HeroUI in your project:
### Global Installation
The easiest way to get started with HeroUI is to use the global installation, which means that all the components are imported from a single package.
Follow the steps below to install all HeroUI components:
#### Install Packages
To install HeroUI, run one of the following commands in your terminal:
npm
yarn
pnpm
bun
#### Hoisted Dependencies Setup
> **Note** : This step is only for those who use `pnpm` to install. If you install HeroUI using other package managers, you may skip this step.
If you are using pnpm, you need to add the following line to your `.npmrc` file to hoist our packages to the root `node_modules`.
After modifying the `.npmrc` file, you need to run `pnpm install` again to ensure that the dependencies are installed correctly.
#### Tailwind CSS Setup
HeroUI is built on top of Tailwind CSS, so you need to install Tailwind CSS first. You can follow the official installation guide to install Tailwind CSS. Then you need to add the following code to your `tailwind.config.js` file:
> **Note** : If you are using pnpm and monorepo architecture, please make sure you are pointing to the ROOT `node_modules`
#### Provider Setup
It is essential to add the `HeroUIProvider` at the `root` of your application.
### Individual Installation
HeroUI is also available as individual packages. You can install each package separately. This is useful if you want to reduce the size of your CSS bundle as it will only include styles for the components you're actually using.
> **Note** : JavaScript bundle size will not change due to tree shaking support in HeroUI.
Follow the steps below to install each package separately:
#### Install Core Packages
Although you can install each package separately, you need to install the core packages first to ensure that all components work correctly.
Run one of the following commands in your terminal to install the core packages:
npm
yarn
pnpm
bun
#### Install Component
Now, let's install the component you want to use. For example, if you want to use the Button component, you need to run one of the following commands in your terminal:
npm
yarn
pnpm
bun
#### Hoisted Dependencies Setup
> **Note** : This step is only for those who use `pnpm` to install. If you install HeroUI using other package managers, you may skip this step.
If you are using pnpm, you need to add the following line to your `.npmrc` file to hoist our packages to the root `node_modules`.
After modifying the `.npmrc` file, you need to run `pnpm install` again to ensure that the dependencies are installed correctly.
#### Tailwind CSS Setup
TailwindCSS setup changes a bit when you use individual packages. You only need to add the styles of the components you're using to your `tailwind.config.js` file. For example, for the Button component, you need to add the following code to your `tailwind.config.js` file:
#### Provider Setup
It is essential to add the `HeroUIProvider` at the `root` of your application.
#### Use the Component
Now, you can use the component you installed in your application:
## Framework Guides
HeroUI is compatible with your preferred framework. We have compiled comprehensive, step-by-step tutorials for the following frameworks:
Next.js
Vite
Remix
Astro
Design PrinciplesCLI
On this page
  * Automatic Installation
  * Installation
  * Initialization and Starting the App
  * Adding the Components
  * Manual Installation
  * Global Installation
  * Install Packages
  * Hoisted Dependencies Setup
  * Tailwind CSS Setup
  * Provider Setup
  * Individual Installation
  * Install Core Packages
  * Install Component
  * Hoisted Dependencies Setup
  * Tailwind CSS Setup
  * Provider Setup
  * Use the Component
  * Framework Guides
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
