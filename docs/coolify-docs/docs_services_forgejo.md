Skip to content
Menu
Return to top
![forgejo](https://forgejo.org/images/forgejo-wordmark.svg)
## What is Forgejo? ​
Forgejo is a self-hosted lightweight software forge. It's easy to install and low maintenance, it just does the job.
## Forgejo Actions Runner ​
Forgejo has available a first party "actions runner" to execute task jobs on a repository, much like GitHub Actions or GitLab CI.
Coolify includes Forgejo services with a single runner, using Docker-in-Docker to handle and report task jobs.
Due to the alpha status of the Forgejo runner, rebooting the Forejo application container after the initial setup is required to fully register the shared secret into Forejo for runners to validate:
  1. In the **Environment Variables** section of the service configuration, you may set as `RUNNER_SHARED_SECRET` a random 40-character hexagesimal string. The command `openssl rand -hex 20` creates something you can copy and paste.
  2. After sucessfully setting up Forejo, **reboot the`forgejo` service** and wait some seconds until the runner appears in Forgejo _Actions_ Configuration section.


Forejo is also compatible with third-party CI apps and platforms. Forgejo is a Gitea-fork, so instructions to incorporate these CI may be the same for both.
## Demo ​
  * Demo ›


## Links ​
  * The official website ›
  * Github ›


