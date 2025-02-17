Skip to content
# DMG
The DMG (Apple Disk Image) format is a common macOS installer file that wraps your App Bundle in a user-friendly installation window.
The installer window includes your app icon and the Applications folder icon, where the user is expected to drag the app icon to the Applications folder icon to install it. It is the most common installation method for macOS applications distributed outside the App Store.
This guide only covers details for distributing apps outside the App Store using the DMG format. See the App Bundle distribution guide for more information on macOS distribution options and configurations. To distribute your macOS app in the App Store, see the App Store distribution guide.
To create an Apple Disk Image for your app you can use the Tauri CLI and run the `tauri build` command in a Mac computer:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauribuild----bundlesdmg

```

```

yarntauribuild--bundlesdmg

```

```

pnpmtauribuild--bundlesdmg

```

```

denotasktauribuild--bundlesdmg

```

```

cargotauribuild--bundlesdmg

```

![Standard DMG window](https://v2.tauri.app/_astro/standard-dmg-light.DwnO_utB_Z21IkvW.webp) ![Standard DMG window](https://v2.tauri.app/_astro/standard-dmg-dark.DDFg0R9E_Z2vFMKv.webp)
## Window background
You can set a custom background image to the DMG installation window with the [`tauri.conf.json > bundle > macOS > dmg > background`] configuration option:
tauri.conf.json```

{
"bundle": {
"macOS": {
"dmg": {
"background": "./images/"
}
}
}
}

```

For instance your DMG background image can include an arrow to indicate to the user that it must drag the app icon to the Applications folder.
## Window size and position
The default window size is 660x400. If you need a different size to fit your custom background image, set the [`tauri.conf.json > bundle > macOS > dmg > windowSize`] configuration:
tauri.conf.json```

{
"bundle": {
"macOS": {
"dmg": {
"windowSize": {
"width": 800,
"height": 600
}
}
}
}
}

```

Additionally you can set the initial window position via [`tauri.conf.json > bundle > macOS > dmg > windowPosition`]:
tauri.conf.json```

{
"bundle": {
"macOS": {
"dmg": {
"windowPosition": {
"x": 400,
"y": 400
}
}
}
}
}

```

## Icon position
You can change the app and _Applications folder_ icon position with the appPosition and applicationFolderPosition configuration values respectively:
tauri.conf.json```

{
"bundle": {
"macOS": {
"dmg": {
"appPosition": {
"x": 180,
"y": 220
},
"applicationFolderPosition": {
"x": 480,
"y": 220
}
}
}
}
}

```

© 2025 Tauri Contributors. CC-BY / MIT
