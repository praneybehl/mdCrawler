# Your Privacy
This site uses tracking technologies. You may opt in or opt out of the use of these technologies.
DenyAccept all
Consent Settings
Privacy Policy
Your Privacy
This site uses tracking technologies. You may opt in or opt out of the use of these technologies.
Marketing
Off
Marketing cookies and services are used to deliver personalized advertisements, promotions, and offers. These technologies enable targeted advertising and marketing campaigns by collecting information about users' interests, preferences, and online activities. 
Analytics
Off
Analytics cookies and services are used for collecting statistical information about how visitors interact with a website. These technologies provide insights into website usage, visitor behavior, and site performance to understand and improve the site and enhance user experience.
Functional
Off
Functional cookies and services are used to offer enhanced and personalized functionalities. These technologies provide additional features and improved user experiences, such as remembering your language preferences, font sizes, region selections, and customized layouts. Opting out of these cookies may render certain services or functionality of the website unavailable.
Essential
On
Essential cookies and services are used to enable core website features, such as ensuring the security of the website. 
SaveDenyAccept all
Privacy Policy
Menu
Using App Router
Features available in /app
Using Latest Version
15.2.0
Using App Router
Features available in /app
Using Latest Version
15.2.0
API ReferenceFunctionsgenerateSitemaps
# generateSitemaps
You can use the `generateSitemaps` function to generate multiple sitemaps for your application.
## Returns
The `generateSitemaps` returns an array of objects with an `id` property.
## URLs
Your generated sitemaps will be available at `/.../sitemap/[id].xml`. For example, `/product/sitemap/1.xml`.
## Example
For example, to split a sitemap using `generateSitemaps`, return an array of objects with the sitemap `id`. Then, use the `id` to generate the unique sitemaps.
app/product/sitemap.ts
TypeScript
JavaScriptTypeScript
```
import { BASE_URL } from'@/app/lib/constants'
exportasyncfunctiongenerateSitemaps() {
// Fetch the total number of products and calculate the number of sitemaps needed
return [{ id:0 }, { id:1 }, { id:2 }, { id:3 }]
}
exportdefaultasyncfunctionsitemap({
 id,
}: {
 id:number
}):Promise<MetadataRoute.Sitemap> {
// Google's limit is 50,000 URLs per sitemap
conststart= id *50000
constend= start +50000
constproducts=awaitgetProducts(
`SELECT id, date FROM products WHERE id BETWEEN ${start} AND ${end}`
 )
returnproducts.map((product) => ({
  url:`${BASE_URL}/product/${product.id}`,
  lastModified:product.date,
 }))
}
```

## Version History
Version| Changes  
---|---  
`v15.0.0`| `generateSitemaps` now generates consistent URLs between development and production  
`v13.3.2`| `generateSitemaps` introduced. In development, you can view the generated sitemap on `/.../sitemap.xml/[id]`. For example, `/product/sitemap.xml/1`.  
## Next Steps
Learn how to create sitemaps for your Next.js application.
### sitemap.xml
API Reference for the sitemap.xml file.
Was this helpful?
supported.
Send
