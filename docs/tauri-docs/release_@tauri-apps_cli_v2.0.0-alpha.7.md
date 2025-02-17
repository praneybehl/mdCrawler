Skip to content
# @tauri-apps/cli@2.0.0-alpha.7
ReturnView on GitHub
  * Add `--release` flag for `tauri android dev` however you will need to sign your Android app, see https://next—tauri.netlify.app/next/guides/distribution/sign-android
    * 63f088e5 feat(cli): add `--release` for `android dev` (#6638) on 2023-04-05
  * Build only specified rust targets for `tauri android build` instead of all. 
    * d03e47d1 fix: only build specified rust targets for aab/apk build (#6625) on 2023-04-05
  * Use local ip address for built-in dev server on mobile. 
    * 7fec0f08 fix(cli): use local ip addr for built-in server on mobile, closes #6454 (#6631) on 2023-04-04
  * Readd the Cargo.toml file to the plugin template. 
    * 5288a386 fix(cli): readd Cargo.toml to the plugin template (#6637) on 2023-04-04


© 2025 Tauri Contributors. CC-BY / MIT
