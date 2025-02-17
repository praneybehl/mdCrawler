Skip to content
# tauri-cli@2.0.0-alpha.6
ReturnView on GitHub
  * Use Ubuntu 20.04 to compile the CLI for cargo-binstall, increasing the minimum libc required.
  * Automatically enable the `rustls-tls` tauri feature on mobile and `native-tls` on desktop if `rustls-tls` is not enabled. 
    * cfdee00f refactor(core): fix tls features, use rustls on mobile (#6591) on 2023-03-30


© 2025 Tauri Contributors. CC-BY / MIT
