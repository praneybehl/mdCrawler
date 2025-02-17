Skip to content
# Logging
GitHub npm  crates.io 
API Reference 
Configurable logging for your Tauri app.
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
Install the log plugin to get started.
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

npmruntauriaddlog

```

```

yarnruntauriaddlog

```

```

pnpmtauriaddlog

```

```

denotasktauriaddlog

```

```

buntauriaddlog

```

```

cargotauriaddlog

```

  1. Run the following command in the `src-tauri` folder to add the plugin to the project’s dependencies in `Cargo.toml`:
```

cargoaddtauri-plugin-log

```

  2. Modify `lib.rs` to initialize the plugin:
src-tauri/src/lib.rs```

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.plugin(tauri_plugin_log::Builder::new().build())
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

  3. Install the JavaScript Guest bindings using your preferred JavaScript package manager:
     * npm 
     * yarn 
     * pnpm 
     * deno 
     * bun 
```

npminstall@tauri-apps/plugin-log

```

```

yarnadd@tauri-apps/plugin-log

```

```

pnpmadd@tauri-apps/plugin-log

```

```

denoaddnpm:@tauri-apps/plugin-log

```

```

bunadd@tauri-apps/plugin-log

```



## Usage
  1. First, you need to register the plugin with Tauri.
src-tauri/src/lib.rs```

use tauri_plugin_log::{Target, TargetKind};
#[cfg_attr(mobile, tauri::mobile_entry_point)]
pubfnrun() {
tauri::Builder::default()
.plugin(tauri_plugin_log::Builder::new().build())
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

  2. Afterwards, all the plugin’s APIs are available through the JavaScript guest bindings:
```

import {
warn,
debug,
trace,
info,
error,
attachConsole,
attachLogger,
} from'@tauri-apps/plugin-log';
// when using `"withGlobalTauri": true`, you may use
// const { warn, debug, trace, info, error, attachConsole, attachLogger } = window.__TAURI__.log;

```



## Logging
  * JavaScript 
  * Rust 


Use one of the plugin’s `warn`, `debug`, `trace`, `info` or `error` APIs to produce a log record from JavaScript code:
```

import { warn, debug, trace, info, error } from'@tauri-apps/plugin-log';
trace('Trace');
info('Info');
error('Error');

```

To automatically forward all `console` messages to the log plugin you can rewrite them:
```

import { warn, debug, trace, info, error } from'@tauri-apps/plugin-log';
functionforwardConsole(
fnName:'log'|'debug'|'info'|'warn'|'error',
logger:(message:string)=>Promise<void>
) {
const original = console[fnName];
console[fnName] =(message)=> {
original(message);
logger(message);
};
}
forwardConsole('log', trace);
forwardConsole('debug', debug);
forwardConsole('info', info);
forwardConsole('warn', warn);
forwardConsole('error', error);

```

To create your own logs on the Rust side you can use the [`log` crate]:
```

log::error!("something bad happened!");
log::info!("Tauri is awesome!");

```

Note that the [`log` crate] must be added to your `Cargo.toml` file:
```

[dependencies]
log = "0.4"

```

## Log targets
The log plugin builder has a `targets` function that lets you configure common destination of all your application logs.
### Printing logs to the terminal
To forward all your logs to the terminal, enable the `Stdout` or `Stderr` targets:
```

tauri_plugin_log::Builder::new()
.target(tauri_plugin_log::Target::new(
tauri_plugin_log::TargetKind::Stdout,
))
.build()

```

This target is enabled by default.
### Logging to the webview console
To view all your Rust logs in the webview console, enable the `Webview` target and run `attachConsole` in your frontend:
```

tauri_plugin_log::Builder::new()
.target(tauri_plugin_log::Target::new(
tauri_plugin_log::TargetKind::Webview,
))
.build()

```

```

import { attachConsole } from'@tauri-apps/plugin-log';
const detach = await attachConsole();
// call detach() if you do not want to print logs to the console anymore

```

### Persisting logs
To write all logs to a file, you can use either the `LogDir` or the `Folder` targets.
  * `LogDir`:


```

