Skip to content
# Announcing the Tauri Mobile Alpha Release
Dec 9, 2022 
![Lucas Nogueira](https://v2.tauri.app/authors/lucasfernog.jpeg)
Lucas Nogueira
Tauri Co-Founder
![Tauri 2.0 Launch Hero Image](https://v2.tauri.app/_astro/header.DJC8YrJ3_Z2lir5I.webp)
Tauri mobile is here! The first alpha release 2.0.0-alpha.0 has been published.
## Updating dependencies
Make sure to update both NPM and Cargo dependencies to the 2.0.0-alpha.0 release. You can update the dependencies with:
  * npm 
  * yarn 
  * pnpm 
  * cargo 


```

npminstall@tauri-apps/cli@next@tauri-apps/api@next

```

```

yarnupgrade@tauri-apps/cli@next@tauri-apps/api@next

```

```

pnpmupdate@tauri-apps/cli@next@tauri-apps/api@next

```

```

cargoaddtauri@2.0.0-alpha.0
cargoaddtauri-build@2.0.0-alpha.0--build
cargoinstalltauri-cli--version"^2.0.0-alpha"--locked

```

## Preview
You can adapt your existing desktop application to run on mobile or start a fresh project. Tauri runs on the connected device or starts an emulator if available.
![iOS Preview](https://v2.tauri.app/_astro/ios-preview.au3ri0xF_Z2bLkJa.webp) ![Android Preview](https://v2.tauri.app/_astro/android-preview.nQXuMXya_Z1Nn7Ek.webp)
## Getting started
Read the complete guide on the `next` documentation website.
## Known issues
  * TLS support has been moved behind a Cargo feature until we figure out how to cross compile OpenSSL on Windows.
  * Currently running on a device is not supported when using Xcode 14.


Migration to webkit2gtk-4.1 on Linux port
Announcing Tauri 1.2.0
© 2025 Tauri Contributors. CC-BY / MIT
