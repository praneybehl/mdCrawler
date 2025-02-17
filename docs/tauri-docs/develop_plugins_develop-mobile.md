Skip to content
# Mobile Plugin Development
Plugins can run native mobile code written in Kotlin (or Java) and Swift. The default plugin template includes an Android library project using Kotlin and a Swift package including an example mobile command showing how to trigger its execution from Rust code.
## Initialize Plugin Project
Follow the steps in the Plugin Development guide to initialize a new plugin project.
If you have an existing plugin and would like to add Android or iOS capabilities to it, you can use `plugin android init` and `plugin ios init` to bootstrap the mobile library projects and guide you through the changes needed.
The default plugin template splits the plugin’s implementation into two separate modules: `desktop.rs` and `mobile.rs`.
The desktop implementation uses Rust code to implement a functionality, while the mobile implementation sends a message to the native mobile code to execute a function and get a result back. If shared logic is needed across both implementations, it can be defined in `lib.rs`:
src/lib.rs```

use tauri::Runtime;
impl<R: Runtime> <plugin-name><R> {
pubfndo_something(&self) {
// do something that is a shared implementation between desktop and mobile
}
}

```

This implementation simplifies the process of sharing an API that can be used both by commands and Rust code.
### Develop an Android Plugin
A Tauri plugin for Android is defined as a Kotlin class that extends `app.tauri.plugin.Plugin` and is annotated with `app.tauri.annotation.TauriPlugin`. Each method annotated with `app.tauri.annotation.Command` can be called by Rust or JavaScript.
Tauri uses Kotlin by default for the Android plugin implementation, but you can switch to Java if you prefer. After generating a plugin, right click the Kotlin plugin class in Android Studio and select the “Convert Kotlin file to Java file” option from the menu. Android Studio will guide you through the project migration to Java.
### Develop an iOS Plugin
A Tauri plugin for iOS is defined as a Swift class that extends the `Plugin` class from the `Tauri` package. Each function with the `@objc` attribute and the `(_ invoke: Invoke)` parameter (for example `@objc private func download(_ invoke: Invoke) { }`) can be called by Rust or JavaScript.
The plugin is defined as a Swift package so that you can use its package manager to manage dependencies.
## Plugin Configuration
Refer to the Plugin Configuration section of the Plugin Development guide for more details on developing plugin configurations.
The plugin instance on mobile has a getter for the plugin configuration:
  * Android 
  * iOS 


```

import android.app.Activity
import android.webkit.WebView
import app.tauri.annotation.TauriPlugin
import app.tauri.annotation.InvokeArg
@InvokeArg
class Config {
var timeout: Int? =3000
}
@TauriPlugin
class ExamplePlugin(privateval activity: Activity): Plugin(activity) {
privatevar timeout: Int? =3000
overridefunload(webView: WebView) {
getConfig(Config::class.java).let {
this.timeout = it.timeout
}
}
}

```

```

struct Config: Decodable {
let timeout: Int?
}
class ExamplePlugin: Plugin {
var timeout: Int?=3000
@objcpublicoverridefuncload(webview: WKWebView) {
do {
let config =tryparseConfig(Config.self)
self.timeout= config.timeout
} catch {}
}
}

```

## Lifecycle Events
Plugins can hook into several lifecycle events:
  * load: When the plugin is loaded into the web view
  * onNewIntent: Android only, when the activity is re-launched


There are also the additional lifecycle events for plugins in the Plugin Development guide.
### load
  * **When** : When the plugin is loaded into the web view
  * **Why** : Execute plugin initialization code


  * Android 
  * iOS 


```

import android.app.Activity
import android.webkit.WebView
import app.tauri.annotation.TauriPlugin
@TauriPlugin
class ExamplePlugin(privateval activity: Activity): Plugin(activity) {
overridefunload(webView: WebView) {
// perform plugin setup here
}
}

```

```

class ExamplePlugin: Plugin {
@objcpublicoverridefuncload(webview: WKWebView) {
let timeout =self.config["timeout"] as?Int??30
}
}

```

