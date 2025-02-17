Skip to content
# tauri-bundler@1.0.0-rc.0
ReturnView on GitHub
  * Provide a provider short name for macOS app notarization if your Apple developer account is connected to more than one team.
    * 8ab8d529 Fix #3288: Add provider_short_name for macOS (#3289) on 2022-01-27
  * Allow building AppImages on systems without FUSE setup.
    * 28dd9adb feat(bundler): support building AppImage without FUSE (#3259) on 2022-01-21
  * Fixes AppImage crashes caused by missing WebKit runtime files.
    * bec7833a fix(bundler): bundle additional webkit files. patch absolute paths in libwebkit*.so files. fixes #2805,#2689 (#2940) on 2021-12-09
  * Initialize the preselected installation path with the location of the previous installation.
    * ac1dfd8c feat(bundler): initialize msi install path with previous location (#3158) on 2022-01-07
  * Replaces usage of the nightly command `RUSTC_BOOTSTRAP=1 rustc -Z unstable-options --print target-spec-json` with the stable command `rustc --print cfg`, improving target triple detection.
    * 839daec7 fix(bundler): Use `arch` instead of `llvm_target`. fix #3285 (#3286) on 2022-02-05
  * Fixes a deadlock on the `ResourcePaths` iterator.
    * 4c1be451 fix(bundler): deadlock on `ResourcePaths` iterator, closes #3146 (#3152) on 2022-01-02
  * Move the copying of resources and sidecars from `cli.rs` to `tauri-build` so using the Cargo CLI directly processes the files for the application execution in development.
    * 5eb72c24 refactor: copy resources and sidecars on the Cargo build script (#3357) on 2022-02-08
  * The minimum Rust version is now `1.56`.
    * a9dfc015 feat: update to edition 2021 and set minimum rust to 1.56 (#2789) on 2021-10-22
  * **Breaking change:** The sidecar’s target triple suffix is now removed at build time.
    * 3035e458 Remove target triple from sidecar bin paths, closes #3355 (#3356) on 2022-02-07
  * When building Universal macOS Binaries through the virtual target `universal-apple-darwin`:
  * Expect a universal binary to be created by the user
  * Ensure that binary is bundled and accessed correctly at runtime
  * 3035e458 Remove target triple from sidecar bin paths, closes #3355 (#3356) on 2022-02-07
  * Allow setting the localization file for WiX.
    * af329f27 feat(bundler): wix localization, closes #3174 (#3179) on 2022-02-05
  * Fix registry keys on the WiX template.
    * 2be1abd1 fix(bundler) wix template escape character (#2608) on 2021-09-21
  * Configure WiX to add an option to launch the application after finishing setup.
    * feb3a8f8 feat(bundler): configure WiX to add launch option, closes #3015 (#3043) on 2021-12-09
  * Sign WiX installer in addition to the executable file.
    * d801cc89 wix installer is also signed (#3266) on 2022-01-23


© 2025 Tauri Contributors. CC-BY / MIT
