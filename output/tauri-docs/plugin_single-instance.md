Skip to content
# Single Instance
GitHub crates.io 
API Reference 
Ensure that a single instance of your tauri app is running at a time using the Single Instance Plugin.
## Supported Platforms
_This plugin requires a Rust version of at least**1.77.2**_
Platform | Level | Notes  
---|---|---  
windows  
linux  
macos  
android  
ios  
## Setup
Install the Single Instance plugin to get started.
  * Automatic 
  * Manual 


Use your project’s package manager to add the dependency:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * bun 
  * cargo 


```

npmruntauriaddsingle-instance

```

```

yarnruntauriaddsingle-instance

```

```

pnpmtauriaddsingle-instance

```

```

denotasktauriaddsingle-instance

```

```

buntauriaddsingle-instance

```

```

cargotauriaddsingle-instance

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-single-instance--target'cfg(any(target_os = "macos", windows, target_os = "linux"))'

```

  2. Modify `lib.rs` to initialize the plugin:
lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.setup(|app| {
#[cfg(desktop)]
app.handle().plugin(tauri_plugin_single_instance::init(|app, args, cwd| {}));
Ok(())
})
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```



## Usage
The plugin is already installed and initialized, and it should be functioning correctly right away. Nevertheless, we can also enhance its functionality with the `init()` method.
The plugin `init()` method takes a closure that is invoked when a new app instance was started, but closed by the plugin. The closure has three arguments:
  1. **`app`:** The AppHandle of the application.
  2. **`args`:** The list of arguments, that was passed by the user to initiate this new instance.
  3. **`cwd`:** The Current Working Directory denotes the directory from which the new application instance was launched.


So, the closure should look like below
```

.plugin(tauri_plugin_single_instance::init(|app, args, cwd| {
// Write your code here...
}))

```

### Focusing on New Instance
By default, when you initiate a new instance while the application is already running, no action is taken. To focus the window of the running instance when user tries to open a new instance, alter the callback closure as follows:
src-tauri/src/lib.rs```

use tauri::{AppHandle, Manager};
pubfnrun() {
letmutbuilder= tauri::Builder::default();
#[cfg(desktop)]
{
builder=builder.plugin(tauri_plugin_single_instance::init(|app, args, cwd| {
let_=app.get_webview_window("main")
.expect("no main window")
.set_focus();
}));
}
builder
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

© 2025 Tauri Contributors. CC-BY / MIT
