Skip to content
# tauri@2.0.0-alpha.17
ReturnView on GitHub
### Enhancements
  * `b89de9fa`(#8092) Add support for onResume and onPause events in android plugins.
  * `c6c59cf2` Pull changes from Tauri 1.5 release.
  * `198abe3c`(#8076) Mobile plugins can now resolve using an arbitrary object instead of using the `JSObject` class via `Invoke.resolve` on iOS and `Invoke.resolveObject` on Android.


### Bug Fixes
  * `22f26882`(#8049) Prevent crash on iOS when the Swift plugin data is not a valid JSON string.


### Dependencies
  * Upgraded to `tauri-build@2.0.0-alpha.11`
  * Upgraded to `tauri-macros@2.0.0-alpha.10`
  * Upgraded to `tauri-utils@2.0.0-alpha.10`
  * Upgraded to `tauri-runtime@1.0.0-alpha.4`
  * Upgraded to `tauri-runtime-wry@1.0.0-alpha.5`
  * `9580df1d`(#8084) Upgrade `gtk` to 0.18.
  * `c7c2507d`(#8035) Update `windows` to version `0.51` and `webview2-com` to version `0.27`
  * `9580df1d`(#8084) Updated to wry@0.34, removing the `dox` feature flag.


### Breaking Changes
  * `198abe3c`(#8076) The Android `PluginManager.loadConfig` now takes a third parameter to define the class type of the config object.
  * `198abe3c`(#8076) Mobile plugins now have access to a parser for the invoke arguments instead of relying on the `Invoke#get$\{TYPE}` methods.
  * `74d2464d`(#8116) Added `WindowBuilder::on_page_load` and refactored the `Builder::on_page_load` handler to take references. The page load hook is now triggered for load started and finished events, to determine what triggered it see `PageLoadPayload::event`.
  * `93c8a77b`(#7996) The event system APIS on Rust is recieving a few changes for consistency and quality of life improvements:
    * Renamed `Manager::emit_all` to just `Manager::emit` and will now both trigger the events on JS side as well as Rust.
    * Removed `Manager::trigger_global`, use `Manager::emit`
    * Added `Manager::emit_filter`.
    * Removed `Window::emit`, and moved the implementation to `Manager::emit`.
    * Removed `Window::emit_and_trigger` and `Window::trigger`, use `Window::emit` instead.
    * Changed `Window::emit_to` to only trigger the target window listeners so it won’t be catched by `Manager::listen_global`


© 2025 Tauri Contributors. CC-BY / MIT
