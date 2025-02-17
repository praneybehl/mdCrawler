Skip to content
Menu
On this page
# GitLab Integration ​
## Public Repositories ​
You can use public repositories without any additional setup.
  1. Select the `Public repository` option in the Coolify when you create a new resource.
  2. Add your repository URL to the input field, for example: `https://gitlab.com/andrasbacsai/coolify-examples`
Caution
You can only use the https URL.
  3. That's it! Coolify will automatically pull the latest version of your repository and deploy it.


## Private Repositories ​
Private repositories require a few more steps to setup.
  1. Add a private key (aka `Deploy Keys`) to Coolify and to your GitLab repository in the `Settings` / `Repository` / `Deploy Keys` menu.


Caution
  * You can generate a new key pair with the following command:


bash```
ssh-keygen -t rsa -b 4096 -C "deploy_key"
```

  * Or you can also use Coolify to generate a new key for you in the `Keys & Tokens` menu.


  1. Create a new resource and select the `Private Repository (with deploy key)`
  2. Add your repository URL to the input field, for example: `git@gitlab.com:andrasbacsai/coolify-examples.git`


Caution
You need to use the SSH URL, so the one that starts with `git@`.
  1. That's it! Coolify will automatically pull the latest version of your repository and deploy it.


## Automatic commit deployments with webhooks (Optional) ​
You can add a custom webhook URL to your GitLab repository to trigger a new deployment when you push to your repository.
Caution
This can be set on either public or private repositories.
In your resource, there is a `Webhooks` menu. In the `Manual Git Webhooks` section, you can find the URL what you need to set in your GitLab repository.
  1. Set a secret key in the `GitLab Webhook Secret` input field.
  2. Go to your repository in GitLab and open the `Settings` / `Webhooks` menu.
  3. Add the URL from Coolify to the `URL` input field and the secret token.
  4. Select the `Push events` option.
  5. That's it! Now when you push to your repository, GitLab will send a webhook request to Coolify and it will trigger a new deployment.


## Merge request deployments with webhooks (Optional) ​
You can add a custom webhook URL to your GitLab repository to trigger a new deployment when you create a new merge request.
Caution
This can be set on either public or private repositories.
The process is the same as the previous one, but you need to select the `Merge request events` option in the `Settings` / `Webhooks` menu.
