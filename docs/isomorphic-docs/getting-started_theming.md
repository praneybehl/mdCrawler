Skip to main content
Version: v7.0.0
On this page
## Theming​
These are the CSS color variables employed in crafting our template design.
### Light Mode​
apps/isomorphic/src/app/globals.css
```
:root{/*  - gray/natural colors for texts, borders and disabled elements.  - If required we can use as background too. */--gray-0:255255255;/* #ffffff */--gray-50:250250250;/* #fafafa */--gray-100:241241241;/* #f1f1f1 */--gray-200:227227227;/* #e3e3e3 */--gray-300:223223223;/* #dfdfdf */--gray-400:146146146;/* #929292 */--gray-500:102102102;/* #666666 */--gray-600:727272;/* #484848 */--gray-700:515151;/* #333333 */--gray-800:343434;/* #222222 */--gray-900:171717;/* #111111 */--gray-1000:000;/* #000000 *//* ----------------------------------- *//* primary/brand colors *//* ----------------------------------- */--primary-lighter:215227254;/* #D7E3FE */--primary-light:96142251;/* #608EFB */--primary-default:56114250;/* #3872FA */--primary-dark:2988216;/* #1d58d8 *//* ----------------------------------- *//* secondary colors *//* ----------------------------------- */--secondary-lighter:227215252;/* #e3d7fc */--secondary-light:13899210;/* #8a63d2 */--secondary-default:12140202;/* #7928ca */--secondary-dark:7640137;/* #4c2889 *//* ----------------------------------- *//* red/error colors *//* ----------------------------------- */--red-lighter:247212214;/* #f7d4d6 */--red-light:2552626;/* #ff1a1a */--red-default:23800;/* #e00 */--red-dark:19700;/* #c50000 *//* ----------------------------------- *//* orange/warning colors *//* ----------------------------------- */--orange-lighter:255239207;/* #ffefcf */--orange-light:24718585;/* #f7b955 */--orange-default:24516635;/* #f5a623 */--orange-dark:1718710;/* #ab570a *//* ----------------------------------- *//* blue/info colors *//* ----------------------------------- */--blue-lighter:211229255;/* #d3e5ff */--blue-light:50145255;/* #3291ff */--blue-default:0112243;/* #0070f3 */--blue-dark:797209;/* #0761d1 *//* ----------------------------------- *//* green/success colors *//* ----------------------------------- */--green-lighter:185249207;/* #b9f9cf */--green-light:6193103;/* #06C167 */--green-default:413672;/* #048848 */--green-dark:311260;/* #03703C */}
```

### Dark Mode​
And these are the dark mode colors
apps/isomorphic/src/app/globals.css
```
/* dark theme */[data-theme="dark"]{/*   - gray/natural color shades for texts, borders and disabled elements.   - If required we can use as background too.  */--gray-0:000;/* #000000 */--gray-50:171717;/* #111111 */--gray-100:343434;/* #222222 */--gray-200:515151;/* #333333 */--gray-300:727272;/* #484848 */--gray-400:102102102;/* #666666 */--gray-500:146146146;/* #929292 */--gray-600:162162162;/* #a2a2a2 */--gray-700:223223223;/* #dfdfdf */--gray-800:226226226;/* #e2e2e2 */--gray-900:241241241;/* #f1f1f1 */--gray-1000:255255255;/* #ffffff *//* ----------------------------------- *//* secondary colors *//* ----------------------------------- */--secondary-default:13899210;/* #7928ca */--secondary-dark:12140202;/* #4c2889 *//* ----------------------------------- *//* red/error colors *//* ----------------------------------- */--red-lighter:253226221;/* #fde2dd */--red-light:2426534;/* #f24122 */--red-default:1974012;/* #c5280c */--red-dark:1593210;/* #9f200a *//* here you can customize other colors for dark theme if design required */}
```

  * Theming
    * Light Mode
    * Dark Mode


