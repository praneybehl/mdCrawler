Skip to content
# Tauri 2.0.0-alpha.4 Released
Mar 20, 2023 
![Lucas Nogueira](https://v2.tauri.app/authors/lucasfernog.jpeg)
Lucas Nogueira
Tauri Co-Founder
![Tauri 1.2 Launch Hero Image](https://v2.tauri.app/_astro/header.DJC8YrJ3_Z2lir5I.webp)
A new alpha release for the 2.0 has been published. This release includes all changes from the upcoming Tauri 1.3 release, an important breaking change on the HTTP client and native mobile capabilities for Tauri plugins.
## Updating dependencies
Make sure to update both NPM and Cargo dependencies to the latest alpha release. You can update the NPM dependencies with:
  * npm 
  * yarn 
  * pnpm 
  * cargo 


```

npminstall@tauri-apps/cli@next@tauri-apps/api@next

```

```

yarnupgrade@tauri-apps/cli@next@tauri-apps/api@next

```

```

pnpmupdate@tauri-apps/cli@next@tauri-apps/api@next

```

```

cargoaddtauri@2.0.0-alpha.4
cargoaddtauri-build@2.0.0-alpha.2--build
cargoinstalltauri-cli--version"^2.0.0-alpha"--locked

```

Recreate the mobile projects to use the new features:
Terminal window```

rm-rsrc-tauri/gen
tauriandroidinit
tauriiosinit

```

## HTTP Client Breaking Change
The default HTTP client using `attohttpc` has been removed due to issues with the development server proxy on Windows. All `reqwest-*` feature flags have been removed because `reqwest` is now the client we use.
## Native Mobile Functionality for Tauri Plugins
A Tauri plugin now can access iOS via Swift and Android APIs via Kotlin or Java code, simplifying usage of platform interfaces such as camera or geolocation. To bootstrap the iOS and Android projects on an existing plugin, run `tauri plugin ios add` and `tauri plugin android add`. New plugins automatically include all the configuration needed to write native mobile code.
Here’s an example of a plugin that takes a string value and resolves an object:
**Android plugin:**
ExamplePlugin.kt```

package com.plugin.example
import android.app.Activity
import app.tauri.annotation.Command
import app.tauri.annotation.TauriPlugin
import app.tauri.plugin.JSObject
import app.tauri.plugin.Plugin
import app.tauri.plugin.Invoke
@TauriPlugin
class ExamplePlugin(privateval activity: Activity): Plugin(activity) {
@Command
funping(invoke: Invoke) {
valvalue= invoke.getString("value") ?: ""
val ret =JSObject()
ret.put("value", value)
invoke.resolve(ret)
}
}

```

**iOS plugin:**
ExamplePlugin.swift```

import UIKit
import WebKit
import Tauri
class ExamplePlugin: Plugin {
@objcpublicfuncping(_invoke: Invoke)throws {
let value = invoke.getString("value")
invoke.resolve(["value": value asAny])
}
}
@_cdecl("init_plugin_example")
funcinitPlugin(name: SRString, webview: WKWebView?) {
Tauri.registerPlugin(webview: webview, name: name.toString(), plugin: ExamplePlugin())
}

```

**Rust code to initialize the plugin:**
```

use tauri::{
plugin::{Builder, TauriPlugin},
Manager, Runtime,
};
#[cfg(target_os ="ios")]
tauri::ios_plugin_binding!(init_plugin_example);
pubfninit<R: Runtime>() -> TauriPlugin<R> {
Builder::new("example")
.setup(|app, api| {
#[cfg(target_os ="android")]
api.register_android_plugin("com.plugin.example", "ExamplePlugin")?;
#[cfg(target_os ="ios")]
api.register_ios_plugin(init_plugin_example)?;
Ok(())
})
.build()
}

```

**Frontend code to call the plugin command:**
```

import { invoke } from'@tauri-apps/api/tauri';
invoke('plugin:example|ping', { value: 'Tauri' }).then(({ value })=>
console.log('Response', value)
);

```

Check out the upcoming camera plugin and path plugin.
Announcing Tauri 1.3.0
create-tauri-app Version 3 Released
© 2025 Tauri Contributors. CC-BY / MIT
