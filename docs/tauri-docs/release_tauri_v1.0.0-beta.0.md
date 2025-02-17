Skip to content
# tauri@1.0.0-beta.0
ReturnView on GitHub
  * **Breaking:** `api::path::resolve_path()` and `api::path::app_dir()` now takes the config as first argument and the `PackageInfo` as second argument. **Breaking:** `api::path::app_dir()` now resolves to `$\{configDir}/$\{config.tauri.bundle.identifier}`.
    * 428d50a refactor(core): use bundle identifier on app dir, closes #1693 (#1703) on 2021-05-04
    * 7bb7dda refactor(core): resolve resource_dir using the package info (#1762) on 2021-05-10
  * Adds `manage` API to the `Builder` struct, which manages app state.
    * 8b6f3de feat(core): add state management, closes #1655 (#1665) on 2021-05-02
  * **Breaking:** The `assets` field on the `tauri::Context` struct is now a `Arc&lt;impl Assets&gt;`.
    * 5110c70 feat(core): allow users to access the Assets instance (#1691) on 2021-05-03
  * Only commands with a `async fn` are executed on a separate task. `#[command] fn command_name` runs on the main thread.
    * bb8dafb feat(core): #[command] return with autoref specialization workaround fix #1672 (#1734) on 2021-05-09
  * Renamed the `command` API module to `process`.
    * b0bb796 refactor: rename `command` mod to `process`, move restart_application (#1667) on 2021-04-30
  * Adds `options` argument to the shell command API (`env` and `cwd` configuration).
    * 721e98f feat(core): add env, cwd to the command API, closes #1634 (#1635) on 2021-04-28
  * Improves support for commands returning `Result`.
    * bb8dafb feat(core): #[command] return with autoref specialization workaround fix #1672 (#1734) on 2021-05-09
  * Adds `status` and `output` APIs to the `tauri::api::process::Command` struct.
    * d92fde7 feat(core): add `output` and `status` APIs to the `Command` struct (#1668) on 2021-05-02
  * The `create_window` API callback now takes two arguments: the `WindowBuilder` and the `WebviewAttributes` and must return a tuple containing both values.
    * c31f097 refactor: update to wry 0.9 (#1630) on 2021-04-28
  * Reintroduce `csp` injection, configured on `tauri.conf.json &gt; tauri &gt; security &gt; csp`.
    * 6132f3f feat(core): reintroduce CSP injection (#1704) on 2021-05-04
  * Adds the default types used with `Builder::default()` to items that expose `Params` in their type. This allows you to skip specifying a generic parameter to types like `Window&lt;P&gt;` if you use the default type.
    * 27a7810 feat(core): add default Args to all types exposing Params (#1777) on 2021-05-11
  * Change draggable region element detection from `drag-region` class to `data-tauri-drag-region` attribute.
    * 4f1e87f refactor(core): change drag element detection to data attr, fixes #1656 (#1659) on 2021-04-29
  * Emit `tauri://resize`, `tauri://move`, `tauri://close-requested`, `tauri://destroyed`, `tauri://focus`, `tauri://blur` and `tauri://scale-change` events to the window.
    * 9c10ccf feat(core) window events, closes #1523 (#1726) on 2021-05-06
  * The event `emit` function payload type is now `impl Serialize` instead of `Option&lt;impl Serialize&gt;`.
    * 4687538 refactor(core): drop `Option` payload type on `event::emit` (#1760) on 2021-05-09
  * Update `tauri-hotkey` to v0.1.2, fixing a compilation issue on 32-bit platforms.
    * 92a01a7 chore(deps): bump tauri-hotkey to 0.1.2 (#1701) on 2021-05-04
  * Implemented window menus APIs.
    * 41d5d6a feat(core): window menus (#1745) on 2021-05-08
  * Added the `#[non_exhaustive] attribute where appropriate.
    * e087f0f feat: add `#[non_exhaustive]` attribute (#1725) on 2021-05-05
  * `Notification.requestPermission()` now returns `&quot;denied&quot;` when not allowlisted. `IsNotificationPermissionGranted` returns `false` when not allowlisted.
    * 8941790 fix(core): notification permission check when !allowlisted, closes #1666 (#1677) on 2021-05-02
  * Refactored the `Plugin` trait `initialize` and `extend_api` signatures. `initialize` now takes the `App` as first argument, and `extend_api` takes an `Invoke` instead of `InvokeMessage`. This adds support to managed state on plugins.
    * 8b6f3de feat(core): add state management, closes #1655 (#1665) on 2021-05-02
    * 1d6f418 refactor(core): merge invoke items into single struct, allow ? (#1683) on 2021-05-02
  * `window.print()` now works on all platforms.
    * 56e74cc feat(core): ensure `window.print()`works on macOS (#1738) on 2021-05-07
  * **Breaking:** `Context` fields are now private, and is expected to be created through `Context::new(...)`. All fields previously available through `Context` are now public methods.
    * 5542359 refactor(core): Context fields now private, Icon used on all platforms (#1774) on 2021-05-11
  * `Settings` is now serialized using `bincode`.
    * 455c550 refactor(core): `Settings` serialization using `bincode` (#1758) on 2021-05-09
  * The window management API was refactored: removed `setX`, `setY`, `setWidth`, `setHeight` APIs, renamed `resize` to `setSize` and the size and position APIs now allow defining both logical and physical values.
    * 6bfac86 refactor(core): add window getters, physical & logical sizes/positions (#1723) on 2021-05-05
  * Removed the `tcp` module from `tauri::api`.
    * e087f0f feat: add `#[non_exhaustive]` attribute (#1725) on 2021-05-05
  * Removes the `with_window` attribute on the `command` macro. Tauri now infers it using the `CommandArg` trait.
    * 8b6f3de feat(core): add state management, closes #1655 (#1665) on 2021-05-02
    * 1d6f418 refactor(core): merge invoke items into single struct, allow ? (#1683) on 2021-05-02
  * Move `restart_application` API from `app` module to `process` module.
    * b0bb796 refactor: rename `command` mod to `process`, move restart_application (#1667) on 2021-04-30
  * `tauri-runtime` crate initial release.
    * 665ec1d refactor: move runtime to `tauri-runtime` crate (#1751) on 2021-05-09
    * 45a7a11 feat(core): add `tauri-wry` crate (#1756) on 2021-05-09
  * The `setup` Error type must be `Send`.
    * e087f0f feat: add `#[non_exhaustive]` attribute (#1725) on 2021-05-05
  * Simplify usage of app event and window label types. The following functions now accept references the `Tag` can be borrowed as. This means an `&amp;str` can now be accepted for functions like `Window::emit`. This is a breaking change for the following items, which now need to take a reference. Additionally, type inference for `&amp;&quot;event&quot;.into()` will no longer work, but `&amp;&quot;event&quot;.to_string()` will. The solution for this is to now just pass `&quot;event&quot;` because `Borrow&lt;str&gt;` is implemented for the default event type `String`.
  * **Breaking:** `Window::emit` now accepts `Borrow` for the event.
  * **Breaking:** `Window::emit_others` now accepts `Borrow` for the event
  * **Breaking:** `Window::trigger` now accepts `Borrow` for the event.
  * **Breaking:** `Manager::emit_all` now accepts `Borrow` for the event.
  * **Breaking:** `Manager::emit_to` now accepts `Borrow` for both the event and window label.
  * **Breaking:** `Manager::trigger_global` now accepts `Borrow` for the event.
  * **Breaking:** `Manager::get_window` now accepts `Borrow` for the window label.
  * _(internal):_ `trait tauri::runtime::tag::TagRef` helper for accepting tag references. Any time you want to accept a tag reference, that trait will handle requiring the reference to have all the necessary bounds, and generate errors when the exposed function doesn’t set a bound like `P::Event: Borrow&lt;E&gt;`.
  * 181e132 refactor(core): simplify usage of app event and window label types (#1623) on 2021-04-27
  * a755d23 refactor(core): more bounds for better errors from #1623 (#1632) on 2021-04-27
  * `tauri-runtime-wry` initial release.
    * 45a7a11 feat(core): add `tauri-wry` crate (#1756) on 2021-05-09
  * Adds system tray support.
    * c090927 feat(core): system tray, closes #157 (#1749) on 2021-05-09
  * Rename `Attributes` to `WindowBuilder`.
    * c31f097 refactor: update to wry 0.9 (#1630) on 2021-04-28
  * The `Window#create_window` API now has the same signature as `App#create_window`.
    * dbd9b07 refactor(core): `create_window` API signature on the Window struct (#1746) on 2021-05-08
  * Adds `on_window_event` API to the `Window` struct.
    * 9c10ccf feat(core) window events, closes #1523 (#1726) on 2021-05-06
  * Adds window getters.
    * 6bfac86 refactor(core): add window getters, physical & logical sizes/positions (#1723) on 2021-05-05
  * Update `wry` to v0.9.
    * c31f097 refactor: update to wry 0.9 (#1630) on 2021-04-28


© 2025 Tauri Contributors. CC-BY / MIT
