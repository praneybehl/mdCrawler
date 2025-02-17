Skip to content
# @tauri-apps/api@1.0.0-rc.7
ReturnView on GitHub
  * Fix `FilePart` usage in `http.Body.form` by renaming the `value` property to `file`. 
    * 55f89d5f fix(api): Rename FormPart `value` to `file` to match docs and endpoint (#4307) on 2022-06-09
  * Fixes a memory leak in the command system. 
    * f72cace3 fix: never remove ipc callback & mem never be released (#4274) on 2022-06-05
  * The notification’s `isPermissionGranted` function now returns `boolean` instead of `boolean | null`. The response is never `null` because we won’t check the permission for now, always returning `true` instead. 
    * f482b094 fix: remove notification permission prompt (#4302) on 2022-06-09
  * Added the `resolveResource` API to the path module. 
    * 7bba8db8 feat(api): add `resolveResource` API to the path module (#4234) on 2022-05-29
  * Renamed `writeFile` to `writeTextFile` but kept the original function for backwards compatibility. 
    * 3f998ca2 feat(api): add `writeTextFile` and `(path, contents, options)` overload (#4228) on 2022-05-29
  * Added `(path, contents[, options])` overload to the `writeTextFile` and `writeBinaryFile` APIs. 
    * 3f998ca2 feat(api): add `writeTextFile` and `(path, contents, options)` overload (#4228) on 2022-05-29


© 2025 Tauri Contributors. CC-BY / MIT
