Skip to main content
Version: v7.0.0
On this page
## Environment Variables​
Every workspace contains their own environment variables. You can check them in the `.env.local.example` file.
> The deployment process requires some environment variables to be set. You have to set these variables in each workspace's `.env` file.
> And also attach these required environment variables in the `turbo.json` files build command in root directory for deployments. Otherwise the deployment process will fail.
turbo.json
```
{"globalDependencies":["**/.env.*local"],"tasks":{"build":{"dependsOn":["^build"],"outputs":["dist/**",".next/**","!.next/cache/**"],"env":["NEXTAUTH_SECRET","NEXTAUTH_URL","NEXT_PUBLIC_GOOGLE_MAP_API_KEY"]}}}
```

  * Environment Variables


