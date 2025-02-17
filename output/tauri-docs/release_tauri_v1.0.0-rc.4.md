Skip to content
# tauri@1.0.0-rc.4
ReturnView on GitHub
  * Run `AppHandle` cleanup code before restarting the application on the `process &gt; relaunch` API. 
    * 9c65abce feat(core): run cleanup code on the relaunch API (#3629) on 2022-03-07
  * **Breaking change:** The `Builder#create_window` API now returns a Result validating the window label. 
    * 64e00542 refactor(core): do not panic on invalid window labels,#3544 (#3596) on 2022-03-03
  * Added `tsp` config option under `tauri &gt; bundle &gt; windows`, which enables Time-Stamp Protocol (RFC 3161) for the timestamping server under code signing on Windows if set to `true`. 
    * bdd5f7c2 fix: add support for Time-Stamping Protocol for Windows codesigning (fix #3563) (#3570) on 2022-03-07
  * Revert the `clap` usage back to the version 3.0 API. 
    * 2b554c38 fix(core): revert to clap 3.0 API, allow deprecations, closes #3549 (#3552) on 2022-02-24
  * The `tauri::api::process::Command` API now properly reads stdout and stderr messages that ends with a carriage return (`\r`) instead of just a newline (`\n`). 
    * 0a0de8ab fix: read Command output ending with a carriage return, closes #3508 (#3523) on 2022-02-24
  * Fixes filesystem and asset scope stripping the first component of the allowed path. 
    * 4d0e2ecc fix(core): scope should not strip the first path component, closes #3592 (#3602) on 2022-03-03
  * Ignore trailing slashes on path scope validation. 
    * 929a83dd fix(core): ignore trailing slashes on scope validation, closes #3580 (#3601) on 2022-03-03
  * Fixes `Command::output` and `Command::status` deadlock when running on async commands. 
    * 0163489e fix(core): `safe_block_on` usage on async contexts, closes #3505 (#3513) on 2022-02-24
  * Update tray menu id map when `SystemTrayHandle::set_menu` is called. 
    * da882431 fix(core): update tray menu ids on `set_menu`, closes #3608 (#3611) on 2022-03-04
  * Allow absolute paths on the filesystem APIs as long as it does not include parent directory components. 
    * b744cd27 feat: extend scopes with user selected paths, closes #3591 (#3595) on 2022-03-03
  * **Breaking change:** The `tauri::api::file::Extract` API is now available when the `fs-extract-api` feature is enabled. 
    * 0f155898 fix(core): docs.rs on Windows and macOS (#3566) on 2022-03-02
  * Allow listening to events on the filesystem and asset scopes. 
    * 58070c1e feat(core): filesystem and asset protocol scope events (#3609) on 2022-03-04
  * Allow configuring forbidden paths on the asset and filesystem scopes. 
    * 983ccb81 feat(core): allow denying paths on the fs and asset scopes (#3607) on 2022-03-03
  * Extend the allowed patterns for the filesystem and asset protocol when the user selects a path (dialog open and save commands and file drop on the window). 
    * b744cd27 feat: extend scopes with user selected paths, closes #3591 (#3595) on 2022-03-03
  * The HTTP scope now matches the entire URL using a glob pattern instead of only its path. 
    * 944b124c feat(core): enhance HTTP scope glob validation, closes #3507 (#3515) on 2022-02-24
  * Parse window icons at compile time. 
    * 8c935872 refactor(core): move `png` and `ico` behind Cargo features (#3588) on 2022-03-05
  * **Breaking change:** Move `ico` and `png` parsing behind `icon-ico` and `icon-png` Cargo features. 
    * 8c935872 refactor(core): move `png` and `ico` behind Cargo features (#3588) on 2022-03-05
  * Return an error when creating a window with an invalid label instead of panicking. 
    * 64e00542 refactor(core): do not panic on invalid window labels,#3544 (#3596) on 2022-03-03
  * Allows the configuration CSP to be an object mapping a directive name to its source list. 
    * 3fe0260f feat(core): allow CSP configuration to be an object, ref #3533 (#3603) on 2022-03-04
  * Allow range in the form of `bytes=0-*` on the asset protocol. 
    * d06efc77 fix(core): parse range `bytes=0-*`, closes #3143 (#3516) on 2022-02-24
  * Reimplement endpoint to read file as string for performance. 
    * 834ccc51 feat(core): reimplement `readTextFile` for performance (#3631) on 2022-03-07
  * **Breaking change:** Renamed the `command` Cargo feature to `process-command-api`. 
    * 4e1af005 refactor(core): rename `command` feature to `process-command-api` (#3594) on 2022-03-03
  * Disabled the default features for the `zip` crate. 
    * 5293445f refactor(core): disable default features for the zip crate (#3624) on 2022-03-06
  * The `cmd` field is no longer required on the shell scope for sidecars. 
    * 9b3b163b feat(core): simplify scope definition for sidecars (#3574) on 2022-03-02
  * Fixes a regression on the `unlisten` command. 
    * 76c791bd fix(core): regression on the unlisten function (#3623) on 2022-03-06
  * Run `AppHandle` cleanup code before restarting the application when a new update is installed. 
    * fce7d3bb feat(core): run app cleanup code before updater restart, closes #3605 (#3616) on 2022-03-04
  * Added a `WindowBuilder` type. 
    * 141133a4 feat(core): add WindowBuilder type (#3598) on 2022-03-04
  * Added `WindowBuilder::on_web_resource_request`, which allows customizing the tauri custom protocol response. 
    * 3b13fda5 feat(core): add `WindowBuilder::on_request`, closes #3533 (#3618) on 2022-03-06


© 2025 Tauri Contributors. CC-BY / MIT
