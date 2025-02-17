Skip to content
# Deep Linking
GitHub npm  crates.io 
API Reference 
Set your Tauri application as the default handler for an URL.
## Supported Platforms
_This plugin requires a Rust version of at least**1.77.2**_
Platform | Level | Notes  
---|---|---  
windows  
linux  
macos |  Runtime deep link registration is not supported  
android |  Runtime deep link registration is not supported  
ios |  Runtime deep link registration is not supported  
## Setup
Install the deep-link plugin to get started.
  * Automatic 
  * Manual 


Use your project’s package manager to add the dependency:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * bun 
  * cargo 


```

npmruntauriadddeep-link

```

```

yarnruntauriadddeep-link

```

```

pnpmtauriadddeep-link

```

```

denotasktauriadddeep-link

```

```

buntauriadddeep-link

```

```

cargotauriadddeep-link

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-deep-link@2.0.0

```

  2. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.plugin(tauri_plugin_deep_link::init())
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

  3. Install the JavaScript Guest bindings using your preferred JavaScript package manager:
     * npm 
     * yarn 
     * pnpm 
     * deno 
     * bun 
```

npminstall@tauri-apps/plugin-deep-link

```

```

yarnadd@tauri-apps/plugin-deep-link

```

```

pnpmadd@tauri-apps/plugin-deep-link

```

```

denoaddnpm:@tauri-apps/plugin-deep-link

```

```

bunadd@tauri-apps/plugin-deep-link

```



## Setting up
### Android
For app links, you need a server with a `.well-known/assetlinks.json` endpoint that must return a text response in the given format:
.well-known/assetlinks.json```

[
{
"relation": ["delegate_permission/common.handle_all_urls"],
"target": {
"namespace": "android_app",
"package_name": "$APP_BUNDLE_ID",
"sha256_cert_fingerprints": [
$CERT_FINGERPRINT
]
}
}
]

```

Where `$APP_BUNDLE_ID` is the value defined on `tauri.conf.json > identifier` with `-` replaced with `_` and `$CERT_FINGERPRINT` is a list of SHA256 fingerprints of your app’s signing certificates, see verify Android applinks for more information.
### iOS
For universal links, you need a server with a `.well-known/apple-app-site-association` endpoint that must return a JSON response in the given format:
.well-known/apple-app-site-association```

{
"applinks": {
"details": [
{
"appIDs": ["$DEVELOPMENT_TEAM_ID.$APP_BUNDLE_ID"],
"components": [
{
"/": "/open/*",
"comment": "Matches any URL whose path starts with /open/"
}
]
}
]
}
}

```

Where `$DEVELOPMENT_TEAM_ID` is the value defined on `tauri.conf.json > tauri > bundle > iOS > developmentTeam` or the `TAURI_APPLE_DEVELOPMENT_TEAM` environment variable and `$APP_BUNDLE_ID` is the value defined on `tauri.conf.json > identifier`.
To verify if your domain has been properly configured to expose the app associations, you can run the following command, replacing `<host>` with your actual host:
Terminal window```

curl-vhttps://app-site-association.cdn-apple.com/a/v1/<host>

```

See applinks.details for more information.
### Desktop
On Linux and Windows deep links are delivered as a command line argument to a new app process. The deep link plugin has integration with the single instance plugin if you prefer having a unique app instance receiving the events.
  * First you must add the `deep-link` feature to the single instance plugin:


src-tauri/Cargo.toml```

[target."cfg(any(target_os = \"macos\", windows, target_os = \"linux\"))".dependencies]
tauri-plugin-single-instance = { version = "2.0.0", features = ["deep-link"] }

```

  * Then configure the single instance plugin which should always be the first plugin you register:


src-tauri/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
letmutbuilder= tauri::Builder::default();
#[cfg(desktop)]
{
builder=builder.plugin(tauri_plugin_single_instance::init(|_app, argv, _cwd| {
println!("a new app instance was opened with {argv:?} and the deep link event was already triggered");
// when defining deep link schemes at runtime, you must also check `argv` here
}));
}
builder=builder.plugin(tauri_plugin_deep_link::init());
}

```

The user could trigger a fake deep link manually by including the URL as argument. Tauri matches the command line argument against the configured schemes to mitigate this, but you should still check if the URL matches the format you expect.
This means Tauri only handles deep links for schemes that were statically configured, and schemes registered at runtime must be manually checked using `Env::args_os`.
## Configuration
Under `tauri.conf.json > plugins > deep-link`, configure the domains (mobile) and schemes (desktop) you want to associate with your application:
tauri.conf.json```

{
"plugins": {
"deep-link": {
"mobile": [
{ "host": "your.website.com", "pathPrefix": ["/open"] },
{ "host": "another.site.br" }
],
"desktop": {
"schemes": ["something", "my-tauri-app"]
}
}
}
}

