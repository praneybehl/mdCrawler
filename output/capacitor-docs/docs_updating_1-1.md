Skip to main content
An **OutSystems** Company →
Version: v7
On this page
If you are using an earlier version of Capacitor in your app, there are some recommended changes to make in your app for Capacitor 1.1.0.
## iOS​
Add `Podfile.lock` to the `ios/.gitignore` file:
```
App/buildApp/PodsApp/public+App/Podfile.lockxcuserdata# Cordova plugins for Capacitor
```

## Android​
Remove the `fileprovider_authority` string from the `android/app/src/main/res/values/strings.xml` file:
```
  <string name="app_name">My App</string>  <string name="title_activity_main">My App</string>  <string name="package_name">com.getcapacitor.myapp</string>-  <string name="fileprovider_authority">com.getcapacitor.myapp.fileprovider</string>  <string name="custom_url_scheme">com.getcapacitor.myapp</string></resources>
```

## Contents
  * iOS
  * Android


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=bfa08d03ffe94cbc8ad825d7c77fcc94&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fupdating%2F1-1&_biz_t=1739803066248&_biz_i=Updating%20to%201.1%20%7C%20Capacitor%20Documentation&_biz_n=27&rnd=316447&cdn_o=a&_biz_z=1739803066248)
