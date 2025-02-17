Skip to content
# tauri@2.0.0-alpha.4
ReturnView on GitHub
  * Allow a wry plugin to be registered at runtime. 
    * ae296f3d refactor(tauri-runtime-wry): register runtime plugin after run() (#6478) on 2023-03-17
  * Inject `proguard-tauri.pro` file in the Android project. 
    * bef4ef51 feat(android): enable minify on release, add proguard rules (#6257) on 2023-02-13
  * Return `bool` in the invoke handler. 
    * 05dad087 feat: initial work for iOS plugins (#6205) on 2023-02-11
  * Use correct lib name in xcode project. 
    * d1752fb1 fix(cli): use correct lib name in xcode project (#6387) on 2023-03-08
  * Run Android and iOS native plugins on the invoke handler if a Rust plugin command is not found. 
    * 05dad087 feat: initial work for iOS plugins (#6205) on 2023-02-11
  * Added `initialize_android_plugin` and `initialize_ios_plugin` APIs on `AppHandle`. 
    * 05dad087 feat: initial work for iOS plugins (#6205) on 2023-02-11
  * Changed the plugin setup hook to take a second argument of type `PluginApi`. 
    * 6aaba834 refactor(plugin): add PluginApi and PluginHandle, expose on setup hook (#6291) on 2023-02-16
  * Refactored the implementation of the `mobile_entry_point` macro. 
    * 9feab904 feat(core): add API to call Android plugin (#6239) on 2023-02-10
  * Removed the attohttpc client. The `reqwest-*` Cargo features were also removed. 
    * dddaa943 refactor(core): remove attohttpc client, closes #6415 (#6468) on 2023-03-17
  * Added `App::run_mobile_plugin` and `AppHandle::run_mobile_plugin`. 
    * bfb2ab24 feat: add API to call iOS plugin (#6242) on 2023-02-11
  * Added the `shadow` option when creating a window and `Window::set_shadow`. 
    * a81750d7 feat(core): add shadow APIs (#6206) on 2023-02-08
  * Implemented `with_webview` on Android and iOS. 
    * 05dad087 feat: initial work for iOS plugins (#6205) on 2023-02-11


© 2025 Tauri Contributors. CC-BY / MIT
