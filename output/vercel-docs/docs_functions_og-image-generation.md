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
Open Graph Image Generation
# Open Graph (OG) Image Generation
Learn how to optimize social media image generation through the Open Graph Protocol and @vercel/og library.
Table of Contents
Next.js (/app)
To assist with generating dynamic Open Graph (OG) images, you can use the Vercel `@vercel/og` library to compute and generate social card images using Vercel Functions.
## Benefits
  * Performance: With a small amount of code needed to generate images,  functions can be started almost instantly. This allows the image generation process to be fast and recognized by tools like the Open Graph Debugger
  * Ease of use: You can define your images using HTML and CSS and the library will dynamically generate images from the markup
  * Cost-effectiveness: `@vercel/og` automatically adds the correct headers to cache computed images at the edge, helping reduce cost and recomputation

Explore the OG Image Playground
## Supported features
  * Basic CSS layouts including flexbox and absolute positioning
  * Custom fonts, text wrapping, centering, and nested images
  * Ability to download the subset characters of the font from Google Fonts
  * Compatible with any framework and application deployed on Vercel
  * View your OG image and other metadata before your deployment goes to production through the Open Graph tab


## Runtime support
Vercel OG image generation is supported on the Node.js runtime.
Local resources can be loaded directly using `fs.readFile`. Alternatively, `fetch` can be used to load remote resources.
og.js
```
constfs=require('fs').promises;
constloadLocalImage=async () => {
constimageData=awaitfs.readFile('/path/to/image.png');
// Process image data
};
```

### Runtime caveats
There are limitations when using `vercel/og` with the Next.js Pages Router and the Node.js runtime. Specifically, this combination does not support the `return new Response(…)` syntax. The table below provides a breakdown of the supported syntaxes for different configurations.
Configuration| Supported Syntax| Notes  
---|---|---  
`pages/` + Edge runtime| `return new Response(…)`| Fully supported.  
`app/` + Node.js runtime| `return new Response(…)`| Fully supported.  
`app/` + Edge runtime| `return new Response(…)`| Fully supported.  
`pages/` + Node.js runtime| Not supported| Does not support `return new Response(…)` syntax with `vercel/og`.  
## Usage
### Requirements
  * Install Node.js 22 or newer by visiting nodejs.org
  * Install `@vercel/og` by running the following command inside your project directory. This isn't required for Next.js App Router projects, as the package is already included:


pnpmyarnnpm
```
pnpm i @vercel/og
```

  * For Next.js implementations, make sure you are using Next.js v12.2.3 or newer
  * Create API endpoints that you can call from your front-end to generate the images. Since the HTML code for generating the image is included as one of the parameters of the `ImageResponse` function, the use of `.jsx` or `.tsx` files is recommended as they are designed to handle this kind of syntax
  * To avoid the possibility of social media providers not being able to fetch your image, it is recommended to add your OG image API route(s) to `Allow` inside your `robots.txt` file. For example, if your OG image API route is `/api/og/`, you can add the following line: 
robots.txt
```
Allow: /api/og/*
```

If you are using Next.js, review robots.txt to learn how to add or generate a `robots.txt` file.


### Getting started
Get started with an example that generates an image from static text using Next.js by setting up a new app with the following command:
pnpmyarnnpm
```
pnpm create next-app
```

Create an API endpoint by adding `route.tsx` under the `app/api/og` directory in the root of your project.
Then paste the following code:
Next.js (/app)Next.js (/pages)Other frameworks
app/api/og/route.tsx
TypeScript
TypeScriptJavaScript
```
import { ImageResponse } from'next/og';
// App router includes @vercel/og.
// No need to install it.
exportasyncfunctionGET() {
returnnewImageResponse(
  (
<div
    style={{
     fontSize:40,
     color:'black',
     background:'white',
     width:'100%',
     height:'100%',
     padding:'50px 200px',
     textAlign:'center',
     justifyContent:'center',
     alignItems:'center',
    }}
>
    👋 Hello
</div>
  ),
  {
   width:1200,
   height:630,
  },
 );
}
```

Open inOpen in v0
If you're not using a framework, you must either add `"type": "module"` to your `package.json` or change your JavaScript Functions' file extensions from `.js` to `.mjs`
Run the following command:
pnpmyarnnpm
```
pnpm dev
```

Then, browse to `http://localhost:3000/api/og`. You will see the following image:
![](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1689795055%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Ffunctions%2Fog-image%2Fog-language.png&w=3840&q=75)
### Consume the OG route
Deploy your project to obtain a publicly accessible path to the OG image API endpoint. You can find an example deployment at https://og-examples.vercel.sh/api/static.
Then, based on the Open Graph Protocol, create the web content for your social media post as follows:
  * Create a `<meta>` tag inside the `<head>` of the webpage
  * Add the `property` attribute with value `og:image` to the `<meta>` tag
  * Add the `content` attribute with value as the absolute path of the `/api/og` endpoint to the `<meta>` tag


With the example deployment at https://og-examples.vercel.sh/api/static, use the following code:
index.js
```
<head>
 <title>Hello world</title>
 <meta
property="og:image"
content="https://og-examples.vercel.sh/api/static"
 />
</head>
```

Every time you create a new social media post, you need to update the API endpoint with the new content. However, if you identify which parts of your `ImageResponse` will change for each post, you can then pass those values as parameters of the endpoint so that you can use the same endpoint for all your posts.
In the examples below, we explore using parameters and including other types of content with `ImageResponse`.
## Examples
### Dynamic title
Passing the image title as a URL parameter.
### Dynamic external image
Passing the username as a URL parameter to pull an external profile image for the image generation.
### Emoji
Using emojis to generate the image.
### SVG
Using SVG embedded content to generate the image.
### Custom font
Using a custom font available in the file system to style your image title.
### Tailwind CSS (Experimental)
Using Tailwind CSS (Experimental) to style your image content.
### Internationalization
Using other languages in the text for generating your image.
### Secure URL
Encrypting parameters so that only certain values can be passed to generate your image.
## Technical details
  * Recommended OG image size: 1200x630 pixels
  * `@vercel/og` uses Satori and Resvg to convert HTML and CSS into PNG
  * `@vercel/og` API reference


## Limitations
  * Only `ttf`, `otf`, and `woff` font formats are supported. To maximize the font parsing speed, `ttf` or `otf` are preferred over `woff`
  * Only flexbox (`display: flex`) and a subset of CSS properties are supported. Advanced layouts (`display: grid`) will not work. See Satori's documentation for more details on supported CSS properties
  * Maximum bundle size of 500KB. The bundle size includes your JSX, CSS, fonts, images, and any other assets. If you exceed the limit, consider reducing the size of any assets or fetching at runtime


Last updated on July 16, 2024
Previous
Usage & Pricing
Next
@vercel/og
Was this helpful?
supported.
Send
AskAsk v0
Open Graph Image Generation
Next.js (/app)
AskAsk v0
