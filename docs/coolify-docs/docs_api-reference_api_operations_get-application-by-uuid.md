Skip to content
Menu
Return to top
# Get​
GET
/applications/{uuid}
Get application by UUID.
## Authorizations​
bearerAuth
Go to `Keys & Tokens` / `API tokens` and create a new token. Use the token as the bearer token.
TypeHTTP (bearer)
## Parameters​
### Path Parameters
uuid*
UUID of the application.
Typestring
Required
format`uuid`
## Responses​
200400401404
Get application by UUID.
Content-Type
application/json
SchemaJSON
JSON
{
"id": 0,
"description": "string",
"repository_project_id": 0,
"uuid": "string",
"name": "string",
"fqdn": "string",
"config_hash": "string",
"git_repository": "string",
"git_branch": "string",
"git_commit_sha": "string",
"git_full_url": "string",
"docker_registry_image_name": "string",
"docker_registry_image_tag": "string",
"build_pack": "string",
"static_image": "string",
"install_command": "string",
"build_command": "string",
"start_command": "string",
"ports_exposes": "string",
"ports_mappings": "string",
"base_directory": "string",
"publish_directory": "string",
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
"status": "string",
"preview_url_template": "string",
"destination_type": "string",
"destination_id": 0,
"source_id": 0,
"private_key_id": 0,
"environment_id": 0,
"dockerfile": "string",
"dockerfile_location": "string",
"custom_labels": "string",
"dockerfile_target_build": "string",
"manual_webhook_secret_github": "string",
"manual_webhook_secret_gitlab": "string",
"manual_webhook_secret_bitbucket": "string",
"manual_webhook_secret_gitea": "string",
"docker_compose_location": "string",
"docker_compose": "string",
"docker_compose_raw": "string",
"docker_compose_domains": "string",
"docker_compose_custom_start_command": "string",
"docker_compose_custom_build_command": "string",
"swarm_replicas": 0,
"swarm_placement_constraints": "string",
"custom_docker_run_options": "string",
"post_deployment_command": "string",
"post_deployment_command_container": "string",
"pre_deployment_command": "string",
"pre_deployment_command_container": "string",
"watch_paths": "string",
"custom_healthcheck_found": true,
"redirect": "string",
"created_at": "string",
"updated_at": "string",
"deleted_at": "string",
"compose_parsing_version": "string",
"custom_nginx_configuration": "string"
}
GET
/applications/{uuid}
Authorization 
bearerAuth
Variables
Key
Value
uuid*
Try it out
## Samples​
brunocURLJavaScriptPHPPython
bruno
```
GET https://app.coolify.io/api/v1/applications/{uuid}
Headers
Content-Type: application/json
authorization: Bearer Bearer Token

```

cURL
```
curl 'https://app.coolify.io/api/v1/applications/%7Buuid%7D' \
 --header 'Authorization: Bearer Bearer Token' \
 --header 'Content-Type: application/json'
```

JavaScript
```
fetch('https://app.coolify.io/api/v1/applications/%7Buuid%7D', {
 headers: {
  Authorization: 'Bearer Bearer Token',
  'Content-Type': 'application/json'
 }
})
```

PHP
```
<?php
$curl = curl_init();
curl_setopt_array($curl, [
 CURLOPT_URL => "https://app.coolify.io/api/v1/applications/%7Buuid%7D",
 CURLOPT_RETURNTRANSFER => true,
 CURLOPT_ENCODING => "",
 CURLOPT_MAXREDIRS => 10,
 CURLOPT_TIMEOUT => 30,
 CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
 CURLOPT_CUSTOMREQUEST => "GET",
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
headers = {
  'Authorization': "Bearer Bearer Token",
  'Content-Type': "application/json"
}
conn.request("GET", "/api/v1/applications/%7Buuid%7D", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

Powered by  VitePress OpenAPI 
