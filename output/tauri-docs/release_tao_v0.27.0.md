Skip to content
# tao@0.27.0
ReturnView on GitHub
  * `c2357732`(#896) Replaced `dpi` module with a re-export of the `dpi` crate which has a few breaking changes:
    * Replaced `LogicalPixel` with `LogicalUnit`
    * Replaced `PhysicalPixel` with `PhysicalUnit`
    * Removed `Size::width`, `Size::height`, `Position::x`, `Position::y` and `PixelUnit::value`.


© 2025 Tauri Contributors. CC-BY / MIT
