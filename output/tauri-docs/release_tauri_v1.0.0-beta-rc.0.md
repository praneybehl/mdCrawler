Skip to content
# tauri@1.0.0-beta-rc.0
ReturnView on GitHub
  * internal refactoring of `Params` to allow for easier usage without a private trait with only 1 implementor. `ParamsPrivate` -> `ParamsBase` `ManagerPrivate` -> `ManagerBase` (new) `Args`, crate only. Now implements `Params`/`ParamsBase`. `App` and `Window` use `WindowManager` directly
  * ec27ca8 refactor(tauri): remove private params trait methods (#1484) on 2021-04-14
  * Updated `wry`, fixing an issue with the draggable region. 
    * f2d24ef chore(deps): update wry (#1482) on 2021-04-14
  * Now Tauri commands always returns Promise<T>. 
    * ea73325 refactor(core): all API are now promise based (#1239) on 2021-02-16
  * Rename macOS bundle settings from `osx` to `macOS`. 
    * 080f639 refactor(bundler): specific settings on dedicated structs, update README (#1380) on 2021-03-25
  * The shell process spawning API was rewritten and now includes stream access. 
    * 3713066 refactor(core): rewrite shell execute API, closes #1229 (#1408) on 2021-03-31
  * The Tauri files are now read on the app space instead of the `tauri` create. Also, the `AppBuilder` `build` function now returns a Result. 
    * e02c941 refactor(tauri): support for building without environmental variables (#850) on 2021-02-09
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
  * Tauri now uses explicit Error variants with `thiserror` instead of relying on `anyhow`. 
    * 156a0ad refactor(tauri): use explicit error types instead of anyhow (#1209) on 2021-02-10
  * Align HTTP API types with the documentation. 
    * 2fc39fc fix(api/http): correct types (#1360) on 2021-03-17
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
  * Replace `\` with `\\` in css assets that are lazy loaded. Since these are injected in a template literal, backslashes must be escaped. Backslashes are sometimes used for octal sequences in CSS. 
    * 4491c70 fix(tauri/asset): escape octal sequences in css (#1166) on 2021-01-30
  * Replaces the embedded-server mode with Wry’s custom protocol feature. This allows assets to be transferred to the webview directly, instead of through a localhost server. 
    * 0c691f4 feat(core): Use Wry custom protocol instead of embedded server (#1296) on 2021-02-25
  * The `message` and `ask` dialogs now use `tinyfiledialogs-rs` instead of `tauri-dialog-rs`. 
    * 6eee355 refactor(core): use tinyfiledialogs-rs for message/confirmation dialogs (#1255) on 2021-02-17
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
  * Refactor the event callback payload and return an unlisten function on the `listen` API. 
    * b670ec5 refactor(core): add `unlisten`, `once` APIs to the event system (#1359) on 2021-03-16
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
  * Adds `unlisten` and `once` APIs on the Rust event system. 
    * b670ec5 refactor(core): add `unlisten`, `once` APIs to the event system (#1359) on 2021-03-16
  * The `tauri::event` module has been moved to a Webview manager API. 
    * 07208df feat(core): add mult-window support (#1217) on 2021-02-11
  * The file dialog API now uses rfd. The filter option is now an array of `{ name: string, extensions: string[] }`. 
    * 2326bcd refactor(core): use `nfd` for file dialogs, closes #1251 (#1257) on 2021-02-18
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
  * Tauri now emits events on file drops on the webview window. 
    * 2db901e feat(core): add file drop handler (#1352) on 2021-03-12
  * Fixes `resource_dir` resolution on AppImage. 
    * bd1df5d fix: get correct resource dir in AppImge (fix #1308) (#1333) on 2021-03-12
  * Fixed missing ‘App’ variant & string promise instead of void promise. 
    * 44fc65c Fixing TS API typings (#1451) on 2021-04-11
    * aea6145 refactor(repo): add /tooling folder (#1457) on 2021-04-12
  * The HTTP API was improved with client caching and better payload and response types. 
    * a7bc472 refactor(core): improve HTTP API, closes #1098 (#1237) on 2021-02-15
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
  * Added new JavaScript API to extract `name`, `version`, `tauri version` from the running application. We exposed `relaunch` and `exit` as well to control your application state. 
    * e511d39 feat(api): Expose application metadata and functions to JS api - fix #1387 (#1445) on 2021-04-08
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
  * The event listener `once` kind was moved to a dedicated function. 
    * 372036c refactor(api): move event’s `once` to its own function (#1276) on 2021-02-23
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
  * Use `JSON.parse(String.raw`{arg}`)` for communicating serialized JSON objects and arrays < 1 GB to the Webview from Rust.


https://github.com/GoogleChromeLabs/json-parse-benchmark
  * eeb2030 Use JSON.parse instead of literal JS for callback formatting (#1370) on 2021-04-07
  * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
  * Update all code files to have our license header. 
    * bf82136 feat(license): SPDX Headers (#1449) on 2021-04-11
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
    * aea6145 refactor(repo): add /tooling folder (#1457) on 2021-04-12
  * Added support to multiple windows. 
    * 07208df feat(core): add mult-window support (#1217) on 2021-02-11
  * Adds `productName` and `version` configs on `tauri.conf.json &gt; package`. 
    * 5b3d9b2 feat(config): allow setting product name and version on tauri.conf.json (#1358) on 2021-03-22
    * aea6145 refactor(repo): add /tooling folder (#1457) on 2021-04-12
  * Plugins are now configurable through a `tauri.conf.json &gt; &quot;plugins&quot; &gt; $pluginName` object. 
    * 2058cc3 feat(tauri): add plugin `initialize` (with config) API, run in parallel (#1194) on 2021-02-10
  * Renamed the `Plugin` trait `init_script` to `initialization_script`. 
    * 5c5d8f8 refactor(tauri): rename `init_script` to `initialization_script` (#1200) on 2021-02-10
  * The plugin instance is now mutable and must be `Send`. 
    * fb607ee refactor(tauri): plugin trait with mutable references (#1197) on 2021-02-10
    * 1318ffb refactor(core): remove async from app hooks, add InvokeMessage type (#1392) on 2021-03-26
  * Fixes the event system usage on the plugin `ready` hook. 
    * 23132ac fix(tauri): run plugin::ready without webview.dispatch (#1164) on 2021-01-29
  * The `allowlist` configuration now has one object per module. 
    * e0be59e refactor(core): split allowlist configuration per module (#1263) on 2021-02-20
  * The Tauri script is now injected with the webview `init` API, so it is available after page changes. 
    * 4412b7c refactor(tauri): inject script with webview init API (#1186) on 2021-02-05
    * 8bdd894 refactor(core): move bundle script to /tauri crate (#1377) on 2021-03-23
  * Removed the `no-server` mode, the `inliner`, the `dev` server proxy and the `loadAsset` API. 
    * 84d7cda refactor(core): remove `no-server` and its APIs (#1215) on 2021-02-11
    * aea6145 refactor(repo): add /tooling folder (#1457) on 2021-04-12
  * Adds a global shortcut API. 
    * 855effa feat(core): globalShortcut API (#1232) on 2021-02-14
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
  * Added `async` support to the Tauri Rust core on commit #a169b67. 
    * 2bf55f8 chore: add changefile on 2021-02-03
    * e02c941 refactor(tauri): support for building without environmental variables (#850) on 2021-02-09
  * Alpha version of tauri-updater. Please refer to the `README` for more details. 
    * 6d70c8e feat(updater): Alpha version (#643) on 2021-04-05
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
    * aea6145 refactor(repo): add /tooling folder (#1457) on 2021-04-12
  * The Tauri integration with Webview was refactored to use traits, which allows custom implementations by developers and simplifies changes on the webview implementation. 
    * b9ce7b9 refactor(tauri): Webview traits (#1183) on 2021-02-05
  * Added window management and window creation APIs. 
    * a3d6dff feat(core): window API (#1225) on 2021-02-13
    * 641374b feat(core): window creation at runtime (#1249) on 2021-02-17
  * Use WRY as Webview interface, thanks to @wusyong. 
    * 99ecf7b feat(tauri): use WRY as webview engine (#1190) on 2021-02-08


© 2025 Tauri Contributors. CC-BY / MIT
