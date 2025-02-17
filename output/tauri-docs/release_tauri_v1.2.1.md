Skip to content
# tauri@1.2.1
ReturnView on GitHub
  * Fixes a double serialization on the IPC. 
    * 677838cc fix double serialize on invoke (#5639) on 2022-11-20
  * Moved the custom protocol headers support on Linux behind the `linux-protocol-headers` Cargo feature to enhance compatibility with older Linux distributions. 
    * d7109460 refactor: move Linux custom protocol headers support behind feature flag (#5683) on 2022-11-24
  * Fixes definition of `impl HasRawDisplayHandle` for `AppHandle` and `App`. 
    * ed43ff32 fix(tauri): add missing generics on AppHandle and App (#5642) on 2022-11-17


© 2025 Tauri Contributors. CC-BY / MIT
