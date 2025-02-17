Skip to content
# Node.js as a sidecar
In this guide we are going to package a Node.js application to a self contained binary to be used as a sidecar in a Tauri application without requiring the end user to have a Node.js installation. This example tutorial is applicable for desktop operating systems only.
We recommend reading the general sidecar guide first for a deeper understanding of how Tauri sidecars work.
In this example we will create a Node.js application that reads input from the command line process.argv and writes output to stdout using console.log. You can leverage alternative inter-process communication systems such as a localhost server, stdin/stdout or local sockets. Note that each has their own advantages, drawbacks and security concerns.
## Prerequisites
An existing Tauri application set up with the shell plugin, that compiles and runs for you locally.
## Guide
  1. ##### Initialize Sidecar Project
Let’s create a new Node.js project to contain our sidecar implementation. Create a new directory **in your Tauri application root folder** (in this example we will call it `sidecar-app`) and run the `init` command of your preferred Node.js package manager inside the directory:
     * npm 
     * yarn 
     * pnpm 
```

npminit

```

```

yarninit

```

```

pnpminit

```

We will compile our Node.js application to a self container binary using pkg. Let’s install it as a development dependency:
     * npm 
     * yarn 
     * pnpm 
```

npmadd@yao-pkg/pkg--save-dev

```

```

yarnadd@yao-pkg/pkg--dev

```

```

pnpmadd@yao-pkg/pkg--save-dev

```

  2. ##### Write Sidecar Logic
Now we can start writing JavaScript code that will be executed by our Tauri application.
In this example we will process a command from the command line argmuents and write output to stdout, which means our process will be short lived and only handle a single command at a time. If your application must be long lived, consider using alternative inter-process communication systems.
Let’s create a `index.js` file in our `sidecar-app` directory and write a basic Node.js app:
sidecar-app/index.js```

const command = process.argv[2];
switch (command) {
case'ping':
const message = process.argv[3];
console.log(`pong, ${message}`);
break;
default:
console.error(`unknown command ${command}`);
process.exit(1);
}

```

  3. ##### Package the Sidecar
To package our Node.js application to a self contained binary, we can run the following `pkg` command:
     * npm 
     * yarn 
     * pnpm 
```

npmrunpkg----outputapp

```

```

yarnpkg--outputapp

```

```

pnpmpkg--outputapp

```

This will create the `sidecar-app/app` binary on Linux and macOS, and a `sidecar-app/app.exe` executable on Windows. To rename this file to the expected Tauri sidecar filename, we can use the following Node.js script:
```

import { execSync } from'child_process';
import fs from'fs';
const ext = process.platform === 'win32' ? '.exe' : '';
const rustInfo = execSync('rustc -vV');
const targetTriple =/host: (\S+)/g.exec(rustInfo)[1];
if (!targetTriple) {
console.error('Failed to determine platform target triple');
}
fs.renameSync(
`app${ext}`,
`../src-tauri/binaries/app-${targetTriple}${ext}`
);

```

  4. ##### Configure the Sidecar in the Tauri Application
Now that we have our Node.js application ready, we can connect it to our Tauri application by configuring the `bundle > externalBin` array:
src-tauri/tauri.conf.json```

{
"bundle": {
"externalBin": ["binaries/app"]
}
}

```

The Tauri CLI will handle the bundling of the sidecar binary as long as it exists as `src-tauri/binaries/app-<target-triple>`.
  5. ##### Execute the Sidecar
We can run the sidecar binary either from Rust code or directly from JavaScript.
     * JavaScript 
     * Rust 
Let’s execute the `ping` command in the Node.js sidecar directly:
```

import { Command } from'@tauri-apps/plugin-shell';
const message = 'Tauri';
const command = Command.sidecar('binaries/app', ['ping', message]);
const output = await command.execute();
const response = output.stdout;

```

Let’s pipe a `ping` Tauri command to the Node.js sidecar:
```

#[tauri::command]
asyncfnping(app: tauri::AppHandle, message: String) -> String {
letsidecar_command=app
.shell()
.sidecar("app")
.unwrap()
.arg("ping")
.arg(message);
letoutput=sidecar_command.output().unwrap();
letresponse= String::from_utf8(output.stdout).unwrap();
response
}

```



© 2025 Tauri Contributors. CC-BY / MIT
