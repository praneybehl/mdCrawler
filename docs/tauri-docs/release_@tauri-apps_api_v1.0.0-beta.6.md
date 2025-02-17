Skip to content
# @tauri-apps/api@1.0.0-beta.6
ReturnView on GitHub
  * `bundle` now exports `clipboard` module so you can `import { clipboard } from &quot;@tauri-apps/api&quot;`. 
    * 4f88c3fb fix(api.js): `bundle` now exports `clipboard` mod, closes #2243 (#2244) on 2021-07-19
  * Fix double window creation 
    * 9fbcc024 fix(api.js): fix double window creation, closes #2284 (#2285) on 2021-07-23
  * Add `os` module which exports `EOL`, `platform()`, `version()`, `type()`, `arch()`, `tempdir()`
    * 05e679a6 feat(api.js): add `os` module (#2299) on 2021-07-28
  *     * Add new nodejs-inspired functions which are `join`, `resolve`, `normalize`, `dirname`, `basename` and `extname`.
  * Add `sep` and `delimiter` constants.
  * Removed `resolvePath` API, use `resolve` instead.
  * 05b9d81e feat(api.js): add nodejs-inspired functions in `path` module (#2310) on 2021-08-02
  * Change target to ES2021. 
    * 97bc52ee Tooling: [API] Changed target in tsconfig to es6 (#2362) on 2021-08-09
  * Add `toggleMaximize()` function to the `WebviewWindow` class. 
    * 1a510066 fix(core): `data-tauri-drag-region` didn’t respect resizable, closes #2314 (#2316) on 2021-08-02
  * Fix `@ts-expect` error usage 
    * dd52e738 fix(api.js): fix `@ts-expect-error` usage, closes #2249 (#2250) on 2021-07-20
  * Fixes file drop events being swapped (`file-drop-hover` on drop and `file-drop` on hover). 
    * c2b0fe1c fix(core): fix wrong file drop events (#2300) on 2021-07-31
  * Fixes the global bundle UMD code. 
    * 268450b1 fix(api): global bundle broken code, closes #2289 (#2297) on 2021-07-26
  *     * Fixes monitor api not working.
  * Fixes window.print() not working on macOS.
  * 0f63f5e7 fix(api): Fix monitor functions, closes #2294 (#2301) on 2021-07-29
  * Improve `EventName` type using `type-fest`’s `LiteralUnion`. 
    * 8e480297 feat(api): improve `EventName` type definition (#2379) on 2021-08-10
  * Update protocol url path with wry 0.12.1 on Windows. 
    * 88382fe1 chore(api): update protocol url path with wry 0.12.1 on Windows (#2409) on 2021-08-13


© 2025 Tauri Contributors. CC-BY / MIT
