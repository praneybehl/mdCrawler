Skip to main content
Version: v7.0.0
On this page
## Static Exports​
### Configure next config​
You need to adjust settings in `next.config.mjs` to disable image optimization and modify the `output` mode as follows:
next.config.mjs
```
import"./src/env.mjs";/** @type {import('next').NextConfig} */const nextConfig ={ output:"export", images:{  unoptimized:true,  remotePatterns:[{    protocol:"https",    hostname:"randomuser.me",    pathname:"/api/portraits/**",},// ... repeat for each domain you want to allow],}, reactStrictMode:false,};exportdefault nextConfig;
```

### Remove NextAuth​
Now, follow the step-by-step process in our documentation here to remove NextAuth, as it requires a server for authentication-related API routes.
### Unsupported Features​
Next.js allows you to export your application as a static website, but some features are not supported in this mode. For example, you cannot use dynamic routes, fallback pages, or incremental static regeneration. You can check the Official Next.js documentation.
### Dynamic Routes​
If you are using **Dynamic page** Like `[id]` or `[slug]` for your application then you need to Dynamic Routes without `generateStaticParams()`.
### Build​
Now Times to run `pnpm build` and when it's done it's look like this:
![build](https://isomorphic-doc.vercel.app/assets/images/build-3101e4fed0bbb4aafdea6f860b6a76d6.png)
Now Check is it working fine or not run `pnpm start`. If it's showing an error then run `npx serve@latest out` for example:
![pnpm-start](https://isomorphic-doc.vercel.app/assets/images/pnpm-start-d7b22a2b0d5c5ca0cfb890c1aa1127e7.png)
  * Static Exports
    * Configure next config
    * Remove NextAuth
    * Unsupported Features
    * Dynamic Routes
    * Build


