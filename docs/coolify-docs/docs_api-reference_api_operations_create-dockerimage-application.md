Skip to content
Menu
Return to top
# Create (Docker Image)​
POST
/applications/dockerimage
Create new application based on a prebuilt docker image
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
"docker_registry_image_name": "string",
"docker_registry_image_tag": "string",
"ports_exposes": "string",
"destination_uuid": "string",
"name": "string",
"description": "string",
"domains": "string",
"ports_mappings": "string",
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
/applications/dockerimage
Authorization 
bearerAuth
Body
{
project_uuid
:
string
server_uuid
:
string
environment_name
:
string
environment_uuid
:
string
docker_registry_image_name
:
string
docker_registry_image_tag
:
string
ports_exposes
:
string
destination_uuid
:
string
name
:
string
description
:
string
domains
:
string
ports_mappings
:
string
health_check_enabled
:
true
health_check_path
:
string
health_check_port
:
string
health_check_host
:
string
health_check_method
:
string
health_check_return_code
:
0
health_check_scheme
:
string
health_check_response_text
:
string
health_check_interval
:
0
health_check_timeout
:
0
health_check_retries
:
0
health_check_start_period
:
0
limits_memory
:
string
limits_memory_swap
:
string
limits_memory_swappiness
:
0
limits_memory_reservation
:
string
limits_cpus
:
string
limits_cpuset
:
string
limits_cpu_shares
:
0
custom_labels
:
string
custom_docker_run_options
:
string
post_deployment_command
:
string
post_deployment_command_container
:
string
pre_deployment_command
:
string
pre_deployment_command_container
:
string
manual_webhook_secret_github
:
string
manual_webhook_secret_gitlab
:
string
manual_webhook_secret_bitbucket
:
string
manual_webhook_secret_gitea
:
string
redirect
:
string
instant_deploy
:
true
use_build_server
:
true
}
Try it out
## Samples​
brunocURLJavaScriptPHPPython
bruno
```
POST https://app.coolify.io/api/v1/applications/dockerimage
Headers
Content-Type: application/json
authorization: Bearer Bearer Token
Body
{
 "project_uuid": "string",
 "server_uuid": "string",
 "environment_name": "string",
 "environment_uuid": "string",
 "docker_registry_image_name": "string",
 "docker_registry_image_tag": "string",
 "ports_exposes": "string",
 "destination_uuid": "string",
 "name": "string",
 "description": "string",
 "domains": "string",
 "ports_mappings": "string",
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
```

cURL
```
curl https://app.coolify.io/api/v1/applications/dockerimage \
 --request POST \
 --header 'Authorization: Bearer Bearer Token' \
 --header 'Content-Type: application/json' \
 --data '{
 "project_uuid": "string",
 "server_uuid": "string",
 "environment_name": "string",
 "environment_uuid": "string",
 "docker_registry_image_name": "string",
 "docker_registry_image_tag": "string",
 "ports_exposes": "string",
 "destination_uuid": "string",
 "name": "string",
 "description": "string",
 "domains": "string",
 "ports_mappings": "string",
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
}'
```

JavaScript
```
fetch('https://app.coolify.io/api/v1/applications/dockerimage', {
 method: 'POST',
 headers: {
  Authorization: 'Bearer Bearer Token',
  'Content-Type': 'application/json'
 },
 body: JSON.stringify({
  project_uuid: 'string',
  server_uuid: 'string',
  environment_name: 'string',
  environment_uuid: 'string',
  docker_registry_image_name: 'string',
  docker_registry_image_tag: 'string',
  ports_exposes: 'string',
  destination_uuid: 'string',
  name: 'string',
  description: 'string',
  domains: 'string',
  ports_mappings: 'string',
  health_check_enabled: true,
  health_check_path: 'string',
  health_check_port: 'string',
  health_check_host: 'string',
  health_check_method: 'string',
  health_check_return_code: 0,
  health_check_scheme: 'string',
  health_check_response_text: 'string',
  health_check_interval: 0,
  health_check_timeout: 0,
  health_check_retries: 0,
  health_check_start_period: 0,
  limits_memory: 'string',
  limits_memory_swap: 'string',
  limits_memory_swappiness: 0,
  limits_memory_reservation: 'string',
  limits_cpus: 'string',
  limits_cpuset: 'string',
  limits_cpu_shares: 0,
  custom_labels: 'string',
  custom_docker_run_options: 'string',
  post_deployment_command: 'string',
  post_deployment_command_container: 'string',
  pre_deployment_command: 'string',
  pre_deployment_command_container: 'string',
  manual_webhook_secret_github: 'string',
  manual_webhook_secret_gitlab: 'string',
  manual_webhook_secret_bitbucket: 'string',
  manual_webhook_secret_gitea: 'string',
  redirect: 'string',
  instant_deploy: true,
  use_build_server: true
 })
})
```

