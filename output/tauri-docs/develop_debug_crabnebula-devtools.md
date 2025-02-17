Skip to content
# CrabNebula DevTools
CrabNebula provides a free DevTools application for Tauri as part of its partnership with the Tauri project. This application allows you to instrument your Tauri app by capturing its embedded assets, Tauri configuration file, logs and spans and providing a web frontend to seamlessly visualize data in real time.
With the CrabNebula DevTools you can inspect your app’s log events (including logs from dependencies), track down the performance of your command calls and overall Tauri API usage, with a special interface for Tauri events and commands, including payload, responses and inner logs and execution spans.
To enable the CrabNebula DevTools, install the devtools crate:
```

cargoaddtauri-plugin-devtools@2.0.0

```

And initialize the plugin as soon as possible in your main function:
```

fnmain() {
// This should be called as early in the execution of the app as possible
#[cfg(debug_assertions)] // only enable instrumentation in development builds
letdevtools= tauri_plugin_devtools::init();
letmutbuilder= tauri::Builder::default();
#[cfg(debug_assertions)]
{
builder=builder.plugin(devtools);
}
builder
.run(tauri::generate_context!())
.expect("error while running tauri application");
}

```

And then run your app as usual, if everything is set up correctly devtools will print the following message:
![DevTools message on terminal](https://v2.tauri.app/_astro/crabnebula-devtools.7F1z87oz_2gi6Uf.webp)
For more information, see the CrabNebula DevTools documentation.
© 2025 Tauri Contributors. CC-BY / MIT