### onNewIntent
**Note** : This is only available on Android.
  * **When** : When the activity is re-launched. See Activity#onNewIntent for more information.
  * **Why** : Handle application re-launch such as when a notification is clicked or a deep link is accessed.


```

import android.app.Activity
import android.content.Intent
import app.tauri.annotation.TauriPlugin
@TauriPlugin
class ExamplePlugin(privateval activity: Activity): Plugin(activity) {
overridefunonNewIntent(intent: Intent) {
// handle new intent event
}
}

```

## Adding Mobile Commands
There is a plugin class inside the respective mobile projects where commands can be defined that can be called by the Rust code:
  * Android 
  * iOS 


```

import android.app.Activity
import app.tauri.annotation.Command
import app.tauri.annotation.TauriPlugin
@TauriPlugin
class ExamplePlugin(privateval activity: Activity): Plugin(activity) {
@Command
funopenCamera(invoke: Invoke) {
val ret =JSObject()
ret.put("path", "/path/to/photo.jpg")
invoke.resolve(ret)
}
}

```

If you want to use a Kotlin `suspend` function, you need to use a custom coroutine scope
```

import android.app.Activity
import app.tauri.annotation.Command
import app.tauri.annotation.TauriPlugin
// Change to Dispatchers.IO if it is intended for fetching data
val scope =CoroutineScope(Dispatchers.Default +SupervisorJob())
@TauriPlugin
class ExamplePlugin(privateval activity: Activity): Plugin(activity) {
@Command
funopenCamera(invoke: Invoke) {
scope.launch {
openCameraInner(invoke)
}
}
privatesuspendfunopenCameraInner(invoke: Invoke) {
val ret =JSObject()
ret.put("path", "/path/to/photo.jpg")
invoke.resolve(ret)
}
}

```

```

class ExamplePlugin: Plugin {
@objcpublicfuncopenCamera(_invoke: Invoke)throws {
invoke.resolve(["path":"/path/to/photo.jpg"])
}
}

```

Use the `tauri::plugin::PluginHandle` to call a mobile command from Rust:
```

use std::path::PathBuf;
use serde::{Deserialize, Serialize};
use tauri::Runtime;
#[derive(Serialize)]
#[serde(rename_all ="camelCase")]
pubstruct CameraRequest {
quality: usize,
allow_edit: bool,
}
#[derive(Deserialize)]
pubstruct Photo {
path: PathBuf,
}
impl<R: Runtime> <plugin-name;pascal-case><R> {
pubfnopen_camera(&self, payload: CameraRequest) ->crate::Result<Photo> {
self
.0
.run_mobile_plugin("openCamera", payload)
.map_err(Into::into)
}
}

```

## Command Arguments
Arguments are serialized to commands and can be parsed on the mobile plugin with the `Invoke::parseArgs` function, taking a class describing the argument object.
### Android
On Android, the arguments are defined as a class annotated with `@app.tauri.annotation.InvokeArg`. Inner objects must also be annotated:
```

import android.app.Activity
import android.webkit.WebView
import app.tauri.annotation.Command
import app.tauri.annotation.InvokeArg
import app.tauri.annotation.TauriPlugin
@InvokeArg
internalclass OpenAppArgs {
lateinitvar name: String
var timeout: Int? =null
}
@InvokeArg
internalclass OpenArgs {
lateinitvar requiredArg: String
var allowEdit: Boolean =false
var quality: Int =100
var app: OpenAppArgs? =null
}
@TauriPlugin
class ExamplePlugin(privateval activity: Activity): Plugin(activity) {
@Command
funopenCamera(invoke: Invoke) {
val args = invoke.parseArgs(OpenArgs::class.java)
}
}

```

### iOS
On iOS, the arguments are defined as a class that inherits `Decodable`. Inner objects must also inherit the Decodable protocol:
```

class OpenAppArgs: Decodable {
let name: String
var timeout: Int?
}
class OpenArgs: Decodable {
let requiredArg: String
var allowEdit: Bool?
var quality: UInt8?
var app: OpenAppArgs?
}
class ExamplePlugin: Plugin {
@objcpublicfuncopenCamera(_invoke: Invoke)throws {
let args =try invoke.parseArgs(OpenArgs.self)
invoke.resolve(["path":"/path/to/photo.jpg"])
}
}

```

