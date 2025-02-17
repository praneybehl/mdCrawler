Skip to content
# wry@0.12.0
ReturnView on GitHub
  * Custom Protocol handlers no longer take a `&amp;Window` parameter. 
    * 0e2574c Remove `&amp;Window` parameter from Custom Protocol handlers (#361) on 2021-07-28
  * Update gtk to version 0.14. This also remove requirement of `clang`. 
    * 251a80b Update gtk to version 0.14 (#364) on 2021-08-06
  * Update tao to v0.5. Please see release notes on tao for more information. 
    * 483bad0 feat: tao as window dependency (#230) on 2021-05-03
    * 51430e9 publish new versions (#221) on 2021-05-09
    * 0cf0089 Update tao to v0.2.6 (#271) on 2021-05-18
    * a76206c publish new versions (#272) on 2021-05-18
    * 3c4f8b8 Update tao to v0.5 (#365) on 2021-08-09
  * Add flags to support all other possible unix systems. 
    * c0d0a78 Add flags to support all other unix systems. (#352) on 2021-07-21
  * Support having multiple webkit2gtk `WebView`s on a single `WebContext`. 
    * 3f03d6b Support multiple webviews on a single WebContext (webkit2gtk) (#359) on 2021-07-28
  * On Windows, Fix cursor flickering when Tao window is without decorations 
    * e28bcce fix(windows): fix mouse style flicker when `decorations: false` (#350) on 2021-07-20
  * Remove winrt support since it’s outdated for a long time. We will reimplement it again once `windws-rs` is stable! 
    * c37973e chore(windows): remove winrt support (#356) on 2021-07-24


© 2025 Tauri Contributors. CC-BY / MIT
