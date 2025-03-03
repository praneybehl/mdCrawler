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


# HeroUI Provider
API reference for the `HeroUIProvider`.
## Import
Individual
Global
```

```

import{HeroUIProvider}from"@heroui/system";

```


```

## Usage
```

```

```

import*asReactfrom"react";
import{HeroUIProvider}from"@heroui/react";
functionApp(){
return(
<HeroUIProvider>
<YourApplication/>
</HeroUIProvider>
);
}

```


```


```

## Props
`navigate`
  * **Description** : Provides a client side router to all nested components such as Link, Menu, Tabs, Table, etc.
  * **Type** : `((path: Href, routerOptions?: RouterOptions) => void) | undefined`


See Router Guide
`useHref`
  * **Description** : Convert an `href` provided to a link component to a native `href`. For example, a router might accept hrefs relative to a base path, or offer additional custom ways of specifying link destinations. The original href specified on the link is passed to the navigate function of the RouterProvider, and useHref is used to generate the full native href to put on the actual DOM element.
  * **Type** : `((href: Href) => string) | undefined`


See Router Guide
`locale`
  * **Description** : The locale to apply to the children.
  * **Type** : `string | undefined`
  * **Default** : `en-US`


Here's the supported locales. By default, It is `en-US`.
Here's an example to set a Spanish locale.
`defaultDates`
  * **Description** : The default dates range that can be selected in the calendar.
  * **Type** : `{ minDate?: CalendarDate | undefined; maxDate?: CalendarDate | undefined; }`
  * **Default** : `{ minDate: new CalendarDate(1900, 1, 1), maxDate: new CalendarDate(2099, 12, 31) }`


`createCalendar`
  * **Description** : This function helps to reduce the bundle size by providing a custom calendar system.
By default, this includes all calendar systems supported by `@internationalized/date`. However, if your application supports a more limited set of regions, or you know you will only be picking dates in a certain calendar system, you can reduce your bundle size by providing your own implementation of `createCalendar` that includes a subset of these Calendar implementations.
For example, if your application only supports Gregorian dates, you could implement a `createCalendar` function like this:
This way, only GregorianCalendar is imported, and the other calendar implementations can be tree-shaken.
  * **Type** : `((calendar: SupportedCalendars) => Calendar | null) | undefined`


`labelPlacement`
  * **Description** : Determines the position where label should appear, such as inside, outside or outside-left of the component.
  * **Type** : `string` | `undefined`
  * **Possible Values** : `inside` | `outside` | `outside-left` | `undefined`
  * **Default** : `undefined`


`spinnerVariant`
  * **Description** : The default variant of the spinner.
  * **Type** : `string` | `undefined`
  * **Possible Values** : `default` | `simple` | `gradient` | `wave` | `dots` | `spinner`
  * **Default** : `default`


`disableAnimation`
  * **Description** : Disables animations globally. This will also avoid `framer-motion` features to be loaded in the bundle which can potentially reduce the bundle size.
  * **Type** : `boolean`
  * **Default** : `false`


`disableRipple`
  * **Description** : Disables ripple effect globally.
  * **Type** : `boolean`
  * **Default** : `false`


`skipFramerMotionAnimations`
  * **Description** : Controls whether `framer-motion` animations are skipped within the application. This property is automatically enabled (`true`) when the `disableAnimation` prop is set to `true`, effectively skipping all `framer-motion` animations. To retain `framer-motion` animations while using the `disableAnimation` prop for other purposes, set this to `false`. However, note that animations in HeroUI Components are still omitted if the `disableAnimation` prop is `true`.
  * **Type** : `boolean`
  * **Default** : Same as `disableAnimation`


`validationBehavior`
  * **Description** : Whether to use native HTML form validation to prevent form submission when the value is missing or invalid, or mark the field as required or invalid via ARIA.
  * **Type** : `native | aria`
  * **Default** : `native`


`reducedMotion`
  * **Description** : Controls the motion preferences for the entire application, allowing developers to respect user settings for reduced motion. The available options are: 
    * `"user"`: Adapts to the user's device settings for reduced motion.
    * `"always"`: Disables all animations.
    * `"never"`: Keeps all animations active.
  * **Type** : `"user" | "always" | "never"`
  * **Default** : `"never"`


`spinnerVariant`
  * **Description** : The default variant of the spinner.
  * **Type** : `string` | `undefined`
  * **Possible Values** : `default` | `gradient` | `wave` | `dots` | `spinner`
  * **Default** : `default`


## Types
`CalendarDate`
  * **Description** : A CalendarDate represents a date without any time components in a specific calendar system from `@internationalized/date`.
  * **Type** : `import {CalendarDate} from '@internationalized/date';`


### SupportedCalendars
Supported react-aria i18n calendars.
HeroUI CLI
On this page
  * Import
  * Usage
  * Props
  * Types
  * SupportedCalendars
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
