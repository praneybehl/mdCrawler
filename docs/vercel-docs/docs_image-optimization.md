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
![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-light.cf7eca76.svg)![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-dark.01246f11.svg)
Search...
`⌘ K`
Feedback
Log In
Sign Up
Infrastructure
Image Optimization
# Image Optimization with Vercel
Vercel has built-in image optimization that automatically serves the optimal image to your visitors.
Table of Contents
Image Optimization is available on all plans
Vercel streamlines the image optimization process and manages the infrastructure for uploading, optimizing, and delivering images based on factors like pixel density, format, size, and quality. These optimized images are cached on the Vercel Edge Network, meaning they're available close to users whenever they're requested.
## Get started
Image Optimization works with many frameworks, including Next.js, Astro, and Nuxt, enabling you to optimize images using built-in components.
To start using Image Optimization, follow the quickstart.
For a live example which demonstrates usage with the `next/image` component, see the Image Optimization demo.
If you are building a custom web framework, you can also use the Build Output API to implement Image Optimization. To learn how to do this, see the Build your own web framework blog post.
## Why should I optimize my images on Vercel?
Optimizing images on Vercel provides several advantages for your application:
  * Reduces the size of images and data transferred, enhancing website performance, user experience, and Fast Data Transfer savings.
  * Improving Core Web Vitals, reduced bounce rates, and speeding up page loads.
  * Sizing images to support different devices and use modern formats like WebP and AVIF.
  * When source images cannot be optimized, Vercel will fall back to serving the original image.
  * Vercel manages the infrastructure for generating and caching optimized images at the edge for quick responses.


## How Image Optimization works
The flow of image optimization on Vercel involves several steps, starting from the image request to serving the optimized image.
![The flow of image optimization on Vercel](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1732552943%2Ffront%2Fdocs%2Fimage-optimization%2Fimage-opt-light.png%3Flightbox&w=3840&q=75)![The flow of image optimization on Vercel](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1732552943%2Ffront%2Fdocs%2Fimage-optimization%2Fimage-opt-dark.png%3Flightbox&w=3840&q=75)The flow of image optimization on VercelZoom Image
![The flow of image optimization on Vercel](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1732552943%2Ffront%2Fdocs%2Fimage-optimization%2Fimage-opt-light.png%3Flightbox&w=3840&q=75)![The flow of image optimization on Vercel](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1732552943%2Ffront%2Fdocs%2Fimage-optimization%2Fimage-opt-dark.png%3Flightbox&w=3840&q=75)The flow of image optimization on Vercel
  1. The optimization process starts with your component choice in your codebase:
     * If you use a standard HTML `img` element, Vercel will bypass optimization and serve the image directly from its source.
     * If you use a framework's `Image` component (like `next/image`) it will use Vercel's image optimization pipeline, allowing your images to be automatically optimized and cached.
  2. When Next.js receives an image request, it checks the `unoptimized` prop on the `Image` component or the configuration in the `next.config.ts` file to determine if optimization is disabled.
     * If you set the `unoptimized` prop on the `Image` component to `true`, Next.js bypasses optimization and serves the image directly from its source.
     * If you don't set the `unoptimized` prop or set it to `false`, Next.js checks the `next.config.ts` file to see if optimization is disabled. This configuration applies to all images and overrides the individual component prop.
     * If neither the `unoptimized` prop is set nor optimization is disabled in the `next.config.ts` file, Next.js continues with the optimization process.
  3. If optimization is enabled, Vercel validates the loader configuration (whether using the default or a custom loader) and verifies that the image source URL matches the allowed patterns defined in your configuration (`remotePatterns` or `localPatterns`).
  4. Vercel then checks the status of the edge cache to see if an image has been previously cached:


  * `HIT`: The image is served directly from the cache.
  * `MISS`: The image is fetched, optimized, cached, and then served to the user. 
    * Counts as one source image, and is reflected in your usage metrics.
  * `STALE`: The image is served from the cache while revalidating it in the background. 
    * If the image has not been previously counted as a source image during the current billing period, it will count as one and be reflected in your usage metrics. Otherwise, it will not count again or appear on the usage page.


## When to use Image Optimization
It's important that you are only optimizing images that need to be optimized otherwise you could end up using your source image quota unnecessarily. For example, if you have a small icon or thumbnail that is under 10 KB, you should not use Image Optimization as these images are already very small and optimizing them further would not provide any benefits.
Image Optimization is ideal for:
  * Responsive layouts where images need to be optimized for different device sizes (e.g. mobile vs desktop)
  * Large, high-quality images (e.g. product photos, hero images)
  * User uploaded images
  * Content where images play a central role (e.g. photography portfolios)


