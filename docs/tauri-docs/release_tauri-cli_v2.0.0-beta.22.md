Skip to content
# tauri-cli@2.0.0-beta.22
ReturnView on GitHub
### New Features
  * `c734b9e3c` (#10072 by @FabianLars) Upgraded the WiX version to 3.14 which fixes vulnerability issues and adds support for Arm targets.
  * `7c7fa0964` (#9963 by @lucasfernog) Added `--method` argument for `ios build` to select the export options’ method.
  * `7c7fa0964` (#9963 by @lucasfernog) Setup iOS signing by reading `IOS_CERTIFICATE`, `IOS_CERTIFICATE_PASSWORD` and `IOS_MOBILE_PROVISION` environment variables.


### Enhancements
  * `c01e87ad4` (#10198 by @amrbashir) Enhance `tauri migrate` to also migrate variables like `appWindow`:
```

import { appWindow } from &#39;@tauri-apps/api/window&#39;

```

will become:
```

import { getCurrentWebviewWindow } from &#39;@tauri-apps/api/webviewWindow&#39;
const appWindow = getCurrentWebviewWindow()

```



### Bug Fixes
  * `94136578b` (#10186 by @amrbashir) Fix `migrate` command, migrating incorrect permissions for `clipboard`.
  * `c01e87ad4` (#10198 by @amrbashir) Fix `tauri migrate` incorrectly migrating `@tauri-apps/api/tauri` module to just `core` and `@tauri-apps/api/window` to just `webviewWindow`.
  * `15e125996` (#10234 by @amrbashir) Fix cli failing to detect the correct cargo target directory when using cargo `--target-dir` flag with `tauri build` or `tauri dev`


### Dependencies
  * Upgraded to `tauri-bundler@2.0.1-beta.18`
  * Upgraded to `tauri-macos-sign@0.1.0-beta.0`
  * Upgraded to `tauri-utils@2.0.0-beta.19`


© 2025 Tauri Contributors. CC-BY / MIT
