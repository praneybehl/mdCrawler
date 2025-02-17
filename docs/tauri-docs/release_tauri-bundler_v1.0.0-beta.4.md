Skip to content
# tauri-bundler@1.0.0-beta.4
ReturnView on GitHub
  * Merge Tauri-generated Info.plist with the contents of `src-tauri/Info.plist` if it exists. 
    * 537ab1b6 feat(core): inject src-tauri/Info.plist file on dev and merge on bundle, closes #1570 #2338 (#2444) on 2021-08-15
  * Change the WiX config to allow upgrading installation with same version instead of duplicating the application. 
    * dd5e1ede fix(bundler): `AllowSameVersionUpgrades` on WiX, closes #2211 (#2428) on 2021-08-14
  * Check target architecture at runtime running `$ RUSTC_BOOTSTRAP=1 rustc -Z unstable-options --print target-spec-json` and parsing the `llvm-target` field, fixing macOS M1 sidecar check until we can compile the CLI with M1 target on GitHub Actions. 
    * 5ebf389f feat(bundler): check target arch at runtime, closes #2286 (#2422) on 2021-08-13
  * Added `banner_path` field to the `WixSettings` struct. 
    * 13003ec7 feat(bundler): add config for WiX banner path, closes #2175 (#2448) on 2021-08-16
  * Added `dialog_image_path` field to the `WixSettings` struct. 
    * 9bfdeb42 feat(bundler): add config for WiX dialog image path (#2449) on 2021-08-16
  * Only convert package name and binary name to kebab-case, keeping the `.desktop` `Name` field with the original configured value. 
    * 3f039cb8 fix: keep original `productName` for .desktop `Name` field, closes #2295 (#2384) on 2021-08-10
  * Use `linuxdeploy` instead of `appimagetool` for `AppImage` bundling. 
    * 397710b2 refactor(bundler): use linuxdeploy instead of appimagetool, closes #1986 (#2437) on 2021-08-15


© 2025 Tauri Contributors. CC-BY / MIT
