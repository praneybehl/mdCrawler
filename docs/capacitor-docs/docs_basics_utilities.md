Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Capacitor has several JavaScript functions available to ensure apps run successfully across multiple platforms with the same codebase.
## The Global Capacitor object​
You can import the global Capacitor object with the following code:
```
import{ Capacitor }from'@capacitor/core';
```

The `Capacitor` object has several functions that help with the most common WebView to Native problems you may face when developing a Capacitor app.
### Capacitor.convertFileSrc​
`convertFileSrc: (filePath: string) => string;`
Converts a device filepath into a Web View-friendly path.
Capacitor apps are served on a different protocol than device files. To avoid difficulties between these protocols, paths to device files must be rewritten. For example, on Android, `file:///path/to/device/file` must be rewritten as `http://localhost/_capacitor_file_/path/to/device/file` before being used in the Web View.
```
// file:///path/to/device/photo.jpgconst rawPhotoUri =await Filesystem.writeFile({ path:"myFile.jpg", data: base64Data, directory: FilesystemDirectory.Data});// http://localhost/path/to/device/photo.jpgconst fixedPhotoUri = Capacitor.convertFileSrc(rawPhotoUri.uri),
```

### Capacitor.getPlatform​
`getPlatform: () => 'web' | 'ios' | 'android';`
Get the name of the Platform the app is currently running on. This will return a value of `"web"`, `"ios"`, or `"android"` depending on the device the app is running on.
```
if(Capacitor.getPlatform()==='ios'){console.log('iOS!');}elseif(Capacitor.getPlatform()==='android'){console.log('Android!');}else{console.log('Web!');}
```

### Capacitor.isNativePlatform​
`isNativePlatform: () => boolean;`
Check whether the currently running platform is native. This function returns a value of `true` if the app is running as a native, installed Capacitor app, or `false` if it is served via a browser or installed as a PWA.
```
if(Capacitor.isNativePlatform()){console.log("I'm a native app!");}else{console.log("I'm a PWA or Web app!");}
```

### Capacitor.isPluginAvailable​
`isPluginAvailable: (name: string) => boolean;`
Check if a plugin is available on the currently running platform. The plugin name is used in the plugin registry, which means it also works with custom plugins.
```
const isAvailable = Capacitor.isPluginAvailable('Camera');if(!isAvailable){// Have the user upload a file instead}else{// Otherwise, make the call:const image =await Camera.getPhoto({  resultType: CameraResultType.Uri,});}
```

## Contents
  * The Global Capacitor object
    * Capacitor.convertFileSrc
    * Capacitor.getPlatform
    * Capacitor.isNativePlatform
    * Capacitor.isPluginAvailable


Edit this page![](https://images.prismic.io/ionicframeworkcom/d3d3f7a3-023b-4cdf-93af-84674f623818_portals+ad.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Micro Frontends for any React Native, Android, or iOS mobile apps.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=bfa08d03ffe94cbc8ad825d7c77fcc94&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fbasics%2Futilities&_biz_t=1739803060538&_biz_i=Capacitor%20Documentation&_biz_n=17&rnd=326492&cdn_o=a&_biz_z=1739803060539)
