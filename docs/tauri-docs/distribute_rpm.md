Skip to content
# RPM
# Packaging for RPM
This guide covers how to distribute and manage RPM packages, including retrieving package information, configuring scripts, setting dependencies, and signing packages.
## Configuring the RPM package
Tauri allows you to configure the RPM package by adding scripts, setting dependencies, adding a license, including custom files, and more. For detailed information about configurable options, please refer to: RpmConfig.
### Add post, pre-install/remove script to the package
The RPM package manager allows you to run scripts before or after the installation or removal of the package. For example, you can use these scripts to start a service after the package is installed.
Here’s an example of how to add these scripts:
  1. Create a folder named `scripts` in the `src-tauri` directory in your project.


Terminal window```

mkdirsrc-tauri/scripts

```

  1. Create the script files in the folder.


Terminal window```

touchsrc-tauri/scripts/postinstall.sh\
touch src-tauri/scripts/preinstall.sh\
touch src-tauri/scripts/preremove.sh\
touch src-tauri/scripts/postremove.sh

```

Now if we look inside `/src-tauri/scripts` we will see:
Terminal window```

lssrc-tauri/scripts/
postinstall.shpostremove.shpreinstall.shpreremove.sh

```

  1. Add some content to the scripts


preinstall.sh```

echo"-------------"
echo"This is pre"
echo"Install Value: $1"
echo"Upgrade Value: $1"
echo"Uninstall Value: $1"
echo"-------------"

```

postinstall.sh```

echo"-------------"
echo"This is post"
echo"Install Value: $1"
echo"Upgrade Value: $1"
echo"Uninstall Value: $1"
echo"-------------"

```

preremove.sh```

echo"-------------"
echo"This is preun"
echo"Install Value: $1"
echo"Upgrade Value: $1"
echo"Uninstall Value: $1"
echo"-------------"

```

postremove.sh```

echo"-------------"
echo"This is postun"
echo"Install Value: $1"
echo"Upgrade Value: $1"
echo"Uninstall Value: $1"
echo"-------------"

```

  1. Add the scripts to the`tauri.conf.json` file


tauri.conf.json```

{
"bundle": {
"linux": {
"rpm": {
"epoch": 0,
"files": {},
"release": "1",
// add the script here
"preInstallScript": "/path/to/your/project/src-tauri/scripts/prescript.sh",
"postInstallScript": "/path/to/your/project/src-tauri/scripts/postscript.sh",
"preRemoveScript": "/path/to/your/project/src-tauri/scripts/prescript.sh",
"postRemoveScript": "/path/to/your/project/src-tauri/scripts/postscript.sh"
}
}
}
}

```

### Setting the Conflict, Provides, Depends, Files, Obsoletes, DesktopTemplate, and Epoch
  * **conflict** : Prevents the installation of the package if it conflicts with another package. For example, if you update an RPM package that your app depends on and the new version is incompatible with your app.
  * **provides** : Lists the RPM dependencies that your application provides.
  * **depends** : Lists the RPM dependencies that your application needs to run.
  * **files** : Specifies which files to include in the package.
  * **obsoletes** : Lists the RPM dependencies that your application obsoletes.


  * **desktopTemplate** : Adds a custom desktop file to the package.
  * **epoch** : Defines weighted dependencies based on version numbers.


To use these options, add the following to your `tauri.conf.json` :
tauri.conf.json```

{
"bundle": {
"linux": {
"rpm": {
"postRemoveScript": "/path/to/your/project/src-tauri/scripts/postscript.sh",
"conflicts": ["oldLib.rpm"],
"depends": ["newLib.rpm"],
"obsoletes": ["veryoldLib.rpm"],
"provides": ["coolLib.rpm"],
"desktopTemplate": "/path/to/your/project/src-tauri/desktop-template.desktop"
}
}
}
}

```

### Add a license to the package
To add a license to the package, add the following to the `src-tauri/cargo.toml` or in the `src-tauri/tauri.conf.json` file:
src-tauri/cargo.toml```

[package]
name = "tauri-app"
version = "0.0.0"
description = "A Tauri App"
authors = ["you"]
edition = "2021"
license = "MIT"# add the license here
# ... rest of the file

```

