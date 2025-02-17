Skip to content
# tauri@1.0.3
ReturnView on GitHub
  * `tauri::Builder` will now include a default menu for macOS without explicitly using `Menu::os_default`, you can still override it through `tauri::Builder::menu` or remove it using `tauri::Builder::enable_macos_default_menu(false)`. 
    * 91055883 feat: add implicit default menu for macOS only, closes #4551 (#4570) on 2022-07-04
  * Use `toString()` on message/confirm/ask dialogs title and message values. 
    * b8cd2a79 feat(api): call `toString()` on dialog title and message, closes #4583 (#4588) on 2022-07-04
  * Fix stack overflow on Windows on commands by changing the implementation of the `async_runtime::spawn` method. 
    * 7e3ac847 fix(core): command stack overflow on Windows, closes #4548 (#4562) on 2022-07-03
  * Emits RunEvent::Exit prior to killing child processes managed by Tauri, allowing graceful shutdown of sidecar binaries. 
    * 34879f73 fix: allow graceful shutdown of sidecar commands on exit (#4561) on 2022-07-03
  * Added option to disable tray menu on left click on macOS. 
    * f8a3becb feat(core): add option to disable tray menu on left click, closes #4584 (#4587) on 2022-07-05
  * Only run the updater default dialog mode in supported platforms or development mode. 
    * e29fff25 fix(updater): do not run in dialog mode on .deb, closes #4573 (#4577) on 2022-07-05
  * Configure the updater to relaunch after installing the update on Windows. 
    * 0fa74534 feat(updater): relaunch on Windows, closes #4220 (#4568) on 2022-07-03


© 2025 Tauri Contributors. CC-BY / MIT
