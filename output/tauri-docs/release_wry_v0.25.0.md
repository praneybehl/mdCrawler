Skip to content
# wry@0.25.0
ReturnView on GitHub
  * **Breaking Change:** Bump webkit2gtk to 0.19. This will use webkit2gtk-4.1 as dependency from now on. Also Bump gtk version: 0.15 -> 0.16. 
    * c5f3b36 Bump gtk version 0.15 -> 0.16 (#851) on 2023-01-26
  * **Breaking** Add position of the drop to `FileDropEvent` struct. 
    * bce39e2 feat: add file drop position (#847) on 2023-01-17
  * On Android, fix the injection of `intialization_scripts` for devServers where the `Content-Type` header includes more information than just `&quot;text/plain&quot;`. 
    * 87216c7 fix: make the Content-Type check spec compliant (#844) on 2023-01-14


© 2025 Tauri Contributors. CC-BY / MIT
