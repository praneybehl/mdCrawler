Skip to main content
Version: v7.0.0
On this page
## Adding a new item to sidebar​
To add a fresh item to the sidebar, navigate to `apps/isomorphic/src/layout/hydrogen/menu-items.tsx`. Locate the menuItems constant, which houses all sidebar items.
Each menu item is an object with properties like `name`, `href`, `icon`, and `dropdownItems`. Follow this template:
apps/isomorphic/src/layouts/hydrogen/menu-items.tsx
```
exportconst menuItems =[...previousMenuItems,{name:"Your new Menu",href:"menu-url",// optionalicon:<PiFileImageDuotone/>,// optional// optional, if your wants children'sdropdownItems:[{name:"Products",href: routes.eCommerce.products,},],},];
```

Customize and expand your sidebar effortlessly!
### Menu Item Type​
```
{ name:string; href?:string; icon?:JSX.Element; dropdownItems?:undefined;}
```

  * Adding a new item to sidebar
    * Menu Item Type


