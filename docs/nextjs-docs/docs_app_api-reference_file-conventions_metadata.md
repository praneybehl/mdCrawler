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
API ReferenceFile ConventionsMetadata Files
# Metadata Files API Reference
This section of the docs covers **Metadata file conventions**. File-based metadata can be defined by adding special metadata files to route segments.
Each file convention can be defined using a static file (e.g. `opengraph-image.jpg`), or a dynamic variant that uses code to generate the file (e.g. `opengraph-image.js`).
Once a file is defined, Next.js will automatically serve the file (with hashes in production for caching) and update the relevant head elements with the correct metadata, such as the asset's URL, file type, and image size.
> **Good to know** :
>   * Special Route Handlers like `sitemap.ts`, `opengraph-image.tsx`, and `icon.tsx`, and other metadata files are cached by default.
>   * If using along with `middleware.ts`, configure the matcher to exclude the metadata files.
> 

### favicon, icon, and apple-icon
API Reference for the Favicon, Icon and Apple Icon file conventions.
### manifest.json
API Reference for manifest.json file.
### opengraph-image and twitter-image
API Reference for the Open Graph Image and Twitter Image file conventions.
### robots.txt
API Reference for robots.txt file.
### sitemap.xml
API Reference for the sitemap.xml file.
Was this helpful?
supported.
Send
