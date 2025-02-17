Skip to content
# tauri@1.0.0-beta.3
ReturnView on GitHub
  * Fixes `api::process::Command` events not firing consistently. 
    * 8c13344f fix(core): command events not firing consistently (#2082) on 2021-06-27
  * Detect ESM scripts and inject the invoke key directly instead of using an IIFE. 
    * 7765c7fa fix(core): invoke key injection on ES module, improve performance (#2094) on 2021-06-27
  * Improve invoke key code injection performance time rewriting code at compile time. 
    * 7765c7fa fix(core): invoke key injection on ES module, improve performance (#2094) on 2021-06-27
  * Enforce uniqueness of window label. 
    * d18b5367 feat(core): enforce label uniqueness, closes #2067 (#2097) on 2021-06-27
  * `Window` is now `Send + Sync` on Windows. 
    * fe32afcc fix(core): `Window` must be `Send + Sync` on Windows, closes #2078 (#2093) on 2021-06-27


© 2025 Tauri Contributors. CC-BY / MIT
