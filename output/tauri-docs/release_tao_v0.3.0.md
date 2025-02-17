Skip to content
# tao@0.3.0
ReturnView on GitHub
  * Drop the event callback before exiting on macOS. 
    * 52ebebbc Drop the event callback before exiting (#86) on 2021-06-18
  * Add `clipboard` api exposing `read_text` and `write_text`. 
    * cf22c902 feat: clipboard api (#85) on 2021-06-21
  * Fix LoopDestroyed to really exit the application. 
    * 55e52a91 Fix LoopDestroy condition to really exit the app on 2021-06-01
  * Implement all control flow variants 
    * 16e2ac06 Add change file on 2021-05-19
  * Add checks before focusing window 
    * 1bd3b1c0 Add change file on 2021-05-22
  * Add `is_visible` getter on `Window`
    * c402a38b feat: Add `is_visible` getter to `Window` (#61) on 2021-05-27
  * **Breaking change** : New keyboard API, including `Accelerator` and `GlobalShortcut`.


`WindowEvent::ModifiersChanged` is emitted when a new keyboard modifier is pressed. This is your responsibility to keep a local state. When the modifier is released, `ModifiersState::empty()` is emitted.
`WindowEvent::KeyboardInput` as been refactored and is exposing the event `KeyEvent`.
All menus (`ContextMenu` and `MenuBar`), now includes `Accelerator` support on Windows, macOS and Linux.
New modules available: `keyboard`, `accelerator` and `platform::global_shortcut`.
_Please refer to the docs and examples for more details._
  * 01fc43b0 refactor: keyboards events (#82) on 2021-06-21
  * **Breaking change** : New menu/tray API.


System tray now expose `set_icon()` to update the tray icon after initialization. The `system_tray::SystemTrayBuilder` has been moved to the root of the package as a module and available on Windows, Linux and macOS, only when the `tray` feature is enabled. Windows expose a `remove()` function available with `SystemTrayExtWindows`.
Menu builder has been rebuilt from scratch, exposing 2 different types, `ContextMenu` and `MenuBar`.
Please refer to the docs and examples for more details.
  * 7546dbd1 refactor: menu & tray (#77) on 2021-06-03
  * Fix match branch of run loop observer on iOS. 
    * 4e9fede6 Add change file on 2021-05-23
  *     * `skip_taskbar` is renamed to `set_skip_taskbar`.
  * `set_skip_taskbar` is now available on `Window` and is no longer behind a PlatformExt.
  * `set_skip_taskbar` takes a boolean to either show or hide the window icon from the taskbar.
  * Add `with_skip_taskbar` to `WindowBuilder`.
  * c0aac091 add `with_skip_taskbar` on 2021-05-29
  * Add `skip_taskbar` implementation for windows 
    * 83341701 feat: add `skip_taskabr` impl for windows (#78) on 2021-05-29


© 2025 Tauri Contributors. CC-BY / MIT
