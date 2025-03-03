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


# NextUI to HeroUI
HeroUI is the new identity for NextUI, bringing the same powerful components and features you love under a new name. This guide will help you migrate your existing NextUI project to HeroUI.
## Automatic Migration (Recommended)
The easiest way to migrate your NextUI project to HeroUI is using our official codemod:
### Run Migration
Execute the codemod in your project directory:
npm
yarn
pnpm
bun
> **Note:** If you're using a monorepo, run the codemod from the root directory
This will automatically:
  * Update all package names from `@nextui-org/*` to `@heroui/*`
  * Rename component imports and references
  * Update TailwindCSS configuration
  * Transform provider components
  * Adjust any NextUI-specific utilities or hooks
  * Update `.npmrc` file pnpm only


### Install Dependencies
After running the codemod, install the new dependencies:
npm
yarn
pnpm
bun
## Manual Migration
If you prefer to migrate manually, follow these steps:
### Update Dependencies
Replace NextUI packages with their HeroUI equivalents:
npm
yarn
pnpm
bun
### Update TailwindCSS Configuration
Update your `tailwind.config.js`:
### Update Provider Component
Replace the NextUI provider with HeroUI's provider:
### Update Imports
Update all component imports to use the new package name:
### Individual Packages
If you're using individual packages, update each package name:
### Npmrc Pnpm Only
If you are using pnpm, you need to update your .npmrc file to use the new package name:
## Verification
After migration, verify that:
  1. All components render correctly
  2. Theme customizations are preserved
  3. No NextUI imports remain in your codebase
  4. Your application builds without errors


> The functionality and API of all components remain the same - only the package names and imports have changed.
## Troubleshooting
If you encounter issues during migration, try these steps:
### NPM Users
If you're using `npm`, you may need to:
  1. Delete your `node_modules` folder
  2. Delete your `package-lock.json` file
  3. Reinstall all packages with `npm install`


### Package.json Check
Ensure that no `@nextui-org` packages remain in your `package.json` dependencies or devDependencies.
### Need Help?
Join our Discord community in the **#nextui-to-heroui** channel https://discord.gg/9b6yyZKmH4 - our team is happy to help!
If you encounter any issues during migration, please open an issue on our GitHub repository.
FormsFigma
On this page
  * Automatic Migration (Recommended)
  * Run Migration
  * Install Dependencies
  * Manual Migration
  * Update Dependencies
  * Update TailwindCSS Configuration
  * Update Provider Component
  * Update Imports
  * Individual Packages
  * Npmrc Pnpm Only
  * Verification
  * Troubleshooting
  * NPM Users
  * Package.json Check
  * Need Help?
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
