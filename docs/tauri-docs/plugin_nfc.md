Skip to content
# NFC
GitHub npm  crates.io 
API Reference 
Read and write NFC tags on Android and iOS.
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
Install the nfc plugin to get started.
  * Automatic 
  * Manual 


Use your project’s package manager to add the dependency:
  * npm 
  * yarn 
  * pnpm 
  * bun 
  * cargo 


```

npmruntauriaddnfc

```

```

yarnruntauriaddnfc

```

```

pnpmtauriaddnfc

```

```

buntauriaddnfc

```

```

cargotauriaddnfc

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-nfc--target'cfg(any(target_os = "android", target_os = "ios"))'

```

  2. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.setup(|app| {
#[cfg(mobile)]
app.handle().plugin(tauri_plugin_nfc::init());
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

npminstall@tauri-apps/plugin-nfc

```

```

yarnadd@tauri-apps/plugin-nfc

```

```

pnpmadd@tauri-apps/plugin-nfc

```

```

denoaddnpm:@tauri-apps/plugin-nfc

```

```

bunadd@tauri-apps/plugin-nfc

```



## Configuration
The NFC plugin requires native configuration for iOS.
### iOS
To access the NFC APIs on iOS you must configure a usage description on the Info.plist file and add the NFC capability to your application.
#### Info.plist
On iOS the NFC plugin requires the `NFCReaderUsageDescription` information property list value, which should describe why your app needs to scan or write to NFC tags.
In the `src-tauri/Info.ios.plist` file, add the following snippet:
src-tauri/Info.ios.plist```

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plistversion="1.0">
<dict>
<key>NFCReaderUsageDescription</key>
<string>Read and write various NFC tags</string>
</dict>
</plist>

```

#### NFC Capability
Additionally iOS requires the NFC capability to be associated with your application.
The capability can be added in Xcode in the project configuration’s “Signing & Capabilities” tab by clicking the ”+ Capability” button and selecting the “Near Field Communication Tag Reading” capability (see Add a capability to a target for more information) or by adding the following configuration to the `gen/apple/<app-name>_iOS/<app-name>_iOS.entitlements` file:
gen/apple/<app-name>_iOS/<app-name>_iOS.entitlements```

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plistversion="1.0">
<dict>
<key>com.apple.developer.nfc.readersession.formats</key>
<array>
<string>TAG</string>
</array>
</dict>
</plist>

```

## Usage
The NFC plugin is available in both JavaScript and Rust, allowing you to scan and write to NFC tags.
### Checking if NFC is supported
Not every mobile device has the capability to scan NFC tags, so you should check for availability before using the scan and write APIs.
  * JavaScript 
  * Rust 


```

import { isAvailable } from'@tauri-apps/plugin-nfc';
const canScanNfc = await isAvailable();

```

```

tauri::Builder::default()
.setup(|app| {
#[cfg(mobile)]
{
use tauri_plugin_nfc::NfcExt;
app.handle().plugin(tauri_plugin_nfc::init());
letcan_scan_nfc=app.nfc().is_available()?;
}
Ok(())
})

```

### Scanning NFC tags
The plugin can scan either generic NFC tags or NFC tags with a NDEF (NFC Data Exchange Format) message, which is a standard format to encapsulate typed data in an NFC tag.
  * JavaScript 
  * Rust 


```

import { scan } from'@tauri-apps/plugin-nfc';
const scanType = {
type: 'ndef', // or 'tag',
};
const options = {
keepSessionAlive: false,
// configure the messages displayed in the "Scan NFC" dialog on iOS
message: 'Scan a NFC tag',
successMessage: 'NFC tag successfully scanned',
};
const tag = await scan(scanType, options);

```

```

tauri::Builder::default()
.setup(|app| {
#[cfg(mobile)]
{
use tauri_plugin_nfc::NfcExt;
app.handle().plugin(tauri_plugin_nfc::init());
lettag=app
.nfc()
.scan(tauri_plugin_nfc::ScanRequest {
kind: tauri_plugin_nfc::ScanKind::Ndef {
mime_type: None,
uri: None,
tech_list: None,
},
keep_session_alive:false,
})?
.tag;
}
Ok(())
})

```

#### Filters
The NFC scanner can also filter tags with a specific URI format, mime type or NFC tag technologies. In this case, the scan will only detect tags that matches the provided filters.
  * JavaScript 
  * Rust 


```

import { scan, TechKind } from'@tauri-apps/plugin-nfc';
const techLists = [
// capture anything using NfcF
[TechKind.NfcF],
// capture all MIFARE Classics with NDEF payloads
[TechKind.NfcA, TechKind.MifareClassic, TechKind.Ndef],
];
const tag = await scan({
type: 'ndef', // or 'tag'
mimeType: 'text/plain',
uri: {
scheme: 'https',
host: 'my.domain.com',
pathPrefix: '/app',
},
techLists,
});

```

```

tauri::Builder::default()
.setup(|app| {
#[cfg(mobile)]
{
use tauri_plugin_nfc::NfcExt;
app.handle().plugin(tauri_plugin_nfc::init());
lettag=app
.nfc()
.scan(tauri_plugin_nfc::ScanRequest {
kind: tauri_plugin_nfc::ScanKind::Ndef {
mime_type: Some("text/plain".to_string()),
uri: Some(tauri_plugin_nfc::UriFilter {
scheme: Some("https".to_string()),
host: Some("my.domain.com".to_string()),
path_prefix: Some("/app".to_string()),
}),
tech_list: Some(vec![
vec![tauri_plugin_nfc::TechKind::Ndef],
]),
},
})?
.tag;
}
Ok(())
})

```

### Writing to NFC tags
The `write` API can be used to write a payload to a NFC tag. If there’s no scanned tag with `keepSessionAlive: true`, the application will first scan an NFC tag.
  * JavaScript 
  * Rust 


```

import { write, textRecord, uriRecord } from'@tauri-apps/plugin-nfc';
const payload = [uriRecord('https://tauri.app'), textRecord('some payload')];
const options = {
// the kind is only required if you do not have a scanned tag session alive
// its format is the same as the argument provided to scan()
kind: {
type: 'ndef',
},
// configure the messages displayed in the "Scan NFC" dialog on iOS
message: 'Scan a NFC tag',
successfulReadMessage: 'NFC tag successfully scanned',
successMessage: 'NFC tag successfully written',
};
awaitwrite(payload, options);

```

```

tauri::Builder::default()
.setup(|app| {
#[cfg(mobile)]
{
use tauri_plugin_nfc::NfcExt;
app.handle().plugin(tauri_plugin_nfc::init());
app
.nfc()
.write(vec![
tauri_plugin_nfc::NfcRecord {
format: tauri_plugin_nfc::NFCTypeNameFormat::NfcWellKnown,
kind:vec![0x55], // URI record
id:vec![],
payload:vec![], // insert payload here
}
])?;
}
Ok(())
})

```

## Permissions
By default all potentially dangerous plugin commands and scopes are blocked and cannot be accessed. You must modify the permissions in your `capabilities` configuration to enable these.
See the Capabilities Overview for more information and the step by step guide to use plugin permissions.
src-tauri/capabilities/default.json```

{
"permissions": [
...,
"nfc:default",
]
}

```

## Default Permission
This permission set configures what kind of operations are available from the nfc plugin.
#### Granted Permissions
Checking if the NFC functionality is available and scanning nearby tags is allowed. Writing to tags needs to be manually enabled.
  * `allow-is-available`
  * `allow-scan`


## Permission Table
Identifier | Description  
---|---  
`nfc:allow-is-available` |  Enables the is_available command without any pre-configured scope.  
`nfc:deny-is-available` |  Denies the is_available command without any pre-configured scope.  
`nfc:allow-scan` |  Enables the scan command without any pre-configured scope.  
`nfc:deny-scan` |  Denies the scan command without any pre-configured scope.  
`nfc:allow-write` |  Enables the write command without any pre-configured scope.  
`nfc:deny-write` |  Denies the write command without any pre-configured scope.  
© 2025 Tauri Contributors. CC-BY / MIT
