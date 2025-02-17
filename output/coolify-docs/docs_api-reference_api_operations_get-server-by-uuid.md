Skip to content
Menu
Return to top
# Get​
GET
/servers/{uuid}
Get server by UUID.
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
200400401404
Get server by UUID
Content-Type
application/json
SchemaJSON
JSON
{
"id": 0,
"uuid": "string",
"name": "string",
"description": "string",
"ip": "string",
"user": "string",
"port": 0,
"proxy": {
},
"proxy_type": "string",
"high_disk_usage_notification_sent": true,
"unreachable_notification_sent": true,
"unreachable_count": 0,
"validation_logs": "string",
"log_drain_notification_sent": true,
"swarm_cluster": "string",
"settings": {
"id": 0,
"concurrent_builds": 0,
"dynamic_timeout": 0,
"force_disabled": true,
"force_server_cleanup": true,
"is_build_server": true,
"is_cloudflare_tunnel": true,
"is_jump_server": true,
"is_logdrain_axiom_enabled": true,
"is_logdrain_custom_enabled": true,
"is_logdrain_highlight_enabled": true,
"is_logdrain_newrelic_enabled": true,
"is_metrics_enabled": true,
"is_reachable": true,
"is_sentinel_enabled": true,
"is_swarm_manager": true,
"is_swarm_worker": true,
"is_usable": true,
"logdrain_axiom_api_key": "string",
"logdrain_axiom_dataset_name": "string",
"logdrain_custom_config": "string",
"logdrain_custom_config_parser": "string",
"logdrain_highlight_project_id": "string",
"logdrain_newrelic_base_uri": "string",
"logdrain_newrelic_license_key": "string",
"sentinel_metrics_history_days": 0,
"sentinel_metrics_refresh_rate_seconds": 0,
"sentinel_token": "string",
"docker_cleanup_frequency": "string",
"docker_cleanup_threshold": 0,
"server_id": 0,
"wildcard_domain": "string",
"created_at": "string",
"updated_at": "string",
"delete_unused_volumes": true,
"delete_unused_networks": true
}
}
GET
/servers/{uuid}
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
GET https://app.coolify.io/api/v1/servers/{uuid}
Headers
Content-Type: application/json
authorization: Bearer Bearer Token

```

cURL
```
curl 'https://app.coolify.io/api/v1/servers/%7Buuid%7D' \
 --header 'Authorization: Bearer Bearer Token' \
 --header 'Content-Type: application/json'
```

JavaScript
```
fetch('https://app.coolify.io/api/v1/servers/%7Buuid%7D', {
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
 CURLOPT_URL => "https://app.coolify.io/api/v1/servers/%7Buuid%7D",
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
conn.request("GET", "/api/v1/servers/%7Buuid%7D", headers=headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

Powered by  VitePress OpenAPI 