And for `src-tauri/tauri.conf.json`
src-tauri/tauri.conf.json```

{
"bundle": {
"licenseFile": "../LICENSE", // put the path to the license file here
"license": "MIT"// add the license here
}
}

```

## Building the RPM package
To build the RPM package, you can use the following command:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauribuild

```

```

yarntauribuild

```

```

pnpmtauribuild

```

```

denotasktauribuild

```

```

cargotauribuild

```

This command will build the RPM package in the `src-tauri/target/release/bundle/rpm` directory.
## Signing the RPM package
Tauri allows you to sign the package with the key you have in your system during the build process. To do this, you will need to generate a GPG key.
#### Generate a GPG key
To generate a GPG key you can use the following command:
Terminal window```

gpg--gen-key

```

Follow the instruction to generate the key.
Once the key is generated, you will need to add it to your environment variable. You can do this by adding the following to your .bashrc or .zshrc file or just export it in the terminal:
Terminal window```

exportTAURI_SIGNING_RPM_KEY=$(cat/home/johndoe/my_super_private.key)

```

If you have a passphrase for the key, you can add it to the environment variable:
Terminal window```

exportTAURI_SIGNING_RPM_KEY_PASSPHRASE=password

```

Now you can build the package with the following command:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * cargo 


```

npmruntauribuild

```

```

yarntauribuild

```

```

pnpmtauribuild

```

```

denotasktauribuild

```

```

cargotauribuild

```

### Verify the signature
Before verifying the signature, you will need to create and import the public key to the RPM database:
Terminal window```

gpg--export-a'Tauri-App'>RPM-GPG-KEY-Tauri-App

```

Terminal window```

sudorpm--importRPM-GPG-KEY-Tauri-App

```

Now that the key is imported, we have to edit the `~/.rpmmacros` file to utilize the key.
~/.rpmmacros```

%_signaturegpg
%_gpg_path/home/johndoe/.gnupg
%_gpg_nameTauri-App
%_gpgbin/usr/bin/gpg2
%__gpg_sign_cmd%{__gpg}\
gpg--force-v3-sigs--digest-algo=sha1--batch--no-verbose--no-armor\
--passphrase-fd3--no-secmem-warning-u"%{_gpg_name}"\
-sbo%{__signature_filename}%{__plaintext_filename}

```

Finally, you can verify the package using the following command:
Terminal window```

rpm-v--checksigtauri-app-0.0.0-1.x86_64.rpm

```

## Debugging the RPM package
In this section, we will see how to debug the RPM package by checking the content of the package and getting information about the package.
### Getting information about the package
To get information about your package, such as the version, release, and architecture, use the following command:
Terminal window```

rpm-qippackage_name.rpm

```

### Query specific information about the package
For example, if you want to get the name, version, release, architecture, and size of the package, use the following command:
Terminal window```

rpm-qp--queryformat'[%{NAME} %{VERSION} %{RELEASE} %{ARCH} %{SIZE}\n]'package_name.rpm

```

### Checking the content of the package
To check the content of the package, use the following command:
Terminal window```

rpm-qlppackage_name.rpm

```

This command will list all the files that are included in the package.
### Debugging scripts
To debug post/pre-install/remove scripts, use the following command:
Terminal window```

rpm-qp--scriptspackage_name.rpm

```

This command will print the content of the scripts.
### Checking dependencies
To check the dependencies of the package, use the following command:
Terminal window```

rpm-qp--requirespackage_name.rpm

```

### List packages that depend on a specific package
To list the packages that depend on a specific package, use the following command:
Terminal window```

rpm-q--whatrequirespackage_name.rpm

```

### Debugging Installation Issues
If you encounter issues during the installation of an RPM package, you can use the `-vv` (very verbose) option to get detailed output:
Terminal window```

rpm-ivvhpackage_name.rpm

```

Or for an already installed package:
Terminal window```

rpm-Uvvhpackage_name.rpm

```

© 2025 Tauri Contributors. CC-BY / MIT