## Permissions
If a plugin requires permissions from the end user, Tauri simplifies the process of checking and requesting permissions.
  * Android 
  * iOS 


First define the list of permissions needed and an alias to identify each group in code. This is done inside the `TauriPlugin` annotation:
```

@TauriPlugin(
permissions = [
Permission(strings = [Manifest.permission.POST_NOTIFICATIONS], alias ="postNotification")
]
)
class ExamplePlugin(privateval activity: Activity): Plugin(activity) { }

```

First override the `checkPermissions` and `requestPermissions` functions:
```

class ExamplePlugin: Plugin {
@objcopenfunccheckPermissions(_invoke: Invoke) {
invoke.resolve(["postNotification":"prompt"])
}
@objcpublicoverridefuncrequestPermissions(_invoke: Invoke) {
// request permissions here
// then resolve the request
invoke.resolve(["postNotification":"granted"])
}
}

```

Tauri automatically implements two commands for the plugin: `checkPermissions` and `requestPermissions`. Those commands can be directly called from JavaScript or Rust:
  * JavaScript 
  * Rust 


```

import { invoke, PermissionState } from'@tauri-apps/api/core'
interface Permissions {
postNotification:PermissionState
}
// check permission state
const permission = await invoke<Permissions>('plugin:<plugin-name>|checkPermissions')
if (permission.postNotification==='prompt-with-rationale') {
// show information to the user about why permission is needed
}
// request permission
if (permission.postNotification.startsWith('prompt')) {
const state = await invoke<Permissions>('plugin:<plugin-name>|requestPermissions', { permissions: ['postNotification'] })
}

```

```

use serde::{Serialize, Deserialize};
use tauri::{plugin::PermissionState, Runtime};
#[derive(Deserialize)]
#[serde(rename_all ="camelCase")]
struct PermissionResponse {
pubpost_notification: PermissionState,
}
#[derive(Serialize)]
#[serde(rename_all ="camelCase")]
struct RequestPermission {
post_notification: bool,
}
impl<R: Runtime> Notification<R> {
pubfnrequest_post_notification_permission(&self) ->crate::Result<PermissionState> {
self.0
.run_mobile_plugin::<PermissionResponse>("requestPermissions", RequestPermission { post_notification:true })
.map(|r|r.post_notification)
.map_err(Into::into)
}
pubfncheck_permissions(&self) ->crate::Result<PermissionResponse> {
self.0
.run_mobile_plugin::<PermissionResponse>("checkPermissions", ())
.map_err(Into::into)
}
}

```

## Plugin Events
Plugins can emit events at any point of time using the `trigger` function:
  * Android 
  * iOS 


```

@TauriPlugin
class ExamplePlugin(privateval activity: Activity): Plugin(activity) {
overridefunload(webView: WebView) {
trigger("load", JSObject())
}
overridefunonNewIntent(intent: Intent) {
// handle new intent event
if (intent.action == Intent.ACTION_VIEW) {
valdata= intent.data.toString()
val event =JSObject()
event.put("data", data)
trigger("newIntent", event)
}
}
@Command
funopenCamera(invoke: Invoke) {
val payload =JSObject()
payload.put("open", true)
trigger("camera", payload)
}
}

```

```

class ExamplePlugin: Plugin {
@objcpublicoverridefuncload(webview: WKWebView) {
trigger("load", data: [:])
}
@objcpublicfuncopenCamera(_invoke: Invoke) {
trigger("camera", data: ["open":true])
}
}

```

The helper functions can then be called from the NPM package by using the `addPluginListener` helper function:
```

import { addPluginListener, PluginListener } from'@tauri-apps/api/core';
exportasyncfunctiononRequest(
handler:(url:string)=>void
):Promise<PluginListener> {
returnawaitaddPluginListener(
'<plugin-name>',
'event-name',
handler
);
}

```

© 2025 Tauri Contributors. CC-BY / MIT
