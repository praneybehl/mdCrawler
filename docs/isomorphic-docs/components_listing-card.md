Skip to main content
Version: v7.0.0
On this page
## Listing Card​
### Preview​
![Listing card preview](https://isomorphic-doc.vercel.app/assets/images/card-listing-ffb011d82cad3c0fee26123a02988b46.png)
### API​
Property| Type| Is Required| Default  
---|---|---|---  
product| Product Type| true  
className| string| false  
title| ReactNode| false  
children| ReactNode| false  
### Product Type​
packages/isomorphic-core/src/components/cards/listing-card.tsx
```
typeProduct={ city:string; country:string; thumbnail:any; rating:number; ratingCount:number; hostname:string; features:string[]; price:{  original:string;  sale:string;}; tag:string;};
```

  * Listing Card
    * Preview
    * API
    * Product Type


