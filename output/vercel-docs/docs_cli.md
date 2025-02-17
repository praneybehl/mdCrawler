![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-light.cf7eca76.svg)![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-dark.01246f11.svg)
Search...
`⌘ K`
Feedback
Log In
Sign Up
CLI & API
Vercel CLI
# Vercel CLI Overview
Learn how to use the Vercel command-line interface (CLI) to manage and configure your Vercel Projects from the command line.
Table of Contents
Vercel gives you multiple ways to interact with and configure your Vercel Projects. With the command-line interface (CLI) you can interact with the Vercel platform using a terminal, or through an automated system, enabling you to retrieve logs, manage certificates, replicate your deployment environment locally, manage Domain Name System (DNS) records, and more.
If you'd like to interface with the platform programmatically, check out the REST API documentation.
## Installing Vercel CLI
To download and install Vercel CLI, run the following command:
pnpmyarnnpm
```
pnpm i -g vercel
```

## Updating Vercel CLI
When there is a new release of Vercel CLI, running any command will show you a message letting you know that an update is available.
If you have installed our command-line interface through npm or Yarn, the easiest way to update it is by running the installation command yet again.
pnpmyarnnpm
```
pnpm i -g vercel@latest
```

If you see permission errors, please read npm's official guide. Yarn depends on the same configuration as npm.
## Checking the version
The `--version` option can be used to verify the version of Vercel CLI currently being used.
terminal
```
vercel--version
```

Using the `vercel` command with the `--version` option.
## Using in a CI/CD environment
Vercel CLI requires you to log in and authenticate before accessing resources or performing administrative tasks. In a terminal environment, you can use `vercel login`, which requires manual input. In a CI/CD environment where manual input is not possible, you can create a token on your tokens page and then use the `--token` option to authenticate.
## Available Commands
- alias
- bisect
- build
- certs
- deploy
- dev
- dns
- domains
- env
- git
- help
- init
- inspect
- link
- list
- login
- logout
- logs
- project
- promote
- pull
- redeploy
- remove
- rollback
- switch
- teams
- whoami
Last updated on July 17, 2024
Previous
CLI & API
Next
Deploying from CLI
Was this helpful?
supported.
Send
AskAsk v0
Vercel CLIAskAsk v0
