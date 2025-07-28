Skip to main content
Version: v7.0.0
On this page
## Legacy Table​
We've following types of tables
  1. Basic
  2. Collapsible
  3. Enhanced
  4. Sticky Header
  5. Pagination
  6. Search


We use Rc-Table for our table components, here is an basic table example. For more details please check out their official doc here https://table-react-component.vercel.app/
There is no view for legacy table demo. But there is a full featured code example in `apps/isomorphic/src/app/shared/legacy-table-demo`.
apps/packages/isomorphic-core/src/components/controlled-table/index.tsx
```
"use client";importControlledTablefrom"@/components/controlled-table";exportdefaultfunctionBasicTable(){return(<ControlledTableisLoading={isLoading}data={tableData}columns={visibleColumns}scroll={scroll}sticky={sticky}variant={variant}className="mt-4"{...(enablePagination&&{paginatorOptions:{pageSize,...(setPageSize&&{setPageSize}),total:totalItems,current:currentPage,onChange:(page:number)=>handlePaginate(page),},paginatorClassName:cn("mt-4lg:mt-5",noGutter&&"px-5lg:px-7",paginatorClassName),})}/>);}
```

  * Legacy Table


