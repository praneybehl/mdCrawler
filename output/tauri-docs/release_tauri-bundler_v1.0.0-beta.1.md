Skip to content
# tauri-bundler@1.0.0-beta.1
ReturnView on GitHub
  * The process of copying binaries and resources to `project_out_directory` was moved to the Tauri CLI. 
    * 8f29a260 fix(cli.rs): copy resources and binaries on dev, closes #1298 (#1946) on 2021-06-04
  * Allow setting a path to a license file for the Windows Installer (`tauri.conf.json &gt; bundle &gt; windows &gt; wix &gt; license`). 
    * b769c7f7 feat(bundler): windows installer license, closes #2009 (#2027) on 2021-06-21
  * Configure app shortcut on the Windows Installer. 
    * f0603fcc feat(bundler): desktop shortcut on Windows (#2052) on 2021-06-23
  * Allow setting the Windows installer language and using project names that contains non-Unicode characters. 
    * 47919619 feat(bundler): allow setting wix language, closes #1976 (#1988) on 2021-06-15
  * Fixes resource bundling on Windows when there is nested resource folders. 
    * 35a20527 fix(bundler): windows resources bundling with nested folders (#1878) on 2021-05-21


© 2025 Tauri Contributors. CC-BY / MIT
