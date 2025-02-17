Skip to content
# tao@0.9.0
ReturnView on GitHub
  * Add standalone webview ndk port. 
    * 68c9f07e Implement standalone webview ndk (#385) on 2022-05-19
  * Update the `windows` crate to the latest 0.37.0 release.


The `#[implement]` macro in `windows-implement` and the `implement` feature in `windows` depend on some `const` generic features which stabilized in `rustc` 1.61. The MSRV on Windows targets is effectively 1.61, but other targets do not require these features.
Since developers on non-Windows platforms are not always able to upgrade their toolchain with `rustup`, the package remains at 1.56. Windows developers may get less friendly compiler errors about using unstable language features until they upgrade their toolchain if they build `tao` without `wry`, which has some Windows-specific dependencies that transitively raise the MSRV for `wry` to 1.61.
  * 93c256f9 Update the windows-rs crate to 0.37.0 (#400) on 2022-05-23


© 2025 Tauri Contributors. CC-BY / MIT
