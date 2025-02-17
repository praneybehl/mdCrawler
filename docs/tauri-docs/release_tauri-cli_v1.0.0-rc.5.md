Skip to content
# tauri-cli@1.0.0-rc.5
ReturnView on GitHub
  * Allow passing arguments to the `build` runner (`tauri build -- &lt;ARGS&gt;...`). 
    * 679fe1fe feat(cli.rs): allow passing arguments to the build runner, closes #3398 (#3431) on 2022-02-13
  * Improve error message when the dev runner command fails. 
    * 759d1afb feat(cli): improve error message when dev runner command fails (#3447) on 2022-02-13
  * Increase `tauri.conf.json` directory lookup depth to `3` and allow changing it with the `TAURI_PATH_DEPTH` environment variable. 
    * c6031c70 feat(cli): increase lookup depth, add env var option (#3451) on 2022-02-13
  * Added `tauri-build`, `tao` and `wry` version to the `info` command output. 
    * 16f1173f feat(cli): add tao and wry version to the `info` output (#3443) on 2022-02-13
  * **Breaking change:** The extra arguments passed to `tauri dev` using `-- &lt;ARGS&gt;...` are now propagated to the runner (defaults to cargo). To pass arguments to your binary using Cargo, you now need to run `tauri dev -- -- &lt;ARGS-TO-YOUR-BINARY&gt;...` (notice the double `--`). 
    * 679fe1fe feat(cli.rs): allow passing arguments to the build runner, closes #3398 (#3431) on 2022-02-13
  * Change the `init` template configuration to disable CSP for better usability for new users. 
    * 102a5e9b refactor(cli.rs): change template config CSP to null, closes #3427 (#3429) on 2022-02-13


© 2025 Tauri Contributors. CC-BY / MIT
