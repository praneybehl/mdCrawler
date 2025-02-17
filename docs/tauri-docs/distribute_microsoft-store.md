Skip to content
# Microsoft Store
Microsoft Store is the Windows app store operated by Microsoft.
This guide only covers details for distributing Windows Apps directly to the Microsoft Store. See the Windows Installer guide for more information on Windows installer distribution options and configurations.
## Requirements
To publish apps on the Microsoft Store you must have a Microsoft account and enroll as a developer either as an individual or as a company.
## Changing App Icon
The Tauri CLI can generate all icons your app needs, including Microsoft Store icons. Use the `tauri icon` command to generate app icons from a single PNG or SVG source:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriicon/path/to/app-icon.png

```

```

yarntauriicon/path/to/app-icon.png

```

```

pnpmtauriicon/path/to/app-icon.png

```

```

denotasktauriicon/path/to/app-icon.png

```

```

cargotauriicon/path/to/app-icon.png

```

## Setting up
After you have enrolled as a developer with your Microsoft account you need to register your app in the Apps and Games page. Click `New Product`, select `EXE or MSI app` and reserve a unique name for your app.
## Build and upload
Currently Tauri only generates EXE and MSI installers, so you must create a Microsoft Store application that only links to the unpacked application. The installer linked in the Microsoft Installer must be offline, handle auto-updates and be code signed.
See the official publish documentation for more information.
### Offline Installer
The Windows installer distributed through the Microsoft Store must use the Offline Installer Webview2 installation option.
To only apply this installer configuration when bundling for Microsoft Store, you can define a separate Tauri configuration file:
"src-tauri/tauri.microsoftstore.conf.json```

{
"bundle": {
"windows": {
"webviewInstallMode": {
"type": "offlineInstaller"
}
}
}
}

```

Then merge that config file with the main one when bundling your Tauri app for Microsoft Store:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauribuild----no-bundle
npmruntauribundle----configsrc-tauri/tauri.microsoftstore.conf.json

```

```

yarntauribuild--no-bundle
yarntauribundle--configsrc-tauri/tauri.microsoftstore.conf.json

```

```

pnpmtauribuild--no-bundle
pnpmtauribundle--configsrc-tauri/tauri.microsoftstore.conf.json

```

```

denotasktauribuild--no-bundle
denotasktauribundle--configsrc-tauri/tauri.microsoftstore.conf.json

```

```

cargotauribuild--no-bundle
cargotauribundle--configsrc-tauri/tauri.microsoftstore.conf.json

```

This is particularly useful when setting up your CI/CD to upload your app to the Microsoft Store while having a separate configuration for the Windows installer you distribute outside the app store.
### Publisher
Your application publisher name cannot match the application product name.
If the publisher configuration value is not set, Tauri derives it from the second part of your bundle identifier. Since the publisher name cannot match the product name, the following configuration is invalid:
tauri.conf.json```

{
"productName": "Example",
"identifier": "com.example.app"
}

```

In this case you can define the publisher value separately to fix this conflict:
tauri.conf.json```

{
"productName": "Example",
"identifier": "com.example.app",
"bundle": {
"publisher": "Example Inc."
}
}

```

### Upload
After building the Windows installer for Microsoft Store, you can upload it to the distribution service of your choice and link it in your application page in the Microsoft Store website.
© 2025 Tauri Contributors. CC-BY / MIT
