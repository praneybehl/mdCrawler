Skip to content
# tao@0.29.0
ReturnView on GitHub
  * `e67cf1b2` (#941 by @Sanae6) Prevent duplicate mouse press, release, and motion events from firing on Linux (fixes #939)
  * `b7dab732` (#947 by @muwoo) Fix `Window::request_user_attention` not taking effect after minimizing the window by clicking the taskbar icon
  * `f54cc11e` (#938 by @andrewbaxter) Add `EventLoopWindowTargetExtUnix::gtk_app` getter.
  * “ Return a new `BadIcon::DimensionsZero` error variant in `Icon::from_rgba` if one of the passed icon dimensions is zero.
  * `80e10084` (#954 by @amrbashir) Return a new `BadIcon::DimensionsZero` error variant in `Icon::from_rgba` if one of the passed icon dimensions is zero.
  * `80e10084` (#954 by @amrbashir) Return a new `BadIcon::DimensionsMultiplyOverflow` error variant in `Icon::from_rgba` if dimensions multiplication overflowed.
  * `f5756196` (#956 by @MarijnS95) **Breaking change** : Upgrade `ndk` crate to `0.9` and `ndk-sys` crate to `0.6`. Types from the `ndk` crate are used in public API surface. **Breaking change** : Change `NativeKeyCode::Android(u32)` type to use `i32`, which is the native type used by all Android API. **Breaking change** : The `setup` function passed to `android_binding!()` must now take a `&amp;ThreadLooper` instead of `&amp;ForeignLooper`, matching the `wry` change in https://github.com/tauri-apps/wry/pull/1296.
  * `f54cc11e` (#938 by @andrewbaxter) Add `WindowExtUnix::new_from_gtk_window`.


© 2025 Tauri Contributors. CC-BY / MIT
