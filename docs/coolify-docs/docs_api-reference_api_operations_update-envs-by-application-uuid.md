Skip to content
Menu
Return to top
# Update Envs (Bulk)​
PATCH
/applications/{uuid}/envs/bulk
Update multiple envs by application UUID.
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
## Request Body​
SchemaJSON
JSON
{
"data": [
{
"key": "string",
"value": "string",
"is_preview": true,
"is_build_time": true,
"is_literal": true,
"is_multiline": true,
"is_shown_once": true
}
]
}
## Responses​
201400401404
Environment variables updated.
Content-Type
application/json
SchemaJSON
JSON
{
"message": "Environment variables updated."
}
PATCH
/applications/{uuid}/envs/bulk
Authorization 
bearerAuth
Variables
Key
Value
uuid*
Body
{
data
:
[
1 item
0
:
{
key
:
string
value
:
string
is_preview
:
true
is_build_time
:
true
is_literal
:
true
is_multiline
:
true
is_shown_once
:
true
}
]
}
Try it out
## Samples​
brunocURLJavaScriptPHPPython
bruno
```
PATCH https://app.coolify.io/api/v1/applications/{uuid}/envs/bulk
Headers
Content-Type: application/json
authorization: Bearer Bearer Token
Body
{
 "data": [
  {
   "key": "string",
   "value": "string",
   "is_preview": true,
   "is_build_time": true,
   "is_literal": true,
   "is_multiline": true,
   "is_shown_once": true
  }
 ]
}
```

cURL
```
curl 'https://app.coolify.io/api/v1/applications/%7Buuid%7D/envs/bulk' \
 --request PATCH \
 --header 'Authorization: Bearer Bearer Token' \
 --header 'Content-Type: application/json' \
 --data '{
 "data": [
  {
   "key": "string",
   "value": "string",
   "is_preview": true,
   "is_build_time": true,
   "is_literal": true,
   "is_multiline": true,
   "is_shown_once": true
  }
 ]
}'
```

JavaScript
```
fetch('https://app.coolify.io/api/v1/applications/%7Buuid%7D/envs/bulk', {
 method: 'PATCH',
 headers: {
  Authorization: 'Bearer Bearer Token',
  'Content-Type': 'application/json'
 },
 body: JSON.stringify({
  data: [{
   key: 'string',
   value: 'string',
   is_preview: true,
   is_build_time: true,
   is_literal: true,
   is_multiline: true,
   is_shown_once: true
  }]
 })
})
```

PHP
```
<?php
$curl = curl_init();
curl_setopt_array($curl, [
 CURLOPT_URL => "https://app.coolify.io/api/v1/applications/%7Buuid%7D/envs/bulk",
 CURLOPT_RETURNTRANSFER => true,
 CURLOPT_ENCODING => "",
 CURLOPT_MAXREDIRS => 10,
 CURLOPT_TIMEOUT => 30,
 CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
 CURLOPT_CUSTOMREQUEST => "PATCH",
 CURLOPT_POSTFIELDS => "{\"data\":[{\"key\":\"string\",\"value\":\"string\",\"is_preview\":true,\"is_build_time\":true,\"is_literal\":true,\"is_multiline\":true,\"is_shown_once\":true}]}",
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
payload = "{\"data\":[{\"key\":\"string\",\"value\":\"string\",\"is_preview\":true,\"is_build_time\":true,\"is_literal\":true,\"is_multiline\":true,\"is_shown_once\":true}]}"
headers = {
  'Authorization': "Bearer Bearer Token",
  'Content-Type': "application/json"
}
conn.request("PATCH", "/api/v1/applications/%7Buuid%7D/envs/bulk", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

Powered by  VitePress OpenAPI 
