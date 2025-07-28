Skip to main content
Version: v7.0.0
On this page
## Frequently Asked Questions​
Since we offer six different layouts, in this example, we’ll primarily focus on the Hydrogen layout for demonstration.
### How to change the Logo?​
Go to `src/layouts/hydrogen/sidebar.tsx` and change the logo component here with your component.
src/layouts/hydrogen/sidebar.tsx
```
"use client";importLinkfrom"next/link";importcnfrom"@core/utils/class-names";importSimpleBarfrom"@core/ui/simplebar";importLogofrom"@core/components/logo";import{SidebarMenu}from"./sidebar-menu";exportdefaultfunctionSidebar({ className }:{ className?:string}){return(<asideclassName={cn("fixed bottom-0 start-0 z-50 h-full w-[270px] border-e-2 border-gray-100 bg-white dark:bg-gray-100/50 2xl:w-72",    className)}><divclassName="sticky top-0 z-40 bg-gray-0/10 px-6 pb-5 pt-5 dark:bg-gray-100/5 2xl:px-8 2xl:pt-6"><Linkhref={"/"}aria-label="Site Logo"className="text-gray-800 hover:text-gray-900"><LogoclassName="max-w-[155px]"/></Link></div><SimpleBarclassName="h-[calc(100%-80px)]"><SidebarMenu/></SimpleBar></aside>);}
```

### How to change the site title for any page?​
In this example we are going to change the site title for home page. Go to `src/app/(hydrogen)/page.tsx` file. You will see something like this.
src/app/(hydrogen)/page.tsx
```
importFileDashboardfrom"@/app/shared/file/dashboard";import{ metaObject }from"@/config/site.config";exportconst metadata ={...metaObject(),};exportdefaultfunctionFileDashboardPage(){return<FileDashboard/>;}
```

The highlighted code is the site title for the page. You can learn more about Next.js Metadata from Next.js Official Documentation.
This is the function that is used to generate the metadata for the page. You can change the title of the page by changing the `title` parameter of the `metaObject` function.
```
exportconst metaObject =( title?:string, openGraph?:OpenGraph, description:string= siteConfig.description):Metadata=>{return{  title: title ?`${title} - Isomorphic Furyroad`: siteConfig.title,  description,  openGraph: openGraph ??{   title: title ?`${title} - Isomorphic Furyroad`: title,   description,   url:"https://isomorphic-furyroad.vercel.app",   siteName:"Isomorphic Furyroad",// https://developers.google.com/search/docs/appearance/site-names   images:{    url:"https://s3.amazonaws.com/redqteam.com/isomorphic-furyroad/itemdep/isobanner.png",    width:1200,    height:630,},   locale:"en_US",   type:"website",},};};
```

  * Frequently Asked Questions
    * How to change the Logo?
    * How to change the site title for any page?


