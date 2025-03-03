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


# Introduction
Welcome to the HeroUI documentation!
![HeroUI banner](https://www.heroui.com/_next/image?url=%2Fheroui-banner.png&w=1920&q=100)
## What is HeroUI?
HeroUI is a UI library for React that helps you build beautiful and accessible user interfaces. Created on top of Tailwind CSS and React Aria.
HeroUI's primary goal is to streamline the development process, offering a beautiful and adaptable system design for an enhanced user experience.
## FAQ
### Is HeroUI a copy-paste library?
No, HeroUI is not a copy-paste library. All components are available through `npm` and can be installed individually or as a whole package.
### How is HeroUI different from TailwindCSS?
  * **TailwindCSS** :
Tailwind CSS is a CSS Framework that provides atomic CSS classes to help you style components, leaving you to handle lots of other things like accessibility, component composition, keyboard navigation, style overrides, etc.
  * **HeroUI** :
HeroUI is a UI library for React that combines the power of TailwindCSS with React Aria to provide complete components (logic and styles) for building accessible and customizable user interfaces. Since HeroUI uses TailwindCSS as its style engine, you can use all TailwindCSS classes within your HeroUI components, ensuring optimal compiled CSS size.


### How is HeroUI different from TailwindCSS components libraries?
TailwindCSS components libraries such as TailwindUI, Flowbite, or Preline, just to name a few, only offer a curated selection of TailwindCSS classes to style your components. They don't provide any React specific components, logic, props, composition, or accessibility features.
In contrast to these libraries, HeroUI is a complete UI library that provides a set of accessible and customizable components, hooks, and utilities.
### How HeroUI deals with TailwindCSS classes conflicts?
We created a TailwindCSS utility library called tailwind-variants that automatically handles TailwindCSS class conflicts. This ensures your custom classes will consistently override the default ones, eliminating any duplication.
### Does HeroUI use runtime CSS?
No. As HeroUI uses TailwindCSS as its style engine, it generates CSS at build time, eliminating the need for runtime CSS. This means that HeroUI is fully compatible with the latest React and Next.js versions.
### Does HeroUI support TypeScript?
Yes, HeroUI is written in TypeScript and has full support for it.
### Can I use HeroUI with other front-end frameworks or libraries, such as Vue or Angular?
No, HeroUI is specifically designed for React as it is built on top of React Aria. However, you can still use the HeroUI components styling part with other frameworks or libraries.
### Why does HeroUI use Framer Motion?
We use Framer Motion to animate some components due to the complexity of the animations and their physics-based nature. Framer Motion allows us to handle these animations in a more straightforward and performant way. In addition, it is well tested and production ready.
## Community
We're excited to see the community adopt HeroUI, raise issues, and provide feedback. Whether it's a feature request, bug report, or a project to showcase, please get involved!
X
For announcements, tips and general information.
Discord
To get involved in the community, ask questions and share tips.
Github
To report bugs, request features and contribute to the project.
## Contributing
PRs on **HeroUI** are always welcome, please see our contribution guidelines to learn how you can contribute to this project.
Design Principles
On this page
  * What is HeroUI?
  * FAQ
  * Is HeroUI a copy-paste library?
  * How is HeroUI different from TailwindCSS?
  * How is HeroUI different from TailwindCSS components libraries?
  * How HeroUI deals with TailwindCSS classes conflicts?
  * Does HeroUI use runtime CSS?
  * Does HeroUI support TypeScript?
  * Can I use HeroUI with other front-end frameworks or libraries, such as Vue or Angular?
  * Why does HeroUI use Framer Motion?
  * Community
  * Contributing
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
