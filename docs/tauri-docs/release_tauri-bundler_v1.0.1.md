Skip to content
# tauri-bundler@1.0.1
ReturnView on GitHub
  * Fix AppImage bundling when appimagelauncher is enabled. 
    * b0133083 Fix appimage creation in container when host has appimagelauncher enabled (#4457) on 2022-06-27
  * Fixes AppImage bundler crashes when the file path contains whitespace. 
    * 82eb6e79 fix(bundler): Fix appimage bundler crashing if path has spaces (#4471) on 2022-06-26
  * Ensure `usr/lib` is a directory in the AppImage bundle. 
    * aa0336d6 fix(bundler): ensure AppImage usr/lib is a dir (#4419) on 2022-06-21
  * AppImage bundling will now prefer bundling correctly named appindicator library (including `.1` version suffix). With a symlink for compatibility with the old naming. 
    * bf45ca1d fix(cli,bundler): prefer AppImage libraries with ABI version (#4505) on 2022-06-29
  * Fix language code for korean (ko-KR). 
    * 08a73acd fix(bundler): fix language code. closes #4437 (#4444) on 2022-06-24
  * Use the plist crate instead of the `PlistBuddy` binary to merge user Info.plist file. 
    * 45076b3e refactor(bundler): use the `plist` crate to create and merge Info.plist (#4412) on 2022-06-21
  * Validate app version before bundling WiX. 
    * 672174b8 feat(bundler): validate version before bundling with WiX (#4429) on 2022-06-21
  * Check if `$HOME\AppData\Local\tauri\WixTools` directory has all the required files and redownload WiX if something is missing. 
    * 956af4f3 feat(bundler): validate wix toolset files, ref #4474 (#4475) on 2022-06-26
  * Added webview install mode options. 
    * 2ca762d2 feat(bundler): extend webview2 installation options, closes #2882 #2452 (#4466) on 2022-06-26


© 2025 Tauri Contributors. CC-BY / MIT
