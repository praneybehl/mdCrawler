Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Capacitor features a native Android runtime that enables developers to communicate between JavaScript and Native Java or Kotlin code.
Capacitor Android apps are configured and managed through Android Studio.
## Android Support​
API 23+ (Android 6 or later) is supported, which represents around 99% of the Android market. Capacitor requires an Android WebView with Chrome version 60 or later. On Android 6, and 10+ Capacitor uses the Android System WebView. On Android 7-9, Google Chrome provides the WebView.
## Adding the Android Platform​
First, install the `@capacitor/android` package.
```
npminstall @capacitor/android
```

Then, add the Android platform.
```
npx cap add android
```

## Opening the Android Project​
To open the project in Android Studio, run:
```
npx cap open android
```

Alternatively, you can open Android Studio and import the `android/` directory as an Android Studio project.
## Running Your App​
You can either run your app on the command-line or with Android Studio.
> To use an Android Emulator you must use an API 24+ system image. The System WebView does not automatically update on emulators. Physical devices should work as low as API 23 as long as their System WebView is updated.
### Running on the Command-Line​
To run the project on a device or emulator, run:
```
npx cap run android
```

The command will prompt you to select a target. Learn more about `run`.
> Either a physical Android device or a downloaded emulator system image is required to use the `run` command. See the documentation here for creating emulator devices and downloading system images in Android Studio.
### Running with Android Studio​
In Android Studio, first select the device or emulator and then click the run or debug button to run your app. Unless you're debugging Java or Kotlin code, the run button is preferred.
![Running App](https://capacitorjs.com/docs/assets/images/running-a42ce0daf3b9d2dd5ee6b94d1c378220.png)
## Troubleshooting​
If you encountered any issues while getting started, you can consult the Android Troubleshooting Guide. Feel free to open a discussion if you need help.
## Next Steps​
If your app ran you are now ready to continue developing and building your app. Use the various APIs available, Capacitor or Cordova plugins, or custom native code to build out the rest of your app.
## Further Reading​
Follow these Android-specific guides for more information on setting permissions for your app, updating dependencies, building plugins, and more:
Configuring and setting permissions for Android ›
Building Native Plugins for Android ›
## Contents
  * Android Support
  * Adding the Android Platform
  * Opening the Android Project
  * Running Your App
    * Running on the Command-Line
    * Running with Android Studio
  * Troubleshooting
  * Next Steps
  * Further Reading


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=bfa08d03ffe94cbc8ad825d7c77fcc94&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fandroid&_biz_t=1739803083297&_biz_i=Capacitor%20Documentation&_biz_n=59&rnd=344691&cdn_o=a&_biz_z=1739803083297)