In some cases, Image Optimization may not be necessary or beneficial, such as:
  * Small icons or thumbnails (under 10 KB)
  * Animated image formats such as GIFs
  * Vector image formats such as SVG
  * Frequently changing images where caching could lead to outdated content


If your images meet any of the above criteria where Image Optimization is not beneficial, we recommend using the `unoptimized` prop on the Next.js `Image` component. For guidance on SvelteKit, Astro, or Nuxt, see their documentation.
## Setting up remote or local patterns
An important aspect of using the `Image` component is properly setting up remote/local patterns in your `next.config.ts` file. This configuration determines which images are allowed to be optimized.
You can set up patterns for both local images (stored as static assets in your `public` folder) and remote images (stored externally). In both cases you specify the pathname the images are located at.
### Local images
A local image is imported from your file system and analyzed at build time. The import is added to the `src` prop: `src={myImage}`
#### Setting up local patterns
To set up local patterns, you need to specify the pathname of the images you want to optimize. This is done in the `next.config.ts` file:
next.config.ts
```
module.exports= {
 images: {
  localPatterns: [
   {
    pathname:'/assets/images/**',
    search:'',
   },
  ],
 },
};
```

See the Next.js documentation for local patterns for more information.
#### Local images cache key
The cache key for local images is based on the query string parameters, the `Accept` HTTP header, and the content hash of the image URL.
  * Cache Key: 
    * Query string parameters: 
      * `q`: The quality of the optimized image, between 1 (lowest quality) and 100 (highest quality).
      * `w`: The width (in pixels) of the optimized image.
      * `url`: The URL of the optimized image is keyed by content hash e.g. `/assets/me.png` is converted to `3399d02f49253deb9f5b5d1159292099`.
    * `Accept` HTTP header (normalized).
  * Local image cache invalidation: 
    * Redeploying your app doesn't invalidate the image cache.
    * To invalidate, replace the image of the same name with different content, then redeploy.
  * Local image cache expiration: 
    * Cached for up to 31 days on the Edge Network.


### Remote images
A remote image requires the `src` property to be a URL string, which can be relative or absolute.
#### Setting up remote patterns
To set up remote patterns, you need to specify the `hostname` of the images you want to optimize. This is done in the `next.config.ts` file:
next.config.ts
```
module.exports= {
 images: {
  remotePatterns: [
   {
    protocol:'https',
    hostname:'example.com',
    port:'',
    pathname:'/account123/**',
    search:'',
   },
  ],
 },
};
```

In the case of external images, you should consider adding your account id to the `pathname` if you don't own the `hostname`. For example `pathname: '/account123/v12h2bv/**'`. This helps protect your source images from potential abuse.
See the Next.js documentation for remote patterns for more information.
#### Remote images cache key
The cache key for remote images is based on the query string parameters, the `Accept` HTTP header, and the content hash of the image URL.
  * Cache Key: 
    * Query string parameters: 
      * `q`: The quality of the optimized image, between 1 (lowest quality) and 100 (highest quality).
      * `w`: The width (in pixels) of the optimized image.
      * `url`: The URL of the optimized image e.g. https://example.com/assets/me.png.
    * `Accept` HTTP header (normalized).
  * Remote image cache invalidation: 
    * Redeploying your app doesn't invalidate the image cache
    * To invalidate, add a query string to the `src` property (e.g., `?v=2`), then redeploy.
    * Alternatively, you can configure the cache to expire more frequently.
  * Remote image cache expiration: 
    * TTL is determined by the `Cache-Control` `max-age` header from the upstream image or `minimumCacheTTL` config (default: `60` seconds), whichever is larger.
    * If your image content changes frequently, it's best to keep this TTL short.


Once an image is cached, it remains so even if you update the source image. For remote images, users accessing a URL with a previously cached image will see the old version until the cache expires or the image is invalidated. Each time an image is requested, it counts towards your Fast Data Transfer and Edge Request usage for your billing cycle.
See Cost implications for more information, and read more about caching behavior in the Next.js documentation.
## Optimized URL format
When you use the `Image` component in common frameworks and deploy your project on Vercel, Image Optimization automatically adjusts your images for different device screen sizes. The `src` prop you provided in your code is dynamically replaced with an optimized image URL. For example:
  * Next.js: `/_next/image?url={link/to/my/image}&w=3840&q=75`
  * Nuxt.js or Astro: `/_vercel/image?url={link/to/my/image}&w=3840&q=75`
  * Build Output API: `/_vercel/image?url={link/to/my/image}&w=3840&q=75`


## Related
For more information on what to do next, we recommend the following articles:
  * Image Optimization quickstart
  * Managing costs
  * Pricing


Last updated on November 27, 2024
Previous
@vercel/og
Next
Quickstart
Was this helpful?
supported.
Send
AskAsk v0
Image OptimizationAskAsk v0
