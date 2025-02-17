Skip to content
# Windows Code Signing
Code signing is required on Windows to allow your application to be listed in the Microsoft Store and to prevent a SmartScreen warning that your application is not trusted and can not be started, when downloaded from the browser.
It is not required to execute your application on Windows, as long as your end user is okay with ignoring the SmartScreen warning or your user does not download via the browser. This guide covers signing via OV (Organization Validated) certificates and Azure Key Vault. If you use any other signing mechanism not documented here, such as EV (Extended Validation) certificates, check out your certificate issuer documentation and refer to the custom sign command section.
## OV Certificates
### Prerequisites
  * Windows - you can likely use other platforms, but this tutorial uses Powershell native features.
  * A working Tauri application
  * Code signing certificate - you can acquire one of these on services listed in Microsoft’s docs. There are likely additional authorities for non-EV certificates than included in that list, please compare them yourself and choose one at your own risk. 
    * Please make sure to get a **code signing** certificate, SSL certificates do not work!


### Getting Started
There are a few things we have to do to get Windows prepared for code signing. This includes converting our certificate to a specific format, installing this certificate, and decoding the required information from the certificate.
  1. #### Convert your `.cer` to `.pfx`
     * You will need the following:
       * certificate file (mine is `cert.cer`)
       * private key file (mine is `private-key.key`)
     * Open up a command prompt and change to your current directory using `cd Documents/Certs`
     * Convert your `.cer` to a `.pfx` using `openssl pkcs12 -export -in cert.cer -inkey private-key.key -out certificate.pfx`
     * You should be prompted to enter an export password **DON’T FORGET IT!**
  2. #### Import your `.pfx` file into the keystore.
     * We now need to import our `.pfx` file.
     * Assign your export password to a variable using `$WINDOWS_PFX_PASSWORD = 'MYPASSWORD'`
     * Now Import the certificate using `Import-PfxCertificate -FilePath certificate.pfx -CertStoreLocation Cert:\CurrentUser\My -Password (ConvertTo-SecureString -String $WINDOWS_PFX_PASSWORD -Force -AsPlainText)`
  3. #### Prepare Variables
     * Start ➡️ `certmgr.msc` to open Personal Certificate Management, then open Personal/Certificates.
     * Find the certificate we just imported and double-click on it, then click on the Details tab.
     * The Signature hash algorithm will be our `digestAlgorithm`. (Hint: this is likely `sha256`)
     * Scroll down to Thumbprint. There should be a value like `A1B1A2B2A3B3A4B4A5B5A6B6A7B7A8B8A9B9A0B0`. This is our `certificateThumbprint`.
     * We also need a timestamp URL; this is a time server used to verify the time of the certificate signing. I’m using `http://timestamp.comodoca.com`, but whoever you got your certificate from likely has one as well.


### Prepare `tauri.conf.json` file
  1. Now that we have our `certificateThumbprint`, `digestAlgorithm`, & `timestampUrl` we will open up the `tauri.conf.json`.
  2. In the `tauri.conf.json` you will look for the `tauri` -> `bundle` -> `windows` section. There are three variables for the information we have captured. Fill it out like below.


```

"windows": {
"certificateThumbprint": "A1B1A2B2A3B3A4B4A5B5A6B6A7B7A8B8A9B9A0B0",
"digestAlgorithm": "sha256",
"timestampUrl": "http://timestamp.comodoca.com"
}

```

  1. Save and run `tauri build`
  2. In the console output, you should see the following output.


```

info: signing app
info: running signtool "C:\\Program Files (x86)\\Windows Kits\\10\\bin\\10.0.19041.0\\x64\\signtool.exe"
info: "Done Adding Additional Store\r\nSuccessfully signed: APPLICATION FILE PATH HERE

```

Which shows you have successfully signed the `.exe`.
And that’s it! You have successfully set up your Tauri application for Windows signing.
### Sign your application with GitHub Actions.
We can also create a workflow to sign the application with GitHub actions.
#### GitHub Secrets
We need to add a few GitHub secrets for the proper configuration of the GitHub Action. These can be named however you would like.
  * You can view the encrypted secrets guide on how to add GitHub secrets.


The secrets we used are as follows
GitHub Secrets| Value for Variable  
---|---  
WINDOWS_CERTIFICATE| Base64 encoded version of your .pfx certificate, can be done using this command `certutil -encode certificate.pfx base64cert.txt`  
WINDOWS_CERTIFICATE_PASSWORD| Certificate export password used on creation of certificate .pfx  
#### Workflow Modifications
  1. We need to add a step in the workflow to import the certificate into the Windows environment. This workflow accomplishes the following
    1. Assign GitHub secrets to environment variables
    2. Create a new `certificate` directory
    3. Import `WINDOWS_CERTIFICATE` into tempCert.txt
    4. Use `certutil` to decode the tempCert.txt from base64 into a `.pfx` file.
    5. Remove tempCert.txt
    6. Import the `.pfx` file into the Cert store of Windows & convert the `WINDOWS_CERTIFICATE_PASSWORD` to a secure string to be used in the import command.
  2. We will be using the `tauri-action` publish template.


