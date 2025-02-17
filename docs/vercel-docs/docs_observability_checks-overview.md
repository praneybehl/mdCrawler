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
Observability
Checks
# Working with Checks
Vercel automatically keeps an eye on various aspects of your web application using the Checks API. Learn how to use Checks in your Vercel workflow here.
Table of Contents
Checks are tests and assertions created and run after every successful deployment. Checks API defines your application's quality metrics, runs end-to-end tests, investigates APIs' reliability, and checks your deployment.
Most testing and CI/CD flows occur in synthetic environments. This leads to false results, overlooked performance degradation, and missed broken connections.
## Types of flows enabled by Checks API
Flow Type| Description  
---|---  
Core| Checks `200` responses on specific pages or APIs. Determine the deployment's health and identify issues with code, errors, or broken connections  
Performance| Collects core web vital information for specific pages and compares it with the new deployment. It helps you decide whether to build the deployment or block it for further investigation  
End-to-end| Validates that your deployment has all the required components to build successfully. And identifies any broken pages, missing images, or other assets  
Optimization| Optimizes information about the bundle size. Ensures that your website manages large assets like package and image size  
## Checks lifecycle
![The depiction of how the Checks lifecycle works.](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1687474748%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fchecks%2Fchecks-overview-light.png&w=3840&q=75)![The depiction of how the Checks lifecycle works.](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1687474748%2Fdocs-assets%2Fstatic%2Fdocs%2Fintegrations%2Fchecks%2Fchecks-overview-dark.png&w=3840&q=75)The depiction of how the Checks lifecycle works.
The diagram shows the complete lifecycle of how a check works:
  1. When a deployment is created, Vercel triggers the `deployment.created` webhook. This tells integrators that checks can now be registered
  2. Next, an integrator uses the Checks API to create checks defined in the integration configuration
  3. When the deployment is built, Vercel triggers the `deployment.ready` webhook. This notifies integrators to begin checks on the deployment
  4. Vercel waits until all the created checks receive an update
  5. Once all checks receive a `conclusion`, aliases will apply, and the deployment will go live


Learn more about this process in the Anatomy of Checks API
## Build your Checks Integration
You can build your Checks integration and publish it to the integration marketplace. Your integration should follow these guidelines:
  * Provide low or no configuration solutions for developers to run checks
  * A guided onboarding process for developers from the installation to the end result
  * Provide relevant information about the outcome of the test on the Vercel dashboard
  * Document how to go beyond the default behavior to build custom tests for advanced users


Last updated on July 23, 2024
Previous
OpenTelemetry Collector
Next
Creating Checks
Was this helpful?
supported.
Send
AskAsk v0
ChecksAskAsk v0
Interested in talking to
a Vercel product expert?
Schedule a call
