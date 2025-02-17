Skip to content
Menu
Return to top
# Uninstalling Coolify ​
If you're using Coolify Cloud ↗, you don't need to uninstall Coolify, as the instance is hosted on servers managed by the Core Team ↗. To stop using Coolify Cloud, simply head over to the **Billing** page and cancel your subscription.
The following instructions are for those who are **self-hosting** Coolify and wish to uninstall it from their server.
The uninstallation process involves the following five steps:
  * Stop and Remove Containers
  * Remove Docker Volumes
  * Remove Docker Network
  * Delete Coolify Data Directory
  * Remove Docker Images


## 1. Stop and Remove Containers ​
Stop all Coolify-related Docker containers and remove them to free up system resources.
Run the following commands in your terminal:
sh```
 sudo docker stop -t 0 coolify coolify-realtime coolify-db coolify-redis coolify-proxy
 sudo docker rm coolify coolify-realtime coolify-db coolify-redis coolify-proxy
```

The `-t 0` flag ensures that the containers stop immediately without waiting for a timeout.
## 2. Remove Docker Volumes ​
To remove the persistent data stored in Docker volumes for Coolify, run:
sh```
 sudo docker volume rm coolify-db coolify-redis
```

CAUTION!!
Removing volumes will delete all data stored in them permanently. Ensure you have backups if needed.
## 3. Remove Docker Network ​
Coolify uses a custom Docker network named coolify. Remove it with the following command:
sh```
 sudo docker network rm coolify
```

📌 Info
If you encounter an error indicating the network is in use, ensure that no containers are using the network before retrying.
## 4. Delete Coolify Data Directory ​
Remove the directory where Coolify stores its data on your server:
sh```
 sudo rm -rf /data/coolify
```

CAUTION!
This will permanently delete all Coolify-related data. Double-check the directory path before executing this command.
## 5. Remove Docker Images ​
To free up disk space, remove all Docker images used by Coolify by running the following commands:
sh```
 sudo docker rmi ghcr.io/coollabsio/coolify:latest
 sudo docker rmi ghcr.io/coollabsio/coolify-helper:latest
 sudo docker rmi quay.io/soketi/soketi:1.6-16-alpine
 sudo docker rmi postgres:15-alpine
 sudo docker rmi redis:alpine
```

If you were using the default proxy, also remove its image:
sh```
 sudo docker rmi traefik:v3.1
```

If you switched to the Caddy proxy, remove its image instead:
sh```
 sudo docker rmi lucaslorentz/caddy-docker-proxy:2.8-alpine
```

### Coolify Successfully Uninstalled ​
After completing these steps, Coolify and all its related resources will be completely removed from your server.
