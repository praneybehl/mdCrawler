Skip to content
Menu
Return to top
# Delete​
DELETE
/databases/{uuid}
Delete database by UUID.
## Authorizations​
bearerAuth
Go to `Keys & Tokens` / `API tokens` and create a new token. Use the token as the bearer token.
TypeHTTP (bearer)
## Parameters​
### Path Parameters
uuid*
UUID of the database.
Typestring
Required
format`uuid`
### Query Parameters
delete_configurations
Delete configurations.
Typeboolean
default`true`
delete_volumes
Delete volumes.
Typeboolean
default`true`
docker_cleanup
Run docker cleanup.
Typeboolean
default`true`
delete_connected_networks
Delete connected networks.
Typeboolean
default`true`
## Responses​
200400401404
Database deleted.
Content-Type
application/json
SchemaJSON
JSON
{
"message": "Database deleted."
}
DELETE
/databases/{uuid}
Authorization 
bearerAuth
Variables
Key
Value
uuid*
delete_configurations
delete_volumes
docker_cleanup
delete_connected_networks
Try it out
## Samples​
brunocURLJavaScriptPHPPython
bruno
```
DELETE https://app.coolify.io/api/v1/databases/{uuid}
Headers
Content-Type: application/json
authorization: Bearer Bearer Token

```

cURL
```
curl 'https://app.coolify.io/api/v1/databases/%7Buuid%7D' \
 --request DELETE \
 --header 'Authorization: Bearer Bearer Token' \
 --header 'Content-Type: application/json'
```

JavaScript
```
fetch('https://app.coolify.io/api/v1/databases/%7Buuid%7D', {
 method: 'DELETE',
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
 CURLOPT_URL => "https://app.coolify.io/api/v1/databases/%7Buuid%7D",
 CURLOPT_RETURNTRANSFER => true,
 CURLOPT_ENCODING => "",
 CURLOPT_MAXREDIRS => 10,
 CURLOPT_TIMEOUT => 30,
 CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
 CURLOPT_CUSTOMREQUEST => "DELETE",
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
conn.request("DELETE", "/api/v1/databases/%7Buuid%7D", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

Powered by  VitePress OpenAPI 