```

With the above configuration, the `something://*` and `my-tauri-app://*` URLs are associated with your desktop application, and on mobile the `https://another.site.br/*` and `https://your.website.com/open/*` URLs will open your mobile app.
## Usage
The deep-link plugin is available in both JavaScript and Rust.
### Listening to Deep Links
  * JavaScript 
  * Rust 


When a deep link triggers your app to be opened, the `onOpenUrl` callback is executed:
```

import { onOpenUrl } from'@tauri-apps/plugin-deep-link';
// when using `"withGlobalTauri": true`, you may use
// const { onOpenUrl } = window.__TAURI__.deepLink;
awaitonOpenUrl((urls)=> {
console.log('deep link:', urls);
});

```

When a deep link triggers your app to be opened, the `on_open_url` closure is called:
src-tauri/src/lib.rs```

use tauri_plugin_deep_link::DeepLinkExt;
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.plugin(tauri_plugin_deep_link::init())
.setup(|app| {
app.deep_link().on_open_url(|event| {
println!("deep link URLs: {:?}", event.urls());
});
Ok(())
})
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

### Registering Desktop Deep Links at Runtime
The configuration section describes how to define static deep link schemes for your application.
On Linux and Windows it is possible to also associate schemes with your application at runtime via the `register` Rust function.
In the following snippet, we will register the `my-app` scheme at runtime. After executing the app for the first time, the operating system will open `my-app://*` URLs with our application:
src-tauri/src/lib.rs```

use tauri_plugin_deep_link::DeepLinkExt;
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.plugin(tauri_plugin_deep_link::init())
.setup(|app| {
#[cfg(desktop)]
app.deep_link().register("my-app")?;
Ok(())
})
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

## Testing
There are some caveats to test deep links for your application.
### Desktop
Deep links are only triggered for installed applications on desktop. On Linux and Windows you can circumvent this using the `register_all` Rust function, which registers all configured schemes to trigger the current executable:
src-tauri/src/lib.rs```

use tauri_plugin_deep_link::DeepLinkExt;
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.plugin(tauri_plugin_deep_link::init())
.setup(|app| {
#[cfg(any(windows, target_os ="linux"))]
{
use tauri_plugin_deep_link::DeepLinkExt;
app.deep_link().register_all()?;
}
Ok(())
})
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

#### Windows
To trigger a deep link on Windows you can either open `<scheme>://url` in the browser or run the following command in the terminal:
Terminal window```

start<scheme>://url

```

#### Linux
To trigger a deep link on Linux you can either open `<scheme>://url` in the browser or run `xdg-open` in the terminal:
Terminal window```

xdg-open<scheme>://url

```

### iOS
To trigger an app link on iOS you can open the `https://<host>/path` URL in the browser. For simulators you can leverage the `simctl` CLI to directly open a link from the terminal:
Terminal window```

xcrunsimctlopenurlbootedhttps://<host>/path

```

### Android
To trigger an app link on Android you can open the `https://<host>/path` URL in the browser. For emulators you can leverage the `adb` CLI to directly open a link from the terminal:
Terminal window```

adbshellamstart-aandroid.intent.action.VIEW-dhttps://<host>/path<bundle-identifier>

```

## Permissions
By default all potentially dangerous plugin commands and scopes are blocked and cannot be accessed. You must modify the permissions in your `capabilities` configuration to enable these.
See the Capabilities Overview for more information and the step by step guide to use plugin permissions.
src-tauri/capabilities/default.json```

{
"$schema": "../gen/schemas/mobile-schema.json",
"identifier": "mobile-capability",
"windows": ["main"],
"platforms": ["iOS", "android"],
"permissions": [
// Usually you will need core:event:default to listen to the deep-link event
"core:event:default",
"deep-link:default"
]
}

```

## Default Permission
Allows reading the opened deep link via the get_current command
  * `allow-get-current`


## Permission Table
Identifier | Description  
---|---  
`deep-link:allow-get-current` |  Enables the get_current command without any pre-configured scope.  
`deep-link:deny-get-current` |  Denies the get_current command without any pre-configured scope.  
`deep-link:allow-is-registered` |  Enables the is_registered command without any pre-configured scope.  
`deep-link:deny-is-registered` |  Denies the is_registered command without any pre-configured scope.  
`deep-link:allow-register` |  Enables the register command without any pre-configured scope.  
`deep-link:deny-register` |  Denies the register command without any pre-configured scope.  
`deep-link:allow-unregister` |  Enables the unregister command without any pre-configured scope.  
`deep-link:deny-unregister` |  Denies the unregister command without any pre-configured scope.  
© 2025 Tauri Contributors. CC-BY / MIT
