Skip to content
# tauri-cli@1.0.0-rc.0
ReturnView on GitHub
  * Do not force Tauri application code on `src-tauri` folder and use a glob pattern to look for a subfolder with a `tauri.conf.json` file. 
    * a8cff6b3 feat(cli): do not enforce `src-tauri` folder structure, closes #2643 (#2654) on 2021-09-27
  * Define `TAURI_PLATFORM`, `TAURI_ARCH`, `TAURI_FAMILY`, `TAURI_PLATFORM_TYPE`, `TAURI_PLATFORM_VERSION` and `TAURI_DEBUG` environment variables for the `beforeDevCommand` and `beforeBuildCommand` scripts. 
    * 8599313a feat(cli.rs): env vars for beforeDev/beforeBuild commands, closes #2610 (#2655) on 2021-09-26
    * b5ee03a1 feat(cli.rs): expose debug flag to beforeDev/beforeBuild commands (#2727) on 2021-10-08
    * 9bb68973 fix(cli.rs): prefix the “before script” env vars with `TAURI_` (#3274) on 2022-01-24
  * Allow `config` arg to be a path to a JSON file on the `dev` and `build` commands. 
    * 7b81e5b8 feat(cli.rs): allow config argument to be a path to a JSON file (#2938) on 2021-11-22
  * Add `rustup` version and active rust toolchain to the `info` command output. 
    * 28aaec87 feat(cli.rs): add active toolchain and rustup to `tauri info`, closes #2730 (#2986) on 2021-12-09
  * Add `Visual Studio Build Tools` installed versions to the `info` command output. 
    * d5f07d14 feat(cli.rs): build tools info (#2618) on 2021-09-21
  * The inferred development server port for Svelte is now `8080` (assumes latest Svelte with `sirv-cli &gt;= 2.0.0`). 
    * de0543f3 feat(cli.rs): change inferred dev server port to 8080 for Svelte apps on 2022-02-05
  * Detect if tauri is used from git in the `info` command. 
    * 65ad5b5e feat(cli.rs/info): detect if tauri is used from git (#3309) on 2022-02-05
  * Drop the `dialoguer` soft fork and use the published version instead. 
    * b1f5c6d7 refactor(cli.rs): drop `dialoguer` and `console` soft fork (#2790) on 2021-10-22
  * Fix `build` command when executed on a 32-bit Windows machine when pulling from the `binary-releases` repo. 
    * 35588b2e fix(cli.rs): check default arch at runtime, closes #3067 (#3078) on 2021-12-27
  * The `generate` and `sign` commands are now available under a `signer` subcommand. 
    * 1458ab3c refactor(cli.rs): `signer` and `plugin` subcommands, use new clap derive syntax (#2928) on 2021-12-09
  * Use `tauri-utils` to get the `Config` types. 
    * 4de285c3 feat(core): validate Cargo features matching allowlist [TRI-023] on 2022-01-09
  * Print warning and exit if `distDir` contains `node_modules`, `src-tauri` or `target` folders. 
    * 7ed3f3b7 feat(cli.rs): validate `distDir`, closes #2554 (#2701) on 2021-10-04
  * Fix `tauri build` failing on Windows if `tauri.conf.json &gt; tauri &gt; bundle &gt; Windows &gt; wix &gt; license` is used. 
    * 17a1ad68 fix(cli.rs): ensure `target/release/wix` exists, closes #2927 (#2987) on 2021-12-07
  * Added `dev_csp` to the `security` configuration object. 
    * cf54dcf9 feat: improve `CSP` security with nonces and hashes, add `devCsp` [TRI-004] (#8) on 2022-01-09
  * Kill process if `beforeDevCommand` exits with a non-zero status code. 
    * a2d5929a feat(cli.rs): wait for dev URL to be reachable, exit if command fails (#3358) on 2022-02-08
  * Fixes output directory detection when using Cargo workspaces. 
    * 8d630bc8 fix(cli.rs): fix workspace detection, fixes #2614, closes #2515 (#2644) on 2021-09-23
  * Allow using a fixed version for the Webview2 runtime via the `tauri &gt; bundle &gt; windows &gt; webviewFixedRuntimePath` config option. 
    * 85df94f2 feat(core): config for fixed webview2 runtime version path (#27) on 2021-11-02
  * Adds support for using JSON5 format for the `tauri.conf.json` file, along with also supporting the `.json5` extension.


Here is the logic flow that determines if JSON or JSON5 will be used to parse the config:
  1. Check if `tauri.conf.json` exists a. Parse it with `serde_json` b. Parse it with `json5` if `serde_json` fails c. Return original `serde_json` error if all above steps failed
  2. Check if `tauri.conf.json5` exists a. Parse it with `json5` b. Return error if all above steps failed
  3. Return error if all above steps failed


  * 995de57a Add seamless support for using JSON5 in the config file (#47) on 2022-02-03
  * Added `$ tauri plugin init` command, which initializes a Tauri plugin. 
    * ac8e69a9 feat(cli.rs): add `init plugin` command, bootstraps a plugin project (#2669) on 2021-09-27
    * db275f0b refactor(cli.rs): rename `init plugin` subcommand to `plugin init` (#2885) on 2021-11-13
  * **Breaking change:** Add `macos-private-api` feature flag, enabled via `tauri.conf.json &gt; tauri &gt; macOSPrivateApi`. 
    * 6ac21b3c feat: add private api feature flag (#7) on 2022-01-09
  * Move the copying of resources and sidecars from `cli.rs` to `tauri-build` so using the Cargo CLI directly processes the files for the application execution in development. 
    * 5eb72c24 refactor: copy resources and sidecars on the Cargo build script (#3357) on 2022-02-08
  * The minimum Rust version is now `1.56`. 
    * a9dfc015 feat: update to edition 2021 and set minimum rust to 1.56 (#2789) on 2021-10-22
  * Automatically `strip` the built binary on Linux and macOS if `--debug` is not specified. 
    * 2f3a582c feat(cli.rs): strip release binaries [TRI-031] (#22) on 2022-01-09
  * Fixes pnpm error when running `pnpm tauri info`. 
    * 2026134f fix(cli.rs): pnpm tauri info exits with error (fix #2509) (#2510) on 2021-08-24
  * Add support to building Universal macOS Binaries through the virtual target `universal-apple-darwin` (run `tauri build --target universal-apple-darwin`). 
    * 83f52fdb feat: Add `universal-darwin-macos` build target, closes #3317 (#3318) on 2022-02-04
  * Wait for `devPath` URL to be reachable before starting the application. Skipped if the `TAURI_SKIP_DEVSERVER_CHECK` environment variable is set to `true`. 
    * a2d5929a feat(cli.rs): wait for dev URL to be reachable, exit if command fails (#3358) on 2022-02-08
  * On Windows, Fix `beforeDevCommand` and `beforeBuildCommand` not executing the expected command if it contains quotes. This is done by executing them with `CMD /S /C {command}` instead of `CMD /C {command}` on Windows. 
    * 52e9a6d8 fix: Make CMD handle quotes `&quot;` properly. (#3334) on 2022-02-06
  * Allow setting the localization file for WiX. 
    * af329f27 feat(bundler): wix localization, closes #3174 (#3179) on 2022-02-05


© 2025 Tauri Contributors. CC-BY / MIT
