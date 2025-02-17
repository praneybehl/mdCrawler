Skip to content
# Flathub
For detailed information on how Flatpak works, you can read Building your first Flatpak
This guide assumes you want to distribute your Flatpak via Flathub, the most commonly used platform for Flatpak distribution. If you plan on using other platforms, please consult their documentation instead.
## Prerequisites
To test your app inside the Flatpak runtime you can build the Flatpak locally first before uploading your app to Flathub. This can also be helpful if you want to quickly share development builds.
**1. Install`flatpak` and `flatpak-builder`**
To build Flatpaks locally you need the `flatpak` and `flatpak-builder` tools. For example on Ubuntu you can run this command:
  * Debian 
  * Arch 
  * Fedora 
  * Gentoo 


Terminal window```

sudoaptinstallflatpakflatpak-builder

```

Terminal window```

sudopacman-S--neededflatpakflatpak-builder

```

Terminal window```

sudodnfinstallflatpakflatpak-builder

```

Terminal window```

sudoemerge--ask\
sys-apps/flatpak \
dev-util/flatpak-builder

```

**2. Install the Flatpak Runtime**
Terminal window```

flatpakinstallflathuborg.gnome.Platform//46org.gnome.Sdk//46

```

**3.Build the .deb of your tauri-app**
**4. Create the manifest**
```

id: org.your.id
runtime: org.gnome.Platform
runtime-version: '46'
sdk: org.gnome.Sdk
command: tauri-app
finish-args:
- --socket=wayland# Permission needed to show the window
- --socket=fallback-x11# Permission needed to show the window
- --device=dri# OpenGL, not necessary for all projects
- --share=ipc
modules:
- name: binary
buildsystem: simple
sources:
- type: file
url: https://github.com/your_username/your_repository/releases/download/v1.0.1/yourapp_1.0.1_amd64.deb
sha256: 08305b5521e2cf0622e084f2b8f7f31f8a989fc7f407a7050fa3649facd61469# This is required if you are using a remote source
only-arches: [x86_64] #This source is only used on x86_64 Computers
# This path points to the binary file which was created in the .deb bundle.
# Tauri also creates a folder which corresponds to the content of the unpacked .deb.
build-commands:
- ar -x *.deb
- tar -xf data.tar.gz
- 'install -Dm755 usr/bin/tauri-app /app/bin/tauri-app'
- install -Dm644 usr/share/applications/yourapp.desktop /app/share/applications/org.your.id.desktop
- install -Dm644 usr/share/icons/hicolor/128x128/apps/yourapp.png /app/share/icons/hicolor/128x128/apps/org.your.id.png
- install -Dm644 usr/share/icons/hicolor/32x32/apps/yourapp.png /app/share/icons/hicolor/32x32/apps/org.your.id.png
- install -Dm644 usr/share/icons/hicolor/256x256@2/apps/yourapp.png /app/share/icons/hicolor/256x256@2/apps/org.your.id.png
- install -Dm644 org.your.id.metainfo.xml /app/share/metainfo/org.your.id.rosary.metainfo.xml

```

The Gnome 46 runtime includes all dependencies of the standard Tauri app with their correct versions.
**5. Install, and Test the app**
Terminal window```

# Install the flatpak
flatpak-y--userinstall<localreponame><yourflatpakid>
# Run it
flatpakrun<yourflatpakid>
# Update it
flatpak-y--userupdate<yourflatpakid>

```

## Adding additional libraries
If your final binary requires more libraries than the default tauri app, you need to add them in your flatpak manifest. There are two ways to do this. For fast local development, it may work to simply include the already built library file (`.so`) from your local system. However, this is not recommended for the final build of the flatpak, as your local library file is not built for the flatpak runtime environment. This can introduce various bugs that can be very hard to find. Therefore, it is recommended to build the library your program depends on from source inside the flatpak as a build step.
## Submitting to flathub
**_1. Fork TheFlathub Repository_**
**_2. Clone the Fork_**
Terminal window```

gitclone--branch=new-prgit@github.com:your_github_username/flathub.git

```

**_3. Enter the repository_**
Terminal window```

cdflathub

```

**_4. Create a new branch_**
Terminal window```

gitcheckout-byour_app_name

```

**_5. Add your apps manifest to the branch. Commit your changes, and then push them._**
**_6. Open a pull request against the`new-pr` branch on github_**
**_7. Your app will now enter the review process in which you may be asked to make changes to your project._**
When your pull request is approved then you will receive an invitation to edit your apps repository. From here on you can update your app continuously.
You can read more about this in the flatpak documentation
© 2025 Tauri Contributors. CC-BY / MIT
