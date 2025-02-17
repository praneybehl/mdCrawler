Skip to content
# tauri-cli@2.0.0-alpha.2
ReturnView on GitHub
  * Fixes `TAURI_*` environment variables for hook scripts on mobile commands. 
    * 1af9be90 feat(cli): properly fill target for TAURI_ env vars on mobile (#6116) on 2023-01-23
  * Force colored logs on mobile commands. 
    * 2c4a0bbd feat(cli): force colored logs on mobile commands (#5934) on 2022-12-28
  * Keep the process alive even when the iOS application is closed. 
    * dee9460f feat: keep CLI alive when iOS app exits, show logs, closes #5855 (#5902) on 2022-12-27
  * Show all application logs on iOS. 
    * dee9460f feat: keep CLI alive when iOS app exits, show logs, closes #5855 (#5902) on 2022-12-27
  * Print log output for all tags on Android development. 
    * 8cc11149 fix(cli): print Android logs for all tags on 2023-01-17
  * Add support to custom and kebab case library names for mobile apps. 
    * 50f6dd87 feat: improvements to support hyphens in crate name (#5989) on 2023-01-06
  * Bump the MSRV to 1.64. 
    * 7eb9aa75 Update gtk to 0.16 (#6155) on 2023-01-30
  * Fix target directory detection when compiling for Android. 
    * e873bae0 fix(cli): Cargo target dir detection on Android, closes #5865 (#5932) on 2022-12-28


© 2025 Tauri Contributors. CC-BY / MIT
