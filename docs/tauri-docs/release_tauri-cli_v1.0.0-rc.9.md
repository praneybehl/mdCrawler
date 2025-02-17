Skip to content
# tauri-cli@1.0.0-rc.9
ReturnView on GitHub
  * Exit CLI when Cargo returns a non-compilation error in `tauri dev`. 
    * b5622882 fix(cli): exit on non-compilation Cargo errors, closes #3930 (#3942) on 2022-04-22
  * Notify CLI update when running `tauri dev`. 
    * a649aad7 feat(cli): check and notify about updates on `tauri dev`, closes #3789 (#3960) on 2022-04-25
  * The CLI will not automatically run `strip` on release binaries anymore. Use the [`strip`][strip] profile setting stabilized with Cargo 1.59.


  * 62106224 refactor: drop strip from build command. closes #3559 (#3863) on 2022-04-06
  * Kill the `beforeDevCommand` and app processes if the dev command returns an error. 
    * 485c9743 fix(cli): kill beforeDevCommand if dev code returns an error (#3907) on 2022-04-19
  * Fix `info` command showing outdated text for latest versions. 
    * 73a4b74a fix(cli.rs/info): don’t show outdated text for latest versions (#3829) on 2022-04-02
  * **Breaking change:** Enable default Cargo features except `tauri/custom-protocol` on the dev command. 
    * f2a30d8b refactor(core): use ayatana appindicator by default, keep option to use gtk (#3916) on 2022-04-19
  * Kill the `beforeDevCommand` process recursively on Unix. 
    * e251e1b0 fix(cli): kill before dev command recursively on Unix, closes #2794 (#3848) on 2022-04-03


© 2025 Tauri Contributors. CC-BY / MIT