tauri_plugin_log::Builder::new()
.target(tauri_plugin_log::Target::new(
tauri_plugin_log::TargetKind::LogDir {
file_name: Some("logs".to_string()),
},
))
.build()

```

When using the LogDir target, all logs are stored in the recommended log directory. The following table describes the location of the logs per platform:
Platform| Value| Example  
---|---|---  
Linux| `{configDir}/{bundleIdentifier}`| `/home/alice/.config/com.tauri.dev`  
macOS| `{homeDir}/Library/Logs/{bundleIdentifier}`| `/Users/Alice/Library/Logs/com.tauri.dev`  
Windows| `{FOLDERID_LocalAppData}/{bundleIdentifier}/logs`| `C:\Users\Alice\AppData\Local\com.tauri.dev\logs`  
  * `Folder`:


The Folder target lets you write logs to a custom location in the filesystem.
```

tauri_plugin_log::Builder::new()
.target(tauri_plugin_log::Target::new(
tauri_plugin_log::TargetKind::Folder {
path: std::path::PathBuf::from("/path/to/logs"),
file_name: None,
},
))
.build()

```

The default `file_name` is the application name.
#### Configuring log file behavior
By default the log file gets discarded when it reaches the maximum size. The maximum file size can be configured via the builder’s `max_file_size` function:
```

tauri_plugin_log::Builder::new()
.max_file_size(50_000/* bytes */)
.build()

```

Tauri can automatically rotate your log file when it reaches the size limit instead of discarding the previous file. This behavior can be configured using `rotation_strategy`:
```

tauri_plugin_log::Builder::new()
.rotation_strategy(tauri_plugin_log::RotationStrategy::KeepAll)
.build()

```

### Filtering
By default **all** logs are processed. There are some mechanisms to reduce the amount of logs and filter only relevant information.
### Maximum log level
To set a maximum log level, use the `level` function:
```

tauri_plugin_log::Builder::new()
.level(log::LevelFilter::Info)
.build()

```

In this example, debug and trace logs are discarded as they have a lower level than _info_.
It is also possible to define separate maximum levels for individual modules:
```

tauri_plugin_log::Builder::new()
.level(log::LevelFilter::Info)
// verbose logs only for the commands module
.level_for("my_crate_name::commands", log::LevelFilter::Trace)
.build()

```

Note that these APIs use the [`log` crate], which must be added to your `Cargo.toml` file:
```

[dependencies]
log = "0.4"

```

### Target filter
A `filter` function can be defined to discard unwanted logs by checking their metadata:
```

tauri_plugin_log::Builder::new()
// exclude logs with target `"hyper"`
.filter(|metadata|metadata.target() !="hyper")
.build()

```

### Formatting
The log plugin formats each log record as `DATE[TARGET][LEVEL] MESSAGE`. A custom format function can be provided with `format`:
```

tauri_plugin_log::Builder::new()
.format(|out, message, record| {
out.finish(format_args!(
"[{} {}] {}",
record.level(),
record.target(),
message
))
})
.build()

```

#### Log dates
By default the log plugin uses the UTC timezone to format dates but you can configure it to use the local timezone with `timezone_strategy`:
```

tauri_plugin_log::Builder::new()
.timezone_strategy(tauri_plugin_log::TimezoneStrategy::UseLocal)
.build()

```

## Permissions
By default, all plugin commands are blocked and cannot be accessed. You must define a list of permissions in your `capabilities` configuration.
See the Capabilities Overview for more information and the step by step guide to use plugin permissions.
src-tauri/capabilities/default.json```

{
"$schema": "../gen/schemas/desktop-schema.json",
"identifier": "main-capability",
"description": "Capability for the main window",
"windows": ["main"],
"permissions": ["log:default"]
}

```

## Default Permission
Allows the log command
  * `allow-log`


## Permission Table
Identifier | Description  
---|---  
`log:allow-log` |  Enables the log command without any pre-configured scope.  
`log:deny-log` |  Denies the log command without any pre-configured scope.  
© 2025 Tauri Contributors. CC-BY / MIT
