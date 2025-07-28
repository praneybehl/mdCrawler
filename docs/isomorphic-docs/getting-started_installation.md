Skip to main content
Version: v7.0.0
On this page
## Requirements​
Before you begin, ensure that your computer has the following software installed.
  * `nodejs` ( 20.16.0 or late ) https://nodejs.org/en
  * `pnpm` Node package manager https://pnpm.io/ ( recommended )
  * `Visual Studio Code` https://code.visualstudio.com/ ( recommended )


## Installation​
Before initiating the installation process, ensure all required environment variables are added.
#### Setting Environment Variables​
Open your terminal, navigate to the `apps -> isomorphic`, `apps -> isomorphic-intl` or `apps -> isomorphic-starter` individually of the project and execute the following command.
```
cp .env.local.example .env.local
```

This command copies the provided example file for local environment variables. Now, proceed to fill in the values for the following environmental variables in the newly created `.env.local` file.
`NEXT_PUBLIC_GOOGLE_MAP_API_KEY` is optional unless you're utilizing Google Maps. If you plan to integrate Google Maps into your project, obtain your API key from this link and assign it to `NEXT_PUBLIC_GOOGLE_MAP_API_KEY` in your environment variables.
`NEXTAUTH_SECRET` Open your terminal in mac/linux and enter the following command and it will generates a random 32-character base64-encoded string using OpenSSL. If your are a Windows user you can generate from here https://generate-secret.vercel.app/32
```
openssl rand -base6432
```

`NEXTAUTH_URL` should be set to your project's base URL. During development, it commonly defaults to http://localhost:3000. However, in a production environment, ensure to update it to match the URL of your deployed application.
`GOOGLE_CLIENT_ID` is your project's Google API client ID. During development, use a test ID, and for production, obtain the official ID from the Google Developer Console (https://console.developers.google.com/). This ID is essential for authenticating with Google services in your application.
`GOOGLE_CLIENT_SECRET` is your project's confidential key for secure communication with the Google API. During development, use a test secret; for production, obtain the official one from the Google Developer Console (https://console.developers.google.com/). This key is essential for authenticating and authorizing your application with Google services.
Once you've completed the aforementioned steps, you can execute the following commands in the terminal/command prompt from the project's root directory.
Command| Description  
---|---  
`pnpm install`| This process will install all the necessary dependencies into the `node_modules` folder.  
`pnpm dev`| It launches all of your workspaces parallelly. Initiates the development server, and monitors any changes in your code. You can access the development server at `http://localhost:3000`, `http://localhost:3001`, `http://localhost:3002`, `http://localhost:3003`.  
## Available Scripts​
These commands will take effect on all workspaces parallelly.
Command| Description  
---|---  
`pnpm lint`| This command will check for eslint configurations, validation. And will through an warning if anywhere inside this package the code not meets the configurations.  
`pnpm build`| This command will build all of your workspaces parallelly. And create a .next folder inside every workspace.  
`pnpm start`| It will run the local build files at `http://localhost:3000`, `http://localhost:3001`, `http://localhost:3002`, `http://localhost:3003`.  
`pnpm clean`| This command removes all the node_modules, .next .cache folder from root or inside workspaces.  
info
**Individual workspace commands are also available. You can find them below.**
## Isomorphic workspace​
These commands will only take effect on the main isomorphic workspace.
Command| Description  
---|---  
`pnpm iso:dev`| It's only launches the main isomorphic workspace, initiates the development server, and monitors any changes in your code. You can access the development server at `http://localhost:3000`  
`pnpm iso:lint`| This command typically checks your code for syntax and ensuring it adheres to predefined coding standards and best practices.  
`pnpm iso:build`| This command is used to create an optimized production build of your application. This command creates a `.next` folder in which it compiles your project, bundles the JavaScript files, and optimizes assets for production deployment.  
`pnpm iso:start`| The command is used to start the application in production mode. This means that it serves the optimized build. Which you can view locally at port `http://localhost:3000`.  
`pnpm iso:clean`| This command removes node_modules, .next .cache .turbo folder from the isomorphic workspaces.  
## Isomorphic intl workspace​
These commands will only take effect on the isomorphic-intl workspace.
Command| Description  
---|---  
`pnpm intl:dev`| It's only launches the isomorphic-intl workspace, initiates the development server, and monitors any changes in your code. You can access the development server at `http://localhost:3001`  
`pnpm intl:lint`| This command typically checks your code for syntax and ensuring it adheres to predefined coding standards and best practices.  
`pnpm intl:build`| This command is used to create an optimized production build of your application. This command creates a `.next` folder in which it compiles your project, bundles the JavaScript files, and optimizes assets for production deployment.  
`pnpm intl:start`| The command is used to start the application in production mode. This means that it serves the optimized build. Which you can view locally at port `http://localhost:3001`.  
`pnpm intl:clean`| This command removes node_modules, .next .cache .turbo folder from the isomorphic-intl workspaces.  
## Isomorphic starter workspace​
These commands will only take effect on the isomorphic-starter workspace.
Command| Description  
---|---  
`pnpm starter:dev`| It's only launches the isomorphic-starter workspace, initiates the development server, and monitors any changes in your code. You can access the development server at `http://localhost:3002`  
`pnpm starter:lint`| This command typically checks your code for syntax and ensuring it adheres to predefined coding standards and best practices.  
`pnpm starter:build`| This command is used to create an optimized production build of your application. This command creates a `.next` folder in which it compiles your project, bundles the JavaScript files, and optimizes assets for production deployment.  
`pnpm starter:start`| The command is used to start the application in production mode. This means that it serves the optimized build. Which you can view locally at port `http://localhost:3002`.  
`pnpm starter:clean`| This command removes node_modules, .next .cache .turbo folder from the isomorphic-starter workspaces.  
## Isomorphic dnd workspace​
These commands will only take effect on the isomorphic-dnd workspace.
Command| Description  
---|---  
`pnpm dnd:dev`| It's only launches the isomorphic-dnd workspace, initiates the development server, and monitors any changes in your code. You can access the development server at `http://localhost:3003`  
`pnpm dnd:lint`| This command typically checks your code for syntax and ensuring it adheres to predefined coding standards and best practices.  
`pnpm dnd:build`| This command is used to create an optimized production build of your application. This command creates a `.next` folder in which it compiles your project, bundles the JavaScript files, and optimizes assets for production deployment.  
`pnpm dnd:start`| The command is used to start the application in production mode. This means that it serves the optimized build. Which you can view locally at port `http://localhost:3003`.  
`pnpm dnd:clean`| This command removes node_modules, .next .cache .turbo folder from the isomorphic-dnd workspaces.  
## More Scripts​
Some more custom commands are available for different uses cases. You can find them below.
Command| Description  
---|---  
`pnpm cache:clean`| Remove all cache and build files named `.turbo`, `.build` & `.cache`  
`pnpm add react --filter=isomorphic`| You can use this command structure for installing packages into individual workspaces. Learn More  
`pnpm gen-icons`| This command will generate icons data from icons store `packages/isomorphic-core/src/components/icons` into `data/icons-data.ts` file  
  * Requirements
  * Installation
  * Available Scripts
  * Isomorphic workspace
  * Isomorphic intl workspace
  * Isomorphic starter workspace
  * Isomorphic dnd workspace
  * More Scripts


