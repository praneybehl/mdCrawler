🚀Generate, edit and deploy beautiful apps
HeroUI Chat
Getting Started
  * Introduction
  * Design Principles
  * Installation
  * CLI
  * Routing
  * Forms
Updated
  * NextUI to HeroUI
  * Figma


Frameworks
  * Next.js
  * Vite
  * Remix
  * Astro
  * Laravel


Customization
  * Theme
  * Layout
  * Colors
  * Customize theme
  * Create theme
  * Dark mode
  * Override styles
  * Custom variants


Components
  * Accordion
  * Autocomplete
  * Alert
  * Avatar
  * Badge
  * Breadcrumbs
  * Button
  * Calendar
  * Card
  * Checkbox
Updated
  * Checkbox Group
  * Chip
  * Circular Progress
  * Code
  * Date Input
  * Date Picker
  * Date Range Picker
  * Divider
  * Dropdown
  * Drawer
  * Form
  * Image
  * Input
Updated
  * Input OTP
Updated
  * Kbd
Updated
  * Link
  * Listbox
  * Modal
  * Navbar
  * Number Input
New
  * Pagination
  * Popover
  * Progress
  * Radio Group
Updated
  * Range Calendar
  * Scroll Shadow
  * Select
  * Skeleton
  * Slider
  * Snippet
  * Spacer
  * Spinner
Updated
  * Switch
  * Table
Updated
  * Tabs
Updated
  * Toast
New
  * Textarea
  * Time Input
  * Tooltip
  * User


API References
  * HeroUI CLI
  * HeroUIProvider
Updated


# HeroUI CLI
Here's the API reference for the `HeroUI CLI`.
Once the `CLI` is installed, run the following command to display available commands:
To get a list of the available CLI commands, run the following command inside your project directory:
```

```

heroui -h

```


```

This will produce the following help output:
```

```

HeroUI CLI <version>
A command line tool for seamless integration with HeroUI
Usage: heroui [command]
Options:
 -v, --version           Output the current version
 --no-cache             Disable cache, by default data will be cached for 30m after the first request
 -d, --debug            Debug mode will not install dependencies
 -h --help             Display help information for commands
Commands:
 init [options][projectName]    Initializes a new project
add[options][components...]   Adds components to your project
 upgrade [options][components...] Upgrades project components to the latest versions
 remove [options][components...]  Removes components from the project
 list [options]           Lists all components, showing status, descriptions, and versions
env[options]           Displays debugging information for the local environment
 doctor [options]          Checks forissuesin the project
help[command]           Display helpforcommand

```


```

## Commands
### Init
Initialize a new HeroUI project with official templates.
#### Init Options
  * `-t --template [string]` The template to use for the new project e.g. app, pages, vite
  * `-p --package [string]` The package manager to use for the new project (default: `npm`)


##### Example
output:
### Add
Add HeroUI components to your project.
#### Features
>   1. Auto add the missing required `dependencies` to your project
>   2. Auto add the required `tailwindcss.config.js` configuration to your project
>   3. Detect whether using pnpm, if so, add the required configuration to your `.npmrc` file
> 

#### Add Options
  * `-a --all` [boolean] Add all the HeroUI components (default: `false`)
  * `-p --packagePath` [string] The path to the package.json file
  * `-tw --tailwindPath` [string] The path to the tailwind.config file file
  * `-app --appPath` [string] The path to the App.tsx file
  * `--prettier` [boolean] Add prettier format in the add content which required installed prettier - (default: `false`)
  * `--addApp` [boolean] Add App.tsx file content which required provider (default: `false`)
  * `-b --beta` [boolean] Add beta components (default: `false`)


##### Example
Without setting a specific component, the `add` command will show a list of available components.
Output:
If you want to add a specific component, you can specify the component name.
Output:
### Upgrade
Upgrade the HeroUI components to the latest version.
#### Upgrade Options
  * `-p --packagePath` [string] The path to the package.json file
  * `-a --all` [boolean] Upgrade all the HeroUI components (default: `false`)
  * `-w --write` [boolean] Write the upgrade version to package.json file (default: `false`)
  * `-b --beta` [boolean] Upgrade beta components (default: `false`)
  * `-h --help` Display help for command


##### Example
Upgrade the **Button** component to the latest version.
Output:
### Remove
Remove HeroUI components from your project.
> **Note** : If there are no HeroUI components after removing, the required content will also be removed
#### Remove Options
  * `-p --packagePath` [string] The path to the package.json file
  * `-a --all` [boolean] Remove all the HeroUI components (default: `false`)
  * `-tw --tailwindPath` [string] The path to the tailwind.config file file
  * `--prettier` [boolean] Add prettier format in the add content which required installed prettier - (default: `false`)


##### Example
Remove the **Button** component from your project.
Output:
### List
List all the current installed components.
#### List Options
  * `-p --packagePath` [string] The path to the package.json file
  * `-r --remote` List all components available remotely


##### Example
Output:
### Doctor
Check whether exist problem in your project by using the `doctor` command.
### Features
>   1. Check whether have `redundant dependencies` in the project
>   2. Check whether the HeroUI components `required dependencies are installed` in the project
>   3. Check the required `tailwind.config.js` file and the content is correct
>   4. Check `.npmrc` is correct when using `pnpm`
>   5. Check `peerDependencies with required version` are installed in the project
> 

#### Doctor Options
  * `-p` `--packagePath` [string] The path to the package.json file
  * `-tw` `--tailwindPath` [string] The path to the tailwind.config file file
  * `-app` `--appPath` [string] The path to the App.tsx file
  * `-ca` `--checkApp` [boolean] Open check App (default: `true`)
  * `-ct` `--checkTailwind` [boolean] Open check tailwind.config file (default: `true`)
  * `-cp` `--checkPnpm` [boolean] Open check Pnpm (default: `true`)


#### Example
Output:
If there is a problem in your project, the `doctor` command will display the problem information.
Otherwise, the `doctor` command will display the following message.
### Env
Display debug information about the local environment.
#### Env Options
  * `-p --packagePath` [string] The path to the package.json file


#### Example
Display the local environment Information by using the `env` command.
Output:
Components: UserHeroUIProvider
On this page
  * Commands
  * Init
  * Init Options
  * Example
  * Add
  * Features
  * Add Options
  * Example
  * Upgrade
  * Upgrade Options
  * Example
  * Remove
  * Remove Options
  * Example
  * List
  * List Options
  * Example
  * Doctor
  * Features
  * Doctor Options
  * Example
  * Env
  * Env Options
  * Example
  * Back to top


Ship fasterwith beautifulcomponents
Discover 210+ stunning components by HeroUI
Explore Components
![docs left background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-left.png)
![docs right background](https://heroui-assets.nyc3.cdn.digitaloceanspaces.com/images/docs-right.png)
