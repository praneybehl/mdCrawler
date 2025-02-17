Skip to content
# Biometric
GitHub npm  crates.io 
API Reference 
Prompt the user for biometric authentication on Android and iOS.
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
Install the biometric plugin to get started.
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

npmruntauriaddbiometric

```

```

yarnruntauriaddbiometric

```

```

pnpmtauriaddbiometric

```

```

denotasktauriaddbiometric

```

```

buntauriaddbiometric

```

```

cargotauriaddbiometric

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-biometric--target'cfg(any(target_os = "android", target_os = "ios"))'

```

  2. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.setup(|app| {
#[cfg(mobile)]
app.handle().plugin(tauri_plugin_biometric::Builder::new().build());
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

npminstall@tauri-apps/plugin-biometric

```

```

yarnadd@tauri-apps/plugin-biometric

```

```

pnpmadd@tauri-apps/plugin-biometric

```

```

denoaddnpm:@tauri-apps/plugin-biometric

```

```

bunadd@tauri-apps/plugin-biometric

```



## Configuration
On iOS the biometric plugin requires the `NSFaceIDUsageDescription` information property list value, which should describe why your app needs to use biometric authentication.
In the `src-tauri/Info.ios.plist` file, add the following snippet:
src-tauri/Info.ios.plist```

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plistversion="1.0">
<dict>
<key>NSFaceIDUsageDescription</key>
<string>Authenticate with biometric</string>
</dict>
</plist>

```

## Usage
This plugin enables you to verify the availability of Biometric Authentication on a device, prompt the user for biometric authentication, and check the result to determine if the authentication was successful or not.
### Check Status
You can check the status of Biometric Authentication, including its availability and the types of biometric authentication methods supported.
  * JavaScript 
  * Rust 


```

import { checkStatus } from'@tauri-apps/plugin-biometric';
const status = await checkStatus();
if (status.isAvailable) {
console.log('Yes! Biometric Authentication is available');
} else {
console.log(
'No! Biometric Authentication is not available due to '+status.error
);
}

```

```

use tauri_plugin_biometric::BiometricExt;
fncheck_biometric(app_handle: tauri::AppHandle) {
letstatus=app_handle.biometric().status().unwrap();
ifstatus.is_available {
println!("Yes! Biometric Authentication is available");
} else {
println!("No! Biometric Authentication is not available due to: {}", status.error.unwrap());
}
}

```

### Authenticate
To prompt the user for Biometric Authentication, utilize the `authenticate()` method.
  * JavaScript 
  * Rust 


```

import { authenticate } from'@tauri-apps/plugin-biometric';
const options = {
// Set true if you want the user to be able to authenticate using phone password
allowDeviceCredential: false,
cancelTitle: "Feature won't work if Canceled",
// iOS only feature
fallbackTitle: 'Sorry, authentication failed',
// Android only features
title: 'Tauri feature',
subtitle: 'Authenticate to access the locked Tauri function',
confirmationRequired: true,
};
try {
awaitauthenticate('This feature is locked', options);
console.log(
'Hooray! Successfully Authenticated! We can now perform the locked Tauri function!'
);
} catch (err) {
console.log('Oh no! Authentication failed because '+err.message);
}

```

```

use tauri_plugin_biometric::{BiometricExt, AuthOptions};
fnbio_auth(app_handle: tauri::AppHandle) {
letoptions= AuthOptions {
// Set True if you want the user to be able to authenticate using phone password
allow_device_credential:false,
cancel_title: Some("Feature won't work if Canceled".to_string()),
// iOS only feature
fallback_title: Some("Sorry, authentication failed".to_string()),
// Android only features
title: Some("Tauri feature".to_string()),
subtitle: Some("Authenticate to access the locked Tauri function".to_string()),
confirmation_required: Some(true),
};
// if the authentication was successful, the function returns Result::Ok()
// otherwise returns Result::Error()
matchapp_handle.biometric().authenticate("This feature is locked".to_string(), options) {
Ok(_) => {
println!("Hooray! Successfully Authenticated! We can now perform the locked Tauri function!");
}
Err(e) => {
println!("Oh no! Authentication failed because : {e}");
}
}
}

```

## Permissions
By default all potentially dangerous plugin commands and scopes are blocked and cannot be accessed. You must modify the permissions in your `capabilities` configuration to enable these.
See the Capabilities Overview for more information and the step by step guide to use plugin permissions.
src-tauri/capabilities/default.json```

{
"$schema": "../gen/schemas/desktop-schema.json",
"identifier": "main-capability",
"description": "Capability for the main window",
"windows": ["main"],
"permissions": ["biometric:default"]
}

```

## Default Permission
This permission set configures which biometric features are by default exposed.
#### Granted Permissions
It allows acccess to all biometric commands.
  * `allow-authenticate`
  * `allow-status`


## Permission Table
Identifier | Description  
---|---  
`biometric:allow-authenticate` |  Enables the authenticate command without any pre-configured scope.  
`biometric:deny-authenticate` |  Denies the authenticate command without any pre-configured scope.  
`biometric:allow-status` |  Enables the status command without any pre-configured scope.  
`biometric:deny-status` |  Denies the status command without any pre-configured scope.  
© 2025 Tauri Contributors. CC-BY / MIT
