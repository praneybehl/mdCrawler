Skip to content
# tao@0.24.1
ReturnView on GitHub
  * `25a8836b`(#860) Fix the app crash on restart due to Android context was not released. Release the Android context when the app is destroyed to avoid assertion failure.
  * `5eb2124e`(#852) Enable macOS secure state restoration on OS versions that support it. This avoids ‘WARNING: Secure coding is not enabled for restorable state!’ on macOS Sonoma.
  * `f0bf850f`(#859) Derive `Debug, Copy, Clone, PartialEq, Eq, Hash` for `ResizeDirection`.
  * `29b01bff`(#849) On Windows, remove `SetWindowTheme` call with `DarkMode_Explorer` theme which fixes a glitch downstream in `muda` crate when manually drawing the menu bar.
  * `60bbcac1`(#858) On Windows, fix when the `Show window contents while dragging` setting is turned off in Windows, there is a window size issue when dragging between multi-monitors with different scaling.
  * `68803e67`(#854) On Windows, fix consecutive calls to `window.set_fullscreen(Some(Fullscreen::Borderless(None)))` resulting in losing previous window state when eventually exiting fullscreen using `window.set_fullscreen(None)`.


© 2025 Tauri Contributors. CC-BY / MIT
