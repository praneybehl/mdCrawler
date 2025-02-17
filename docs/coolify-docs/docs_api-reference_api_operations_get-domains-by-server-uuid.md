Skip to content
Menu
Return to top
# Domains​
GET
/servers/{uuid}/domains
Get domains by server.
## Authorizations​
bearerAuth
Go to `Keys & Tokens` / `API tokens` and create a new token. Use the token as the bearer token.
TypeHTTP (bearer)
## Parameters​
### Path Parameters
uuid*
Server's UUID
Typestring
Required
## Responses​
200400401
Get domains by server
Content-Type
application/json
SchemaJSON
JSON
[
{
"ip": "string",
"domains": [
"string"
]
}
]
GET
/servers/{uuid}/domains
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
GET https://app.coolify.io/api/v1/servers/{uuid}/domains
Headers
Content-Type: application/json
authorization: Bearer Bearer Token

```

cURL
```
curl 'https://app.coolify.io/api/v1/servers/%7Buuid%7D/domains' \
 --header 'Authorization: Bearer Bearer Token' \
 --header 'Content-Type: application/json'
```

JavaScript
```
fetch('https://app.coolify.io/api/v1/servers/%7Buuid%7D/domains', {
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
 CURLOPT_URL => "https://app.coolify.io/api/v1/servers/%7Buuid%7D/domains",
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
conn.request("GET", "/api/v1/servers/%7Buuid%7D/domains", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

Powered by  VitePress OpenAPI 
