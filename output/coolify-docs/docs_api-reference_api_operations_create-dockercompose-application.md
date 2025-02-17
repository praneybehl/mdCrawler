Skip to content
Menu
Return to top
# Create (Docker Compose)​
POST
/applications/dockercompose
Create new application based on a docker-compose file.
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
"docker_compose_raw": "string",
"destination_uuid": "string",
"name": "string",
"description": "string",
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
/applications/dockercompose
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
docker_compose_raw
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
POST https://app.coolify.io/api/v1/applications/dockercompose
Headers
Content-Type: application/json
authorization: Bearer Bearer Token
Body
{
 "project_uuid": "string",
 "server_uuid": "string",
 "environment_name": "string",
 "environment_uuid": "string",
 "docker_compose_raw": "string",
 "destination_uuid": "string",
 "name": "string",
 "description": "string",
 "instant_deploy": true,
 "use_build_server": true
}
```

cURL
```
curl https://app.coolify.io/api/v1/applications/dockercompose \
 --request POST \
 --header 'Authorization: Bearer Bearer Token' \
 --header 'Content-Type: application/json' \
 --data '{
 "project_uuid": "string",
 "server_uuid": "string",
 "environment_name": "string",
 "environment_uuid": "string",
 "docker_compose_raw": "string",
 "destination_uuid": "string",
 "name": "string",
 "description": "string",
 "instant_deploy": true,
 "use_build_server": true
}'
```

JavaScript
```
fetch('https://app.coolify.io/api/v1/applications/dockercompose', {
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
  docker_compose_raw: 'string',
  destination_uuid: 'string',
  name: 'string',
  description: 'string',
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
 CURLOPT_URL => "https://app.coolify.io/api/v1/applications/dockercompose",
 CURLOPT_RETURNTRANSFER => true,
 CURLOPT_ENCODING => "",
 CURLOPT_MAXREDIRS => 10,
 CURLOPT_TIMEOUT => 30,
 CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
 CURLOPT_CUSTOMREQUEST => "POST",
 CURLOPT_POSTFIELDS => "{\"project_uuid\":\"string\",\"server_uuid\":\"string\",\"environment_name\":\"string\",\"environment_uuid\":\"string\",\"docker_compose_raw\":\"string\",\"destination_uuid\":\"string\",\"name\":\"string\",\"description\":\"string\",\"instant_deploy\":true,\"use_build_server\":true}",
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
payload = "{\"project_uuid\":\"string\",\"server_uuid\":\"string\",\"environment_name\":\"string\",\"environment_uuid\":\"string\",\"docker_compose_raw\":\"string\",\"destination_uuid\":\"string\",\"name\":\"string\",\"description\":\"string\",\"instant_deploy\":true,\"use_build_server\":true}"
headers = {
  'Authorization': "Bearer Bearer Token",
  'Content-Type': "application/json"
}
conn.request("POST", "/api/v1/applications/dockercompose", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

Powered by  VitePress OpenAPI 
