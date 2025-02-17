Skip to content
# tauri-cli@1.0.0-beta.6
ReturnView on GitHub
  * Added `APPLE_SIGNING_IDENTITY` as supported environment variable for the bundler. 
    * 44f6ee4c chore(ci): add step to detect code signing (#2245) on 2021-08-08
  * Added configuration for the WiX banner icon under `tauri.conf.json &gt; tauri &gt; bundle &gt; windows &gt; wix &gt; bannerPath`. 
    * 13003ec7 feat(bundler): add config for WiX banner path, closes #2175 (#2448) on 2021-08-16
  * Added configuration for the WiX dialog background bitmap under `tauri.conf.json &gt; tauri &gt; bundle &gt; windows &gt; wix &gt; dialogImagePath`. 
    * 9bfdeb42 feat(bundler): add config for WiX dialog image path (#2449) on 2021-08-16
  * Only convert package name and binary name to kebab-case, keeping the `.desktop` `Name` field with the original configured value. 
    * 3f039cb8 fix: keep original `productName` for .desktop `Name` field, closes #2295 (#2384) on 2021-08-10
  * Merge platform-specific `tauri.linux.conf.json`, `tauri.windows.conf.json` and `tauri.macos.conf.json` into the config JSON from `tauri.conf.json`. 
    * 71d687b7 feat(cli.rs): platform-specific conf.json (#2309) on 2021-07-28
  * Update minimum Rust version to 1.54.0. 
    * a5394716 chore: update rust to 1.54.0 (#2434) on 2021-08-15


© 2025 Tauri Contributors. CC-BY / MIT
