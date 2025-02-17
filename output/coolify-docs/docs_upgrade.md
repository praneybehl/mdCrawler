Skip to content
Menu
Return to top
# Upgrading Coolify ​
If you're using Coolify Cloud ↗, updates are managed by the Coolify Core Team ↗, so you don't need to worry about them. The following instructions are for those who are self-hosting Coolify.
There are three ways to upgrade your self-hosted instance:
  1. Automatic Upgrade is for users who want easy, hands-off updates.
  2. Semi-Automatic Upgrade gives you control over when to apply updates.
  3. Manual Upgrade is for advanced users who want to manage the upgrade process themselves.


CAUTION!
**We highly recommend you to backup Coolify before you proceed with the update.**
## 1. Automatic Upgrade ​
Coolify automatically checks for new updates and will upgrade your instance to the latest version as soon as it becomes available. This ensures that your instance remains up to date without requiring any manual intervention.
### How it works: ​
The automatic update feature is enabled by default, and Coolify will automatically pull the latest version from the official repository ↗ whenever a new version is released. Once the update is detected, the Coolify will begin the upgrade process without you needing to take any action.
### Customizing Automatic Updates: ​
If you'd like to disable the auto-update feature, you can do so by navigating to the Settings menu in your Coolify dashboard.
![](https://coolify.io/docs/images/get-started/upgrade-disable-auto-update.webp)
📌 Info
Disabling automatic updates may be helpful if you want to test a new version on a staging environment first, or if you require more control over when updates are applied to your instance.
## 2. Semi-Automatic Upgrade ​
For users who want to stay up to date but prefer some control over when the update happens, Coolify offers a semi-automatic upgrade option. In this method, Coolify will notify you whenever a new version is available, and you can choose when to apply the update.
### How it works: ​
If an update is available, you will see an Upgrade button in the Navigation bar within the Coolify interface.
![](https://coolify.io/docs/images/get-started/upgrade-button-ui.webp)
Clicking this button will start the upgrade process, allowing you to update Coolify to the latest version.
### Configuring Update Checks: ​
You can configure how often Coolify checks for updates within the Settings menu. Coolify will notify you based on the interval you set, allowing you to choose the frequency of update checks (e.g., daily, weekly, etc.).
![](https://coolify.io/docs/images/get-started/upgrade-change-frequency.webp)
📌 Info
This method is great for users who want to review the new version notes or test the upgrade process in a controlled manner before applying the update to their production environment.
## 3. Manual Upgrade ​
If you prefer to have full control over when and how your instance is updated, you can manually upgrade your Coolify instance by running a simple command. This method is ideal for advanced users who prefer to execute the update themselves and want more control over the process.
### How it works: ​
To manually upgrade your Coolify instance, open the terminal on your server and execute the following command:
sh```
curl -fsSL https://cdn.coollabs.io/coolify/install.sh | sudo bash
```

This command will download and execute the official Coolify installation script ↗. The script will check for the latest version and perform the necessary upgrade steps.
### What the Script Does: ​
The script automatically downloads the latest version of Coolify from the official repository ↗ and installs it over your current installation.
