Skip to content
# tauri@1.0.0-beta.5
ReturnView on GitHub
  * Allow preventing window close when the user requests it. 
    * 8157a68a feat(core): allow listening to event loop events & prevent window close (#2131) on 2021-07-06
  * Add `App#run` method with callback argument (event loop event handler). 
    * 8157a68a feat(core): allow listening to event loop events & prevent window close (#2131) on 2021-07-06
  * Fixes `data-tauri-drag-region` not firing its events. 
    * 578610a2 fix(core): fix drag-region not sending its events correctly (#2196) on 2021-07-12
  * Fix macOS `EXC_BAD_ACCESS` panic when app is code-signed. 
    * 456a94f6 fix(macOS): updater `EXC_BAD_ACCESS` (#2181) on 2021-07-12
  * Fixes SVG loading on custom protocol. 
    * e663bdd5 fix(core): svg mime type (#2129) on 2021-06-30
  * Expose `gtk_window` getter. 
    * e0a8e09c feat(core): expose `gtk_window`, closes #2083 (#2141) on 2021-07-02
  * Inject invoke key on `script` tags with `type=&quot;module&quot;`. 
    * f03eea9c feat(core): inject invoke key on `&lt;script type=&quot;module&quot;&gt;` (#2120) on 2021-06-29
  * Fix macOS high CPU usage. 
    * a280ee90 Fix high cpu usage on mac, fix #2074 (#2125) on 2021-06-30
  * Export `MenuHandle` and `MenuEvent` types on `tauri::window`. 
    * acb88929 fix(core): export `MenuHandle` and `MenuEvent` (#2148) on 2021-07-03
  * Use glib context for linux updater to prevent GTK panic. 
    * 3389bd81 fix(linux): use glib main context for the updater on linux (#2222) on 2021-07-16
  * Bump `wry` 0.11 and fix focus integration to make it compatible with tao 0.4. 
    * f0a8db62 core(deps): bump `wry` to `0.11` (#2210) on 2021-07-15
  * `Params` has been removed, along with all the associated types on it. Functions that previously accepted those associated types now accept strings instead. Type that used a generic parameter `Params` now use `Runtime` instead. If you use the `wry` feature, then types with a `Runtime` generic parameter should default to `Wry`, letting you omit the explicit type and let the compiler infer it instead.


`tauri`:
  * See `Params` note
  * If you were using `Params` inside a function parameter or definition, all references to it have been replaced with a simple runtime that defaults to `Wry`. If you are not using a custom runtime, just remove `Params` from the definition of functions/items that previously took it. If you are using a custom runtime, you _may_ need to pass the runtime type to these functions.
  * If you were using custom types for `Params` (uncommon and if you don’t understand you probably were not using it), all methods that were previously taking the custom type now takes an `Into&lt;String&gt;` or a `&amp;str`. The types were already required to be string-able, so just make sure to convert it into a string before passing it in if this breaking change affects you.


`tauri-macros`:
  * (internal) Added private `default_runtime` proc macro to allow us to give item definitions a custom runtime only when the specified feature is enabled.


`tauri-runtime`:
  * See `Params` note
  * Removed `Params`, `MenuId`, `Tag`, `TagRef`.
  * Added `menu::{MenuHash, MenuId, MenuIdRef}` as type aliases for the internal type that menu types now use. 
    * All previous menu items that had a `MenuId` generic now use the underlying `MenuId` type without a generic.
  * `Runtime`, `RuntimeHandle`, and `Dispatch` have no more generic parameter on `create_window(...)` and instead use the `Runtime` type directly
  * `Runtime::system_tray` has no more `MenuId` generic and uses the string based `SystemTray` type directly.
  * (internal) `CustomMenuItem::id_value()` is now hashed on creation and exposed as the `id` field with type `MenuHash`.


`tauri-runtime-wry`:
  * See `Params` note
  * update menu and runtime related types to the ones changed in `tauri-runtime`.


`tauri-utils`:
  * `Assets::get` signature has changed to take a `&amp;AssetKey` instead of `impl Into&lt;AssetKey&gt;` to become trait object safe.
  * fd8fab50 refactor(core): remove `Params` and replace with strings (#2191) on 2021-07-15


© 2025 Tauri Contributors. CC-BY / MIT
