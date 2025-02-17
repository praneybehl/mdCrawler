Skip to content
Menu
Return to top
# Create​
POST
/services
Create a one-click service
## Authorizations​
bearerAuth
Go to `Keys & Tokens` / `API tokens` and create a new token. Use the token as the bearer token.
TypeHTTP (bearer)
## Request Body​
SchemaJSON
JSON
{
"type": "string",
"name": "string",
"description": "string",
"project_uuid": "string",
"environment_name": "string",
"environment_uuid": "string",
"server_uuid": "string",
"destination_uuid": "string",
"instant_deploy": false
}
## Responses​
201400401
Create a service.
Content-Type
application/json
SchemaJSON
JSON
{
"uuid": "string",
"domains": [
"string"
]
}
POST
/services
Authorization 
bearerAuth
Body
{
type
:
string
name
:
string
description
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
server_uuid
:
string
destination_uuid
:
string
instant_deploy
:
false
}
Try it out
## Samples​
brunocURLJavaScriptPHPPython
bruno
```
POST https://app.coolify.io/api/v1/services
Headers
Content-Type: application/json
authorization: Bearer Bearer Token
Body
{
 "type": "string",
 "name": "string",
 "description": "string",
 "project_uuid": "string",
 "environment_name": "string",
 "environment_uuid": "string",
 "server_uuid": "string",
 "destination_uuid": "string",
 "instant_deploy": false
}
```

cURL
```
curl https://app.coolify.io/api/v1/services \
 --request POST \
 --header 'Authorization: Bearer Bearer Token' \
 --header 'Content-Type: application/json' \
 --data '{
 "type": "string",
 "name": "string",
 "description": "string",
 "project_uuid": "string",
 "environment_name": "string",
 "environment_uuid": "string",
 "server_uuid": "string",
 "destination_uuid": "string",
 "instant_deploy": false
}'
```

JavaScript
```
fetch('https://app.coolify.io/api/v1/services', {
 method: 'POST',
 headers: {
  Authorization: 'Bearer Bearer Token',
  'Content-Type': 'application/json'
 },
 body: JSON.stringify({
  type: 'string',
  name: 'string',
  description: 'string',
  project_uuid: 'string',
  environment_name: 'string',
  environment_uuid: 'string',
  server_uuid: 'string',
  destination_uuid: 'string',
  instant_deploy: false
 })
})
```

PHP
```
<?php
$curl = curl_init();
curl_setopt_array($curl, [
 CURLOPT_URL => "https://app.coolify.io/api/v1/services",
 CURLOPT_RETURNTRANSFER => true,
 CURLOPT_ENCODING => "",
 CURLOPT_MAXREDIRS => 10,
 CURLOPT_TIMEOUT => 30,
 CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
 CURLOPT_CUSTOMREQUEST => "POST",
 CURLOPT_POSTFIELDS => "{\"type\":\"string\",\"name\":\"string\",\"description\":\"string\",\"project_uuid\":\"string\",\"environment_name\":\"string\",\"environment_uuid\":\"string\",\"server_uuid\":\"string\",\"destination_uuid\":\"string\",\"instant_deploy\":false}",
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
payload = "{\"type\":\"string\",\"name\":\"string\",\"description\":\"string\",\"project_uuid\":\"string\",\"environment_name\":\"string\",\"environment_uuid\":\"string\",\"server_uuid\":\"string\",\"destination_uuid\":\"string\",\"instant_deploy\":false}"
headers = {
  'Authorization': "Bearer Bearer Token",
  'Content-Type': "application/json"
}
conn.request("POST", "/api/v1/services", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

Powered by  VitePress OpenAPI 
