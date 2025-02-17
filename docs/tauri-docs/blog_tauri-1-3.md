Skip to content
# Announcing Tauri 1.3.0
May 3, 2023 
![Lucas Nogueira](https://v2.tauri.app/authors/lucasfernog.jpeg)
Lucas Nogueira
Tauri Co-Founder
![Tillmann Weidinger](https://v2.tauri.app/authors/tweidinger.png)
Tillmann Weidinger
Tauri Security
![Tauri 1.3 Launch Hero Image](https://v2.tauri.app/_astro/header.w5CMWRUj_2k2GgM.webp)
The Tauri team is excited to announce the 1.3 release. This version includes security improvements, new features and important bug fixes.
## Upgrading
Make sure to update both NPM and Cargo dependencies to the 1.3.0 release. You can update the dependencies with:
  * npm 
  * yarn 
  * pnpm 
  * cargo 


```

npminstall@tauri-apps/cli@latest@tauri-apps/api@latest

```

```

yarnupgrade@tauri-apps/cli@tauri-apps/api--latest

```

```

pnpmupdate@tauri-apps/cli@tauri-apps/api--latest

```

```

cargoupdate

```

## What’s in 1.3.0
### NSIS
The Tauri CLI can now create Windows application installers using NSIS. This new bundle target is also available on macOS and Linux as an experimental feature, so you can cross-compile your Windows installer. Documentation on the latter will be published soon.
### Tauri 1.3 Audit
The internal audit was performed by @tweidinger and @chippers, who are involved in most security topics at the Tauri project. It was performed during paid time at CrabNebula and we are grateful to be able to spend parts of our work time contributing to the open source project and making it a more secure environment :heart:.
We manually audited over 45 PRs. Some PRs (e.g. #5544) lead us to diving into very old RFCs (RFC6068 and RFC3966), NSIS documentation (e.g. #6039) and many other external resources. We documented questions, notes and findings in markdown files and shared these notes with the responsible developers to ensure appropriate fixes.
The changes from a security perspective and findings of the audit are summarized in the following sub-sections.
### External API Access #5918
This was by far the most impactful and time consuming PR we investigated. This PR introduces a streamlined way for applications to allow external domains access to the Tauri IPC layer1 and usage majorly impacts the security model of a Tauri application. Security impact2 depends on exposure3 of the feature, enabled Tauri commands and the capabilities of an adversary4.
We consider this new feature similar to driving a very fast race car without any safety features enabled and urge developers to _very very carefully_ consider if they really need this exposure.
Before this addition was merged, a semi-known vulnerability was (ab)used by application developers to achieve the same functionality. To make the whole community aware of this risk we published a security advisory to give a heads up. Applications are affected if they allow users to navigate to arbitrary domains or have an open redirect vulnerability5. If you implement such a feature you should update to the 1.3 release as fast as possible.
The initial PR changes allowed wildcards (`https://*`) and glob patterns, which we believe are helpful but shouldn’t be exposed to all Tauri developers. We concluded that the risk of over-exposure, like the allow list toggle to enable all Tauri API endpoints, does not justify this permissive exposure. The final implementation allows to configure specified _(sub)domains_6 (eg: `example.com`) to gain remote access to the Tauri IPC.
The few edge use cases, which require wildcards or even further exposure can be implemented by custom Rust code which is able to dynamically modify the IPC access. We now expose this remote IPC scope in a similar fashion as the `fs` or `http` scope.
Assuming a **fully trusted** web service on `https://trusted.example` it is now possible to configure the security scope to allow certain windows or even plugins access to custom implemented commands and optionally the inbuilt Tauri API:
```

"security": {
"dangerousRemoteUrlIpcAccess": [
{
"windows": ["main", "settings"],
"domain": "trusted.example",
"plugins": ["trusted-plugin"],
"enableTauriAPI": false
},
],
}

```

Shared domains **MUST NOT** be used for this in any circumstances. We do not limit access to paths or specific files. You can only scope with **trusted** _(sub)domains_6. Another very risky catch is that developers must be sure that the domain ownership does not change over the lifetime of the application. Domain takeover could lead to compromised user devices.
### Browser Arguments #5799
Due to certain webview features not enabled nor being accessible, a community contribution introduced the possibility to add additional arguments to the webview process, which is created in a new window.
This feature was exposed to the frontend in the `window` endpoint. We found that this exposure was highly risky, as most webviews have very impactful features and flags that can be allowed via the process arguments.
All of the following threat model assumptions are based on the Tauri window creation being allowed in the `allowlist` of the `tauri.conf` and therefore exposed to the frontend. This PR affects Windows only, therefore there is no impact on the other supported operating systems.
An adversary with the capabilities to create windows and pass command line arguments to the webview can elevate their privileges to escape the strict sandboxing of Tauri and the webview.
The flags allow to enable several dangerous webview features, from loading profiles outside of the current default profile folder (stealing browser sessions from the device) to disabling security measurements of the webview (eg: certificate validation, sandboxing, webdriver/headless mode, device management endpoints, …).
We found an old but gold and still unique documentation reference at https://peter.sh/experiments/chromium-command-line-switches/, which helped us understand possible risks on Windows, as the Webview2 uses the same flags.
The feature was then changed to be only exposed on the rust side. Tauri application developers can use this to implement custom commands to invoke webview windows with use case specific arguments.
### Possible ZipSlip #4674
We found that the components to extract remote bundler files like the Webview2 installer were manually extracting single files with the `extract_zip` function, which uses `ZipFile::name()` instead of `ZipFile::enclosed_name()` as recommended in the documentation. Files which had names like `../../../../foo.sh` could be extracted outside of the intended directory on the filesystem. This kind of vulnerability is called ZipSlip.
As the function was only used on verified and trusted files the impact here was nearly zero. Regardless we changed the implementation to facilitate the proper extraction method.
### Bundler Hardening #6039
The bundler was not escaping content passed to the `handlebars::Handlebars::render()`, which could cause unwanted code execution during the bundler phase. This was also a low impact issue but was promptly fixed.
### Other changes
#### New
  * `additional_browser_args` option when creating windows #5799
  * Add `is_minimized()` window method. #5618
  * Add `title` getter on window. #5515
  * content protection APIs #5513
  * Added `Builder::device_event_filter` and `App::set_device_event_filter` methods. #5562
  * Add `WindowsAttributes::app_manifest` to specify the application manifest on Windows. #5730
  * Add support for Cargo’s workspace inheritance. #5775 #6144
  * Added window’s `url()` getter. #5914
  * Added `Window::on_navigation`. #5686
  * Allow setting the text of the dialog buttons. #4383
  * Implement `SystemTray::with_tooltip` and `SystemTrayHandle::set_tooltip` for Windows and macOS. #5938
  * Add dylib support to `tauri.bundle.macOS.frameworks`. #5732


#### Enhancements
  * On Windows, the `msi` installer’s `Launch App` checkbox will be checked by default. #5871
  * Add `--png` option for the `icon` command to generate custom icon sizes. #5246
  * On Windows, change webview theme based on Window theme for more accurate `prefers-color-scheme` support. #5874
  * Remove default features from Cargo.toml template. #6074
  * Add a method to the `WindowBuilder` struct to recreate windows from tauri.conf.json configurations.#6073
  * Improve the error message when `rustc` couldn’t be found. #6021
  * Added support for pre-release identifiers and build numbers for the `.msi` bundle target. Only one of each can be used and it must be numeric only. The version must still be semver compatible according to https://semver.org/. #6096
  * Add `--ci` flag and respect the `CI` environment variable on the `signer generate` command. In this case the default password will be an empty string and the CLI will not prompt for a value. #6097
  * Skip the password prompt on the build command when `TAURI_KEY_PASSWORD` environment variable is empty and the `--ci` argument is provided or the `CI` environment variable is set. d4f89af18d69fd95a4d8a1ede8442547c6a6d0ee


#### Fixes
  * Fix `tauri info` panicking when parsing crates version on a newly created project without a `Cargo.lock` file. #5873
  * Fix building apps with unicode characters in their `productName`. #5872
  * Sync `__TAURI_METADATA__.__windows` across all windows. #5615
  * Fix resize glitch when double clicking a custom titlebar in the top resize area. #5966
  * Disable cursor mouse events on Linux. #6025
  * Fix serialization of js `Map` when used in `invoke`. #6099


## Footnotes
  1. _Inter-Process Communication_ , in this instance the communication between the Tauri core and the frontend code run inside the webview. ↩
  2. _Security Impact_ : What is the theoretical biggest impact of this threat combination? This highly depends on correct scoping of Tauri API endpoints and hardening of custom implemented Tauri commands. ↩
  3. _Exposure_ : Describes the exposed scope items of this feature to either an user or adversary. It is possible to restrict exposure to only certain domains, windows or only to custom implemented commands. ↩
  4. _Adversary Capabilities_ : Which kind of privileges has the adversary? Can range from tricking user into entering malicious input to code execution in the frontend via cross-site-scripting (which is the highest privilege for frontend code in our case). Common capabilities are described in the OWASP documentation. ↩
  5. _An application can be exploited if it parses user input for making an URL redirection decision, which is then not properly validated._ Wikipedia Source ↩
  6. see the Reqwest reference ↩ ↩2


Announcing Tauri 1.4.0
Tauri 2.0.0-alpha.4 Released
© 2025 Tauri Contributors. CC-BY / MIT
