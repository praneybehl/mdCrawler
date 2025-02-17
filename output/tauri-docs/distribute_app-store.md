Skip to content
# App Store
The Apple App Store is the app marketplace maintained by Apple. You can distribute your Tauri app targeting macOS and iOS via this App Store.
This guide only covers details for distributing apps directly to the App Store. See the general App Bundle for more information on macOS distribution options and configurations.
## Requirements
Distributing iOS and macOS apps requires enrolling to the Apple Developer program.
Additionally, you must setup code signing for macOS and iOS.
## Changing App Icon
After running `tauri ios init` to setup the Xcode project, you can use the `tauri icon` command to update the app icons.
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriicon/path/to/app-icon.png----ios-color#fff

```

```

yarntauriicon/path/to/app-icon.png--ios-color#fff

```

```

pnpmtauriicon/path/to/app-icon.png--ios-color#fff

```

```

denotasktauriicon/path/to/app-icon.png--ios-color#fff

```

```

cargotauriicon/path/to/app-icon.png--ios-color#fff

```

The `--ios-color` argument defines the background color for the iOS icons.
## Setting up
After enrolling to the Apple Developer program, the first step to distribute your Tauri app in the App Store is to register your app in the App Store Connect.
## Build and upload
The Tauri CLI can package your app for macOS and iOS. Running on a macOS machine is a requirement.
Note that Tauri leverages Xcode for the iOS app so you can use Xcode to archive and distribute for iOS instead of the Tauri CLI. To open the iOS project in Xcode for building you must run the following command:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriiosbuild----open

```

```

yarntauriiosbuild--open

```

```

pnpmtauriiosbuild--open

```

```

denotasktauriiosbuild--open

```

```

cargotauriiosbuild--open

```

### macOS
To upload your app to the App Store, first you must ensure all required configuration options are set so you can package the App Bundle, create a signed `.pkg` file and upload it.
The following sections will guide you through the process.
#### Setup
Your app must include some configurations to be accepted by the App Store verification system.
  * Category


Your app must define its `tauri.conf.json > bundle > category` to be displayed in the App Store:
tauri.conf.json```

{
"bundle": {
"category": "Utility"
}
}

```

  * Provisioning profile


You must also create a provisioning profile for your app to be accepted by Apple.
In the Identifiers page, create a new App ID and make sure its “Bundle ID” value matches the identifier set in `tauri.conf.json > identifier`.
Navigate to the Profiles page to create a new provisioning profile. For App Store macOS distribution, it must be a “Mac App Store Connect” profile. Select the appropriate App ID and link the certificate you are using for code signing.
After creating the provisioning profile, download it and save it to a known location and configure Tauri to include it in your app bundle:
tauri.conf.json```

{
"bundle": {
"macOS": {
"files": {
"embedded.provisionprofile": "path/to/profile-name.provisionprofile"
}
}
}
}

```

  * Info.plist


Your app must comply with encryption export regulations. See the official documentation for more information.
Create a Info.plist file in the src-tauri folder:
```

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plistversion="1.0">
<dict>
<key>ITSAppUsesNonExemptEncryption</key>
<false/> # or `true` if your app uses encryption
</dict>
</plist>

```

  * Entitlements


Your app must include the App Sandbox capability to be distributed in the App Store. Additionally, you must also set your App ID and Team ID in the code signing entitlements.
Create a `Entitlements.plist` file in the `src-tauri` folder:
```

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plistversion="1.0">
<dict>
<key>com.apple.security.app-sandbox</key>
<true/>
<key>com.apple.application-identifier</key>
<string>$TEAM_ID.$IDENTIFIER</string>
<key>com.apple.developer.team-identifier</key>
<string>$TEAM_ID</string>
</dict>
</plist>

```

Note that you must replace `$IDENTIFIER` with the `tauri.conf.json > identifier` value and `$TEAM_ID` with your Apple Developer team ID, which can be found in the `App ID Prefix` section in the Identifier you created for the provisioning profile.
And reference that file in the macOS bundle configuration `tauri.conf.json > bundle > macOS > entitlements`:
tauri.conf.json```

{
"bundle": {
"macOS": {
"entitlements": "./Entitlements.plist"
}
}
}

```

You now must build your application with code signing enabled for the entitlements to apply.
Make sure your app works when running in an App Sandbox context.
#### Build
You must upload your macOS application as a `.pkg` file to the App Store. Run the following command to package your app as a macOS App Bundle (`.app` extension):
```

tauri build --bundles app --target universal-apple-darwin

```

See the App Bundle distribution guide for more information on configuration options.
To generate a signed `.pkg` from your app bundle, run the following command:
```

xcrun productbuild --sign "<certificate signing identity>" --component "target/universal-apple-darwin/release/bundle/macos/$APPNAME.app" /Applications "$APPNAME.pkg"

```

Note that you must replace _$APPNAME_ with your app name.
#### Upload
Now you can use the `altool` CLI to upload your app PKG to the App Store:
```

xcrun altool --upload-app --type macos --file "$APPNAME.pkg" --apiKey $APPLE_API_KEY_ID --apiIssuer $APPLE_API_ISSUER

```

Note that `altool` requires an App Store Connect API key to upload your app. See the authentication section for more information.
Your app will then be validated by Apple and available in TestFlight if approved.
### iOS
To build your iOS app, run the `tauri ios build` command:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriiosbuild----export-methodapp-store-connect

```

```

yarntauriiosbuild--export-methodapp-store-connect

```

```

pnpmtauriiosbuild--export-methodapp-store-connect

```

```

denotasktauriiosbuild--export-methodapp-store-connect

```

```

cargotauriiosbuild--export-methodapp-store-connect

```

The generated IPA file can be found in `src-tauri/gen/apple/build/arm64/$APPNAME.ipa`.
Note that you must replace _$APPNAME_ with your app name.
Now you can use the `altool` CLI to upload your iOS app to the App Store:
```

xcrun altool --upload-app --type ios --file "src-tauri/gen/apple/build/arm64/$APPNAME.ipa" --apiKey $APPLE_API_KEY_ID --apiIssuer $APPLE_API_ISSUER

```

Note that `altool` requires an App Store Connect API key to upload your app. See the authentication section for more information.
Your app will then be validated by Apple and available in TestFlight if approved.
### Authentication
The iOS and macOS apps are uploaded using `altool`, which uses an App Store Connect API key to authenticate.
To create a new API key, open the App Store Connect’s Users and Access page, select the Integrations > Individual Keys tab, click on the Add button and select a name and the Developer access. The `APPLE_API_ISSUER` (Issuer ID) is presented above the keys table, and the `APPLE_API_KEY_ID` is the value on the Key ID column on that table. You also need to download the private key, which can only be done once and is only visible after a page reload (the button is shown on the table row for the newly created key). The private key file path must be saved as `AuthKey\_<APPLE_API_KEY_ID>.p8` in one of these directories:`<current-working-directory>/private_keys`, `~/private_keys`, `~/.private_keys`or`~/.appstoreconnect/private_keys`.
© 2025 Tauri Contributors. CC-BY / MIT
