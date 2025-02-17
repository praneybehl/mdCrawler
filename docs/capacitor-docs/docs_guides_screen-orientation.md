Skip to main content
An **OutSystems** Company →
Version: v7
On this page
## Screen Orientation in your Capacitor App​
Many apps work well in portrait and landscape device orientations. However, many don't, and there are good reasons to require an app to function solely or occasionally in one mode or the other.
## Global Orientation Settings​
To set a global setting for orientation in your Capacitor app, you'll set the configuration value necessary for the platform you're targeting.
### iOS Configuration​
iOS allows for different screen orientations to be supported on iPhones and iPads. To limit the allowed orientations for iOS, open Xcode and open the `Info.plist` file. Find the following keys: `Supported interface orientation` and `Supported interface orientation (iPad)`. Using these values, specify the different orientations you would like supported for iPhones and for iPads.
If editting the `Info.plist` file directly look for the following keys: `UISupportedInterfaceOrientations` and `UISupportedInterfaceOrientations~ipad`. For example, the following settings will limit the orientation to right-side-up `Portrait` on iPhones and either of the `Landscape` orientations on iPads:
```
 <key>UISupportedInterfaceOrientations</key> <array>  <string>UIInterfaceOrientationPortrait</string> </array> <key>UISupportedInterfaceOrientations~ipad</key> <array>  <string>UIInterfaceOrientationLandscapeRight</string>  <string>UIInterfaceOrientationLandscapeLeft</string> </array>
```

### Android Configuration​
On Android, orientation can be set by modifying the `AndroidManifest.xml` and setting `android:screenOrientation` on the `<activity>` entry for your main app activity. See the Android Manifest Documentation for details on the possible entries.
## Dynamic Orientation Settings​
Many apps need to support multiple orientations, with the ability to lock orientations occasionally depending on the content.
Capacitor supports this through the `@capacitor/screen-orientation` plugin:
```
npminstall @capacitor/screen-orientationnpx cap sync
```

Then, use the `lock` and `unlock` methods:
```
import{ ScreenOrientation }from'@capacitor/screen-orientation';...await ScreenOrientation.lock({ orientation:'portrait'});await ScreenOrientation.lock({ orientation:'landscape'});// To unlock orientation which will default back to the global setting:await ScreenOrientation.unlock();
```

See the Orientation Plugin Docs for the full range of possible orientation values and configuration options.
### iPad Orientation Lock​
By default, an iPad allows Multitasking and its orientation cannot be locked. If you need to lock orientation on an iPad set the option `Requires Full Screen` to `YES` by adding the following to `Info.plist`:
```
	<key>UIRequiresFullScreen</key>	<true/>
```

## Contents
  * Screen Orientation in your Capacitor App
  * Global Orientation Settings
    * iOS Configuration
    * Android Configuration
  * Dynamic Orientation Settings
    * iPad Orientation Lock


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=bfa08d03ffe94cbc8ad825d7c77fcc94&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fguides%2Fscreen-orientation&_biz_t=1739803076558&_biz_i=Screen%20Orientation%20%7C%20Capacitor%20Documentation&_biz_n=46&rnd=5282&cdn_o=a&_biz_z=1739803076559)
