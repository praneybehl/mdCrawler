Skip to content
Menu
Return to top
# Private NPM Registry ​
If you would like to use a private NPM registry with Coolify, you can do so by following the steps below.
  1. Add `.npmrc` file to your project root with the following content:


bash```
//registry.npmjs.org/:_authToken=$NPM_TOKEN
```

  1. Add the following environment variables to your project as a `build` variable:


bash```
NPM_TOKEN=your_npm_token
```

  1. Deploy your application.


