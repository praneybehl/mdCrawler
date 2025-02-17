Skip to content
# Create a Project
One thing that makes Tauri so flexible is its ability to work with virtually any frontend framework. We’ve created the `create-tauri-app` utility to help you create a new Tauri project using one of the officially maintained framework templates.
`create-tauri-app` currently includes templates for vanilla (HTML, CSS and JavaScript without a framework), Vue.js, Svelte, React, SolidJS, Angular, Preact, Yew, Leptos, and Sycamore. You can also find or add your own community templates and frameworks in the Awesome Tauri repo.
Alternatively, you can add Tauri to an existing project to quickly turn your existing codebase into a Tauri app.
## Using `create-tauri-app`
To get started using `create-tauri-app` run one of the below commands in the folder you’d like to setup your project. If you’re not sure which command to use we recommend the Bash command on Linux and macOS and the PowerShell command on Windows.
  * Bash 
  * PowerShell 
  * npm 
  * Yarn 
  * pnpm 
  * deno 
  * bun 
  * Cargo 


```

sh<(curl https://create.tauri.app/sh)

```

```

irmhttps://create.tauri.app/ps|iex

```

```

npmcreatetauri-app@latest

```

```

yarncreatetauri-app

```

```

pnpmcreatetauri-app

```

```

denorun-Anpm:create-tauri-app

```

```

buncreatetauri-app

```

```

cargoinstallcreate-tauri-app--locked
cargocreate-tauri-app

```

Follow along with the prompts to choose your project name, frontend language, package manager, and frontend framework, and frontend framework options if applicable.
#### Scaffold a new project
  1. Choose a name and a bundle identifier (unique-id for your app):
```

? Project name (tauri-app) ›
? Identifier (com.tauri-app.app) ›

```

  2. Select a flavor for your frontend. First the language:
```

? Choose which language to use for your frontend ›
Rust (cargo)
TypeScript / JavaScript (pnpm, yarn, npm, bun)
.NET (dotnet)

```

  3. Select a package manager (if there are multiple available):
Options for **TypeScript / JavaScript** :
```

? Choose your package manager ›
pnpm
yarn
npm
bun

```

  4. Select a UI Template and flavor (if there are multiple available):
Options for **Rust** :
```

? Choose your UI template ›
Vanilla
Yew
Leptos
Sycamore

```

Options for **TypeScript / JavaScript** :
```

? Choose your UI template ›
Vanilla
Vue
Svelte
React
Solid
Angular
Preact
? Choose your UI flavor ›
TypeScript
JavaScript

```

Options for **.NET** :
```

? Choose your UI template ›
Blazor (https://dotnet.microsoft.com/en-us/apps/aspnet/web-apps/blazor/)

```



Once completed, the utility reports that the template has been created and displays how to run it using the configured package manager. If it detects missing dependencies on your system, it prints a list of packages and prompts how to install them.
#### Start the development server
After `create-tauri-app` has complete you can navigate into your project’s folder, install dependencies, then use the Tauri CLI to start the development server:
  * npm 
  * yarn 
  * pnpm 
  * deno 
  * bun 
  * cargo 


```

cdtauri-app
npminstall
npmruntauridev

```

```

cdtauri-app
yarninstall
yarntauridev

```

```

cdtauri-app
pnpminstall
pnpmtauridev

```

```

cdtauri-app
denoinstall
denotasktauridev

```

```

cdtauri-app
buninstall
buntauridev

```

```

cdtauri-app
cargotauridev

```

You’ll now see a new window open with your app running.
**Congratulations!** You’ve made your Tauri app! 🚀
## Manual Setup (Tauri CLI)
If you already have an existing frontend or prefer to set it up yourself, you can use the Tauri CLI to initialize the backend for your project separately.
  1. Create a new directory for your project and initialize the frontend. You can use plain HTML, CSS, and JavaScript, or any framework you prefer such as Next.js, Nuxt, Svelte, Yew, or Leptos. You just need a way of serving the app in your browser. Just as an example, this is how you would setup a simple Vite app:
     * npm 
     * yarn 
     * pnpm 
     * deno 
     * bun 
```

mkdirtauri-app
cdtauri-app
npmcreatevite@latest.

```

```

mkdirtauri-app
cdtauri-app
yarncreatevite.

```

```

mkdirtauri-app
cdtauri-app
pnpmcreatevite.

```

```

mkdirtauri-app
cdtauri-app
denorun-Anpm:create-vite.

```

```

mkdirtauri-app
cdtauri-app
buncreatevite

```

  2. Then, install Tauri’s CLI tool using your package manager of choice. If you are using `cargo` to install the Tauri CLI, you will have to install it globally.
     * npm 
     * yarn 
     * pnpm 
     * deno 
     * bun 
     * cargo 
```

npminstall-D@tauri-apps/cli@latest

```

```

yarnadd-D@tauri-apps/cli@latest

```

```

pnpmadd-D@tauri-apps/cli@latest

```

```

denoadd-Dnpm:@tauri-apps/cli@latest

```

```

bunadd-D@tauri-apps/cli@latest

```

```

cargoinstalltauri-cli--version"^2.0.0"--locked

```

  3. Determine the URL of your frontend development server. This is the URL that Tauri will use to load your content. For example, if you are using Vite, the default URL is `http://localhost:5173`.
  4. In your project directory, initialize Tauri:
     * npm 
     * yarn 
     * pnpm 
     * deno 
     * bun 
     * cargo 
```

npxtauriinit

```

```

yarntauriinit

```

```

pnpmtauriinit

```

```

denotasktauriinit

```

```

buntauriinit

```

```

cargotauriinit

```

After running the command it will display a prompt asking you for different options:
```

✔Whatisyourappname?tauri-app
✔Whatshouldthewindowtitlebe?tauri-app
✔Whereareyourwebassetslocated?..
✔Whatistheurlofyourdevserver?http://localhost:5173
✔Whatisyourfrontenddevcommand?pnpmrundev
✔Whatisyourfrontendbuildcommand?pnpmrunbuild

```

This will create a `src-tauri` directory in your project with the necessary Tauri configuration files.
  5. Verify your Tauri app is working by running the development server:
     * npm 
     * yarn 
     * pnpm 
     * deno 
     * bun 
     * cargo 
```

npxtauridev

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

buntauridev

```

```

cargotauridev

```

This command will compile the Rust code and open a window with your web content.


**Congratulations!** You’ve created a new Tauri project using the Tauri CLI! 🚀
## Next Steps
  * Add and Configure a Frontend Framework
  * Tauri Command Line Interface (CLI) Reference
  * Learn how to build your Tauri app
  * Discover additional features to extend Tauri


© 2025 Tauri Contributors. CC-BY / MIT
