Skip to content
# tauri@2.0.0-beta.22
ReturnView on GitHub
### Bug Fixes
  * `dfd05441c`(#9860) Revert adding `app-region: drag` to HTML elements with `data-tauri-drag-region` on Windows as it has a few issues:
    * Doesn’t allow right click, as it will always show the system context menu on right click.
    * `data-tauri-drag-region` works only if the click was on an element that has it, this allows buttons in the custom titlebar to work, however `app-region: drag` will treat the whole area as a titlebar won’t even allow clicks on buttons.


© 2025 Tauri Contributors. CC-BY / MIT