```

name: 'publish'
on:
push:
branches:
- release
jobs:
publish-tauri:
strategy:
fail-fast: false
matrix:
platform: [macos-latest, ubuntu-latest, windows-latest]
runs-on: ${{ matrix.platform }}
steps:
- uses: actions/checkout@v2
- name: setup node
uses: actions/setup-node@v1
with:
node-version: 12
- name: install Rust stable
uses: actions-rs/toolchain@v1
with:
toolchain: stable
- name: install webkit2gtk (ubuntu only)
if: matrix.platform == 'ubuntu-latest'
run: |
sudo apt-get update
sudo apt-get install -y webkit2gtk-4.0
- name: install app dependencies and build it
run: yarn && yarn build
- uses: tauri-apps/tauri-action@v0
env:
GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
with:
tagName: app-v__VERSION__# the action automatically replaces \_\_VERSION\_\_ with the app version
releaseName: 'App v__VERSION__'
releaseBody: 'See the assets to download this version and install.'
releaseDraft: true
prerelease: false

```

  1. Right above `-name: install app dependencies and build it` you will want to add the following step


```

- name: import windows certificate
if: matrix.platform == 'windows-latest'
env:
WINDOWS_CERTIFICATE: ${{ secrets.WINDOWS_CERTIFICATE }}
WINDOWS_CERTIFICATE_PASSWORD: ${{ secrets.WINDOWS_CERTIFICATE_PASSWORD }}
run: |
New-Item -ItemType directory -Path certificate
Set-Content -Path certificate/tempCert.txt -Value $env:WINDOWS_CERTIFICATE
certutil -decode certificate/tempCert.txt certificate/certificate.pfx
Remove-Item -path certificate -include tempCert.txt
Import-PfxCertificate -FilePath certificate/certificate.pfx -CertStoreLocation Cert:\CurrentUser\My -Password (ConvertTo-SecureString -String $env:WINDOWS_CERTIFICATE_PASSWORD -Force -AsPlainText)

```

  1. Save and push to your repo.
  2. Your workflow can now import your windows certificate and import it into the GitHub runner, allowing for automated code signing!


## Azure Key Vault
You can sign the Windows executables by providing an Azure Key Vault certificate and credentials.
  1. Key Vault


In the Azure Portal navigate to the Key vaults service to create a new key vault by clicking the “Create” button. Remember the “Key vault name” as you will need that information to configure the certificate URL.
  1. Certificate


After creating a key vault, select it and go to the “Objects > Certificates” page to create a new certificate and click the “Generate/Import” button. Remember the “Certificate name” as you will need that information to configure the certificate URL.
  1. Tauri Configuration


relic uses a configuration file to determine which signing key it should use. For Azure Key Vault you also need the certificate URL. Create a `relic.conf` file in the `src-tauri` folder and configure relic to use your certificate:
src-tauri/relic.conf```

tokens:
azure:
type: azure
keys:
azure:
token: azure
id: https://\<KEY_VAULT_NAME\>.vault.azure.net/certificates/\<CERTIFICATE_NAME\>

```

Note that you must replace <KEY_VAULT_NAME> and <CERTIFICATE_NAME> with the appropriate names from the previous steps.
To configure Tauri to use your Azure Key Vault configuration for signing change the bundle > windows > signCommand config value:
tauri.conf.json```

{
"bundle": {
"windows": {
"signCommand": "relic sign --file %1 --key azure --config relic.conf"
}
}
}

```

  1. Credentials


relic must authenticate with Azure in order to load the certificate. In the Azure portal landing page, go to the “Microsoft Entra ID” service and head to the “Manage > App registrations” page. Click “New registration” to create a new app. After creating the app, you are redirected to the application details page where you can see the “Application (client) ID” and “Directory (tenant) ID” values. Set these IDs to the `AZURE_CLIENT_ID` and `AZURE_TENANT_ID` environment variables respectively.
In the “Manage > Certificates & secrets” page click the “New client secret” button and set the text in the “Value” column as the `AZURE_CLIENT_SECRET` environment variable.
After setting up all the credentials, head back to your key vault’s page and navigate to the “Access control (IAM)” page. You must assign the “Key Vault Certificate User” and “Key Vault Crypto User” roles to your newly created application.
After setting up all these variables, running `tauri build` will produce signed Windows installers!
## Custom Sign Command
In the Azure Key Vault documentation above we used a powerful Tauri Windows signing configuration to force the Tauri CLI to use a special shell command to sign Windows installer executables. The bundle > windows > signCommand configuration option can be used to use any codesign tool that can sign Windows executables.
## Azure Code Signing
You can sign the Windows executables by providing an Azure Code signing certificate and credentials. If you don’t have an Azure Code signing Account yet you can follow this tutorial.
### Prerequisites
If you want to sign with Github Actions everything should be installed.
  1. Trusted Signing Account and permissions configured
  2. .NET (.NET 6 or later recommended)
  3. Azure CLI
  4. Signtool (Windows 11 SDK 10.0.22000.0 or later recommended)


### Getting Started
You need to install trusted-signing-cli and configure your environment variables.
  1. #### Install trusted-signing-cli
     * `cargo install trusted-signing-cli`
  2. #### Configure environment variables
     * trusted-signing-cli needs the following environment variables to be set, don’t forget to add these as Github Actions secrets:
       * `AZURE_CLIENT_ID`: The client ID of your App Registration
       * `AZURE_CLIENT_SECRET`: The client secret of App Registration
       * `AZURE_TENANT_ID`: The tenant ID of your Azure directory, you can also get this from your App Registration
  3. ### Modify your `tauri.conf.json` file
     * You can modify your `tauri.conf.json` or you can create a specific config file for Windows. Replace the URL and the certificate name with your own values.
       * -e: The endpoint of your Azure Code Signing account
       * -a: The name of your Azure Code Signing Account
       * -c: The name of your Certificate profile inside your Azure Code Signing Account
tauri.conf.json```

{
"bundle": {
"windows": {
"signCommand": "trusted-signing-cli -e https://wus2.codesigning.azure.net -a MyAccount -c MyProfile %1"
}
}
}

```



© 2025 Tauri Contributors. CC-BY / MIT
