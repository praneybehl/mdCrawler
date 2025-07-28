Skip to main content
Version: v7.0.0
On this page
## Tables​
We've following types of tables
  1. Basic
  2. Collapsible
  3. Enhanced
  4. Sticky Header
  5. Pagination
  6. Search
  7. Resizable
  8. Pinning
  9. Drag & Drop


We use Tanstack-Table for our table components, here is an basic table example. For more details please check out their official doc here https://tanstack.com/table/latest/docs/introduction
You'll find all our tables in action https://isomorphic-furyroad.vercel.app/tables/basic
apps/packages/isomorphic-core/src/components/table/index.tsx
```
"use client";importTablefrom"@core/components/table";import{ useTanStackTable }from"@core/components/table/custom/use-TanStack-Table";exportdefaultfunctionRecentCustomers({ className }:{ className?:string}){const{ table }=useTanStackTable<RecentCustomersDataType>({  tableData: recentCustomers,// data array  columnConfig: recentCustomersColumns,// column config  options:{   initialState:{    pagination:{     pageIndex:0,     pageSize:7,},},   enableColumnResizing:false,},});return(<><Tabletable={table}/></>);}
```

  * Tables


