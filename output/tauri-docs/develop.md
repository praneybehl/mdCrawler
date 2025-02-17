Skip to content
# Develop
Now that you have everything set up, you are ready to run your application using Tauri.
If you are using an UI framework or JavaScript bundler you likely have access to a development server that will speed up your development process, so if you haven’t configured your app’s dev URL and script that starts it, you can do so via the devUrl and beforeDevCommand config values:
tauri.conf.json```

{
"build": {
"devUrl": "http://localhost:3000",
"beforeDevCommand": "npm run dev"
}
}

```

Otherwise if you are not using a UI framework or module bundler you can point Tauri to your frontend source code and the Tauri CLI will start a development server for you:
tauri.conf.json```

{
"build": {
"frontendDist": "./src"
}
}

```

Note that in this example the `src` folder must include a `index.html` file along any other assets loaded by your frontend.
### Developing Your Desktop Application
To develop your application for desktop, run the `tauri dev` command.
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauridev

```

```

yarntauridev

```

```

pnpmtauridev

```

```

denotasktauridev

```

```

cargotauridev

```

The first time you run this command, the Rust package manager may need **several minutes** to download and build all the required packages. Since they are cached, subsequent builds are much faster, as only your code needs rebuilding.
Once Rust has finished building, the webview opens, displaying your web app. You can make changes to your web app, and if your tooling supports it, the webview should update automatically, just like a browser.
#### Opening the Web Inspector
You can open the Web Inspector to debug your application by performing a right-click on the webview and clicking “Inspect” or using the `Ctrl + Shift + I` shortcut on Windows and Linux or `Cmd + Option + I` shortcut on macOS.
### Developing your Mobile Application
Developing for mobile is similar to how desktop development works, but you must run `tauri android dev` or `tauri ios dev` instead:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauri [android|ios]dev

```

```

yarntauri [android|ios]dev

```

```

pnpmtauri [android|ios]dev

```

```

denotasktauri [android|ios]dev

```

```

cargotauri [android|ios]dev

```

The first time you run this command, the Rust package manager may need **several minutes** to download and build all the required packages. Since they are cached, subsequent builds are much faster, as only your code needs rebuilding.
#### Development Server
The development server on mobile works similarly to the desktop one, but if you are trying to run on a physical iOS device, you must configure it to listen to a particular address provided by the Tauri CLI, defined in the `TAURI_DEV_HOST` environment variable. This address is either a public network address (which is the default behavior) or the actual iOS device TUN address - which is more secure, but currently needs Xcode to connect to the device.
To use the iOS device’s address you must open Xcode before running the dev command and ensure your device is connected via network in the Window > Devices and Simulators menu. Then you must run `tauri ios dev --force-ip-prompt` to select the iOS device address (a IPv6 address ending with **::2**).
To make your development server listen on the correct host to be accessible by the iOS device you must tweak its configuration to use the `TAURI_DEV_HOST` value if it has been provided. Here is an example configuration for Vite:
```

import { defineConfig } from'vite';
const host = process.env.TAURI_DEV_HOST;
// https://vitejs.dev/config/
exportdefaultdefineConfig({
clearScreen: false,
server: {
host: host||false,
port: 1420,
strictPort: true,
hmr: host
? {
protocol: 'ws',
host,
port: 1421,
}
:undefined,
},
});

```

Check your framework’s setup guide for more information.
#### Device Selection
By default the mobile dev command tries to run your application in a connected device, and fallbacks to prompting you to select a simulator to use. To define the run target upfront you can provide the device or simulator name as argument:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauriiosdev'iPhone 15'

```

```

yarntauriiosdev'iPhone 15'

```

```

pnpmtauriiosdev'iPhone 15'

```

```

denotasktauriiosdev'iPhone 15'

```

```

cargotauriiosdev'iPhone 15'

```

#### Using Xcode or Android Studio
Alternatively you can choose to use Xcode or Android Studio to develop your application. This can help you troubleshoot some development issues by using the IDE instead of the command line tools. To open the mobile IDE instead of running on a connected device or simulator, use the `--open` flag:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauri [android|ios]dev--open

```

```

yarntauri [android|ios]dev--open

```

```

pnpmtauri [android|ios]dev--open

```

```

denotasktauri [android|ios]dev--open

```

```

cargotauri [android|ios]dev--open

```

#### Opening the Web Inspector
  * iOS
Safari must be used to access the Web Inspector for your iOS application.
Open the Safari on your Mac machine, choose **Safari > Settings** in the menu bar, click **Advanced** , then select **Show features for web developers**.
If you are running on a physical device you must enable **Web Inspector** in **Settings > Safari > Advanced**.
After following all steps you should see a **Develop** menu in Safari, where you will find the connected devices and applications to inspect. Select on your device or simulator and click on **localhost** to open the Safari Developer Tools window.
  * Android
The inspector is enabled by default for Android emulators, but you must enable it for physical devices. Connect your Android device to the computer, open the **Settings** app in the Android device, select **About** , scroll to Build Number and tap that 7 times. This will enable Developer Mode for your Android device and the **Developer Options** settings.
To enable application debugging on your device you must enter the **Developer Options** settings, toggle on the developer options switch and enable **USB Debugging**.
The Web Inspector for Android is powered by Google Chrome’s DevTools and can be accessed by navigating to `chrome://inspect` in the Chrome browser. Your device or emulator should appear in the remote devices list if your Android application is running, and you can open the developer tools by clicking **inspect** on your device.


#### Troubleshooting
  1. Error running build script on Xcode


Tauri hooks into the iOS Xcode project by creating a build phase that executes the Tauri CLI to compile the Rust source as a library that is loaded at runtime. The build phase is executed on the Xcode process context, so it might not be able to use shell modifications such as PATH additions, so be careful when using tools such as Node.js version managers which may not be compatible.
  1. Network permission prompt on first iOS app execution


On the first time you execute `tauri ios dev` you might see iOS prompting you for permission to find and connect to devices on your local network. This permission is required because to access your development server from an iOS device, we must expose it in the local network. To run your app in your device you must click Allow and restart your application.
### Reacting to Source Code Changes
Similarly to how your webview reflects changes in real time, Tauri watches your Rust files for changes so when you modify any of them your application is automatically rebuilt and restarted.
You can disable this behavior by using the `--no-watch` flag on the `tauri dev` command.
To restrict the files that are watched for changes you can create a `.taurignore` file in the src-tauri folder. This file works just like a regular Git ignore file, so you can ignore any folder or file:
```

build/
src/generated/*.rs
deny.toml

```

### Using the Browser DevTools
Tauri’s APIs only work in your app window, so once you start using them you won’t be able to open your frontend in your system’s browser anymore.
If you prefer using your browser’s developer tooling, you must configure tauri-invoke-http to bridge Tauri API calls through a HTTP server.
### Source Control
In your project repository, you **SHOULD** commit the `src-tauri/Cargo.lock` along with the `src-tauri/Cargo.toml` to git because Cargo uses the lockfile to provide deterministic builds. As a result, it is recommended that all applications check in their `Cargo.lock`. You **SHOULD NOT** commit the `src-tauri/target` folder or any of its contents.
© 2025 Tauri Contributors. CC-BY / MIT
