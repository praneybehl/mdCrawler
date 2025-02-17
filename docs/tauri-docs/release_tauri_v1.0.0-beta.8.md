Skip to content
# tauri@1.0.0-beta.8
ReturnView on GitHub
  * Fix missing asset protocol path.Now the protocol is `https://asset.localhost/path/to/file` on Windows. Lunix and macOS is still `asset://path/to/file`. 
    * 994b5325 fix: missing asset protocol path (#2484) on 2021-08-23
  * **Breaking change:** Removed `register_uri_scheme_protocol` from the `WebviewAttributes` struct and renamed `register_global_uri_scheme_protocol` to `register_uri_scheme_protocol` on the `Builder` struct, which now takes a `Fn(&amp;AppHandle, &amp;http::Request) -&gt; http::Response` closure. 
    * 539e4489 refactor: custom protocol (#2503) on 2021-08-23
  * Migrate to latest custom protocol allowing `Partial content` streaming and Header parsing. 
    * 539e4489 refactor: custom protocol (#2503) on 2021-08-23


© 2025 Tauri Contributors. CC-BY / MIT
