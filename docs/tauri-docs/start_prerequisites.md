Skip to content
# Prerequisites
In order to get started building your project with Tauri you’ll first need to install a few dependencies:
  1. System Dependencies
  2. Rust
  3. Configure for Mobile Targets (only required if developing for mobile)


## System Dependencies
Follow the link to get started for your respective operating system:
  * Linux (see below for specific distributions)
  * macOS Catalina (10.15) and later
  * Windows 7 and later


### Linux
Tauri requires various system dependencies for development on Linux. These may be different depending on your distribution but we’ve included some popular distributions below to help you get setup.
  * Debian 
  * Arch 
  * Fedora 
  * Gentoo 
  * openSUSE 
  * Alpine 
  * NixOS 


Terminal window```

sudoaptupdate
sudoaptinstalllibwebkit2gtk-4.1-dev\
build-essential\
curl\
wget\
file\
libxdo-dev\
libssl-dev\
libayatana-appindicator3-dev\
librsvg2-dev

```

Terminal window```

sudopacman-Syu
sudopacman-S--needed\
webkit2gtk-4.1\
base-devel\
curl\
wget\
file\
openssl\
appmenu-gtk-module\
libappindicator-gtk3\
librsvg

```

Terminal window```

sudodnfcheck-update
sudodnfinstallwebkit2gtk4.1-devel\
openssl-devel\
curl\
wget\
file\
libappindicator-gtk3-devel\
librsvg2-devel
sudodnfgroupinstall"c-development"

```

Terminal window```

sudoemerge--ask\
net-libs/webkit-gtk:4.1\
dev-libs/libappindicator\
net-misc/curl\
net-misc/wget\
sys-apps/file

```

Terminal window```

sudozypperup
sudozypperinwebkit2gtk3-devel\
libopenssl-devel\
curl\
wget\
file\
libappindicator3-1\
librsvg-devel
sudozypperin-tpatterndevel_basis

```

Terminal window```

sudoapkadd\
build-base\
webkit2gtk\
curl\
wget\
file\
openssl\
libayatana-appindicator-dev\
librsvg

```

Using `nix-shell`:
```

let
pkgs=import<nixpkgs> { };
in
pkgs.mkShell {
nativeBuildInputs=withpkgs; [
pkg-config
gobject-introspection
cargo
cargo-tauri
nodejs
];
buildInputs=withpkgs;[
at-spi2-atk
atkmm
cairo
gdk-pixbuf
glib
gtk3
harfbuzz
librsvg
libsoup_3
pango
webkitgtk_4_1
openssl
];
}

```

If your distribution isn’t included above then you may want to check Awesome Tauri on GitHub to see if a guide has been created.
Next: Install Rust
### macOS
Tauri uses Xcode and various macOS and iOS development dependencies.
Download and install Xcode from one of the following places:
  * Mac App Store
  * Apple Developer website.


Be sure to launch Xcode after installing so that it can finish setting up.
Only developing for desktop targets? If you’re only planning to develop desktop apps and not targeting iOS then you can install Xcode Command Line Tools instead:
Terminal window```

xcode-select--install

```

Next: Install Rust
### Windows
Tauri uses the Microsoft C++ Build Tools for development as well as Microsoft Edge WebView2. These are both required for development on Windows.
Follow the steps below to install the required dependencies.
#### Microsoft C++ Build Tools
  1. Download the Microsoft C++ Build Tools installer and open it to begin installation.
  2. During installation check the “Desktop development with C++” option.


