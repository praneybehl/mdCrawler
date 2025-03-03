🚀Generate, edit and deploy beautiful apps
HeroUI Chat
HeroUI v2.7.0 🔥
# Make 
# beautiful 
# websites regardless of your design experience.
## Beautiful, fast and modern React UI library for building accessible and customizable web applications.
Get Started
```
$ npx heroui-cli@latest init
```

GitHub
Input
![Professional camera](https://www.heroui.com/_next/image?url=%2Fimages%2Fcard-example-6.webp&w=256&q=75)
Camera
$525
Notes
Tasks
Files
![Zoey Lang](https://www.heroui.com/avatars/avatar-1.webp)
#### Zoey Lang
##### @zoeylang
Follow
Full-stack developer, @hero_ui lover she/her 🎉
4
Following
97.1K
Followers
Tooltip
![Woman listing to music](https://www.heroui.com/_next/image?url=%2Fimages%2Fhero-card.webp&w=640&q=75)
Available soon.
Notify me
Themeable
Provides a plugin to customize default themes, you can change all semantic tokens or create an entire new theme.
Fast
Built on top of Tailwind CSS, which means no runtime styles, and no unnecessary classes in your bundle.
Light & Dark UI
Automatic dark mode recognition, HeroUI automatically changes the theme when detects HTML theme prop changes.
Unique DX
HeroUI is fully-typed to minimize the learning curve, and provide the best possible developer experience.
### Supported and backed by
Your Company
# Apply your own
# theming 
# decisions.
HeroUI provides a custom TailwindCSS plugin that allows you to customize the default themes or create your own.
HeroUI
Modern
Elegant
Retro
![Shoes theme example](https://www.heroui.com/_next/image?url=%2Fimages%2Fshoes-1.png&w=3840&q=75)
# Nike Adapt BB 2.0
Consistent, customized fit, game-changing.
$279.97
$350
20% off
XS
S
M
L
XL
Buy nowAdd to bag
Learn more
```

tailwind.config.js
const { heroui } = require("@heroui/react");

module.exports = {

 // ...

 plugins: [

  heroui({

   themes: {

    light: {

     colors: {

      primary: "#0072f5",

     }

    },

    dark: {

     colors: {

      primary: "#0072f5",

     }

    },

   },

  }),

 ],

};

module.exports = {

 // ...

 plugins: [

  heroui({

   themes: {

    light: {

     colors: {

      primary: "#7828c8",

     }

    },

    dark: {

     colors: {

      primary: "#9353d3",

     }

    },

   },

  }),

 ],

};

module.exports = {

 // ...

 plugins: [

  heroui({

   themes: {

    light: {

     colors: {

      primary: "#FFFFFF",

     }

    },

    dark: {

     colors: {

      primary: "#000000",

     }

    },

   },

  }),

 ],

};

module.exports = {

 // ...

 plugins: [

  heroui({

   themes: {

    light: {

     colors: {

      primary: "#FFD34E",

      secondary: "#EE457E",

      background:"#F4E8D1"

     }

    },

    dark: {

     colors: {

      primary: "#FFD34E",

      secondary: "#EE457E",

      background: "#E1CA9E"

     }

    },

   },

  }),

 ],

};


```

![custom themes background](https://www.heroui.com/gradients/blue-purple-1.svg)
# Accessibility
# out of the 
# box.
HeroUI components are built on top of React Aria ensuring exceptional accessibility support as a top priority.
Keyboard navigation
Managed focus
Collision aware
Alignment control
Screen reader support
Typehead support
Learn more
Actions
![a11y background](https://www.heroui.com/gradients/green.svg)
# Dark mode
# is 
# effortless.
HeroUI comes with a fully well-scaled default dark theme that you can apply to your application with just adding the `dark` attribute to your `html`.
![Album cover](https://www.heroui.com/_next/image?url=%2Fimages%2Falbum-cover.png&w=640&q=75)
Daily Mix
12 Tracks
Frontend Radio
1:23
4:32
```

_app.tsx
import React from "react";

import {HeroUIProvider} from "@heroui/react";

const Application = ({Component, pageProps}) => {

 return (

  <HeroUIProvider>

<main className={isDark ? "dark" : "light"}>

<Component {...pageProps} />

</main>

</HeroUIProvider>

 );

};

export default Application; 


```

Learn more
# Customization made
# easy.
HeroUI is based on Tailwind Variants, it simplifies component slots customization while avoiding Tailwind class conflicts.
```

custom-button.tsx
import React from 'react';

import {Button} from '@heroui/react';

import confetti from 'canvas-confetti';

const CustomButton = () => {

 const handleConfetti = () => {

  confetti({...});

 };

 return (

  <Button
   ref={buttonRef}
   disableRipple
   className="relative overflow-visible rounded-full hover:-translate-y-1 px-12 shadow-xl bg-background/30 after:content-[''] after:absolute after:rounded-full after:inset-0 after:bg-background/40 after:z-[-1] after:transition after:!duration-500 hover:after:scale-150 hover:after:opacity-0"
   size="lg"
   onPress={handleConfetti}
  >

   Press me

</Button>

 );

};

export default CustomButton;


```

Press me
Learn more
PRO
# Ship 
# faster 
# with 
# beautiful 
# components
Premade templates of over 210+ beautiful and responsive components, professionally created by the team behind HeroUI.
210+ Components
Lifetime Access
Free Updates
Figma Files Included
Explore HeroUI Pro
![Hero Background](https://www.heroui.com/images/herouipro-section-background.webp)
# Last 
# but
# not 
# least.
A fully-featured React UI library.
React server components
All HeroUI components already include the `"use client"` directive, which means you can import and use them directly in your RSC.
Accessible components
HeroUI components follow the WAI-ARIA guidelines, provide keyboard support and sensible focus management.
Focus interactions
Focus ring will appear only when user navigates with keyboard or screen reader.
Multiple packages
HeroUI is divided into multiple packages, so you can install only the components you need.
TypeScript based
Build type safe applications, HeroUI has a fully-typed API to minimize the learning curve, and help you build applications.
Override components tags
A polymorphic `as` prop is included in all HeroUI components.
No runtime styles
HeroUI is based on Tailwind CSS, it means that there are no runtime styles, and no unnecessary classes in your bundle.
Beautifully designed
HeroUI components are unique and are not tied to any visual trend or design rule, which makes us unique and of course your projects as well.
# Support HeroUI 
Using HeroUI in a profit-making product, as a freelancer, or for fun projects? Your contributions will help to make HeroUI better.
Open Collective
Sponsor the HeroUI maintainers.
Patreon
Sponsor the creator, Junior Garcia.
![JO](https://www.heroui.com/sponsors/undefined)JO![DH](https://www.heroui.com/sponsors/undefined)DH![MA](https://www.heroui.com/sponsors/292380.jpg)![LO](https://www.heroui.com/sponsors/327844.jpg)![WI](https://www.heroui.com/sponsors/347048.jpg)![CH](https://www.heroui.com/sponsors/374896.jpg)![PR](https://www.heroui.com/sponsors/375034.jpg)![LI](https://www.heroui.com/sponsors/395990.jpg)![RH](https://www.heroui.com/sponsors/404415.jpg)![HI](https://www.heroui.com/sponsors/407510.jpg)![KR](https://www.heroui.com/sponsors/undefined)KR![EL](https://www.heroui.com/sponsors/438158.jpg)![GA](https://www.heroui.com/sponsors/undefined)GA![JA](https://www.heroui.com/sponsors/439182.jpg)JA![EN](https://www.heroui.com/sponsors/442878.jpg)![CO](https://www.heroui.com/sponsors/571230.jpg)![MO](https://www.heroui.com/sponsors/000000.webp)
# Let's make the
# Web 
# Prettier
Experience it firsthand and show us your creations!
Get StartedGithub
Getting Started
Make beautiful, modern, and fast websites/applications regardless of your design experience.
HeroUI + Next.js
HeroUI is fully compatible with the new Next.js `app/` directory structure.
# Community
Get involved in our community. Everyone is welcome!
X
For announcements, tips and general information.
Discord
To get involved in the community, ask questions and share tips.
Github
To report bugs, request features and contribute to the project.
Build beautiful apps faster
