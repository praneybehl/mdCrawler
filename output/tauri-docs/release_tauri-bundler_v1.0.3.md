Skip to content
# tauri-bundler@1.0.3
ReturnView on GitHub
  * Build AppImages inside the `src-tauri/target` folder rather than `~/.cache/tauri`. Making it easier to clean and rebuild from scratch. 
    * 8dd03e69 fix(bundler): Build AppImages inside the target folder (#4521) on 2022-07-03
  * Ensure the notarization `RequestUUID` and `Status` parser works on macOS 10.13.6+. 
    * 23d3d847 fix(bundler): ensure RequestUUID and Status parser adds a \n, closes #4549 (#4559) on 2022-07-03
    * f7c59ecf fix(bundler): support macOS 10.13.6+ on notarization, closes #4549 (#4593) on 2022-07-05


© 2025 Tauri Contributors. CC-BY / MIT
