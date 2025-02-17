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
CLI & API
Vercel SDK
How-to
# Vercel SDK
Learn how to use the Vercel SDK to interact with the Vercel REST API.
Table of Contents
The `@vercel/sdk` is a type-safe Typescript SDK that allows you to access the resources and methods of the Vercel REST API.
To view the methods for all endpoints, and explore code examples, see the reference documentation.
## Installing Vercel SDK
To download and install Vercel SDK, run the following command:
pnpmyarnnpm
```
pnpm i @vercel/sdk
```

## Authentication
Vercel Access Tokens are required to authenticate and use the Vercel SDK.
Once you have created a token, you can use it to initialize the SDK as follows:
run.ts
```
import { Vercel } from'@vercel/sdk';
constvercel=newVercel({
 bearerToken:'<YOUR_BEARER_TOKEN_HERE>',
});
```

### Troubleshooting
Make sure that you create a token with the correct Vercel scope. If you face permission (403) errors when you are already sending a token, it can be one of the following problems:
  * The token you are using has expired. Check the expiry date of the token in the Vercel dashboard.
  * The token does not have access to the correct scope, either not the right team or it does not have account level access.
  * The resource or operation you are trying to use is not available for that team. For example, AccessGroups is an Enterprise only feature and you are using a token for a team on the pro plan.


## Examples
Learn how to use Vercel SDK through the following categories of examples:
  * Deployments Automation
  * Project Management
  * Domain Management
  * Team Management
  * Environment Variables
  * Logs and Monitoring
  * Integrations


Last updated on December 9, 2024
Previous
Building Integrations
Next
Build Output API
Was this helpful?
supported.
Send
AskAsk v0
Vercel SDKAskAsk v0
