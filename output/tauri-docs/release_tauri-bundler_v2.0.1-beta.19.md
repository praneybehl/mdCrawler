Skip to content
# tauri-bundler@2.0.1-beta.19
ReturnView on GitHub
### Bug Fixes
  * `d1df6be70` (#10270 by @Legend-Master) Fix bundler warns about no updater-enabled targets were built for self contained updaters like app image, nsis, msi


### What’s Changed
  * `9f0a5fcea` (#10271 by @Legend-Master) Make `NSIS_HOOK_PREINSTALL` and `NSIS_HOOK_PREUNINSTALL` run before `CheckIfAppIsRunning` (which checks if the app is running and asks the user if they want to kill the app)


© 2025 Tauri Contributors. CC-BY / MIT
