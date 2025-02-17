Skip to main content
An **OutSystems** Company →
Version: v7
On this page
## iOS​
### Remove removeAllListeners method​
If your plugin has `CAP_PLUGIN_METHOD(removeAllListeners, CAPPluginReturnPromise)` in the `.m` file, it can be removed now, the method is now available for all plugins without defining it.
### Add SPM support​
Capacitor 6 adds experimental SPM support, you can add support for your plugin following Converting existing plugins to SPM
## definitions.ts​
`addListener` signature has been changed to only return a `Promise`, remove the `& PluginListenerHandle`.
```
 addListener(  eventName: 'resume',  listenerFunc: () => void,- ): Promise<PluginListenerHandle> & PluginListenerHandle;+ ): Promise<PluginListenerHandle>;
```

# Updating Capacitor to 6.0 in your plugin
## Using @capacitor/plugin-migration-v5-to-v6​
From the plugin folder, run `npx @capacitor/plugin-migration-v5-to-v6@latest` and it will perform all the file changes automatically.
## Updating the files manually​
### Updating package.json​
Update `@capacitor/cli`, `@capacitor/core`, `@capacitor/android` and `@capacitor/ios` to `latest` version.
### Replace deprecated compileSdkVersion and update targetSDK / compileSDK to 34​
```
# build.gradleandroid {-  compileSdkVersion project.hasProperty('compileSdkVersion') ? rootProject.ext.compileSdkVersion : 33+  compileSdk project.hasProperty('compileSdkVersion') ? rootProject.ext.compileSdkVersion : 34-  targetSdkVersion project.hasProperty('targetSdkVersion') ? rootProject.ext.targetSdkVersion : 33+  targetSdkVersion project.hasProperty('targetSdkVersion') ? rootProject.ext.targetSdkVersion : 34
```

### Update gradle plugin to 8.2.1​
```
  dependencies {-    classpath 'com.android.tools.build:gradle:8.0.0'+    classpath 'com.android.tools.build:gradle:8.2.1'  }
```

### Update gradle wrapper to 8.2.1​
```
# gradle-wrapper.propertiesdistributionBase=GRADLE_USER_HOMEdistributionPath=wrapper/dists- distributionUrl=https\://services.gradle.org/distributions/gradle-8.0.2-all.zip+ distributionUrl=https\://services.gradle.org/distributions/gradle-8.2.1-all.zipzipStoreBase=GRADLE_USER_HOMEzipStorePath=wrapper/dists
```

### Update kotlin_version​
If your plugin uses kotlin, update the default `kotlin_version`
```
# build.gradlebuildscript {-  ext.kotlin_version = project.hasProperty("kotlin_version") ? rootProject.ext.kotlin_version : '1.8.20'+  ext.kotlin_version = project.hasProperty("kotlin_version") ? rootProject.ext.kotlin_version : '1.9.10'  repositories {
```

## Contents
  * iOS
    * Remove removeAllListeners method
    * Add SPM support
  * definitions.ts
  * Using @capacitor/plugin-migration-v5-to-v6
  * Updating the files manually
    * Updating package.json
    * Replace deprecated compileSdkVersion and update targetSDK / compileSDK to 34
    * Update gradle plugin to 8.2.1
    * Update gradle wrapper to 8.2.1
    * Update kotlin_version


Edit this page![](https://images.prismic.io/ionicframeworkcom/50ede1c5-d69d-4c9d-bf0d-4c9ab7c14724_doc-ad-appflow.png?auto=compress,format&rect=0,0,280,200&w=280&h=200)
Mobile CI/CD made easy. Build, publish, and update from the cloud.
![](https://cdn.bizible.com/ipv?_biz_r=&_biz_h=802059049&_biz_u=bfa08d03ffe94cbc8ad825d7c77fcc94&_biz_l=https%3A%2F%2Fcapacitorjs.com%2Fdocs%2Fupdating%2Fplugins%2F6-0&_biz_t=1739803062707&_biz_i=Capacitor%20Documentation&_biz_n=21&rnd=770184&cdn_o=a&_biz_z=1739803062708)