PHP
```
<?php
$curl = curl_init();
curl_setopt_array($curl, [
 CURLOPT_URL => "https://app.coolify.io/api/v1/applications/dockerimage",
 CURLOPT_RETURNTRANSFER => true,
 CURLOPT_ENCODING => "",
 CURLOPT_MAXREDIRS => 10,
 CURLOPT_TIMEOUT => 30,
 CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
 CURLOPT_CUSTOMREQUEST => "POST",
 CURLOPT_POSTFIELDS => "{\"project_uuid\":\"string\",\"server_uuid\":\"string\",\"environment_name\":\"string\",\"environment_uuid\":\"string\",\"docker_registry_image_name\":\"string\",\"docker_registry_image_tag\":\"string\",\"ports_exposes\":\"string\",\"destination_uuid\":\"string\",\"name\":\"string\",\"description\":\"string\",\"domains\":\"string\",\"ports_mappings\":\"string\",\"health_check_enabled\":true,\"health_check_path\":\"string\",\"health_check_port\":\"string\",\"health_check_host\":\"string\",\"health_check_method\":\"string\",\"health_check_return_code\":0,\"health_check_scheme\":\"string\",\"health_check_response_text\":\"string\",\"health_check_interval\":0,\"health_check_timeout\":0,\"health_check_retries\":0,\"health_check_start_period\":0,\"limits_memory\":\"string\",\"limits_memory_swap\":\"string\",\"limits_memory_swappiness\":0,\"limits_memory_reservation\":\"string\",\"limits_cpus\":\"string\",\"limits_cpuset\":\"string\",\"limits_cpu_shares\":0,\"custom_labels\":\"string\",\"custom_docker_run_options\":\"string\",\"post_deployment_command\":\"string\",\"post_deployment_command_container\":\"string\",\"pre_deployment_command\":\"string\",\"pre_deployment_command_container\":\"string\",\"manual_webhook_secret_github\":\"string\",\"manual_webhook_secret_gitlab\":\"string\",\"manual_webhook_secret_bitbucket\":\"string\",\"manual_webhook_secret_gitea\":\"string\",\"redirect\":\"string\",\"instant_deploy\":true,\"use_build_server\":true}",
 CURLOPT_HTTPHEADER => [
  "Authorization: Bearer Bearer Token",
  "Content-Type: application/json"
 ],
]);
$response = curl_exec($curl);
$err = curl_error($curl);
curl_close($curl);
if ($err) {
 echo "cURL Error #:" . $err;
} else {
 echo $response;
}
```

Python
```
import http.client
conn = http.client.HTTPSConnection("app.coolify.io")
payload = "{\"project_uuid\":\"string\",\"server_uuid\":\"string\",\"environment_name\":\"string\",\"environment_uuid\":\"string\",\"docker_registry_image_name\":\"string\",\"docker_registry_image_tag\":\"string\",\"ports_exposes\":\"string\",\"destination_uuid\":\"string\",\"name\":\"string\",\"description\":\"string\",\"domains\":\"string\",\"ports_mappings\":\"string\",\"health_check_enabled\":true,\"health_check_path\":\"string\",\"health_check_port\":\"string\",\"health_check_host\":\"string\",\"health_check_method\":\"string\",\"health_check_return_code\":0,\"health_check_scheme\":\"string\",\"health_check_response_text\":\"string\",\"health_check_interval\":0,\"health_check_timeout\":0,\"health_check_retries\":0,\"health_check_start_period\":0,\"limits_memory\":\"string\",\"limits_memory_swap\":\"string\",\"limits_memory_swappiness\":0,\"limits_memory_reservation\":\"string\",\"limits_cpus\":\"string\",\"limits_cpuset\":\"string\",\"limits_cpu_shares\":0,\"custom_labels\":\"string\",\"custom_docker_run_options\":\"string\",\"post_deployment_command\":\"string\",\"post_deployment_command_container\":\"string\",\"pre_deployment_command\":\"string\",\"pre_deployment_command_container\":\"string\",\"manual_webhook_secret_github\":\"string\",\"manual_webhook_secret_gitlab\":\"string\",\"manual_webhook_secret_bitbucket\":\"string\",\"manual_webhook_secret_gitea\":\"string\",\"redirect\":\"string\",\"instant_deploy\":true,\"use_build_server\":true}"
headers = {
  'Authorization': "Bearer Bearer Token",
  'Content-Type': "application/json"
}
conn.request("POST", "/api/v1/applications/dockerimage", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

Powered by  VitePress OpenAPI 
