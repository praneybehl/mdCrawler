Skip to content
# tao@0.8.0
ReturnView on GitHub
  * Add `EventLoopWindowTargetExtMacOS::set_activation_policy_at_runtime`. 
    * ef06c508 Set activation policy at runtime (#353) on 2022-03-30
  * On Windows and Linux, disable resizing maximized borderless windows. 
    * 13c5c996 fix(win,linux): disable resizing maximized borderless windows (#356) on 2022-03-30
  * **Breaking change:** Renamed the `ayatana` Cargo feature to `ayatana-tray`, now the default feature for tray on Linux, and added the `gtk-tray` feature. 
    * 40ec796d refactor(tray): split gtk and ayatana appindicator features (#362) on 2022-04-05
  *     * On Windows, Fix random characters when changing menu items title through `CustomMenunItem::set_title`.
    * e4725bf5 fix(Windows): fix random chars when changing menu item title (#361) on 2022-03-31
  * On Windows, Fix `Window::set_inner_size` setting a bigger size than requested. 
    * 089f3878 fix(Windows): fix `set_inner_size` setting a bigger size, closes #194 (#354) on 2022-04-03


© 2025 Tauri Contributors. CC-BY / MIT
