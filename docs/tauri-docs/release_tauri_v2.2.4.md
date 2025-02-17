Skip to content
# tauri@2.2.4
ReturnView on GitHub
### Bug Fixes
  * `27096cdc0` (#12445 by @FabianLars) Fixed an issue that caused Tauri’s CLI to enable tauri’s `native-tls` feature even though it wasn’t needed. Moved `reqwest` to a mobile-only dependency in `tauri` and enabled its `rustls-tls` feature flag.


© 2025 Tauri Contributors. CC-BY / MIT
