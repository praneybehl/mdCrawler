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
Platform
Deployments
Conceptual
# Deploying to Vercel
Learn how to create Deployments on Vercel using Git, Vercel CLI, Deploy Hooks, and Vercel REST API.
Table of Contents
A Vercel deployment is the result of a successful build of your project. With any new deployment, Vercel automatically creates a new and unique Generated URL that you or your team can use to preview the changes in a live environment.
You can also enable visitors to leave feedback or interact with your preview deployments through the Vercel Toolbar.
## Deployment Methods
You can deploy your projects to Vercel with the following methods:
  * Git
  * Vercel CLI
  * Deploy Hooks
  * Vercel REST API


## Deployment Lifecycle
The deployment lifecycle includes several stages from development to production:
  1. Local Development: You and your team will work in a personalized, local environment. You can pull the latest `env.local` file to make sure the requirement environment variables are available for each user. See Local Development for more information.
  2. Commit and build: When you're ready, you can push your code to a development branch on your connected Git repository. Each commit initiates a deployment, part of which is the build step. Vercel uses a build container to compile your code. You can learn more about the build process in the Builds section.
  3. Preview: Once Vercel has created a successful build, it will run checks and assign the relevant domains to create a deployments with a generated URL. This deployment is created in a production-like environment, and you can set specific pre-production environment variables. Deployment Protection is enabled on all pre-production deployments by default.
  4. Production: Once you've gone through your development cycle, you'll eventually merge or commit your changes to your production branch, which is usually `main`. Vercel will go through the build and deploy process again, but this time will use production environment variables. At the end of this process, your deployment will automatically be assigned domains, including any custom domains you have added. This process happens automatically, but you can also manually promote a deployment to production if you need to. To learn more see Promoting Deployments. You can also learn more about the production deployment state.
  5. Retention: After active use, deployments enter a retention phase based on the policies set, until they are marked as deleted. At this point the deployment will serve a 410 status code. 
Current production deployments are not removed under retention policies and become eligible for removal only after they are no longer active.
  6. Recovery: A period of 30 days after a deployment was marked for deletion, during which the deployment can be restored back to its original state. 
After the recovery period has passed, a deployment can't be restored.


## Accessing deployments
By default, Vercel automatically generates a URL for each deployment that is made for a pre-production or production environment. You can use this URL to access the deployment.
  * Preview: 
    * When working with Git, you'll get a URL for the branch and for each commit, which you can access through your pull request or through the dashboard.
    * When working with CLI, you can access the URL from the standard output to see the latest deployment for the project.
  * Production: You can access the URL from the Deployments tab of your project in the Vercel Dashboard. From here, you'll see two URLS: 
    * The production deployment domain the relates to the specific commit that was promoted to production.
    * The domain that is aliased to the production deployment domain. This is what your users will use to access your site.


## Using the dashboard
There are a number of ways to interact with your deployments from the Vercel Dashboard:
  * Deployment Summary: This is a detailed overview of all the artifacts generated from your build, including edge middleware, static assets, functions, and ISR functions. You can use this summary to understand the output of your build and determine what's being deployed. See Deployment Summary to learn more.
  * Production Deployment: When you select your project from the dashboard, you'll see the Project Overview page, which shows all the important information about your production deployment including the generated URL, the branch and commit that was deployed, the Speed Insights score, and a link to the logs. See the Project Dashboard to learn more.
  * Deployments Overview: To manage a deployment, select the project in the dashboard and click the Deployments tab. From the overview, you can sort your deployments by branch, environment, or status. You can also interact with your deployment by redeploying it, inspecting it, assigning it a domain, and more.


See Managing Deployments to learn more.
### Deployment Summary
When you deploy your website to Vercel, the platform generates multiple outputs as a result of your build. Those outputs could be Edge Middleware, Static Assets (e.g. HTML, CSS, JavaScript files), Vercel Functions, or ISR Functions.
The deployment summary provides a detailed overview of all these outputs, organized by the type. You can use this summary to understand the output of your build and determine what's being deployed.
To access the deployment summary:
  1. From the dashboard, select your project.
  2. Select the Deployments tab and click the deployment you want to view.
  3. Under Deployment Details, expand the Deployment Summary tab.

![Example of an open deployment summary.](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1689795055%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fdeploy-outputs-light.png&w=3840&q=75)![Example of an open deployment summary.](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1689795055%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fdeploy-outputs-dark.png&w=3840&q=75)Example of an open deployment summary.
### What information is available in this summary?
In the deployment summary, you can see a list of all the artifacts generated from your build and specific information about them.
  * Edge Middleware: matcher
  * Static Assets: name and size
  * Functions: type, name, runtime, size and region
  * ISR Functions: name, runtime, size and region. ISR functions are grouped by related path


You can also see the time it takes to deploy your application, and the framework, when available.
Last updated on December 16, 2024
Previous
Troubleshoot a Build
Next
Deploy to Vercel
Was this helpful?
supported.
Send
AskAsk v0
DeploymentsAskAsk v0
