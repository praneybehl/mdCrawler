Skip to content
# @tauri-apps/api@1.0.0-rc.0
ReturnView on GitHub
  * Add `fileDropEnabled` property to `WindowOptions` so you can now disable it when creating windows from js.
    * 1bfc32a3 fix(api.js): add `fileDropEnabled` to `WindowOptions`, closes #2968 (#2989) on 2021-12-09
  * Add `logDir` function to the `path` module to access the suggested log directory. Add `BaseDirectory.Log` to the `fs` module.
    * acbb3ae7 feat: add Log directory (#2736) on 2021-10-16
    * 62c7a8ad chore(covector): prepare for `rc` release (#3376) on 2022-02-10
  * Expose `ask`, `message` and `confirm` APIs on the dialog module.
    * e98c1af4 feat(core): expose message dialog APIs, fix window.confirm, implement HasRawWindowHandle for Window, closes #2535 (#2700) on 2021-10-02
  * Event `emit` now automatically serialize non-string types.
    * 06000996 feat(api): support unknown types for event emit payload, closes #2929 (#2964) on 2022-01-07
  * Fix `http.fetch` throwing error if the response is successful but the body is empty.
    * 50c63900 fix(api.js): fix `http.fetch` throwing error if response body is empty, closes #2831 (#3008) on 2021-12-09
  * Add `title` option to file open/save dialogs.
    * e1d6a6e6 Create api-file-dialog-title.md (#3235) on 2022-01-16
    * 62c7a8ad chore(covector): prepare for `rc` release (#3376) on 2022-02-10
  * Fix `os.platform` returning `macos` and `windows` instead of `darwin` and `win32`.
    * 3924c3d8 fix(api.js): fix `os.platform` return on macos and windows, closes #2698 (#2699) on 2021-10-02
  * The `formatCallback` helper function now returns a number instead of a string.
    * a48b8b18 feat(core): validate callbacks and event names [TRI-038] [TRI-020] (#21) on 2022-01-09
  * Added `rawHeaders` to `http &gt; Response`.
    * b7a2345b feat(core): add raw headers to HTTP API, closes #2695 (#3053) on 2022-01-07
  * Removed the `currentDir` API from the `path` module.
    * a08509c6 fix(api): remove `currentDir` API from the `path` module on 2022-02-04
  * Remove `.ts` files on the published package.
    * 0f321ac0 fix(api): do not ship TS files, closes #2598 (#2645) on 2021-09-23
  * **Breaking change:** Replaces all usages of `number[]` with `Uint8Array` to be closer aligned with the wider JS ecosystem.
    * 9b19a805 fix(api.js) Replace `number[]`with `Uint8Array`. fixes #3306 (#3305) on 2022-02-05
  * `WindowManager` methods `innerPosition` `outerPosition` now correctly return instance of `PhysicalPosition`. `WindowManager` methods `innerSize` `outerSize` now correctly return instance of `PhysicalSize`.
    * cc8b1468 Fix(api): Window size and position returning wrong class (fix: #2599) (#2621) on 2021-09-22
  * Change the `event` field of the `Event` interface to type `EventName` instead of `string`.
    * b5d9bcb4 Consistent event name usage (#3228) on 2022-01-15
    * 62c7a8ad chore(covector): prepare for `rc` release (#3376) on 2022-02-10
  * Now `resolve()`, `join()` and `normalize()` from the `path` module, won’t throw errors if the path doesn’t exist, which matches NodeJS behavior.
    * fe381a0b fix: `join` no longer cares if path doesn’t exist, closes #2499 (#2548) on 2021-09-21
  * Fixes the dialog `defaultPath` usage on Linux.
    * 2212bd5d fix: dialog default path on Linux, closes #3091 (#3123) on 2021-12-27
  * Fixes `window.label` property returning null instead of the actual label.
    * f5109e0c fix(api): window label null instead of actual value, closes #3295 (#3332) on 2022-02-04
  * Remove the `BaseDirectory::Current` enum variant for security reasons.
    * 696dca58 refactor(core): remove `BaseDirectory::Current` variant on 2022-01-26
  * Change `WindowLabel` type to `string`.
    * f68603ae chore(docs): simplify event system documentation on 2021-09-27
  * When building Universal macOS Binaries through the virtual target `universal-apple-darwin`:
  * Expect a universal binary to be created by the user
  * Ensure that binary is bundled and accessed correctly at runtime
  * 3035e458 Remove target triple from sidecar bin paths, closes #3355 (#3356) on 2022-02-07


© 2025 Tauri Contributors. CC-BY / MIT
