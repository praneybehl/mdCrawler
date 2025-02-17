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
Workflow
Vercel Toolbar
Reference
# Vercel Toolbar
Learn how to use the Vercel Toolbar to leave feedback, navigate through important dashboard pages, share deployments, use Draft Mode for previewing unpublished content, and Edit Mode for editing content in real-time.
Table of Contents
Vercel Toolbar is available on all plans
The Vercel Toolbar is a tool that assists in the iteration and development process. Through the toolbar, you can:
  * Leave feedback on deployments with Comments
  * Navigate through dashboard pages, and share deployments
  * Read and set Feature Flags
  * Use Draft Mode for previewing unpublished content
  * Edit content in real-time using Edit Mode
  * Inspect for Layout Shifts and Interaction Timing
  * Check for accessibility issues with the Accessibility Audit Tool


## Activating the Toolbar
By default, when the toolbar first shows up on your deployments it is sleeping. This means it will not run any tools in the background or show comments on pages. You can activate it by clicking it or using `CtrlK`. It will start activated if a tool is needed to show you the link you’re visiting, like a link to a comment thread or a link with flags overrides.
Users who have installed the browser extension can toggle on Always Activate in Preferences from the Toolbar menu.
## Enabling or Disabling the toolbar
The Vercel Toolbar is enabled by default for all preview deployments. You can disable the toolbar at the team, project, or session level.
You can also manage its visibility for automation with HTTP headers and through environment variables. To learn more, see Managing the toolbar.
To enable the toolbar for your local or production environments, see Adding the toolbar to your environment.
## Using the Command Menu
You can access the Command Menu by pressing `Ctrlk` on your keyboard.
If your app already implements a `Ctrlk` shortcut, see the Using your own CMD + K feature section.
Alternatively, you can also access the Command Menu through the Vercel Toolbar by clicking the menu icon. If the toolbar hasn't been activated yet, you may have to log in first for the menu to show.
Feature| Description  
---|---  
Search| Quickly search the toolbar and access dashboard pages.  
Quick branch access| View the current branch and commit hash.  
Switch branches| Quickly switch between branches (on preview and production branches - not locally).  
Layout shifts| Open the Layout Shift Tool to identify elements causing layout shifts.  
Interaction timing| Inspect in detail each interaction's latency and view your current session's INP.  
Accessibility audit tool| Automatically check the Web Content Accessibility Guidelines 2.0 level A and AA rules.  
Open Graph| View open graph properties for the page you are on and see what the link preview will look like.  
Comments| Access the Comments panel to leave or view feedback.  
View inbox | View all open comments.  
Navigate to your team| Navigate to your team's dashboard.  
Navigate to your project| Navigate to your project's dashboard.  
Navigate to your deployment| Navigate to your deployment's dashboard.  
Hide Toolbar | Hide the toolbar.  
Disable for session| Disable the toolbar for the current session.  
Set preferences| Set personal preferences for the toolbar.  
Logout| Logout of the toolbar.  
### Using your own cmd+k feature
If your app already has a `Ctrlk` feature, you can still open your menu by:
  * Adding `event.preventDefault()` to the handler that toggles the menu, to prevent Vercel's Command Menu from opening with the `Ctrlk` shortcut
  * Using `Ctrl⇧k` to open Vercel's Command Menu


## Sharing deployments
You can use the Share button in deployments with the Vercel Toolbar enabled, as well as in all preview deployments, to share your deployment's generated URL. When you use the Share button from the toolbar, the URL will contain any relevant query parameters.
To share a deployment:
  1. Go to the deployment you want to share and ensure you're logged into the Vercel Toolbar.
  2. Find the Share button in the Command Menu and select it.
  3. From the Share dialog, ensure you're allowing the right permissions and click Copy Link to copy the deployment URL to your clipboard. To learn more, see Sharing Deployments.


If you're on an Enterprise team, you will be able to see who shared deployment URLs in your audit logs.
## Reposition toolbar
You can reposition the toolbar by dragging it to either side of your screen. It will snap into place and appear there across deployments until you move it again. Repositioning only affects where you see the toolbar, it does not change the toolbar position for your collaborators.
## Command Menu preferences
When logged into the Vercel Toolbar, you'll find a Preferences button in the Command Menu. In this menu, you can update the following settings:
Setting| Description  
---|---  
Notifications| Set when you will receive notifications for comments in the deployment you're viewing  
Theme| Select your color theme  
Layout Shift Detection| Enable or disable the Layout Shift Tool  
Accessibility Audit| Enable or disable the Accessibility Audit Tool  
Measure Interaction Timing| Enable or disable the Interaction Timing Tool  
Browser Extension| Add Vercel's extension to your browser to take screenshots, enable the toolbar in production, and access Always Activate and Start Hidden preferences.  
Always Activate| Sets the toolbar to activate anytime you are authenticated as your Vercel user instead of waiting to be clicked.  
Start Hidden| Sets the toolbar to start hidden. Read more about hiding and showing the toolbar.  
## More resources
### Preview deployments
Preview Deployments allow you to preview changes to your app in a live deployment without merging those changes to your Git project's production branch.
### Comments
Learn how to use Comments to leave feedback on your deployments.
### Draft Mode
Vercel's Draft Mode enables you to view your unpublished headless CMS content on your site before publishing it.
### Edit Mode
Learn how Edit Mode enhances content management for headless CMSs, enabling real-time editing, and seamless collaboration.
Last updated on December 18, 2024
Previous
Workflow
Next
Managing the Toolbar's Visibility
Was this helpful?
supported.
Send
AskAsk v0
Vercel ToolbarAskAsk v0
