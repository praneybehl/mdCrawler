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
Build Output API
Reference
# Build Output API (v3)
The Build Output API is a file-system-based specification for a directory structure that can produce a Vercel deployment.
Table of Contents
The Build Output API is a file-system-based specification for a directory structure that can produce a Vercel deployment.
Framework authors can take advantage of framework-defined infrastructure by implementing this directory structure as the output of their build command. This allows the framework to define and use all of the Vercel platform features.
## Overview
The Build Output API closely maps to the Vercel product features in a logical and understandable format.
It is primarily targeted toward authors of web frameworks who would like to utilize all of the Vercel platform features, such as Vercel Functions, Routing, Caching, etc.
If you are a framework author looking to integrate with Vercel, you can use this reference as a way to understand which files the framework should emit to the `.vercel/output` directory.
If you are not using a framework and would like to still take advantage of any of the features that those frameworks provide, you can create the `.vercel/output` directory and populate it according to this specification yourself.
You can find complete examples of Build Output API directories in vercel/examples.
Check out our blog post on using the Build Output API to build your own framework with Vercel.
## Known limitations
Native Dependencies: Please keep in mind that when building locally, your build tools will compile native dependencies targeting your machine’s architecture. This will not necessarily match what runs in production on Vercel.
For projects that depend on native binaries, you should build on a host machine running Linux with a `x64` CPU architecture, ideally the same as the platform Build Image.
## Next steps
### Configuration
Learn about the Build Output Configuration file, which is used to configure the behavior of a Deployment.
### Vercel Primitives
Learn about the Vercel platform primitives and how they work together to create a Vercel Deployment.
### Features
Learn how to implement common Vercel platform features through the Build Output API.
Last updated on September 10, 2024
Previous
Vercel SDK
Next
Configuration
Was this helpful?
supported.
Send
AskAsk v0
Build Output APIAskAsk v0
