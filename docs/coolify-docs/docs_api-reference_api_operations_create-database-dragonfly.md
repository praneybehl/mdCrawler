Skip to content
Menu
Return to top
# Create (DragonFly)​
POST
/databases/dragonfly
Create a new DragonFly database.
## Authorizations​
bearerAuth
Go to `Keys & Tokens` / `API tokens` and create a new token. Use the token as the bearer token.
TypeHTTP (bearer)
## Request Body​
SchemaJSON
JSON
{
"server_uuid": "string",
"project_uuid": "string",
"environment_name": "string",
"environment_uuid": "string",
"destination_uuid": "string",
"dragonfly_password": "string",
"name": "string",
"description": "string",
"image": "string",
"is_public": true,
"public_port": 0,
"limits_memory": "string",
"limits_memory_swap": "string",
"limits_memory_swappiness": 0,
"limits_memory_reservation": "string",
"limits_cpus": "string",
"limits_cpuset": "string",
"limits_cpu_shares": 0,
"instant_deploy": true
}
## Responses​
200400401
Database updated
POST
/databases/dragonfly
Authorization 
bearerAuth
Body
{
server_uuid
:
string
project_uuid
:
string
environment_name
:
string
environment_uuid
:
string
destination_uuid
:
string
dragonfly_password
:
string
name
:
string
description
:
string
image
:
string
is_public
:
true
public_port
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
instant_deploy
:
true
}
Try it out
## Samples​
brunocURLJavaScriptPHPPython
bruno
```
POST https://app.coolify.io/api/v1/databases/dragonfly
Headers
Content-Type: application/json
authorization: Bearer Bearer Token
Body
{
 "server_uuid": "string",
 "project_uuid": "string",
 "environment_name": "string",
 "environment_uuid": "string",
 "destination_uuid": "string",
 "dragonfly_password": "string",
 "name": "string",
 "description": "string",
 "image": "string",
 "is_public": true,
 "public_port": 0,
 "limits_memory": "string",
 "limits_memory_swap": "string",
 "limits_memory_swappiness": 0,
 "limits_memory_reservation": "string",
 "limits_cpus": "string",
 "limits_cpuset": "string",
 "limits_cpu_shares": 0,
 "instant_deploy": true
}
```

cURL
```
curl https://app.coolify.io/api/v1/databases/dragonfly \
 --request POST \
 --header 'Authorization: Bearer Bearer Token' \
 --header 'Content-Type: application/json' \
 --data '{
 "server_uuid": "string",
 "project_uuid": "string",
 "environment_name": "string",
 "environment_uuid": "string",
 "destination_uuid": "string",
 "dragonfly_password": "string",
 "name": "string",
 "description": "string",
 "image": "string",
 "is_public": true,
 "public_port": 0,
 "limits_memory": "string",
 "limits_memory_swap": "string",
 "limits_memory_swappiness": 0,
 "limits_memory_reservation": "string",
 "limits_cpus": "string",
 "limits_cpuset": "string",
 "limits_cpu_shares": 0,
 "instant_deploy": true
}'
```

JavaScript
```
fetch('https://app.coolify.io/api/v1/databases/dragonfly', {
 method: 'POST',
 headers: {
  Authorization: 'Bearer Bearer Token',
  'Content-Type': 'application/json'
 },
 body: JSON.stringify({
  server_uuid: 'string',
  project_uuid: 'string',
  environment_name: 'string',
  environment_uuid: 'string',
  destination_uuid: 'string',
  dragonfly_password: 'string',
  name: 'string',
  description: 'string',
  image: 'string',
  is_public: true,
  public_port: 0,
  limits_memory: 'string',
  limits_memory_swap: 'string',
  limits_memory_swappiness: 0,
  limits_memory_reservation: 'string',
  limits_cpus: 'string',
  limits_cpuset: 'string',
  limits_cpu_shares: 0,
  instant_deploy: true
 })
})
```

PHP
```
<?php
$curl = curl_init();
curl_setopt_array($curl, [
 CURLOPT_URL => "https://app.coolify.io/api/v1/databases/dragonfly",
 CURLOPT_RETURNTRANSFER => true,
 CURLOPT_ENCODING => "",
 CURLOPT_MAXREDIRS => 10,
 CURLOPT_TIMEOUT => 30,
 CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
 CURLOPT_CUSTOMREQUEST => "POST",
 CURLOPT_POSTFIELDS => "{\"server_uuid\":\"string\",\"project_uuid\":\"string\",\"environment_name\":\"string\",\"environment_uuid\":\"string\",\"destination_uuid\":\"string\",\"dragonfly_password\":\"string\",\"name\":\"string\",\"description\":\"string\",\"image\":\"string\",\"is_public\":true,\"public_port\":0,\"limits_memory\":\"string\",\"limits_memory_swap\":\"string\",\"limits_memory_swappiness\":0,\"limits_memory_reservation\":\"string\",\"limits_cpus\":\"string\",\"limits_cpuset\":\"string\",\"limits_cpu_shares\":0,\"instant_deploy\":true}",
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
payload = "{\"server_uuid\":\"string\",\"project_uuid\":\"string\",\"environment_name\":\"string\",\"environment_uuid\":\"string\",\"destination_uuid\":\"string\",\"dragonfly_password\":\"string\",\"name\":\"string\",\"description\":\"string\",\"image\":\"string\",\"is_public\":true,\"public_port\":0,\"limits_memory\":\"string\",\"limits_memory_swap\":\"string\",\"limits_memory_swappiness\":0,\"limits_memory_reservation\":\"string\",\"limits_cpus\":\"string\",\"limits_cpuset\":\"string\",\"limits_cpu_shares\":0,\"instant_deploy\":true}"
headers = {
  'Authorization': "Bearer Bearer Token",
  'Content-Type': "application/json"
}
conn.request("POST", "/api/v1/databases/dragonfly", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

Powered by  VitePress OpenAPI 
