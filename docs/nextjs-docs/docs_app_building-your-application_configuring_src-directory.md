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
Building Your ApplicationConfiguringsrc Directory
# src Directory
As an alternative to having the special Next.js `app` or `pages` directories in the root of your project, Next.js also supports the common pattern of placing application code under the `src` directory.
This separates application code from project configuration files which mostly live in the root of a project, which is preferred by some individuals and teams.
To use the `src` directory, move the `app` Router folder or `pages` Router folder to `src/app` or `src/pages` respectively.
![An example folder structure with the `src` directory](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Flight%2Fproject-organization-src-directory.png&w=3840&q=75)![An example folder structure with the `src` directory](https://nextjs.org/_next/image?url=https%3A%2F%2Fh8DxKfmAPhn8O0p3.public.blob.vercel-storage.com%2Fdocs%2Fdark%2Fproject-organization-src-directory.png&w=3840&q=75)
> **Good to know** :
>   * The `/public` directory should remain in the root of your project.
>   * Config files like `package.json`, `next.config.js` and `tsconfig.json` should remain in the root of your project.
>   * `.env.*` files should remain in the root of your project.
>   * `src/app` or `src/pages` will be ignored if `app` or `pages` are present in the root directory.
>   * If you're using `src`, you'll probably also move other application folders such as `/components` or `/lib`.
>   * If you're using Middleware, ensure it is placed inside the `src` directory.
>   * If you're using Tailwind CSS, you'll need to add the `/src` prefix to the `tailwind.config.js` file in the content section.
>   * If you are using TypeScript paths for imports such as `@/*`, you should update the `paths` object in `tsconfig.json` to include `src/`.
> 

## Next Steps
### Project Structure
An overview of the folder and file conventions in Next.js, and how to organize your project.
Was this helpful?
supported.
Send
