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


# Dark mode
HeroUI supports both `light` and `dark` themes. To enable dark mode, simply add the `dark` class to your root element (`html`, `body`, or `main`).
```

```

```

// main.tsx or main.jsx
importReactfrom"react";
importReactDOMfrom"react-dom/client";
import{HeroUIProvider}from"@heroui/react";
importAppfrom"./App";
import"./index.css";
ReactDOM.createRoot(document.getElementById("root")).render(
<React.StrictMode>
<HeroUIProvider>
<mainclassName="dark text-foreground bg-background">
<App/>
</main>
</HeroUIProvider>
</React.StrictMode>,
);

```


```


```

This enables dark mode application-wide. For theme switching functionality, you can use a theme library or create a custom implementation.
## Using next-themes
For Next.js applications, next-themes provides seamless theme switching functionality.
> For more information, refer to the next-themes documentation.
### Next.js App Directory Setup
### Install next-themes
Install `next-themes` in your project.
npm
yarn
pnpm
### Add next-themes provider
Wrap your app with the `ThemeProvider` component from `next-themes`.
Go to your `app/providers.tsx` or `app/providers.jsx` (create it if it doesn't exist) and wrap the Component with the `HeroUIProvider` and the `next-themes` provider components.
> Note: We're using the `class` attribute to switch between themes, this is because HeroUI uses the `className` attribute.
### Add the theme switcher
Add the theme switcher to your app.
> **Note** : You can use any theme name you want, but make sure it exists in your `tailwind.config.js` file. See Create Theme for more details.
### Next.js Pages Directory Setup
### Install next-themes
Install `next-themes` in your project.
npm
yarn
pnpm
### Add next-themes provider
Go to pages`/_app.js` or `pages/_app.tsx` (create it if it doesn't exist) and wrap the Component with the `HeroUIProvider` and the `next-themes` provider components.
> Note: We're using the `class` attribute to switch between themes, this is because HeroUI uses the `className` attribute.
### Add the theme switcher
Add the theme switcher to your app.
> **Note** : You can use any theme name you want, but make sure it exists in your `tailwind.config.js` file. See Create Theme for more details.
## Using use-theme hook
In case you're using plain React with Vite or Create React App you can use the @heroui/use-theme hook to switch between themes.
### Install @heroui/use-theme
Install `@heroui/use-theme` in your project.
npm
yarn
pnpm
### Add the theme switcher
Add the theme switcher to your app.
> **Note** : You can use any theme name you want, but make sure it exists in your `tailwind.config.js` file. See Create Theme for more details.
Create themeOverride styles
On this page
  * Using next-themes
  * Next.js App Directory Setup
  * Install next-themes
  * Add next-themes provider
  * Add the theme switcher
  * Next.js Pages Directory Setup
  * Install next-themes
  * Add next-themes provider
  * Add the theme switcher
  * Using use-theme hook
  * Install @heroui/use-theme
  * Add the theme switcher
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
