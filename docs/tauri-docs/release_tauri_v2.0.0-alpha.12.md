Skip to content
# tauri@2.0.0-alpha.12
ReturnView on GitHub
### Enhancements
  * `8a676617`(#7618) Ensure Builder is Send by requiring the menu closure to be Send.
  * `0d63732b`(#7754) Added `Builder::register_asynchronous_uri_scheme_protocol` to allow resolving a custom URI scheme protocol request asynchronously to prevent blocking the main thread.


### Bug Fixes
  * `0d63732b`(#7754) Fixes invalid header value type when requesting IPC body through a channel.
  * `e98393e4`(#7673) No longer unpacking and flattening the `payload` over the IPC so that commands with arguments called `cmd`, `callback`, `error`, `options` or `payload` aren’t breaking the IPC.
  * `29818de6`(#7662) Fixes IPC failing to communicate for remote URLs on macOS and iOS.


### What’s Changed
  * `6177150b`(#7601) Changed `FileDropEvent` to include drop and hover position.


### Dependencies
  * Upgraded to `tauri-runtime@1.0.0-alpha.1`
  * Upgraded to `tauri-runtime-wry@1.0.0-alpha.1`


### Breaking Changes
  * `0d63732b`(#7754) Changed `Builder::register_uri_scheme_protocol` to return a `http::Response` instead of `Result&lt;http::Response&gt;`. To return an error response, manually create a response with status code >= 400.
  * `0d63732b`(#7754) `tauri-runtime` no longer implements its own HTTP types and relies on the `http` crate instead.
  * `0d63732b`(#7754) Changed `Builder::invoke_system` to take references instead of owned values.
  * `5c95152c`(#7621) Changed `MenuBuilder\SubmenuBuilder::text`, `MenuBuilder\SubmenuBuilder::check`, `MenuBuilder\SubmenuBuilder::icon` and `MenuBuilder\SubmenuBuilder::native_icon` to take an `id` as the first argument.
  * `0d63732b`(#7754) Changed `Window::on_message` signature to take a responder closure instead of returning the response object in order to asynchronously process the request.


© 2025 Tauri Contributors. CC-BY / MIT
