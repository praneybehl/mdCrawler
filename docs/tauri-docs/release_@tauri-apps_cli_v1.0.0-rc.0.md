Skip to content
# @tauri-apps/cli@1.0.0-rc.0
ReturnView on GitHub
  * Do not force Tauri application code on `src-tauri` folder and use a glob pattern to look for a subfolder with a `tauri.conf.json` file. 
    * a8cff6b3 feat(cli): do not enforce `src-tauri` folder structure, closes #2643 (#2654) on 2021-09-27
  * Added CommonJS output to the `dist` folder. 
    * 205b0dc8 feat(cli.js): add CommonJS dist files (#2646) on 2021-09-23
  * Fixes `.ico` icon generation. 
    * 11db96e4 fix(cli.js): `.ico` icon generation, closes #2692 (#2694) on 2021-10-02
  * Automatically unplug `@tauri-apps/cli` in yarn 2+ installations to fix the download of the rust-cli. 
    * 1e336b68 fix(cli.js): Fix package installation on yarn 2+ (#3012) on 2021-12-09
  * Read `package.json` and check for a `tauri` object containing the `appPath` string, which points to the tauri crate path. 
    * fb2b9a52 feat(cli.js): allow configuring tauri app path on package.json #2752 (#3035) on 2021-12-09
  * Removed the `icon` command, now exposed as a separate package, see https://github.com/tauri-apps/tauricon. 
    * 58030172 feat(tauricon): remove from cli (#3293) on 2022-02-07


© 2025 Tauri Contributors. CC-BY / MIT
