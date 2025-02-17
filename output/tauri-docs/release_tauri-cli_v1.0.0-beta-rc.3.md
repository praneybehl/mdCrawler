Skip to content
# tauri-cli@1.0.0-beta-rc.3
ReturnView on GitHub
  * Check if distDir assets are built after running `beforeDevCommand`. 
    * a670d3a fix(cli.rs): check if distDir exists after running `beforeDevCommand` (#1586) on 2021-04-22
  * Fixes `tauri info` display version for the `@tauri-apps/api` package. 
    * 0012782 fix(cli.rs): `info` command `npm_package_version` parsing `beta-rc` (#1587) on 2021-04-22
  * Fixes crash on usage of modifier keys on Windows when running `tauri init`. 
    * d623d95 fix(cli.rs): inliner dialoguer & console until they publish, fixes #1492 (#1610) on 2021-04-25
  * Enable `tauri` `updater` feature when `tauri.conf.json &gt; tauri &gt; updater &gt; active` is set to `true`. 
    * 9490b25 fix(cli.rs): enable the `updater` feature on cli (#1597) on 2021-04-23


© 2025 Tauri Contributors. CC-BY / MIT
