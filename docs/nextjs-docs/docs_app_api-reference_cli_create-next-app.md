# Your Privacy
This site uses tracking technologies. You may opt in or opt out of the use of these technologies.
DenyAccept all
Consent Settings
Privacy Policy
Your Privacy
This site uses tracking technologies. You may opt in or opt out of the use of these technologies.
Marketing
Off
Marketing cookies and services are used to deliver personalized advertisements, promotions, and offers. These technologies enable targeted advertising and marketing campaigns by collecting information about users' interests, preferences, and online activities. 
Analytics
Off
Analytics cookies and services are used for collecting statistical information about how visitors interact with a website. These technologies provide insights into website usage, visitor behavior, and site performance to understand and improve the site and enhance user experience.
Functional
Off
Functional cookies and services are used to offer enhanced and personalized functionalities. These technologies provide additional features and improved user experiences, such as remembering your language preferences, font sizes, region selections, and customized layouts. Opting out of these cookies may render certain services or functionality of the website unavailable.
Essential
On
Essential cookies and services are used to enable core website features, such as ensuring the security of the website. 
SaveDenyAccept all
Privacy Policy
Menu
Using App Router
Features available in /app
Using Latest Version
15.2.0
Using App Router
Features available in /app
Using Latest Version
15.2.0
API ReferenceCLIcreate-next-app
# create-next-app
The `create-next-app` CLI allow you to create a new Next.js application using the default template or an example from a public GitHub repository. It is the easiest way to get started with Next.js.
Basic usage:
Terminal
```
npxcreate-next-app@latest [project-name] [options]
```

## Reference
The following options are available:
Options| Description  
---|---  
`-h` or `--help`| Show all available options  
`-v` or `--version`| Output the version number  
`--no-*`| Negate default options. E.g. `--no-eslint`  
`--ts` or `--typescript`| Initialize as a TypeScript project (default)  
`--js` or `--javascript`| Initialize as a JavaScript project  
`--tailwind`| Initialize with Tailwind CSS config (default)  
`--eslint`| Initialize with ESLint config  
`--app`| Initialize as an App Router project  
`--api`| Initialize a project with only route handlers  
`--src-dir`| Initialize inside a `src/` directory  
`--turbopack`| Enable Turbopack by default for development  
`--import-alias <alias-to-configure>`| Specify import alias to use (default "@/*")  
`--empty`| Initialize an empty project  
`--use-npm`| Explicitly tell the CLI to bootstrap the application using npm  
`--use-pnpm`| Explicitly tell the CLI to bootstrap the application using pnpm  
`--use-yarn`| Explicitly tell the CLI to bootstrap the application using Yarn  
`--use-bun`| Explicitly tell the CLI to bootstrap the application using Bun  
`-e` or `--example [name] [github-url]`| An example to bootstrap the app with  
`--example-path <path-to-example>`| Specify the path to the example separately  
`--reset-preferences`| Explicitly tell the CLI to reset any stored preferences  
`--skip-install`| Explicitly tell the CLI to skip installing packages  
`--yes`| Use previous preferences or defaults for all options  
## Examples
### With the default template
To create a new app using the default template, run the following command in your terminal:
Terminal
```
npxcreate-next-app@latest
```

You will then be asked the following prompts:
Terminal
```
What is your project named? my-app
Would you like to use TypeScript? No / Yes
Would you like to use ESLint? No / Yes
Would you like to use Tailwind CSS? No / Yes
Would you like your code inside a `src/` directory? No / Yes
Would you like to use App Router? (recommended) No / Yes
Would you like to use Turbopack for `next dev`? No / Yes
Would you like to customize the import alias (`@/*` by default)? No / Yes
```

Once you've answered the prompts, a new project will be created with your chosen configuration.
### With an official Next.js example
To create a new app using an official Next.js example, use the `--example` flag. For example:
Terminal
```
npxcreate-next-app@latest--example [example-name] [your-project-name]
```

You can view a list of all available examples along with setup instructions in the Next.js repository.
### With any public GitHub example
To create a new app using any public GitHub example, use the `--example` option with the GitHub repo's URL. For example:
Terminal
```
npxcreate-next-app@latest--example"https://github.com/.../" [your-project-name]
```

Was this helpful?
supported.
Send
