Introduction
Please keep in mind that PocketBase is still under active development and full backward compatibility is not guaranteed before reaching v1.0.0. PocketBase is NOT recommended for production critical applications yet, unless you are fine with reading the changelog and applying some manual migration steps from time to time.
PocketBase is an open source backend consisting of embedded database (SQLite) with realtime subscriptions, built-in auth management, convenient dashboard UI and simple REST-ish API. It can be used both as Go framework and as standalone application.
The easiest way to get started is to download the prebuilt minimal PocketBase executable:
x64 ARM64
  * Download v0.29.0 for Linux x64 (~12MB zip)
  * Download v0.29.0 for Windows x64 (~12MB zip)
  * Download v0.29.0 for macOS x64 (~12MB zip)


  * Download v0.29.0 for Linux ARM64 (~11MB zip)
  * Download v0.29.0 for Windows ARM64 (~11MB zip)
  * Download v0.29.0 for macOS ARM64 (~11MB zip)


See the GitHub Releases page for other platforms and more details.
Once you've extracted the archive, you could start the application by running `**./pocketbase serve**`in the extracted directory.
**And that's it!** The first time it will generate an installer link that should be automatically opened in the browser to setup your first superuser account (you can also create the first superuser manually via `./pocketbase superuser create EMAIL PASS`) .
The started web server has the following default routes:
  * `http://127.0.0.1:8090` - if `pb_public` directory exists, serves the static content from it (html, css, images, etc.)
  * `http://127.0.0.1:8090/_/` - superusers dashboard
  * `http://127.0.0.1:8090/api/` - REST-ish API


The prebuilt PocketBase executable will create and manage 2 new directories alongside the executable:
  * `pb_data` - stores your application data, uploaded files, etc. (usually should be added in `.gitignore`).
  * `pb_migrations` - contains JS migration files with your collection changes (can be safely committed in your repository). 
You can even write custom migration scripts. For more info check the JS migrations docs.


You could find all available commands and their options by running `./pocketbase --help` or `./pocketbase [command] --help`
Next: How to use PocketBase
