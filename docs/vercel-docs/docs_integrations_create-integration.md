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
Integrations
Integrate with Vercel
How-to
# Integrate with Vercel
Learn how to create and manage your own integration for internal or public use with Vercel.
Table of Contents
This guide walks you through the process of creating and managing integrations on Vercel, helping you to extend the capabilities of your Vercel projects by connecting with third-party services.
## Understanding native integrations
Given the strong connection and flexibility of native integrations with Vercel, understanding the fundamentals of how they interact with Vercel's platform will facilitate the creation and optimization of native integrations for integration providers.
Review Native Integration Concepts to learn more.
## Creating an integration
Integrations can be created by filling out the Create Integration form. To access the form:
  1. From your Vercel dashboard, select your account/team from the scope selector
  2. Select the Integrations tab to see the Integrations overview
  3. Then, select the Integrations Console button and then select Create
  4. Fill out all the entries in the Create integration form as necessary
  5. At the end of the form, depending on the type of integration you are creating, you must accept the terms provided by Vercel so that your integration can be published
  6. If you are creating a native integration, continue to the Native integration product creation process.


### Native integration product creation
In order to create native integrations, please share your `team_id` and Integration's URL Slug with Vercel in your shared Slack channel (`#shared-mycompanyname`). You can sign up to be a native integration provider here.
You can create your product(s) using the Create product form after you have submitted the integration form.
### Create Integration form details
The Create Integration form must be completed in full before you can submit your integration for review. The form has the following fields:
Field| Description| Required  
---|---|---  
Name| The name of your integration.  
URL Slug| The URL slug for your integration.  
Developer| The owner of the Integration, generally a legal name.  
Contact Email| The contact email for the owner of the integration. This will not be publicly listed.  
Support Contact Email| The support email for the integration. This will be publicly listed.  
Short Description| A short description of your integration.  
Logo| The logo for your integration.  
Category| The category for your integration.  
Website| The website for your integration.  
Documentation URL| The documentation URL for your integration.  
EULA URL| The URL to your End User License Agreement (EULA) for your integration.  
Privacy Policy URL| The URL to your Privacy Policy for your integration.  
Overview| A detailed overview of your integration.  
Additional Information| Additional information about configuring your integration.  
Feature Media| A featured image or video for your integration. You can link up to 5 images or videos for your integration with the aspect ratio of 3:2.  
Redirect URL| The URL the user sees during installation.  
API Scopes| The API scopes for your integration.  
Webhook URL| The URL to receive webhooks from Vercel.  
Configuration URL| The URL to configure your integration.  
Base URL (Native integration)| The URL that points to your integration server  
Redirect Login URL (Native integration)| The URL where the integration users are redirected to when they open your product's dashboard  
Installation-level Billing Plans (Native integration)| Enable the ability to select billing plans when installing the integration  
Integrations Agreement| The agreement to the Vercel terms (which may differ based on the type of integration)  
### Create Product form details
The Create Product form must be completed in full for at least one product before you can submit your product for review. The form has the following fields:
Field| Description| Required  
---|---|---  
Name| The name of your product.  
URL Slug| The URL slug for your product.  
Short Description| A short description of your product.  
Short Billing Plans Description| A short description of your billing plan.  
Metadata Schema| The metadata your product will receive when a store is created or updated.  
Logo| The logo for your product.  
Tags| Tags for the integrations marketplace categories.  
Guides| Getting started guides for specific frameworks.  
Resource Links| Resource links such as documentation.  
Snippets| Add up to 6 code snippets to help users get started with your product.  
## After integration creation
### Native integrations
To create a product for your native integration, follow the steps in Create a product for a native integration.
### Connectable account integrations
Once you have created your connectable account integration, it will be assigned the Community badge and be available for external users to download. You can share it with users either through your site or through the Vercel deploy button.
If you are interested in having your integration listed on the public Integrations page:
  * The integration must have at least 500 active installations (500 accounts that have the integration installed).
  * The integration follows our review guidelines.
  * Once you've reached this minimum install requirement, please email integrations@vercel.com with your request to be reviewed for listing.


### View created integration
You can view all integrations that you have created on the Integrations Console.
To preview an integration's live URL, click View Integration. This URL can be shared for installation based on the integration's visibility settings.
The live URL has the following format:
example-url
```
https://vercel.com/integrations/<slug>
```

Where, `<slug>` is the name you specified in the URL Slug field during the integration creation process.
### View logs
To help troubleshoot errors with your integration, select the View Logs button on the Edit Integration page. You will see a list of all requests made to this integration with the most recent at the top. You can use filters on the left column such as selecting only requests with the `error` level. When you select a row, you can view the detailed information for that request in the right column.
### Community badge
In the Integrations Console, a Community badge will appear under your new integration's title once you have submitted the integration. While integrations with a Community badge do not appear in the marketplace, they are available to be installed through your site or through the Vercel deploy button
Community integrations are developed by third parties and are supported solely by the developers. Before installing, review the developer's Privacy Policy and End User License Agreement on the integration page.
## Installation flow
The installation of the integration is a critical component of the developer experience that must cater to all types of developers. While deciding the installation flow you should consider the following:
  * New user flow: Developers should be able to create an account on your service while installing the integration
  * Existing user flow: With existing accounts, developers should sign in as they install the integration. Also, make sure the forgotten password flow doesn't break the installation flow
  * Strong defaults: The installation flow should have minimal steps and have set defaults whenever possible
  * Advanced settings: Provide developers with the ability to override or expand settings when installing the integration


For the installation flow, you should consider adding the following specs:
Spec Name| Required| Spec Notes  
---|---|---  
Documentation| Yes| Explain the integration and how to use it. Also explain the defaults and how to override them.  
Deploy Button| No| Create a Deploy Button for projects based on a Git repository.  
## Integration support
As an integration creator, you are solely responsible for the support of your integration developed and listed on Vercel. When providing user support, your response times and the scope of support must be the same or exceed the level of Vercel's support. For more information, refer to the Vercel Integrations Marketplace Agreement.
When submitting an integration, you'll enter a support email, which will be listed publicly. It's through this email that integration users will be able to reach out to you.
Last updated on December 18, 2024
Previous
Permissions and Access
Next
Native Integration Concepts
Was this helpful?
supported.
Send
AskAsk v0
Integrate with VercelAskAsk v0
Interested in talking to
a Vercel product expert?
Schedule a call
