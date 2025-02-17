Skip to content
# Migration to webkit2gtk-4.1 on Linux port
Feb 3, 2023 
![Wu Yu Wei](https://v2.tauri.app/authors/wusyong.png)
Wu Yu Wei
Tauri Development Lead
Hello everybody! We just released Tauri v2.0.0-alpha3 recently. While it doesn’t bring any major feature, it does bring some huge impacts on Linux port. We will use WebKit2GTK–4.1 in 2.0 from now on.
## What does this mean?
If you are using Tauri version 1.x, there’s nothing to worry about. Everything you need is still the same. But if you are using Tauri version 2.0 alpha version starting from `alpha.3`, you will need to install the new WebKit2GTK package with API version 4.1. We will update the prerequisites in our site soon. But if you want to know how to install such version, here are some instructions from wry:
Terminal window```

# On Arch Linux / Manjaro:
sudopacman-Swebkit2gtk-4.1
# On Debian / Ubuntu:
sudoaptinstalllibwebkit2gtk-4.1-dev
# On Fedora:
sudodnfinstallwebkit2gtk4.1-devel

```

## Will this bring breaking changes to my code?
The main difference between version 4.0 and 4.1 are the soup library. WebKit2GTK-4.0 uses soup2 and WebKit2GTK-4.1 uses soup3. So if you didn’t use any soup2-specific APIs, your applications should continue to work fine.
The reason behind this change is because we aim to add flatpak support, but Gnome runtime uses webkit2gtk-4.1. There are also some subtle bugs like this that only happen in soup2 and they can be fixed by upgrading to soup3.
## What other breaking changes we are going to expect?
The major one will be the MSRV. With Tauri v2.0.0-alpha.3 released, MSRV is bumped to 1.64. We will also update windows-rs in the future. This Rust version should satisfy the latest version of windows-rs. We do plan to update our MSRV with minor releases after 2.0. This could ease the friction to stick to any fixed Rust version while updating dependencies.
Tauri Community Growth & Feedback
Announcing the Tauri Mobile Alpha Release
© 2025 Tauri Contributors. CC-BY / MIT
