Skip to content
Menu
Return to top
# Get​
GET
/deployments/{uuid}
Get deployment by UUID.
## Authorizations​
bearerAuth
Go to `Keys & Tokens` / `API tokens` and create a new token. Use the token as the bearer token.
TypeHTTP (bearer)
## Parameters​
### Path Parameters
uuid*
Deployment UUID
Typestring
Required
## Responses​
200400401404
Get deployment by UUID.
Content-Type
application/json
SchemaJSON
JSON
{
"id": 0,
"application_id": "string",
"deployment_uuid": "string",
"pull_request_id": 0,
"force_rebuild": true,
"commit": "string",
"status": "string",
"is_webhook": true,
"is_api": true,
"created_at": "string",
"updated_at": "string",
"logs": "string",
"current_process_id": "string",
"restart_only": true,
"git_type": "string",
"server_id": 0,
"application_name": "string",
"server_name": "string",
"deployment_url": "string",
"destination_id": "string",
"only_this_server": true,
"rollback": true,
"commit_message": "string"
}
GET
/deployments/{uuid}
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
GET https://app.coolify.io/api/v1/deployments/{uuid}
Headers
Content-Type: application/json
authorization: Bearer Bearer Token

```

cURL
```
curl 'https://app.coolify.io/api/v1/deployments/%7Buuid%7D' \
 --header 'Authorization: Bearer Bearer Token' \
 --header 'Content-Type: application/json'
```

JavaScript
```
fetch('https://app.coolify.io/api/v1/deployments/%7Buuid%7D', {
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
 CURLOPT_URL => "https://app.coolify.io/api/v1/deployments/%7Buuid%7D",
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
conn.request("GET", "/api/v1/deployments/%7Buuid%7D", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

Powered by  VitePress OpenAPI 
