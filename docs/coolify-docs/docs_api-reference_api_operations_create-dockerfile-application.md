Skip to content
Menu
Return to top
# Create (Dockerfile)​
POST
/applications/dockerfile
Create new application based on a simple Dockerfile.
## Authorizations​
bearerAuth
Go to `Keys & Tokens` / `API tokens` and create a new token. Use the token as the bearer token.
TypeHTTP (bearer)
## Request Body​
SchemaJSON
JSON
{
"project_uuid": "string",
"server_uuid": "string",
"environment_name": "string",
"environment_uuid": "string",
"dockerfile": "string",
"build_pack": "string",
"ports_exposes": "string",
"destination_uuid": "string",
"name": "string",
"description": "string",
"domains": "string",
"docker_registry_image_name": "string",
"docker_registry_image_tag": "string",
"ports_mappings": "string",
"base_directory": "string",
"health_check_enabled": true,
"health_check_path": "string",
"health_check_port": "string",
"health_check_host": "string",
"health_check_method": "string",
"health_check_return_code": 0,
"health_check_scheme": "string",
"health_check_response_text": "string",
"health_check_interval": 0,
"health_check_timeout": 0,
"health_check_retries": 0,
"health_check_start_period": 0,
"limits_memory": "string",
"limits_memory_swap": "string",
"limits_memory_swappiness": 0,
"limits_memory_reservation": "string",
"limits_cpus": "string",
"limits_cpuset": "string",
"limits_cpu_shares": 0,
"custom_labels": "string",
"custom_docker_run_options": "string",
"post_deployment_command": "string",
"post_deployment_command_container": "string",
"pre_deployment_command": "string",
"pre_deployment_command_container": "string",
"manual_webhook_secret_github": "string",
"manual_webhook_secret_gitlab": "string",
"manual_webhook_secret_bitbucket": "string",
"manual_webhook_secret_gitea": "string",
"redirect": "string",
"instant_deploy": true,
"use_build_server": true
}
## Responses​
201400401
Application created successfully.
Content-Type
application/json
SchemaJSON
JSON
{
"uuid": "string"
}
POST
/applications/dockerfile
## Samples​
Powered by  VitePress OpenAPI 
