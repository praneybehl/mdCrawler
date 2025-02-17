Skip to content
# @tauri-apps/cli@1.0.0-rc.4
ReturnView on GitHub
  * Change the `run` function to take a callback and run asynchronously instead of blocking the event loop. 
    * cd9a20b9 refactor(cli.js): run on separate thread (#3436) on 2022-02-13
  * Improve error message when the dev runner command fails. 
    * 759d1afb feat(cli): improve error message when dev runner command fails (#3447) on 2022-02-13
  * Show full error message from `cli.rs` instead of just the outermost underlying error message. 
    * 63826010 feat(cli.js): show full error message (#3442) on 2022-02-13
  * Increase `tauri.conf.json` directory lookup depth to `3` and allow changing it with the `TAURI_PATH_DEPTH` environment variable. 
    * c6031c70 feat(cli): increase lookup depth, add env var option (#3451) on 2022-02-13
  * Added `tauri-build`, `tao` and `wry` version to the `info` command output. 
    * 16f1173f feat(cli): add tao and wry version to the `info` output (#3443) on 2022-02-13


© 2025 Tauri Contributors. CC-BY / MIT
