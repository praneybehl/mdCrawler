Skip to content
# tauri-cli@1.0.0-beta-rc.0
ReturnView on GitHub
  * You can now run `cargo tauri build -t none` to speed up the build if you don’t need executables. 
    * 4d507f9 feat(cli/core): add support for building without targets (#1203) on 2021-02-10
    * aea6145 refactor(repo): add /tooling folder (#1457) on 2021-04-12
  * The `dev` and `build` pipeline is now written in Rust. 
    * 3e8abe3 feat(cli) rewrite the core CLI in Rust (#851) on 2021-01-30
    * aea6145 refactor(repo): add /tooling folder (#1457) on 2021-04-12
  * Run `beforeDevCommand` and `beforeBuildCommand` in a shell. 
    * 32eb0d5 feat(cli): run beforeDev and beforeBuild in a shell, closes #1295 (#1399) on 2021-03-28
    * aea6145 refactor(repo): add /tooling folder (#1457) on 2021-04-12
  * Fixes `&lt;a target=&quot;_blank&quot;&gt;` polyfill. 
    * 4ee044a fix(cli): use correct arg in `_blanks` links polyfill (#1362) on 2021-03-17
    * aea6145 refactor(repo): add /tooling folder (#1457) on 2021-04-12
  * Update all code files to have our license header. 
    * bf82136 feat(license): SPDX Headers (#1449) on 2021-04-11
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
    * aea6145 refactor(repo): add /tooling folder (#1457) on 2021-04-12
  * Adds `productName` and `version` configs on `tauri.conf.json &gt; package`. 
    * 5b3d9b2 feat(config): allow setting product name and version on tauri.conf.json (#1358) on 2021-03-22
    * aea6145 refactor(repo): add /tooling folder (#1457) on 2021-04-12
  * The `info` command was rewritten in Rust. 
    * c3e06ee refactor(cli): rewrite info in Rust (#1389) on 2021-03-25
    * aea6145 refactor(repo): add /tooling folder (#1457) on 2021-04-12
  * The `init` command was rewritten in Rust. 
    * f72b93b refactor(cli): rewrite init command in Rust (#1382) on 2021-03-24
    * aea6145 refactor(repo): add /tooling folder (#1457) on 2021-04-12
  * All the arguments passed after `tauri dev --` are now propagated to the binary. 
    * 4e9d31c feat(cli): propagate args passed after `dev --`, closes #1406 (#1407) on 2021-03-30
    * aea6145 refactor(repo): add /tooling folder (#1457) on 2021-04-12
  * Alpha version of tauri-updater. Please refer to the `README` for more details. 
    * 6d70c8e feat(updater): Alpha version (#643) on 2021-04-05
    * a6def70 Refactor(tauri): move tauri-api and tauri-updater to tauri (#1455) on 2021-04-11
    * aea6145 refactor(repo): add /tooling folder (#1457) on 2021-04-12


© 2025 Tauri Contributors. CC-BY / MIT
