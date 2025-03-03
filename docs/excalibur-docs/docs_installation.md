Skip to main content
On this page
First time here?
If this is your first time using Excalibur, we recommend you start with our Excalibird tutorial where you can learn Excalibur in the browser.
Prerequisite for NPM
Install node.js
NPM is the most common way to install Excalibur
```

sh
npm install excalibur@latest`
Copy
```
```

sh
npm install excalibur@latest`
Copy
```

But there are several ways you can start from scratch with Excalibur
  * From `npm` or `nuget`
  * Using a template from the Excalibur CLI
  * as ESM script, or old school JavaScript from downloaded scripts on our releases page
  * by using a script CDN - e.g. for working with `Deno`


## Start From a Template​
If you want to get up and running quickly with a familiar toolchain, we have several templates and samples available on GitHub. These examples allow you to simply clone and start building your game! They are also a great way to learn how to integrate Excalibur into your existing toolchain.
Check out the Excalibur CLI to spin up a template or sample quick!
### Templates​
  * Vite and TypeScript
  * Parcel 2 and TypeScript
  * Rollup and TypeScript
  * Webpack and TypeScript
  * Electron
  * Capacitor


### Samples​
  * Sample Platfomer
  * Sample Shootem-Up
  * Sample Brick Breaker


### Older Templates​
  * TypeScript, Angular2 & SystemJS
  * TypeScript & Browserify
  * Universal Windows Platform (UWP)
  * Apache Cordova
  * Xamarin Forms


## Starting from Scratch​
There are several ways you can start from scratch with Excalibur:
  * as standalone packages from `npm` or `nuget`
  * as raw script files you can download
  * by using a CDN - e.g. for working with `Deno`


note
Excalibur is a client-side library and cannot be used in a server-side Node.js, however it can be downloaded with npm.
### npm Package​
note
Best for JavaScript/TypeScript projects
If you’re using Node.js or intend to use Excalibur in a primarily JavaScript project, you can install it via npm.
With Node installed, run the following on the command-line:
```

bash
npm install excalibur
Copy
```
```

bash
npm install excalibur
Copy
```

This will add excalibur to your package.json as a project dependency and will create a folder structure like:
```

/node_modules
  /excalibur
    /build
      /dist
        excalibur.js
        excalibur.min.js
        excalibur.d.ts
        ...other files
Copy
```
```

/node_modules
  /excalibur
    /build
      /dist
        excalibur.js
        excalibur.min.js
        excalibur.d.ts
        ...other files
Copy
```

See below for how to reference these files in your project after Excalibur is installed.
View the excalibur package on npm.
tip
If you used `npm` to install Excalibur, you can use the `node_modules/excalibur/build/dist/excalibur.min.js` path above in the HTML. We recommend parcel for quick projects or webpack for more sophisticated projects. Read more about builds and bundlers
### ESM JavaScript​
Excalibur publishes an ESM build that you can use with modern ES module syntax.
```

html
<!DOCTYPEhtml>
<htmllang="en">
<head>
  <metacharset="UTF-8">
  <linkrel="icon"href="favicon.ico" />
  <metaname="viewport"content="width=device-width, initial-scale=1.0">
  <title>Excalibur Vanilla JS</title>
</head>
<body>
  <scripttype="importmap">
    {
      "imports": {
        "excalibur": "https://www.unpkg.com/excalibur@next/build/esm/excalibur.min.js"
      }
    }
  </script>
  <scripttype="module"src="src/game.js"></script>
</body>
</html>
Copy
```
```

html
<!DOCTYPEhtml>
<htmllang="en">
<head>
  <metacharset="UTF-8">
  <linkrel="icon"href="favicon.ico" />
  <metaname="viewport"content="width=device-width, initial-scale=1.0">
  <title>Excalibur Vanilla JS</title>
</head>
<body>
  <scripttype="importmap">
    {
      "imports": {
        "excalibur": "https://www.unpkg.com/excalibur@next/build/esm/excalibur.min.js"
      }
    }
  </script>
  <scripttype="module"src="src/game.js"></script>
</body>
</html>
Copy
```

### Old School JavaScript​
note
Best for quick prototypes or small projects
If you are using Excalibur in a script tag, unpkg provides a quick way to include published npm packages as scripts.
It is recommended you pin your version of excalibur to specific version like `excalibur@0.30.0`, however you can get the latest `https://unpkg.com/excalibur@latest`
```

html
<!DOCTYPEhtml>
<html>
 <head></head>
 <body>
  <scriptsrc="https://unpkg.com/excalibur@0.30.0"></script>
  <scriptsrc="./my-game.js"></script>
 </body>
</html>
Copy
```
```

html
<!DOCTYPEhtml>
<html>
 <head></head>
 <body>
  <scriptsrc="https://unpkg.com/excalibur@0.30.0"></script>
  <scriptsrc="./my-game.js"></script>
 </body>
</html>
Copy
```

You can also download the compiled script from Excalibur repository.
```

html
<!DOCTYPEhtml>
<html>
 <head></head>
 <body>
  <scriptsrc="excalibur.min.js"></script>
  <scriptsrc="./my-game.js"></script>
 </body>
</html>
Copy
```
```

html
<!DOCTYPEhtml>
<html>
 <head></head>
 <body>
  <scriptsrc="excalibur.min.js"></script>
  <scriptsrc="./my-game.js"></script>
 </body>
</html>
Copy
```

### Nuget Package​
note
Best for .NET projects
If you intend to use Excalibur in a primarily .NET-based project (like Xamarin, Windows 10, etc.), you can use Nuget.
With the .NET SDK installed, run the following on the command-line:
```

bash
Install-Package Excalibur
Copy
```
```

bash
Install-Package Excalibur
Copy
```

Nuget will automatically place the Excalibur files in the `Content/Scripts` folder of your project:
```

/Content
  /Scripts
    excalibur.js
    excalibur.min.js
    excalibur.d.ts
    ...other files
Copy
```
```

/Content
  /Scripts
    excalibur.js
    excalibur.min.js
    excalibur.d.ts
    ...other files
Copy
```

See below for how to reference these files in your project after Excalibur is installed.
View the Excalibur package on Nuget.
### Using a CDN​
If you want to use Excalibur in a `Deno` environment, use a content delivery network like `esm.sh` or `skypack.dev`. They transform our `NPM` package into an `ES Module`. That may sound complicated, but it's really just one line of code:
```

typescript
// index.ts
import { Engine } from'https://esm.sh/excalibur';
// and Tada!
constgame=newEngine();
game.start();
Copy
```
```

typescript
// index.ts
import { Engine } from'https://esm.sh/excalibur';
// and Tada!
constgame=newEngine();
game.start();
Copy
```

tip
To see the full instructions on setting up Excalibur with `Deno`, check out our `Deno` guide.
### Unstable Builds​
If you want to live on the edge and get the latest unreleased and possibly unstable builds, you can download -alpha `npm` packages.
The latest documentation for the Unstable Builds.
  * Start From a Template
    * Templates
    * Samples
    * Older Templates
  * Starting from Scratch
    * npm Package
    * ESM JavaScript
    * Old School JavaScript
    * Nuget Package
    * Using a CDN
    * Unstable Builds


