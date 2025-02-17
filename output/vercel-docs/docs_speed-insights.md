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
Speed Insights
Conceptual
# Speed Insights Overview
This page lists out and explains all the performance metrics provided by Vercel's Speed Insights feature.
Table of Contents
Speed Insights is available on all plans
Vercel Speed Insights provides you with a detailed view of your website's performance metrics, based on Core Web Vitals, enabling you to make data-driven decisions for optimizing your site. For granular visitor data, use Web Analytics.
The Speed Insights dashboard offers in-depth information about scores and individual metrics without the need for code modifications or leaving the Vercel dashboard.
To get started, follow the quickstart to enable Speed Insights and learn more about the dashboard view and metrics.
When you enable Speed Insights, data will be tracked on all deployed environments, including preview and production deployments.
## Dashboard view
![A snapshot of the Speed Insights tab from the project view.](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1689795055%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fres-chart-light.png&w=3840&q=75)![A snapshot of the Speed Insights tab from the project view.](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1689795055%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fres-chart-dark.png&w=3840&q=75)A snapshot of the Speed Insights tab from the project view.
Once you enable Speed Insights, you can access the dashboard by selecting your project in the Vercel dashboard, and clicking the Speed Insights tab.
The Speed Insights dashboard displays data that you can sort and inspect based on a variety of parameters:
  * Device type: Toggle between mobile and desktop.
  * Environment: Filter by preview, production, or all environments.
  * Time range: Select the timeframe dropdown in the top-right of the page to choose a predefined timeframe. Alternatively, select the Calendar icon to specify a custom timeframe. The available durations vary, depending on the account type.
  * Performance metric: Switch between parameters that include Real Experience Score (RES), First Contentful Paint (FCP) and Largest Contentful Paint (LCP), and use the views to view more information.
  * Performance metric views: When you select a performance metric, the dashboard displays three views: 
    * Time-based line graph that, by default, shows the P75 percentile of data for the selected metric data points and time range. You can include P90, P95 and P99 in this view.
    * Kanban board that shows which routes, paths, or HTML elements need improvement (URLs that make up less than 0.5% of visits are not shown by default).
    * Geographical map showing the experience metric by country: ![Geographic map of the P75 score where the color intensity indicates the relative amount of data points per country](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1689795055%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fcountry-map-light.png&w=3840&q=75)![Geographic map of the P75 score where the color intensity indicates the relative amount of data points per country](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1689795055%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Fspeed-insights%2Fv2%2Fcountry-map-dark.png&w=3840&q=75)Geographic map of the P75 score where the color intensity indicates the relative amount of data points per country


The data in the Kanban and map views is selectable so that you can filter by country, route, path and HTML element. The red, orange and green colors in the map view indicate the P75 score.
### Quickstart
To get started with Speed Insights, use the Quickstart.
### Usage and pricing
Learn about the costs for Speed Insights, which are based on data points.
### Data Points
Learn how data points are calculated.
### Metrics
Learn about the performance metrics in Speed Insights and how the scores are calculated.
Last updated on November 11, 2024
Previous
Troubleshooting
Next
Quickstart
Was this helpful?
supported.
Send
AskAsk v0
Speed InsightsAskAsk v0
