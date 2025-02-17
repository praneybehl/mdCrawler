Skip to content
# Announcing Tauri 1.1.0
Sep 15, 2022 
![Lucas Nogueira](https://v2.tauri.app/authors/lucasfernog.jpeg)
Lucas Nogueira
Tauri Co-Founder
![Tauri 1.1 Launch Hero Image](https://v2.tauri.app/_astro/header.CFmsZxST_Zpnkhx.webp)
After 113 pull requests and nearly two months of work, the Tauri team is pleased to announce the 1.1.0 release. The changes were internally audited and no security issues were found.
You can update the dependencies with:
  * npm 
  * yarn 
  * pnpm 
  * cargo 


```

npminstall@tauri-apps/cli@latest@tauri-apps/api@latest

```

```

yarnupgrade@tauri-apps/cli@tauri-apps/api--latest

```

```

pnpmupdate@tauri-apps/cli@tauri-apps/api--latest

```

```

cargoupdate

```

## What’s New in 1.1.0
### Security patch
This release includes a patch for a security vulnerability reported by @martin-ocasek. The `readDir` function was able to return entries outside the configured scope when a symlink is found. The patch is also available in Tauri 1.0.6. See the issue on GitHub for more details.
### Icon Generation
We have been recommending to use the tauricon project to generate icons for your Tauri application using a single source PNG. Several issues have been reported, and we decided to “Rewrite It In Rust” to enhance its stability. This allowed us to move this functionality to the main Tauri CLI, so now you can use the `tauri icon` command.
### `cargo-binstall` Support for Tauri CLI
The Tauri CLI can now be installed using cargo-binstall, a mechanism to download and install pre-built Rust binaries. The binaries are available for the main targets and can be installed with:
```

$ cargo install cargo-binstall
$ cargo binstall tauri-cli
$ cargo tauri dev # run any Tauri command!

```

### Create System Trays at Runtime
The system tray APIs (previously only available in `tauri::Builder::system_tray`) can now be used at runtime with `tauri::SystemTray` giving you control over its lifetime and even create multiple trays.
Here’s a quick example on how to use it:
```

use tauri::{Builder, CustomMenuItem, SystemTray, SystemTrayEvent, SystemTrayMenu};
Builder::default()
.setup(|app| {
lethandle=app.handle();
SystemTray::new()
.with_id("main")
.with_menu(
SystemTrayMenu::new().add_item(CustomMenuItem::new("quit", "Quit"))
)
.on_event(move|event| {
lettray_handle=handle.tray_handle_by_id("main").unwrap();
iflet SystemTrayEvent::MenuItemClick { id, .. } =event {
ifid=="quit" {
tray_handle.destroy().unwrap();
}
}
})
.build(&handle)
.expect("unable to create tray");
});

```

### TOML Configuration Support
In the 1.0 releases Tauri supports the `JSON` configuration format by default, and `JSON5` when the `config-json5` Cargo feature is enabled, meaning the following configurations are valid:
tauri.conf.json```

{
"build": {
"devPath": "http://localhost:8000",
"distDir": "../dist"
}
}

```

```

{
build: {
// devServer URL (comments are allowed!)
devPath: 'http://localhost:8000',
distDir: '../dist',
},
}

```

The 1.1.0 release includes TOML support behind the `config-toml` Cargo feature. Now you can define your Tauri configuration in a `Tauri.toml` file:
Tauri.toml```

[build]
dev-path = "http://localhost:8000"
dist-dir = "../dist"

```

### Dependency Updates
This release includes some dependency updates that must be handled in your app if you implement platform-specific functionalities using these crates. The most important updates are:
  * `windows` updated to 0.39.0
  * `webview2-com` updated to 0.19.1
  * `raw-window-handle` updated to 0.5.0


Make sure you also update plugins such as `window-vibrancy` and `window-shadows` to latest.
## Contributors to 1.1.0
The Tauri team thanks the following contributors for the 1.1.0 release:
  * Berrysoft
  * keraf
  * jsoref
  * A-kirami
  * olivierlemasle
  * mateo-gallardo
  * rockerBOO
  * Flecart
  * brian14708
  * koriwi
  * paul-soporan
  * shniubobo
  * horochx
  * RubenKelevra
  * LIMPIX31
  * AxlLind


# Other Changes
There are a lot of smaller changes and bug fixes in this release. You can see a summary of the release notes in the following sections. The complete changelog can be found on the releases page.
## New
  * `tauri icon` command
  * `exists` API in the `fs` module
  * Option to disable the dev watcher with `tauri dev --no-watch`
  * Automatically use any `.taurignore` file as ignore rules for dev watcher and app path finder
  * Add support to cargo-binstall for the Tauri CLI
  * TOML configuration format (Tauri.toml)
  * Theme APIs on Linux
  * Create system trays at runtime
  * `beforeBundleCommand` configuration
  * `beforeDevCommand` and `beforeBuildCommand` now has an option to configure the current working directory
  * `api::Command::encoding` method to set the stdout/stderr encoding
  * Added `native-tls-vendored` and `reqwest-native-tls-vendored` Cargo features to compile and statically link to a vendored copy of OpenSSL on Linux
  * Implement `raw_window_handle::HasRawDisplayHandle` for `App` and `AppHandle`


## Fixes
  * CLI parser ignoring inner subcommands.
  * Updater breaking the app icon in Finder.
  * Fix root of codegen output when using the `CodegenContext` API.


## Security
  * Fix `fs.readDir` recursive option reading symlinked directories that are not allowed by the scope


## Improvements
  * Validate updater signature against configured public key
  * Return an error if a sidecar is configured with the same file name as the application.
  * Keep the created windows in a RefCell instead of a Mutex, avoiding deadlocks
  * Prompt for `beforeDevCommand` and `beforeBuildCommand` in `tauri init`.
  * Use `cargo metadata` to detect the workspace root and target directory.
  * Allow configuring the `before_dev_command` to force the CLI to wait for the command to finish before proceeding.
  * Avoid re-downloading AppImage build tools on every build.
  * Retain command line arguments in `api::process::restart`
  * Enhance the dialog style on Windows via the manifest dependency `Microsoft.Windows.Common-Controls v6.0.0.0`.
  * Rerun codegen if assets or icons change
  * Only rewrite temporary icon files when the content change, avoid needless rebuilds.


Announcing tauri-egui 0.1.0
Tauri Programme Turns 1 and Board Elections
© 2025 Tauri Contributors. CC-BY / MIT
