Skip to content
# tauri-cli@1.0.1
ReturnView on GitHub
  * No longer adds the `pkg-config` dependency to `.deb` packages when the `systemTray` is used. This only works with recent versions of `libappindicator-sys` (including https://github.com/tauri-apps/libappindicator-rs/pull/38), so a `cargo update` may be necessary if you create `.deb` bundles and use the tray feature. 
    * 0e6edeb1 fix(cli): Don’t add `pkg-config` to `deb` (#4508) on 2022-06-29
  * AppImage bundling will now prefer bundling correctly named appindicator library (including `.1` version suffix). With a symlink for compatibility with the old naming. 
    * bf45ca1d fix(cli,bundler): prefer AppImage libraries with ABI version (#4505) on 2022-06-29
  * Improve error message when `cargo` is not installed. 
    * e0e5f772 feat(cli): improve `cargo not found` error message, closes #4428 (#4430) on 2022-06-21
  * The app template now only sets the default menu on macOS. 
    * 5105b428 feat(cli): change app template to only set default menu on macOS (#4518) on 2022-06-29
  * Warn if updater is enabled but not in the bundle target list. 
    * 31c15cd2 docs(config): enhance documentation for bundle targets, closes #3251 (#4418) on 2022-06-21
  * Check if target exists and is installed on dev and build commands. 
    * 13b8a240 feat(cli): validate target argument (#4458) on 2022-06-24
  * Fixes the covector configuration on the plugin templates. 
    * b8a64d01 fix(cli): add prepublish scripts to the plugin templates on 2022-06-19
  * Set the binary name to the product name in development. 
    * b025b9f5 refactor(cli): set binary name on dev (#4447) on 2022-06-23
  * Allow registering a `.gitignore` file to skip watching some project files and directories via the `TAURI_DEV_WATCHER_IGNORE_FILE` environment variable. 
    * 83186dd8 Read extra ignore file for dev watcher, closes #4406 (#4409) on 2022-06-20
  * Fix shebang for `kill-children.sh`. 
    * 35dd51db fix(cli): add shebang for kill-children.sh, closes #4262 (#4416) on 2022-06-22
  * Update plugin templates to use newer `tauri-apps/create-pull-request` GitHub action. 
    * 07f90795 chore(cli): update plugin template tauri-apps/create-pull-request on 2022-06-19
  * Use UNIX path separator on the init `$schema` field. 
    * 01053045 chore(cli): use unix path separator on $schema (#4384) on 2022-06-19
  * The `info` command now can check the Cargo lockfile on workspaces. 
    * 12f65219 fix(cli): read lockfile from workspace on the info command, closes #4232 (#4423) on 2022-06-21
  * Preserve the `Cargo.toml` formatting when the features array is not changed. 
    * 6650e5d6 fix(cli): preserve Cargo manifest formatting when possible (#4431) on 2022-06-21
  * Change the updater signature metadata to include the file name instead of its full path. 
    * 094b3eb3 fix(cli): file name instead of path on updater sig comment, closes #4467 (#4484) on 2022-06-27
  * Validate bundle identifier as it must only contain alphanumeric characters, hyphens and periods. 
    * 0674a801 fix: assert config.bundle.identifier to be only alphanumeric, hyphens or dots. closes #4359 (#4363) on 2022-06-17


© 2025 Tauri Contributors. CC-BY / MIT
