Skip to main content
An **OutSystems** Company →
Version: v7
On this page
With Capacitor, you are encouraged to write Swift or Objective-C code to implement the native features your app needs.
There may not be a Capacitor plugin for everything--and that's okay! It is possible to write WebView-accessible native code right in your app.
## WebView-Accessible Native Code​
The easiest way to communicate between JavaScript and native code is to build a custom Capacitor plugin that is local to your app.
### `EchoPlugin.swift`​
First, create a `EchoPlugin.swift` file by opening Xcode, right-clicking on the **App** group (under the **App** target), selecting **New File...** from the context menu, choosing **Swift File** in the window, and creating the file.
![New Swift File in Xcode](https://capacitorjs.com/docs/assets/images/xcode-new-swift-file-617ac7330b95f987e64d016f160b1c02.png)
Copy the following Swift code into `EchoPlugin.swift`:
```
importCapacitor@objc(EchoPlugin)publicclassEchoPlugin:CAPPlugin,CAPBridgedPlugin{publiclet identifier ="EchoPlugin"publiclet jsName ="Echo"publiclet pluginMethods:[CAPPluginMethod]=[CAPPluginMethod(name:"echo", returnType:CAPPluginReturnPromise)]@objcfuncecho(_ call:CAPPluginCall){let value = call.getString("value")??""    call.resolve(["value": value])}}
```

> The `@objc` decorators are required to make sure Capacitor's runtime (which must use Objective-C for dynamic plugin support) can see it.
### Register the Plugin​
We must register custom plugins on both iOS and web so that Capacitor can bridge between Swift and JavaScript.
#### `MyViewController.swift`​
Create a custom `MyViewController.swift`.
Then add a `capacitorDidLoad()` method override and register the plugin:
```
overrideopenfunccapacitorDidLoad(){  bridge?.registerPluginInstance(EchoPlugin())}
```

#### JavaScript​
In JS, we use `registerPlugin()` from `@capacitor/core` to create an object which is linked to our Swift plugin.
```
import{ registerPlugin }from'@capacitor/core';const Echo =registerPlugin('Echo');exportdefault Echo;
```

> The first parameter to `registerPlugin()` is the plugin name, which must match the second parameter to the `CAP_PLUGIN` macro in `EchoPlugin.m`.
**TypeScript**
We can define types on our linked object by defining an interface and using it in the call to `registerPlugin()`.
```
import { registerPlugin } from '@capacitor/core';+export interface EchoPlugin {+ echo(options: { value: string }): Promise<{ value: string }>;+}-const Echo = registerPlugin('Echo');+const Echo = registerPlugin<EchoPlugin>('Echo');export default Echo;
```

The generic parameter of `registerPlugin()` is what defines the structure of the linked object. You can use `registerPlugin<any>('Echo')` to ignore types if you need to. No judgment. ❤️
### Use the Plugin​
Use the exported `Echo` object to call your plugin methods. The following snippet will call into Swift on iOS and print the result:
```
import Echo from'../path/to/echo-plugin';const{ value }=await Echo.echo({ value:'Hello World!'});console.log('Response from native:', value);
```

### Next Steps​
Read the iOS Plugin Guide ›
## Contents
  * WebView-Accessible Native Code
    * `EchoPlugin.swift`
    * Register the Plugin
    * Use the Plugin
    * Next Steps


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=bfa08d03ffe94cbc8ad825d7c77fcc94&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fios%2Fcustom-code&_biz_t=1739803080033&_biz_i=Custom%20Native%20iOS%20Code%20%7C%20Capacitor%20Documentation&_biz_n=53&rnd=281219&cdn_o=a&_biz_z=1739803080034)
