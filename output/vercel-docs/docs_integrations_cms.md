![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-light.cf7eca76.svg)![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-dark.01246f11.svg)
Search...
`⌘ K`
Feedback
Log In
Sign Up
Integrations
CMS
How-to
# Vercel CMS Integrations
Learn how to integrate Vercel with CMS platforms, including Contentful, Sanity, and Sitecore XM Cloud.
Table of Contents
Vercel Content Management System (CMS) Integrations allow you to connect your projects with CMS platforms, including Contentful, Sanity, Sitecore XM Cloud and more. These integrations provide a direct path to incorporating CMS into your applications, enabling you to build, deploy, and leverage CMS-powered features with minimal hassle.
You can use the following methods to integrate your CMS with Vercel:
  * Environment variable import: Quickly setup your Vercel project with environment variables from your CMS
  * Edit Mode through the Vercel Toolbar: Visualize content from your CMS within a Vercel deployments and edit directly in your CMS 
    * Content Link: Lets you visualize content models from your CMS within a Vercel deployments and edit directly in your CMS
  * Deploy changes from CMS: Connect and deploy content from your CMS to your Vercel site


## Environment variable import
The most common way to setup a CMS with Vercel is by installing an integration through the Integrations Marketplace. This method allows you to quickly setup your Vercel project with environment variables from your CMS.
Once a CMS has been installed, and a project linked you can pull in environment variables from the CMS to your Vercel project using the Vercel CLI.
  1. ### Install the Vercel CLI
To pull in environment variables from your CMS to your Vercel project, you need to install the Vercel CLI. Run the following command in your terminal:
pnpmyarnnpm
```
pnpm i -g vercel@latest
```

  2. ### Install your CMS integration
Navigate to the CMS integration you want to install into your project, and follow the steps to install the integration.
  3. ### Pull in environment variables
Once you've installed the CMS integration, you can pull in environment variables from the CMS to your Vercel project. In your terminal, run:
```
vercelenvpull.env.development.local
```



See your installed CMSs documentation for next steps on how to use the integration.
## Edit mode with the Vercel Toolbar
To access Edit Mode:
  1. Ensure you're logged into the Vercel Toolbar with your Vercel account.
  2. Navigate to a page with editable content. The Edit Mode option will only appear in the Vercel Toolbar menu when there are elements on the page matched to fields in the CMS.
  3. Select the Edit Mode option in the toolbar menu. This will highlight the editable fields as Content Links, which turn blue as you hover near them.


The following CMS integrations support Content Link:
  * Contentful
  * Sanity
  * Builder
  * TinaCMS
  * DatoCMS
  * Payload
  * Uniform
  * Strapi


See the Edit Mode documentation for information on setup and configuration.
## Draft mode through the Vercel Toolbar
Draft mode allows you to view unpublished content from your CMS within a Vercel preview, and works with Next.js and SvelteKit. See the Draft Mode documentation for information and setup and configuration.
## Deploy changes from CMS
This method is generally setup through webhooks or APIs that trigger a deployment when content is updated in the CMS. See your CMSs documentation for information on how to set this up.
## Featured CMS integrations
### Agility CMS
The headless CMS for developers
Env varsDeploy from CMS
### DatoCMS
The API-based CMS
Content LinkEnv varsDeploy from CMS
### ButterCMS
The headless CMS for developers
Env varsDeploy from CMS
### Formspree
The form backend for developers
Env varsDeploy from CMS
### Makeswift
The headless CMS for developers
Env varsDeploy from CMS
### Sanity
The unified content platform
Content LinkEnv varsDeploy from CMS
### Contentful
A modern content platform
Content LinkEnv varsDeploy from CMS
### Sitecore XM Cloud
The modern SaaS CMS
Env varsDeploy from CMS
Last updated on December 4, 2024
Previous
Together AI
Next
Agility CMS
Was this helpful?
supported.
Send
AskAsk v0
CMSAskAsk v0
Interested in talking to
a Vercel product expert?
Schedule a call
