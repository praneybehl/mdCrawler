Skip to content
# Barcode Scanner
GitHub npm  crates.io 
API Reference 
Allows your mobile application to use the camera to scan QR codes, EAN-13 and other kinds of barcodes.
## Supported Platforms
_This plugin requires a Rust version of at least**1.77.2**_
Platform | Level | Notes  
---|---|---  
windows  
linux  
macos  
android  
ios  
## Setup
Install the barcode-scanner plugin to get started.
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

npmruntauriaddbarcode-scanner

```

```

yarnruntauriaddbarcode-scanner

```

```

pnpmtauriaddbarcode-scanner

```

```

denotasktauriaddbarcode-scanner

```

```

buntauriaddbarcode-scanner

```

```

cargotauriaddbarcode-scanner

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-barcode-scanner--target'cfg(any(target_os = "android", target_os = "ios"))'

```

  2. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.setup(|app| {
#[cfg(mobile)]
app.handle().plugin(tauri_plugin_barcode_scanner::init());
Ok(())
})
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

npminstall@tauri-apps/plugin-barcode-scanner

```

```

yarnadd@tauri-apps/plugin-barcode-scanner

```

```

pnpmadd@tauri-apps/plugin-barcode-scanner

```

```

denoaddnpm:@tauri-apps/plugin-barcode-scanner

```

```

bunadd@tauri-apps/plugin-barcode-scanner

```



## Configuration
On iOS the barcode scanner plugin requires the `NSCameraUsageDescription` information property list value, which should describe why your app needs to use the camera.
In the `src-tauri/Info.ios.plist` file, add the following snippet:
src-tauri/Info.ios.plist```

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plistversion="1.0">
<dict>
<key>NSCameraUsageDescription</key>
<string>Read QR codes</string>
</dict>
</plist>

```

## Usage
The barcode scanner plugin is available in JavaScript.
```

import { scan, Format } from'@tauri-apps/plugin-barcode-scanner';
// when using `"withGlobalTauri": true`, you may use
// const { scan, Format } = window.__TAURI__.barcodeScanner;
// `windowed: true` actually sets the webview to transparent
// instead of opening a separate view for the camera
// make sure your user interface is ready to show what is underneath with a transparent element
scan({ windowed: true, formats: [Format.QRCode] });

```

## Permissions
By default all potentially dangerous plugin commands and scopes are blocked and cannot be accessed. You must modify the permissions in your `capabilities` configuration to enable these.
See the Capabilities Overview for more information and the step by step guide to use plugin permissions.
src-tauri/capabilities/mobile.json```

{
"$schema": "../gen/schemas/mobile-schema.json",
"identifier": "mobile-capability",
"windows": ["main"],
"platforms": ["iOS", "android"],
"permissions": ["barcode-scanner:allow-scan", "barcode-scanner:allow-cancel"]
}

```

## Default Permission
This permission set configures which barcode scanning features are by default exposed.
#### Granted Permissions
It allows all barcode related features.
  * `allow-cancel`
  * `allow-check-permissions`
  * `allow-open-app-settings`
  * `allow-request-permissions`
  * `allow-scan`
  * `allow-vibrate`


## Permission Table
Identifier | Description  
---|---  
`barcode-scanner:allow-cancel` |  Enables the cancel command without any pre-configured scope.  
`barcode-scanner:deny-cancel` |  Denies the cancel command without any pre-configured scope.  
`barcode-scanner:allow-check-permissions` |  Enables the check_permissions command without any pre-configured scope.  
`barcode-scanner:deny-check-permissions` |  Denies the check_permissions command without any pre-configured scope.  
`barcode-scanner:allow-open-app-settings` |  Enables the open_app_settings command without any pre-configured scope.  
`barcode-scanner:deny-open-app-settings` |  Denies the open_app_settings command without any pre-configured scope.  
`barcode-scanner:allow-request-permissions` |  Enables the request_permissions command without any pre-configured scope.  
`barcode-scanner:deny-request-permissions` |  Denies the request_permissions command without any pre-configured scope.  
`barcode-scanner:allow-scan` |  Enables the scan command without any pre-configured scope.  
`barcode-scanner:deny-scan` |  Denies the scan command without any pre-configured scope.  
`barcode-scanner:allow-vibrate` |  Enables the vibrate command without any pre-configured scope.  
`barcode-scanner:deny-vibrate` |  Denies the vibrate command without any pre-configured scope.  
© 2025 Tauri Contributors. CC-BY / MIT
