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
Builds
Conceptual
# Builds
Understand how the build step works when creating a Vercel Deployment.
Table of Contents
When you create a new project or push a new commit to a project on Vercel, you initiate a deployment. A deployment is made up of a few steps:
  * The build step
  * Running checks
  * Assigning a domain


This guide is focused on the build step, where Vercel validates and builds your source code, outputting all assets into storage.
For any of the supported frameworks, Vercel will automatically configure the build settings with the most common configurations for the framework. If you have specific settings, you can configure the build, output, and environment variables when you create a new Vercel project or within your project's settings.
If your project does not require building, for example, a website with only static source files, you can choose to skip the build step.
## Build process
You can initiate a Vercel deployment in two ways: with Vercel CLI or by pushing changes to a connected Git repository on GitHub, GitLab, or Bitbucket. It's also possible for deployments to be initiated through an integration using Vercel REST API.
Depending on how you initiate the build, Vercel may put it in a queue to ensure we build things in the right order and only build the most recent deployment.
![](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1689795055%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fbuild-step%2Finfra-light.png&w=3840&q=75)![](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1689795055%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fdeployments%2Fbuild-step%2Finfra-dark.png&w=3840&q=75)
A deployment from CLI triggers a build in the build container which provisions resources and updates the deployment's status
  1. Once you trigger a deployment, the build container will receive a request that there is a job available. The build container is a Docker container that uses an Amazon Linux based image and includes some pre-installed packages. The build container runs in a few regions on our Edge Network⁠—you can determine which one by viewing your build logs.
  2. Vercel first authenticates and inspects the request to confirm its authenticity and your permission to create the deployment to protect against unauthorized access and loss of integrity. At this point, Vercel also validates the Vercel configuration in the vercel.json file.
  3. Depending on whether your plan allows for concurrent builds, Vercel may queue your build until other builds from your team have been completed.
  4. If you use Git to initiate your deployment, Vercel performs a shallow clone on your Git repository to fetch the most recent Git commit history. CLI deployments won't do this step—they'll follow the flow in the next step.
  5. If you use Vercel CLI to initiate your deployment, the following flow will happen. Git deployments won't go through this flow:
     * A POST request is made containing the project’s files to be uploaded (without these ignored files) to a scalable, secure, and highly durable data storage service
     * Once the source files have been uploaded, another POST request is made to start the build and deployment process.
  6. Vercel will check for an existing build cache key. If it finds one, it will restore the previous build cache. For more information on the build cache, see the "Caching process" docs.
  7. Now that the build container has your source files, it installs any necessary tools and then will do the actual build by running the build command.
During this phase, the build step transforms the project into a Vercel deployment by executing a builder (or multiple builders, depending on the frameworks) on the source code. The builder can be an internal one provided by Vercel (for example, Next.js builder) or a custom builder that requires installation from an npm registry. If this npm registry is private, see "Private npm packages".
  8. Concurrently, while the build container processes the file, it pings an API endpoint that keeps track of the deployment’s status. Vercel will then use this endpoint to update you on the dashboard, in the CLI, or in your pull request about the live status of the build.
  9. The build container creates a build output that runs on one of Vercel's supported runtimes and provisions resources such as:
     * Vercel Functions for handling API routes and server-side rendered pages
     * Optimized Images
     * Static output
You can check the detailed output from your build on the deployment summary.
  10. Finally, once the resources have been created and provisioned, Vercel uploads them to a dedicated static storage, along with metadata that is used to route the user to the correct location on the network. To learn more about what happens when a user requests these resources, see "Behind the scenes of Vercel's infrastructure - Request phase".


## Build limits
The maximum duration of the build is 45 minutes. When the limit is reached, the build will be interrupted and the deployment will fail. For more information, see "Cancelled Builds due to limits".
The build container is created with a specific amount of resources that cannot be increased.
Each build's cache can be a maximum of 1 GB and applies at the level of each build cache key. The build cache is retained for one month and currently you cannot configure which files are cached.
## Pricing
Manage and Optimize pricingMetric| Description| Priced| Optimize  
---|---|---|---  
Build Time| The amount of time your Deployments have spent being queued or building| Additional concurrent builds| Learn More  
Number of Builds| How many times a build was issued for one of your Deployments| No| N/A  
Last updated on July 23, 2024
Previous
Project Dashboard
Next
Configure a Build
Was this helpful?
supported.
Send
AskAsk v0
BuildsAskAsk v0
