Skip to content
# @tauri-apps/api@1.0.0-beta-rc.0
ReturnView on GitHub
  * Add current working directory to the path api module. 
    * 52c2baf feat: add current working directory to path api module (#1375) on 2021-03-23
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
  * The shell process spawning API was rewritten and now includes stream access. 
    * 3713066 refactor(core): rewrite shell execute API, closes #1229 (#1408) on 2021-03-31
  * The file dialog API now uses rfd. The filter option is now an array of `{ name: string, extensions: string[] }`. 
    * 2326bcd refactor(core): use `nfd` for file dialogs, closes #1251 (#1257) on 2021-02-18
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
  * The HTTP API was improved with client caching and better payload and response types. 
    * a7bc472 refactor(core): improve HTTP API, closes #1098 (#1237) on 2021-02-15
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
  * Update all code files to have our license header. 
    * bf82136 feat(license): SPDX Headers (#1449) on 2021-04-11
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
    * aea6145 refactor(repo): add /tooling folder (#1457) on 2021-04-12
  * Use secure RNG on callback function names. 
    * c8992bb refactor(api): use secure RNG, closes #1356 (#1398) on 2021-03-30
  * The invoke function can now be called with the cmd as the first parameter and the args as the second. 
    * 427d170 feat(api/invoke): separate cmd arg (#1321) on 2021-03-04
  * Adds a global shortcut API. 
    * 855effa feat(core): globalShortcut API (#1232) on 2021-02-14
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
  * Added window management and window creation APIs. 
    * a3d6dff feat(core): window API (#1225) on 2021-02-13
    * 641374b feat(core): window creation at runtime (#1249) on 2021-02-17


© 2025 Tauri Contributors. CC-BY / MIT
