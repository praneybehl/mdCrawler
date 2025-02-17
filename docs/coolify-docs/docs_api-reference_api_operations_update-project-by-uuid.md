Skip to content
Menu
Return to top
# Update​
PATCH
/projects/{uuid}
Update Project.
## Authorizations​
bearerAuth
Go to `Keys & Tokens` / `API tokens` and create a new token. Use the token as the bearer token.
TypeHTTP (bearer)
## Request Body​
SchemaJSON
JSON
{
"name": "string",
"description": "string"
}
## Responses​
201400401404
Project updated.
Content-Type
application/json
SchemaJSON
JSON
{
"uuid": "og888os",
"name": "Project Name",
"description": "Project Description"
}
PATCH
/projects/{uuid}
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
}
Try it out
## Samples​
brunocURLJavaScriptPHPPython
bruno
```
PATCH https://app.coolify.io/api/v1/projects/{uuid}
Headers
Content-Type: application/json
authorization: Bearer Bearer Token
Body
{
 "name": "string",
 "description": "string"
}
```

cURL
```
curl 'https://app.coolify.io/api/v1/projects/%7Buuid%7D' \
 --request PATCH \
 --header 'Authorization: Bearer Bearer Token' \
 --header 'Content-Type: application/json' \
 --data '{
 "name": "string",
 "description": "string"
}'
```

JavaScript
```
fetch('https://app.coolify.io/api/v1/projects/%7Buuid%7D', {
 method: 'PATCH',
 headers: {
  Authorization: 'Bearer Bearer Token',
  'Content-Type': 'application/json'
 },
 body: JSON.stringify({
  name: 'string',
  description: 'string'
 })
})
```

PHP
```
<?php
$curl = curl_init();
curl_setopt_array($curl, [
 CURLOPT_URL => "https://app.coolify.io/api/v1/projects/%7Buuid%7D",
 CURLOPT_RETURNTRANSFER => true,
 CURLOPT_ENCODING => "",
 CURLOPT_MAXREDIRS => 10,
 CURLOPT_TIMEOUT => 30,
 CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
 CURLOPT_CUSTOMREQUEST => "PATCH",
 CURLOPT_POSTFIELDS => "{\"name\":\"string\",\"description\":\"string\"}",
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
payload = "{\"name\":\"string\",\"description\":\"string\"}"
headers = {
  'Authorization': "Bearer Bearer Token",
  'Content-Type': "application/json"
}
conn.request("PATCH", "/api/v1/projects/%7Buuid%7D", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

Powered by  VitePress OpenAPI 
