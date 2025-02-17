Skip to content
Menu
Return to top
# Update Env​
PATCH
/services/{uuid}/envs
Update env by service UUID.
## Authorizations​
bearerAuth
Go to `Keys & Tokens` / `API tokens` and create a new token. Use the token as the bearer token.
TypeHTTP (bearer)
## Parameters​
### Path Parameters
uuid*
UUID of the service.
Typestring
Required
format`uuid`
## Request Body​
SchemaJSON
JSON
{
"key": "string",
"value": "string",
"is_preview": true,
"is_build_time": true,
"is_literal": true,
"is_multiline": true,
"is_shown_once": true
}
## Responses​
201400401404
Environment variable updated.
Content-Type
application/json
SchemaJSON
JSON
{
"message": "Environment variable updated."
}
PATCH
/services/{uuid}/envs
Authorization 
bearerAuth
Variables
Key
Value
uuid*
Body
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
Try it out
## Samples​
brunocURLJavaScriptPHPPython
bruno
```
PATCH https://app.coolify.io/api/v1/services/{uuid}/envs
Headers
Content-Type: application/json
authorization: Bearer Bearer Token
Body
{
 "key": "string",
 "value": "string",
 "is_preview": true,
 "is_build_time": true,
 "is_literal": true,
 "is_multiline": true,
 "is_shown_once": true
}
```

cURL
```
curl 'https://app.coolify.io/api/v1/services/%7Buuid%7D/envs' \
 --request PATCH \
 --header 'Authorization: Bearer Bearer Token' \
 --header 'Content-Type: application/json' \
 --data '{
 "key": "string",
 "value": "string",
 "is_preview": true,
 "is_build_time": true,
 "is_literal": true,
 "is_multiline": true,
 "is_shown_once": true
}'
```

JavaScript
```
fetch('https://app.coolify.io/api/v1/services/%7Buuid%7D/envs', {
 method: 'PATCH',
 headers: {
  Authorization: 'Bearer Bearer Token',
  'Content-Type': 'application/json'
 },
 body: JSON.stringify({
  key: 'string',
  value: 'string',
  is_preview: true,
  is_build_time: true,
  is_literal: true,
  is_multiline: true,
  is_shown_once: true
 })
})
```

PHP
```
<?php
$curl = curl_init();
curl_setopt_array($curl, [
 CURLOPT_URL => "https://app.coolify.io/api/v1/services/%7Buuid%7D/envs",
 CURLOPT_RETURNTRANSFER => true,
 CURLOPT_ENCODING => "",
 CURLOPT_MAXREDIRS => 10,
 CURLOPT_TIMEOUT => 30,
 CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
 CURLOPT_CUSTOMREQUEST => "PATCH",
 CURLOPT_POSTFIELDS => "{\"key\":\"string\",\"value\":\"string\",\"is_preview\":true,\"is_build_time\":true,\"is_literal\":true,\"is_multiline\":true,\"is_shown_once\":true}",
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
payload = "{\"key\":\"string\",\"value\":\"string\",\"is_preview\":true,\"is_build_time\":true,\"is_literal\":true,\"is_multiline\":true,\"is_shown_once\":true}"
headers = {
  'Authorization': "Bearer Bearer Token",
  'Content-Type': "application/json"
}
conn.request("PATCH", "/api/v1/services/%7Buuid%7D/envs", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

Powered by  VitePress OpenAPI 
