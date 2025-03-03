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
Using App Router
Features available in /app
Using Latest Version
15.2.0
Using App Router
Features available in /app
Using Latest Version
15.2.0
API ReferenceFunctionsuserAgent
# userAgent
The `userAgent` helper extends the Web Request API with additional properties and methods to interact with the user agent object from the request.
middleware.ts
TypeScript
JavaScriptTypeScript
```
import { NextRequest, NextResponse, userAgent } from'next/server'
exportfunctionmiddleware(request:NextRequest) {
consturl=request.nextUrl
const { device } =userAgent(request)
constviewport=device.type ==='mobile'?'mobile':'desktop'
url.searchParams.set('viewport', viewport)
returnNextResponse.rewrite(url)
}
```

## `isBot`
A boolean indicating whether the request comes from a known bot.
## `browser`
An object containing information about the browser used in the request.
  * `name`: A string representing the browser's name, or `undefined` if not identifiable.
  * `version`: A string representing the browser's version, or `undefined`.


## `device`
An object containing information about the device used in the request.
  * `model`: A string representing the model of the device, or `undefined`.
  * `type`: A string representing the type of the device, such as `console`, `mobile`, `tablet`, `smarttv`, `wearable`, `embedded`, or `undefined`.
  * `vendor`: A string representing the vendor of the device, or `undefined`.


## `engine`
An object containing information about the browser's engine.
  * `name`: A string representing the engine's name. Possible values include: `Amaya`, `Blink`, `EdgeHTML`, `Flow`, `Gecko`, `Goanna`, `iCab`, `KHTML`, `Links`, `Lynx`, `NetFront`, `NetSurf`, `Presto`, `Tasman`, `Trident`, `w3m`, `WebKit` or `undefined`.
  * `version`: A string representing the engine's version, or `undefined`.


## `os`
An object containing information about the operating system.
  * `name`: A string representing the name of the OS, or `undefined`.
  * `version`: A string representing the version of the OS, or `undefined`.


## `cpu`
An object containing information about the CPU architecture.
  * `architecture`: A string representing the architecture of the CPU. Possible values include: `68k`, `amd64`, `arm`, `arm64`, `armhf`, `avr`, `ia32`, `ia64`, `irix`, `irix64`, `mips`, `mips64`, `pa-risc`, `ppc`, `sparc`, `sparc64` or `undefined`


Was this helpful?
supported.
Send
