Skip to main content
Version: v7.0.0
On this page
## Create New Page​
To create a new page, follow these steps:
  1. Create a new folder in `apps/isomorphic/src/app/(hydrogen)`, for example, `new-page`.
  2. Inside the `new-page` folder, create a TypeScript file named `page.tsx`.
  3. Add the following code to page.tsx:


```
import{Metadata}from"next";importPageHeaderfrom"@/app/shared/page-header";// SEO metadataexportconst metadata:Metadata={ title:"New Page | Isomorphic",};const pageHeader ={ title:"NewPage", breadcrumb:[{   href:"/",   name:"Home",},{   name:"NewPage",},],};exportdefaultfunctionNewPage(){return(<><PageHeadertitle={pageHeader.title}breadcrumb={pageHeader.breadcrumb}/></>);}
```

Remember to replace the content inside the `NewPage` component with your actual page content.
Also, note that there is a blank page example located in `src/app/(hydrogen)/blank` that you can use as a reference.
  * Create New Page


