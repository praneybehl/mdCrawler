Skip to content
Menu
On this page
![](https://coolify.io/docs/images/services/nexus0.webp)
## What is Sonatype Nexus ​
Sonatype Nexus is a repository manager that allows you to store, manage, and distribute your software artifacts. The official container is for x86_64 architecture. The arm64 version is community maintained and synced with the official repository.
## Setup ​
  * The setup relies on starting as default user "admin" with password "admin123".
  * Once the service is running, login with the default credentials and change the password.
  * After that, delete `NEXUS_SECURITY_RANDOMPASSWORD=false` line from the compose file and restart the service to apply the changes.


Minimum requirements:
  * 4 vCPU
  * 3 GB RAM


## Screenshots ​
![](https://coolify.io/docs/images/services/nexus1.webp)
![](https://coolify.io/docs/images/services/nexus2.webp)
## Links ​
  * The official website ›
  * GitHub ›


