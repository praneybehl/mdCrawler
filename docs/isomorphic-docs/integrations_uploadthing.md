Skip to main content
Version: v7.0.0
On this page
## Uploadthing​
UploadThing is the easiest way to add file uploads to your full stack TypeScript application. Many services have tried to build a "better S3", but in our opinion, none found the right compromise of ownership, flexibility and safety.
## Get Uploadthing API​
Log in at https://uploadthing.com/sign-in.
  1. After logging in, you will see a `create a new app` button. simply click on it
  2. A form will now display, with two inputs: `app name` and `app url`. Fill in the blanks and press the `create app` button. This will generate a new dashboard for your application.
  3. In the left sidebar of your newly established app's dashboard, click on API keys.
  4. Copy and paste the `UPLOADTHING_SECRET` into your `.env.local` file.


apps/isomorphic/.env.local
```
UPLOADTHING_SECRET=your_uploadthing_secret_key_here
```

  1. You're finished. You may now easily upload any media/file to uploadthing.
  2. For further information, please visit their official documents here https://docs.uploadthing.com/ and you can see it live on the `Your Photo` part https://isomorphic-furyroad.vercel.app/forms/profile-settings.


  * Uploadthing
  * Get Uploadthing API