![Visual Studio C++ Build Tools installer screenshot](https://v2.tauri.app/_astro/visual-studio-build-tools-installer.BWhlyd8N_Z2amjwc.webp)
Next: Install WebView2.
#### WebView2
Tauri uses Microsoft Edge WebView2 to render content on Windows.
Install WebView2 by visiting the WebView2 Runtime download section. Download the “Evergreen Bootstrapper” and install it.
Next: Install Rust
## Rust
Tauri is built with Rust and requires it for development. Install Rust using one of following methods. You can view more installation methods at https://www.rust-lang.org/tools/install.
  * Linux and macOS 
  * Windows 


Install via `rustup` using the following command:
Terminal window```

curl--proto'=https'--tlsv1.2https://sh.rustup.rs-sSf|sh

```

Visit https://www.rust-lang.org/tools/install to install `rustup`.
Alternatively, you can use `winget` to install rustup using the following command in PowerShell:
Terminal window```

winget install --id Rustlang.Rustup

```

**Be sure to restart your Terminal (and in some cases your system) for the changes to take affect.**
Next: Configure for Mobile Targets if you’d like to build for Android and iOS, or, if you’d like to use a JavaScript framework, install Node. Otherwise Create a Project.
## Node.js
  1. Go to Node.js website, download the Long Term Support (LTS) version and install it.
  2. Check if Node was successfully installed by running:


Terminal window```

node-v
# v20.10.0
npm-v
# 10.2.3

```

It’s important to restart your Terminal to ensure it recognizes the new installation. In some cases, you might need to restart your computer.
While npm is the default package manager for Node.js, you can also use others like pnpm or yarn. To enable these, run `corepack enable` in your Terminal. This step is optional and only needed if you prefer using a package manager other than npm.
Next: Configure for Mobile Targets or Create a project.
## Configure for Mobile Targets
If you’d like to target your app for Android or iOS then there are a few additional dependencies that you need to install:
  * Android
  * iOS


### Android
  1. Download and install Android Studio from the Android Developers website
  2. Set the `JAVA_HOME` environment variable:


  * Linux 
  * macOS 
  * Windows 


Terminal window```

exportJAVA_HOME=/opt/android-studio/jbr

```

Terminal window```

exportJAVA_HOME="/Applications/Android Studio.app/Contents/jbr/Contents/Home"

```

Terminal window```

[System.Environment]::SetEnvironmentVariable("JAVA_HOME","C:\Program Files\Android\Android Studio\jbr","User")

```

  1. Use the SDK Manager in Android Studio to install the following:


  * Android SDK Platform
  * Android SDK Platform-Tools
  * NDK (Side by side)
  * Android SDK Build-Tools
  * Android SDK Command-line Tools


Selecting “Show Package Details” in the SDK Manager enables the installation of older package versions. Only install older versions if necessary, as they may introduce compatibility issues or security risks.
  1. Set `ANDROID_HOME` and `NDK_HOME` environment variables.


  * Linux 
  * macOS 
  * Windows 


Terminal window```

exportANDROID_HOME="$HOME/Android/Sdk"
exportNDK_HOME="$ANDROID_HOME/ndk/$(ls-1$ANDROID_HOME/ndk)"

```

Terminal window```

exportANDROID_HOME="$HOME/Library/Android/sdk"
exportNDK_HOME="$ANDROID_HOME/ndk/$(ls-1$ANDROID_HOME/ndk)"

```

Terminal window```

[System.Environment]::SetEnvironmentVariable("ANDROID_HOME","$env:LocalAppData\Android\Sdk","User")
$VERSION=Get-ChildItem-Name "$env:LocalAppData\Android\Sdk\ndk"
[System.Environment]::SetEnvironmentVariable("NDK_HOME","$env:LocalAppData\Android\Sdk\ndk\$VERSION","User")

```

  1. Add the Android targets with `rustup`:


Terminal window```

rustuptargetaddaarch64-linux-androidarmv7-linux-androideabii686-linux-androidx86_64-linux-android

```

Next: Setup for iOS or Create a project.
### iOS
  1. Add the iOS targets with `rustup` in Terminal:


Terminal window```

rustuptargetaddaarch64-apple-iosx86_64-apple-iosaarch64-apple-ios-sim

```

  1. Install Homebrew:


Terminal window```

/bin/bash-c"$(curl-fsSLhttps://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

```

  1. Install Cocoapods using Homebrew:


Terminal window```

brewinstallcocoapods

```

Next: Create a project.
## Troubleshooting
If you run into any issues during installation be sure to check the Troubleshooting Guide or reach out on the Tauri Discord.
Next Steps
Now that you’ve installed all of the prerequisistes you’re ready to create your first Tauri project!
© 2025 Tauri Contributors. CC-BY / MIT
