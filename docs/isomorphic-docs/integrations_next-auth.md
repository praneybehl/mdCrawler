Skip to main content
Version: v7.0.0
On this page
## Next Auth​
Isomorphic seamlessly integrates `next-auth` authentication, providing a robust and flexible authentication solution for your Next.js projects. With `next-auth`, you can easily implement authentication features and manage user sessions with minimal effort.
## Configuration​
Start by configuring `NEXTAUTH_SECRET`, `NEXTAUTH_URL` and `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET` in your `.env.local` file, a detailed documentation is available here
Currently there are two default options available, `CredentialsProvider` and `GoogleProvider`
## Credentials Provider​
In `CredentialsProvider` currently has static validation, you have to change this if you want to keep `CredentialsProvider`. Refer to the official NextAuth documentation on `CredentialsProvider` https://next-auth.js.org/v3/configuration/providers#credentials-provider
## Google Provider​
We've already integrated the Google provider to streamline the process for you. Simply configure the environment variables, and you're all set!
apps/isomorphic/src/app/api/auth/[...nextauth]/auth-options.ts
```
GoogleProvider({clientId: env.GOOGLE_CLIENT_ID||'',clientSecret: env.GOOGLE_CLIENT_SECRET||'',allowDangerousEmailAccountLinking:true,}),
```

## Add a New Provider​
If you wish to add another provider, refer to the comprehensive official documentation, which not only offers a guide on how to integrate a new one but also includes a list of available providers here https://next-auth.js.org/v3/configuration/providers#adding-a-new-provider
## How to Remove NextAuth​
We understand that not everyone requires authentication for their project, if your project falls into this category and you do not require authentication then you're in right place. Lets remove next auth.
First, navigate to the project root folder. Then, from the project root, go to `src` and remove the `apps/isomorphic/src/middleware.ts` file.
Second, you will see a folder called `auth` inside another folder called `api`. You can delete this folder they are not needed anymore.
Now, inside `src`, open `env.mjs` and remove `NEXTAUTH_SECRET` and `NEXTAUTH_URL`:
apps/isomorphic/src/env.mjs
```
import{ z }from'zod';import{ createEnv }from'@t3-oss/env-nextjs';exportconst env =createEnv({/*  * ServerSide Environment variables, not available on the client.  */ server:{NODE_ENV: z.enum(['development','test','production']),-NEXTAUTH_SECRET:-   process.env.NODE_ENV==='production'-? z.string().min(1)-: z.string().min(1).optional(),-NEXTAUTH_URL: z.preprocess(-// This makes Vercel deployments not fail if you don't set NEXTAUTH_URL-// Since NextAuth.js automatically uses the VERCEL_URL if present.-(str)=> process.env.VERCEL_URL?? str,-// VERCEL_URL doesn't include `https` so it cant be validated as a URL-   process.env.VERCEL? z.string().min(1): z.string().url()-),// emailSMTP_HOST: z.string().optional(),SMTP_PORT: z.string().optional(),SMTP_USER: z.string().optional(),SMTP_PASSWORD: z.string().optional(),SMTP_FROM_EMAIL: z.string().email().optional(),GOOGLE_CLIENT_ID: z.string().optional(),GOOGLE_CLIENT_SECRET: z.string().optional(),},/*  * Environment variables available on the client (and server).  */ client:{NEXT_PUBLIC_APP_NAME: z.string().optional(),NEXT_PUBLIC_GOOGLE_MAP_API_KEY: z.string().optional(),}, runtimeEnv: process.env,});
```

go to `apps/isomorphic/src/app/layout.tsx` and remove the highlighted imports and other codes.
apps/isomorphic/src/app/layout.tsx
```
import dynamic from'next/dynamic';import{ Toaster }from'react-hot-toast';-import{ getServerSession }from'next-auth/next';-import{ authOptions }from'@/app/api/auth/[...nextauth]/auth-options';-import AuthProvider from'@/app/api/auth/[...nextauth]/auth-provider';import{ CartProvider }from'@/store/quick-cart/cart.context';import GlobalDrawer from'@/app/shared/drawer-views/container';import GlobalModal from'@/app/shared/modal-views/container';import{ ThemeProvider }from'@/app/shared/theme-provider';import{ siteConfig }from'@/config/site.config';import{ inter, lexendDeca }from'@/app/fonts';import cn from'@/utils/class-names';import'react-big-calendar/lib/css/react-big-calendar.css';const NextProgress =dynamic(()=>import('@/components/next-progress'),{   ssr:false,});// stylesimport'@/app/globals.css';exportconst metadata ={   title: siteConfig.title,   description: siteConfig.description,};exportdefaultasyncfunctionRootLayout({   children,}:{   children: React.ReactNode;}){-const session =awaitgetServerSession(authOptions);return(-<AuthProvider session={session}><ThemeProvider><NextProgress />{children}<Toaster /><GlobalDrawer /><GlobalModal /></ThemeProvider>-</AuthProvider>);}
```

  * Next Auth
  * Configuration
  * Credentials Provider
  * Google Provider
  * Add a New Provider
  * How to Remove NextAuth


