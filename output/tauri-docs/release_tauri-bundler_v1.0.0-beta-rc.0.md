Skip to content
# tauri-bundler@1.0.0-beta-rc.0
ReturnView on GitHub
  * Append app version and OS architecture on AppImage output filename. 
    * ae76c60 fix(bundler): appimage paths and filename (#1227) on 2021-02-13
  * The Tauri bundler is now a general purpose library instead of a Cargo custom subcommand. 
    * b1e6b74 refactor(cli): decouple bundler from cargo (#1269) on 2021-02-21
  * Rename macOS bundle settings from `osx` to `macOS`. 
    * 080f639 refactor(bundler): specific settings on dedicated structs, update README (#1380) on 2021-03-25
  * The `dev` and `build` pipeline is now written in Rust. 
    * 3e8abe3 feat(cli) rewrite the core CLI in Rust (#851) on 2021-01-30
    * aea6145 refactor(repo): add /tooling folder (#1457) on 2021-04-12
  * Update all code files to have our license header. 
    * bf82136 feat(license): SPDX Headers (#1449) on 2021-04-11
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
    * aea6145 refactor(repo): add /tooling folder (#1457) on 2021-04-12
  * Alpha version of tauri-updater. Please refer to the `README` for more details. 
    * 6d70c8e feat(updater): Alpha version (#643) on 2021-04-05
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
    * aea6145 refactor(repo): add /tooling folder (#1457) on 2021-04-12
  * Bundle Visual C++ redistributable files with VC142_CRT merge modules. 
    * 3047a18 feat(bundler): add visual c++ redistributable files with MSM (#1368) on 2021-03-22
  * Automatically install Webview2 runtime alongside app. 
    * 8e9752b feat(bundler/wix): install webview2 runtime (#1329) on 2021-03-07
  * Fixes the bundler workspace detection. 
    * e34ee4c fix(bundler): workspace detection, closes #1007 (#1235) on 2021-02-14


© 2025 Tauri Contributors. CC-BY / MIT
