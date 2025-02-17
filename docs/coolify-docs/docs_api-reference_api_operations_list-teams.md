Skip to content
Menu
Return to top
# List​
GET
/teams
Get all teams.
## Authorizations​
bearerAuth
Go to `Keys & Tokens` / `API tokens` and create a new token. Use the token as the bearer token.
TypeHTTP (bearer)
## Responses​
200400401
List of teams.
Content-Type
application/json
SchemaJSON
JSON
[
{
"id": 0,
"name": "string",
"description": "string",
"personal_team": true,
"created_at": "string",
"updated_at": "string",
"show_boarding": true,
"custom_server_limit": "string",
"members": [
{
"id": 0,
"name": "string",
"email": "string",
"email_verified_at": "string",
"created_at": "string",
"updated_at": "string",
"two_factor_confirmed_at": "string",
"force_password_reset": true,
"marketing_emails": true
}
]
}
]
GET
/teams
Authorization 
bearerAuth
Try it out
## Samples​
brunocURLJavaScriptPHPPython
bruno
```
GET https://app.coolify.io/api/v1/teams
Headers
Content-Type: application/json
authorization: Bearer Bearer Token

```

cURL
```
curl https://app.coolify.io/api/v1/teams \
 --header 'Authorization: Bearer Bearer Token' \
 --header 'Content-Type: application/json'
```

JavaScript
```
fetch('https://app.coolify.io/api/v1/teams', {
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
 CURLOPT_URL => "https://app.coolify.io/api/v1/teams",
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
conn.request("GET", "/api/v1/teams", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

Powered by  VitePress OpenAPI 
