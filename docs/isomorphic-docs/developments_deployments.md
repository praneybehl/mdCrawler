Skip to main content
Version: v7.0.0
On this page
## Deployments​
## NEXT.JS Official Documentation​
For a seamless deployment of your Next.js app, leverage the simplicity of Vercel, provided by the creators of Next.js.
For an in-depth guide on deploying with Next.js, dive into their comprehensive documentation available here. **https://nextjs.org/docs/deployment**
## Isomorphic Deployments Steps​
note
We are going to deploy the `isomorphic` workspace to Vercel.
### 1. Import project to Vercel.​
![Import Project](https://isomorphic-doc.vercel.app/assets/images/import-git-repo-1e656ebf138afde48a68901317faf9d8.png)
### 2. Edit Root Directory.​
![Edit Root Directory](https://isomorphic-doc.vercel.app/assets/images/edit-root-directory-45bb9db3fa3f2ca82f021f027d821bdb.png)
### 3. Select Workspace.​
In our case it's `isomorphic`.
![Edit Root Directory](https://isomorphic-doc.vercel.app/assets/images/select-iso-cfe981ae6a5a6a87a91c6b34e650adcb.png)
### 4. Override Build Command​
We have already provided custom build commands for every workspace in the root `package.json` file. **Check All Commands**. For isomorphic workspace, the build command is `pnpm iso:build` s
```
cd../..&&pnpm iso:build
```

![Custom Build Command](https://isomorphic-doc.vercel.app/assets/images/custom-build-cmd-b7b7b6350ef62d07bc7853b786d029fb.png)
### 5 Environment Variables.​
If your project requires any environment variables provide those. In our case `isomorphic` workspace required variables are `NEXTAUTH_SECRET` & `NEXTAUTH_URL`. Learn more about **Environment Variables in Turborepo**
```
NEXTAUTH_SECRET="your-next-auth-secret"NEXTAUTH_URL="your-next-auth-url"NEXT_PUBLIC_GOOGLE_MAP_API_KEY="your-google-map-api-key"
```

![Custom Build Command](https://isomorphic-doc.vercel.app/assets/images/environments-1433fcbd6d08f93bf30e1ece248f4a7c.png)
### 6 Click Deploy​
More Information
For more information on Vercel deployment, refer to the **Official Documentation**
  * Deployments
  * NEXT.JS Official Documentation
  * Isomorphic Deployments Steps
    * 1. Import project to Vercel.
    * 2. Edit Root Directory.
    * 3. Select Workspace.
    * 4. Override Build Command
    * 5 Environment Variables.
    * 6 Click Deploy


