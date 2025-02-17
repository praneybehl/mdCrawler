Skip to content
# @tauri-apps/cli@1.0.0-rc.10
ReturnView on GitHub
  * Resolve binary file extension from target triple instead of compile-time checks to allow cross compilation. 
    * 4562e671 fix(build): append .exe binary based on target triple instead of running OS, closes #3870 (#4032) on 2022-05-03
  * Fixes text overflow on `tauri dev` on Windows. 
    * 094534d1 fix(cli): dev command stderr text overflow on Windows, closes #3995 (#4000) on 2022-04-29
  * Improve CLI’s logging output, making use of the standard rust `log` system. 
    * 35f21471 feat(cli): Improve CLI logging (#4060) on 2022-05-07
  * Don’t override the default keychain on macOS while code signing. 
    * a4fcaf1d fix: don’t override default keychain, closes #4008 (#4053) on 2022-05-05
  *     * Remove startup delay in `tauri dev` caused by checking for a newer cli version. The check is now done upon process exit.
  * Add `TAURI_SKIP_UPDATE_CHECK` env variable to skip checking for a newer CLI version.
  * bbabc8cd fix(cli.rs): remove startup delay in `tauri dev` (#3999) on 2022-04-29
  * Fix `tauri info` panic when a package isn’t installed. 
    * 4f0f3187 fix(cli.rs): fix `tauri info` panic when a package isn’t installed, closes #3985 (#3996) on 2022-04-29
  * Added `$schema` support to `tauri.conf.json`. 
    * 715cbde3 feat(config): add `$schema` to `tauri.conf.json`, closes #3464 (#4031) on 2022-05-03
  * **Breaking change:** The `dev` command now reads the custom config file from CWD instead of the Tauri folder. 
    * a1929c6d fix(cli): always read custom config file from CWD, closes #4067 (#4074) on 2022-05-07
  * Fixes a Powershell crash when sending SIGINT to the dev command. 
    * 32048486 fix(cli): powershell crashing on SIGINT, closes #3997 (#4007) on 2022-04-29
  * Prevent building when the bundle identifier is the default `com.tauri.dev`. 
    * 95726ebb feat(cli): prevent default bundle identifier from building, closes #4041 (#4042) on 2022-05-04


© 2025 Tauri Contributors. CC-BY / MIT
