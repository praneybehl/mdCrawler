Skip to main content
An **OutSystems** Company →
Version: v7
On this page
Capacitor does not require Ionic Framework in order to build apps. However, developers may find the large collection of Ionic UI components helpful in order to build a high-quality app.
Capacitor can quickly be installed directly into any new or existing Ionic app by using the Ionic CLI.
## Installing Capacitor in a new Ionic Project​
For new Ionic projects, Capacitor is already installed in new Ionic apps by default! All you have to do is start a new project. To create a new Ionic project, run the following command:
```
ionic start
```

If you'd like a tutorial for building your first Capacitor-based Ionic app, check out this tutorial by the Ionic Framework team.
## Installing Capacitor to an existing Ionic Project​
If you have an existing Ionic project that doesn't have Capacitor enabled, you can enable Capacitor by running the following command.
```
ionic integrations enable capacitor
```

### Install Capacitor Plugin Dependencies​
Ionic Framework makes use of the APIs in the following Capacitor plugins:
  * `@capacitor/app`
  * `@capacitor/haptics`
  * `@capacitor/keyboard`
  * `@capacitor/status-bar`


For the best user experience, you should make sure these plugins are installed even if you don't import them in your app. To install these plugins, run the following command in the root of your project:
```
npm i @capacitor/app @capacitor/haptics @capacitor/keyboard @capacitor/status-bar
```

### Add Platforms​
After Capacitor installed and its plugins are installed, you can add mobile platforms to your app:
```
ionic capacitor add androidionic capacitor add ios
```

This will create a new directory in the root of your project for the native platform. This directory is a native project that should be considered a source artifact. Learn more about native project management.
info
If your Ionic app uses Cordova, we have a guide on how to migrate from Cordova to Capacitor as well.
## Ionic CLI Capacitor Commands​
The Ionic CLI has a variety of high-level commands that wrap the Capacitor CLI for convenience. See the documentation for each below. Help output is also available by using the `--help` flag after each command.
  * `ionic capacitor add`
  * `ionic capacitor build`
  * `ionic capacitor run`
  * `ionic capacitor sync`
  * `ionic capacitor open`


For more information on the Ionic CLI, and how to use it with Capacitor, you can see the documentation here.
## Contents
  * Installing Capacitor in a new Ionic Project
  * Installing Capacitor to an existing Ionic Project
    * Install Capacitor Plugin Dependencies
    * Add Platforms
  * Ionic CLI Capacitor Commands


Edit this page![](https://images.prismic.io/ionicframeworkcom/d3d3f7a3-023b-4cdf-93af-84674f623818_portals+ad.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Micro Frontends for any React Native, Android, or iOS mobile apps.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=bfa08d03ffe94cbc8ad825d7c77fcc94&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fgetting-started%2Fwith-ionic&_biz_t=1739803057100&_biz_i=Using%20with%20Ionic%20Framework%20%7C%20Capacitor%20Documentation&_biz_n=10&rnd=639105&cdn_o=a&_biz_z=1739803057101)
