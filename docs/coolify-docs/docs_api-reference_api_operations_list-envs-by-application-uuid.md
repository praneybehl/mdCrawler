Skip to content
Menu
Return to top
# List Envs​
GET
/applications/{uuid}/envs
List all envs by application UUID.
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
All environment variables by application UUID.
Content-Type
application/json
SchemaJSON
JSON
[
{
"id": 0,
"uuid": "string",
"resourceable_type": "string",
"resourceable_id": 0,
"is_build_time": true,
"is_literal": true,
"is_multiline": true,
"is_preview": true,
"is_shared": true,
"is_shown_once": true,
"key": "string",
"value": "string",
"real_value": "string",
"version": "string",
"created_at": "string",
"updated_at": "string"
}
]
GET
/applications/{uuid}/envs
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
GET https://app.coolify.io/api/v1/applications/{uuid}/envs
Headers
Content-Type: application/json
authorization: Bearer Bearer Token

```

cURL
```
curl 'https://app.coolify.io/api/v1/applications/%7Buuid%7D/envs' \
 --header 'Authorization: Bearer Bearer Token' \
 --header 'Content-Type: application/json'
```

JavaScript
```
fetch('https://app.coolify.io/api/v1/applications/%7Buuid%7D/envs', {
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
 CURLOPT_URL => "https://app.coolify.io/api/v1/applications/%7Buuid%7D/envs",
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
conn.request("GET", "/api/v1/applications/%7Buuid%7D/envs", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

Powered by  VitePress OpenAPI 
