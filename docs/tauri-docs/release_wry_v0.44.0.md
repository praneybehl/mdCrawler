Skip to content
# wry@0.44.0
ReturnView on GitHub
  * `b863d38` (#1356 by @SpikeHD) Expose ability to enable browser extensions in WebView2
  * `9220793` (#1361 by @amrbashir) Ignore duplicate custom protocols in `WebviewBuilder::with_custom_protocol` and `WebviewBuilder::with_async_custom_protocol` and use the last registered one.
  * `9220793` (#1361 by @amrbashir) Removed `Error::DuplicateCustomProtocol` variant.
  * `5915341` (#1354 by @millermk) Fixes Android webview error page flashing when a redirect to the app is performed.
  * `170095b` (#1360 by @Steve-xmh) Fix web resource loading in android binding by skip duplicate Content-Type/Content-Length headers.
  * `5915341` (#1354 by @millermk) Fix navigation error handling to trigger custom protocol on Android.


© 2025 Tauri Contributors. CC-BY / MIT
