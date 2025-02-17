Skip to content
# Snapcraft
## Prerequisites
**1. Install`snap`**
  * Debian 
  * Arch 
  * Fedora 


Terminal window```

sudoaptinstallsnapd

```

Terminal window```

sudopacman-S--neededgitbase-devel
gitclonehttps://aur.archlinux.org/snapd.git
cdsnapd
makepkg-si
sudosystemctlenable--nowsnapd.socket
sudosystemctlstartsnapd.socket
sudosystemctlenable--nowsnapd.apparmor.service

```

Terminal window```

sudodnfinstallsnapd
# Enable classic snap support
sudoln-s/var/lib/snapd/snap/snap

```

Reboot your system afterwards.
**2. Install a base snap**
Terminal window```

sudosnapinstallcore22

```

**3. Install`snapcraft`**
Terminal window```

sudosnapinstallsnapcraft--classic

```

## Configuration
  1. Create an UbuntuOne account.
  2. Go to the Snapcraft website and register an App name.
  3. Create a snapcraft.yaml file in your projects root.
  4. Adjust the names in the snapcraft.yaml file.


```

name: appname
base: core22
version: '0.1.0'
summary: Your summary# 79 char long summary
description: |
Your description
grade: stable
confinement: strict
layout:
/usr/lib/$SNAPCRAFT_ARCH_TRIPLET/webkit2gtk-4.1:
bind: $SNAP/usr/lib/$SNAPCRAFT_ARCH_TRIPLET/webkit2gtk-4.1
apps:
appname:
command: usr/bin/appname
desktop: usr/share/applications/appname.desktop
extensions: [gnome]
#plugs:
# - network
# Add whatever plugs you need here, see https://snapcraft.io/docs/snapcraft-interfaces for more info.
# The gnome extension already includes [ desktop, desktop-legacy, gsettings, opengl, wayland, x11, mount-observe, calendar-service ]
package-repositories:
- type: apt
components: [main]
suites: [noble]
key-id: 78E1918602959B9C59103100F1831DDAFC42E99D
url: http://ppa.launchpad.net/snappy-dev/snapcraft-daily/ubuntu
parts:
build-app:
plugin: dump
build-snaps:
- node/20/stable
- rustup/latest/stable
build-packages:
- libwebkit2gtk-4.1-dev
- build-essential
- curl
- wget
- file
- libxdo-dev
- libssl-dev
- libayatana-appindicator3-dev
- librsvg2-dev
- dpkg
stage-packages:
- libwebkit2gtk-4.1-0
- libayatana-appindicator3-1
source: .
override-build: |
set -eu
npm install
npm run tauri build -- --bundles deb
dpkg -x src-tauri/target/release/bundle/deb/*.deb $SNAPCRAFT_PART_INSTALL/
sed -i -e "s|Icon=appname|Icon=/usr/share/icons/hicolor/32x32/apps/appname.png|g" $SNAPCRAFT_PART_INSTALL/usr/share/applications/appname.desktop

```

### Explanation
  * The `name` variable defines the name of your app and is required to be set to the name that you have registered earlier.
  * The `base` variable defines which core you are using.
  * The `version` variable defines the version, and should be updated with each change to the source repository.
  * The `apps` section allows you to expose the desktop and binary files to allow the user to run your app.
  * The `package-repositories` section allows you to add a package repository to help you satisfy your dependencies.
  * `build-packages`/`build-snaps` defines the build dependencies for your snap.
  * `stage-packages`/`stage-snaps` defines the runtime dependencies for your snap.
  * The `override-pull` section runs a series of commands before the sources are pulled.
  * `craftctl default` performs the default pull commands.
  * The `organize` section moves your files to the proper directories so that the binary and desktop file can be exposed to the `apps` sections.


## Building
Terminal window```

sudosnapcraft

```

## Testing
Terminal window```

snaprunyour-app

```

## Releasing Manually
Terminal window```

snapcraftlogin# Login with your UbuntuOne credentials
snapcraftupload--release=stablemysnap_latest_amd64.snap

```

## Building automatically
  1. On your apps developer page click on the `builds` tab.
  2. Click `login with github`.
  3. Enter in your repository’s details.


© 2025 Tauri Contributors. CC-BY / MIT
