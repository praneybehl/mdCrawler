Follow us on 
X
to hear about the changes first.
  * Feb 14, 2025
## Additional options for sharing deployments externally
![Deployment Sharing Dark](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F72o8OiCQSfuuS4jL4Wk9w8%2F113c80bd5e09b07ddd52ed8b4cf0b8e6%2FDeployment_Sharing_Light.jpg&w=3840&q=75)![Deployment Sharing Dark](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F7gRI2IZNRkLpjpjBuj6PBj%2F472438d48a52d960e92b56ea6e887f44%2FDeployment_Sharing_Dark.jpg&w=3840&q=75)
You can now share deployments with external collaborators. Previously, invitations, access requests, and shareable links were limited to the preview URL for a branch or custom aliases.
The share modal—accessible by selecting **Share** on a deployment page or from the Vercel Toolbar menu—now allows sharing the specific deployment you are on or the always up-to-date preview URL for the branch.
Read more about sharing deployments. 
![Avatar for gkaragkiaouris](https://vercel.com/api/www/avatar?u=gkaragkiaouris&s=44)![Avatar for kitfos](https://vercel.com/api/www/avatar?u=kitfos&s=44)![Avatar for skllcrn](https://vercel.com/api/www/avatar?u=skllcrn&s=44)
George Karagkiaouris, Kit Foster, Christopher Skillicorn
  * Feb 14, 2025
## Automated DNS configuration with Domain Connect
![Domain connect dark](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F5mL8o0y3KKibm7HTYTzGkv%2F24640b6c57aeb728f39c2479fb6c2466%2Fimage.png&w=3840&q=75)![Domain connect dark](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F1USuH0Yt9t06HjozowsQ65%2Fd1a45e830395de07981b5c92a43211ae%2Fimage__1_.png&w=3840&q=75)
Vercel now supports Domain Connect, an open standard that simplifies DNS configuration. With one click, you can set up your domain without manually copying DNS records—saving time and reducing errors.
Cloudflare-managed domains are now supported with more providers coming soon.
**To get started:**Add a new domain to your Vercel project, and Vercel will detect if your domain qualifies for setup through Domain Connect, prompting you to proceed automatically or configure it manually.
We're also implementing Domain Connect as a DNS provider, enabling external services to configure Vercel Domains just as easily.
Learn more about Vercel domains.
![Avatar for rhyssullivan](https://vercel.com/api/www/avatar?u=rhyssullivan&s=44)![Avatar for megbird](https://vercel.com/api/www/avatar?u=megbird&s=44)![Avatar for mglagola](https://vercel.com/api/www/avatar?u=mglagola&s=44)+2
Rhys S, Meg B, Mark G, Dillon M
  * Feb 13, 2025
## Support for React Router v7
![RRv7 Dark](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F7GcVmscGYK75LuQqHIXyCJ%2F1802d0a16d2f6e1cc202bf4e143119e0%2FRRv7_Light.jpg&w=3840&q=75)![RRv7 Dark](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F7sc6zKPM4smZHtfsZ0nzYY%2Fe9c7566d04fd801b48ca495bd56ee994%2FRRv7_Dark.jpg&w=3840&q=75)
Vercel now supports React Router v7 applications when used as a framework:
react-router.config.ts
```

import{ vercelPreset }from"@vercel/react-router/vite";
import type {Config}from"@react-router/dev/config";
exportdefault{
 ssr:true,
 presets:[vercelPreset()],
} satisfies Config;

```

Configuring your React Router application with the Vercel preset.
This includes support for server-rendered React Router applications using Vercel's Fluid compute. Further, the Vercel preset intelligently splits application bundles across Vercel Functions, and supports custom server entry points.
Deploy React Router to Vercel or learn more about React Router on Vercel.
![Avatar for tootallnate](https://vercel.com/api/www/avatar?u=tootallnate&s=44)
Nathan Rajlich
Show more

**Ready to deploy?** Start building with a free account. Speak to an expert for your _Pro_ or _Enterprise_ needs.
Start Deploying
Contact Sales
**Explore Vercel Enterprise** with an interactive product tour, trial, or a personalized demo.
Explore Enterprise
