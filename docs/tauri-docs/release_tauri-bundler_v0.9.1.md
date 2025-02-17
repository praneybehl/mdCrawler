Skip to content
# tauri-bundler@0.9.1
ReturnView on GitHub
  * Hide external scripts output unless `--verbose` is passed. 
    * 78add1e feat(bundler): hide output from shell scripts unless —verbose is passed (fixes #888) (#893) on 2020-07-26
  * Fixes the target directory detection, respecting the `CARGO_TARGET_DIR` and `.cargo/config (build.target-dir)` options to set the Cargo output directory. 
    * 63b9c64 fix(bundler) properly detect the target directory (#895) on 2020-07-25
  * Bundling every DLL file on the binary directory. 
    * a00ac02 fix(bundler) webview dll not being bundled, fixes #875 (#889) on 2020-07-24


© 2025 Tauri Contributors. CC-BY / MIT
