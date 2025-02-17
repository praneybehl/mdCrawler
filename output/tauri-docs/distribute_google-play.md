Skip to content
# Google Play
Google Play is the Android app distribution service maintained by Google.
This guide covers the requirements for publishing your Android app on Google Play.
## Requirements
To distribute Android apps in the Play Store you must create a Play Console developer account.
Additionally, you must setup code signing.
See the release checklist for more information.
## Changing App Icon
After running `tauri android init` to setup the Android Studio project, you can use the `tauri icon` command to update the app icons.
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
Once you’ve created a Play Console developer account, you need to register your app on the Google Play Console website. It will guide you through all the required forms and setup tasks.
## Build
You can build an Android App Bundle (AAB) to upload to Google Play by running the following command:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriandroidbuild----aab

```

```

yarntauriandroidbuild--aab

```

```

pnpmtauriandroidbuild--aab

```

```

denotasktauriandroidbuild--aab

```

```

cargotauriandroidbuild--aab

```

Tauri derives the version code from the value defined in `tauri.conf.json > version` (`versionCode = major*1000000 + minor*1000 + patch`). You can set a custom version code in the [`tauri.conf.json > bundle > android > versionCode`] configuration if you need a different version code scheme e.g. sequential codes:
tauri.conf.json```

{
"bundle": {
"android": {
"versionCode": 100
}
}
}

```

### Build APKs
The AAB format is the recommended bundle file to upload to Google Play, but it is also possible to generate APKs that can be used for testing or distribution outside the store. To compile APKs for your app you can use the `--apk` argument:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriandroidbuild----apk

```

```

yarntauriandroidbuild--apk

```

```

pnpmtauriandroidbuild--apk

```

```

denotasktauriandroidbuild--apk

```

```

cargotauriandroidbuild--apk

```

### Architecture selection
By default Tauri builds your app for all supported architectures (aarch64, armv7, i686 and x86_64). To only compile for a subset of targets, you can use the `--target` argument:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriandroidbuild----aab--targetaarch64--targetarmv7

```

```

yarntauriandroidbuild--aab--targetaarch64--targetarmv7

```

```

pnpmtauriandroidbuild--aab--targetaarch64--targetarmv7

```

```

denotasktauriandroidbuild--aab--targetaarch64--targetarmv7

```

```

cargotauriandroidbuild--aab--targetaarch64--targetarmv7

```

### Separate bundles per architecture
By default the generated AAB and APK is universal, containing all supported targets. To generate individual bundles per target, use the `--split-per-abi` argument.
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriandroidbuild----apk--split-per-abi

```

```

yarntauriandroidbuild--apk--split-per-abi

```

```

pnpmtauriandroidbuild--apk--split-per-abi

```

```

denotasktauriandroidbuild--apk--split-per-abi

```

```

cargotauriandroidbuild--apk--split-per-abi

```

### Changing the minimum supported Android version
The minimum supported Android version for Tauri apps is Android 7.0 (codename Nougat, SDK 24).
There are some techniques to use newer Android APIs while still supporting older systems. See the Android documentation for more information.
If your app must execute on a newer Android version, you can configure [`tauri.conf.json > bundle > android > minSdkVersion`]:
tauri.conf.json```

{
"bundle": {
"android": {
"minSdkVersion": 28
}
}
}

```

## Upload
After building your app and generating the Android App Bundle file, which can be found in `gen/android/app/build/outputs/bundle/universalRelease/app-universal-release.aab`, you can now create a new release and upload it in the Google Play Console.
The first upload must be made manually in the website so it can verify your app signature and bundle identifier. Tauri currently does not offer a way to automate the process of creating Android releases, which must leverage the Google Play Developer API, but it is a work in progress.
© 2025 Tauri Contributors. CC-BY / MIT
