Skip to content
Menu
Return to top
# Create​
POST
/security/keys
Create a new private key.
## Authorizations​
bearerAuth
Go to `Keys & Tokens` / `API tokens` and create a new token. Use the token as the bearer token.
TypeHTTP (bearer)
## Request Body​
SchemaJSON
JSON
{
"name": "string",
"description": "string",
"private_key": "string"
}
## Responses​
201400401
The created private key's UUID.
Content-Type
application/json
SchemaJSON
JSON
{
"uuid": "string"
}
POST
/security/keys
Authorization 
bearerAuth
Body
{
name
:
string
description
:
string
private_key
:
string
}
Try it out
## Samples​
brunocURLJavaScriptPHPPython
bruno
```
POST https://app.coolify.io/api/v1/security/keys
Headers
Content-Type: application/json
authorization: Bearer Bearer Token
Body
{
 "name": "string",
 "description": "string",
 "private_key": "string"
}
```

cURL
```
curl https://app.coolify.io/api/v1/security/keys \
 --request POST \
 --header 'Authorization: Bearer Bearer Token' \
 --header 'Content-Type: application/json' \
 --data '{
 "name": "string",
 "description": "string",
 "private_key": "string"
}'
```

JavaScript
```
fetch('https://app.coolify.io/api/v1/security/keys', {
 method: 'POST',
 headers: {
  Authorization: 'Bearer Bearer Token',
  'Content-Type': 'application/json'
 },
 body: JSON.stringify({
  name: 'string',
  description: 'string',
  private_key: 'string'
 })
})
```

PHP
```
<?php
$curl = curl_init();
curl_setopt_array($curl, [
 CURLOPT_URL => "https://app.coolify.io/api/v1/security/keys",
 CURLOPT_RETURNTRANSFER => true,
 CURLOPT_ENCODING => "",
 CURLOPT_MAXREDIRS => 10,
 CURLOPT_TIMEOUT => 30,
 CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
 CURLOPT_CUSTOMREQUEST => "POST",
 CURLOPT_POSTFIELDS => "{\"name\":\"string\",\"description\":\"string\",\"private_key\":\"string\"}",
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
payload = "{\"name\":\"string\",\"description\":\"string\",\"private_key\":\"string\"}"
headers = {
  'Authorization': "Bearer Bearer Token",
  'Content-Type': "application/json"
}
conn.request("POST", "/api/v1/security/keys", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

Powered by  VitePress OpenAPI 
