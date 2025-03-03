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


# Routing
HeroUI Components such as Tabs, Listbox, Dropdown and many others offer the flexibility to be rendered as **HTML links**.
## Introduction
By default, links perform native browser navigation when they are interacted with. However, many apps and frameworks use client side routers to avoid a full page reload when navigating between pages.
The `HeroUIProvider` component configures all HeroUI components within it to navigate using the client side router you provide.
Set this up once in the `root` of your app, and any HeroUI component with the `href` prop will automatically navigate using your router.
## HeroUIProvider Setup
The `HeroUIProvider` component accepts `navigate` and `useHref` props. `navigate` is a router function for client-side navigation, while `useHref` optionally converts router hrefs to native HTML hrefs. Here's the pattern:
> **Note** : Framework-specific examples are shown below.
### Router Options
All `HeroUI` link components accept a `routerOptions` prop that passes options to the router's navigate function for controlling behavior like scrolling and history navigation.
When using TypeScript, you can configure the RouterConfig type globally so that all link components have auto complete and type safety using a type provided by your router.
## Next.js
#### App Router
Go to your `app/providers.tsx` or `app/providers.jsx` (create it if it doesn't exist) and add the `useRouter` hook from `next/navigation`, it returns a router object that can be used to perform navigation.
> Check the Next.js docs for more details.
#### Add the `useRouter`
#### Add Provider to Root
Now, Go to your `root` layout page and wrap it with the `HeroUIProvider`:
> **Note** : Skip this step if you already set up the `HeroUIProvider` in your app.
#### Next.js Base Path (Optional)
If you are using the Next.js basePath setting, you'll need to configure an environment variable to access it.
Then, provide a custom `useHref` function to prepend it to the href for all links.
### Pages Router
Go to pages`/_app.js` or `pages/_app.tsx` (create it if it doesn't exist) and add the`useRouter` hook from `next/router`, it returns a router object that can be used to perform navigation.
When using the basePath configuration option, provide a `useHref` option to the router passed to Provider to prepend it to links automatically.
## React Router
Use the `useNavigate` hook from `react-router-dom` to get the `navigate` function for routing. The `useHref` hook can be used with React Router's `basename` option.
Make sure to place the component using these hooks inside `BrowserRouter` and keep `<Routes>` within `HeroUIProvider`. Here's how to set it up in your App component:
Ensure that the component that calls `useNavigate` and renders `HeroUIProvider` is inside the router component (e.g. `BrowserRouter`) so that it has access to React Router's internal context. The React Router `<Routes>` element should also be defined inside `HeroUIProvider` so that links inside the rendered routes have access to the router.
## Remix
Remix uses React Router under the hood, so the same `useNavigate` and `useHref` hook described above also works in Remix apps. `HeroUIProvider` should be rendered at the `root` of each page that includes HeroUI components, or in `app/root.tsx` to add it to all pages. See the Remix docs for more details.
## TanStack
To use TanStack Router with HeroUI, render HeroUI's RouterProvider inside your root route. Use `router.navigate` in the `navigate` prop, and `router.buildLocation` in the `useHref` prop.
## Usage examples
Now that you have set up the `HeroUIProvider` in your app, you can use the `href` prop in the `Tabs`, `Listbox` and `Dropdown` items to navigate between pages.
The Link component will also use the `navigate` function from the `HeroUIProvider` to navigate between pages.
> For more information about routing in React Aria, visit the React Aria Routing Guide.
CLIForms
On this page
  * Introduction
  * HeroUIProvider Setup
  * Router Options
  * Next.js
  * App Router
  * Add the `useRouter`
  * Add Provider to Root
  * Next.js Base Path (Optional)
  * Pages Router
  * React Router
  * Remix
  * TanStack
  * Usage examples
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
