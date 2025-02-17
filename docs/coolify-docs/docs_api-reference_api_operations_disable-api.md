Skip to content
Menu
Return to top
# Disable API​
GET
/disable
Disable API (only with root permissions).
## Authorizations​
bearerAuth
Go to `Keys & Tokens` / `API tokens` and create a new token. Use the token as the bearer token.
TypeHTTP (bearer)
## Responses​
200400401403
Disable API.
Content-Type
application/json
SchemaJSON
JSON
{
"message": "API disabled."
}
GET
/disable
Authorization 
bearerAuth
Try it out
## Samples​
brunocURLJavaScriptPHPPython
bruno
```
GET https://app.coolify.io/api/v1/disable
Headers
Content-Type: application/json
authorization: Bearer Bearer Token

```

cURL
```
curl https://app.coolify.io/api/v1/disable \
 --header 'Authorization: Bearer Bearer Token' \
 --header 'Content-Type: application/json'
```

JavaScript
```
fetch('https://app.coolify.io/api/v1/disable', {
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
 CURLOPT_URL => "https://app.coolify.io/api/v1/disable",
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
conn.request("GET", "/api/v1/disable", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

Powered by  VitePress OpenAPI 
