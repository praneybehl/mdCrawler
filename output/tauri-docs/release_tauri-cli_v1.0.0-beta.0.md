Skip to content
# tauri-cli@1.0.0-beta.0
ReturnView on GitHub
  * Fixes a cargo `target/` cache issue. 
    * 79feb6a fix(cli.rs): cargo build failed due to cache issue, closes #1543 (#1741) on 2021-05-07
  * Improve error logging. 
    * 5cc4b11 feat(cli.rs): add context to errors (#1674) on 2021-05-01
  * Adds Webview2 version on `info` command. 
    * 2b4e2b7 feat(cli.rs/info): get webview2 version on windows (#1669) on 2021-05-04
  * Adds `--runner [PROGRAM]` argument on the `dev` and `build` command, allowing using the specified program to run and build the application (example program: `cross`). 
    * 5c1fe52 feat(cli.rs): allow using cross instead of cargo, add target triple arg (#1664) on 2021-04-30
  * Adds `--target [TARGET_TRIPLE]` option to the `build` command (example: `--target arm-unknown-linux-gnueabihf`). 
    * 5c1fe52 feat(cli.rs): allow using cross instead of cargo, add target triple arg (#1664) on 2021-04-30
  * Rename `--target` option on the `build` command to `--bundle`. 
    * 5c1fe52 feat(cli.rs): allow using cross instead of cargo, add target triple arg (#1664) on 2021-04-30
  * Automatically add Tauri dependencies to the debian package `Depends` section. 
    * 72b8048 feat(cli.rs): fill debian `depends` with tauri dependencies (#1767) on 2021-05-10
  * Properly kill `beforeDevCommand` process. 
    * ac2cbcb fix(cli.rs): `before dev` process kill, closes #1626 (#1700) on 2021-05-04
  * Adds support to `tauri` dependency as string and table on `Cargo.toml`. 
    * df8bdcf feat(cli.rs): add support to string and table dependency, closes #1653 (#1654) on 2021-04-29
  * Show `framework` and `bundler` on the `info` command by reading the `package.json` file and matching known dependencies. 
    * 152c755 feat(cli.rs): `framework` and `bundler` on info cmd, closes #1681 (#1682) on 2021-05-02


© 2025 Tauri Contributors. CC-BY / MIT
