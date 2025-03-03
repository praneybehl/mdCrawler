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
Using Pages Router
Features available in /pages
Using Latest Version
15.2.0
Using Pages Router
Features available in /pages
Using Latest Version
15.2.0
Configurationnext.config.js OptionsoptimizePackageImports
# optimizePackageImports
Some packages can export hundreds or thousands of modules, which can cause performance issues in development and production.
Adding a package to `experimental.optimizePackageImports` will only load the modules you are actually using, while still giving you the convenience of writing import statements with many named exports.
next.config.js
```
module.exports= {
 experimental: {
  optimizePackageImports: ['package-name'],
 },
}
```

The following libraries are optimized by default:
  * `lucide-react`
  * `date-fns`
  * `lodash-es`
  * `ramda`
  * `antd`
  * `react-bootstrap`
  * `ahooks`
  * `@ant-design/icons`
  * `@headlessui/react`
  * `@headlessui-float/react`
  * `@heroicons/react/20/solid`
  * `@heroicons/react/24/solid`
  * `@heroicons/react/24/outline`
  * `@visx/visx`
  * `@tremor/react`
  * `rxjs`
  * `@mui/material`
  * `@mui/icons-material`
  * `recharts`
  * `react-use`
  * `@material-ui/core`
  * `@material-ui/icons`
  * `@tabler/icons-react`
  * `mui-core`
  * `react-icons/*`


Was this helpful?
supported.
Send
