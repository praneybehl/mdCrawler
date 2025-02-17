Skip to content
# wry@0.12.2
ReturnView on GitHub
  * Fixed a Linux multi-window issue where the internal url loader didn’t unlock when flushed while empty
    * 5377821 Fix async multiwindow deadlock (#382) on 2021-08-16
  * The custom protocol now returns a `Request` and expects a `Response`.
  * This allows us to get the complete request from the Webview. (Method, GET, POST, PUT etc..) Read the complete header.
  * And allow us to be more flexible in the future without bringing breaking changes.
  * d202573 refactor: Custom protocol request/response (#387) on 2021-08-22
  * On Linux, automation callbacks now use the first created webview as the return value
    * f9d7049 Use the first created webview for webkit2gtk automation callbacks (#383) on 2021-08-16


© 2025 Tauri Contributors. CC-BY / MIT
