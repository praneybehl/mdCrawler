Skip to content
Menu
Return to top
# Create​
POST
/servers
Create Server.
## Authorizations​
bearerAuth
Go to `Keys & Tokens` / `API tokens` and create a new token. Use the token as the bearer token.
TypeHTTP (bearer)
## Request Body​
SchemaJSON
JSON
{
"name": "My Server",
"description": "My Server Description",
"ip": "127.0.0.1",
"port": 22,
"user": "root",
"private_key_uuid": "og888os",
"is_build_server": false,
"instant_validate": false,
"proxy_type": "string"
}
## Responses​
201400401404
Server created.
Content-Type
application/json
SchemaJSON
JSON
{
"uuid": "og888os"
}
POST
/servers
Authorization 
bearerAuth
Body
{
name
:
My Server
description
:
My Server Description
ip
:
127.0.0.1
port
:
22
user
:
root
private_key_uuid
:
og888os
is_build_server
:
false
instant_validate
:
false
proxy_type
:
string
}
Try it out
## Samples​
brunocURLJavaScriptPHPPython
bruno
```
POST https://app.coolify.io/api/v1/servers
Headers
Content-Type: application/json
authorization: Bearer Bearer Token
Body
{
 "name": "My Server",
 "description": "My Server Description",
 "ip": "127.0.0.1",
 "port": 22,
 "user": "root",
 "private_key_uuid": "og888os",
 "is_build_server": false,
 "instant_validate": false,
 "proxy_type": "string"
}
```

cURL
```
curl https://app.coolify.io/api/v1/servers \
 --request POST \
 --header 'Authorization: Bearer Bearer Token' \
 --header 'Content-Type: application/json' \
 --data '{
 "name": "My Server",
 "description": "My Server Description",
 "ip": "127.0.0.1",
 "port": 22,
 "user": "root",
 "private_key_uuid": "og888os",
 "is_build_server": false,
 "instant_validate": false,
 "proxy_type": "string"
}'
```

JavaScript
```
fetch('https://app.coolify.io/api/v1/servers', {
 method: 'POST',
 headers: {
  Authorization: 'Bearer Bearer Token',
  'Content-Type': 'application/json'
 },
 body: JSON.stringify({
  name: 'My Server',
  description: 'My Server Description',
  ip: '127.0.0.1',
  port: 22,
  user: 'root',
  private_key_uuid: 'og888os',
  is_build_server: false,
  instant_validate: false,
  proxy_type: 'string'
 })
})
```

PHP
```
<?php
$curl = curl_init();
curl_setopt_array($curl, [
 CURLOPT_URL => "https://app.coolify.io/api/v1/servers",
 CURLOPT_RETURNTRANSFER => true,
 CURLOPT_ENCODING => "",
 CURLOPT_MAXREDIRS => 10,
 CURLOPT_TIMEOUT => 30,
 CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
 CURLOPT_CUSTOMREQUEST => "POST",
 CURLOPT_POSTFIELDS => "{\"name\":\"My Server\",\"description\":\"My Server Description\",\"ip\":\"127.0.0.1\",\"port\":22,\"user\":\"root\",\"private_key_uuid\":\"og888os\",\"is_build_server\":false,\"instant_validate\":false,\"proxy_type\":\"string\"}",
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
payload = "{\"name\":\"My Server\",\"description\":\"My Server Description\",\"ip\":\"127.0.0.1\",\"port\":22,\"user\":\"root\",\"private_key_uuid\":\"og888os\",\"is_build_server\":false,\"instant_validate\":false,\"proxy_type\":\"string\"}"
headers = {
  'Authorization': "Bearer Bearer Token",
  'Content-Type': "application/json"
}
conn.request("POST", "/api/v1/servers", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

Powered by  VitePress OpenAPI 
