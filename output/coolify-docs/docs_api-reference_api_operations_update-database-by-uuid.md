Skip to content
Menu
Return to top
# Update​
PATCH
/databases/{uuid}
Update database by UUID.
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
## Request Body​
SchemaJSON
JSON
{
"name": "string",
"description": "string",
"image": "string",
"is_public": true,
"public_port": 0,
"limits_memory": "string",
"limits_memory_swap": "string",
"limits_memory_swappiness": 0,
"limits_memory_reservation": "string",
"limits_cpus": "string",
"limits_cpuset": "string",
"limits_cpu_shares": 0,
"postgres_user": "string",
"postgres_password": "string",
"postgres_db": "string",
"postgres_initdb_args": "string",
"postgres_host_auth_method": "string",
"postgres_conf": "string",
"clickhouse_admin_user": "string",
"clickhouse_admin_password": "string",
"dragonfly_password": "string",
"redis_password": "string",
"redis_conf": "string",
"keydb_password": "string",
"keydb_conf": "string",
"mariadb_conf": "string",
"mariadb_root_password": "string",
"mariadb_user": "string",
"mariadb_password": "string",
"mariadb_database": "string",
"mongo_conf": "string",
"mongo_initdb_root_username": "string",
"mongo_initdb_root_password": "string",
"mongo_initdb_database": "string",
"mysql_root_password": "string",
"mysql_password": "string",
"mysql_user": "string",
"mysql_database": "string",
"mysql_conf": "string"
}
## Responses​
200400401404
Database updated
PATCH
/databases/{uuid}
Authorization 
bearerAuth
Variables
Key
Value
uuid*
Body
{
name
:
string
description
:
string
image
:
string
is_public
:
true
public_port
:
0
limits_memory
:
string
limits_memory_swap
:
string
limits_memory_swappiness
:
0
limits_memory_reservation
:
string
limits_cpus
:
string
limits_cpuset
:
string
limits_cpu_shares
:
0
postgres_user
:
string
postgres_password
:
string
postgres_db
:
string
postgres_initdb_args
:
string
postgres_host_auth_method
:
string
postgres_conf
:
string
clickhouse_admin_user
:
string
clickhouse_admin_password
:
string
dragonfly_password
:
string
redis_password
:
string
redis_conf
:
string
keydb_password
:
string
keydb_conf
:
string
mariadb_conf
:
string
mariadb_root_password
:
string
mariadb_user
:
string
mariadb_password
:
string
mariadb_database
:
string
mongo_conf
:
string
mongo_initdb_root_username
:
string
mongo_initdb_root_password
:
string
mongo_initdb_database
:
string
mysql_root_password
:
string
mysql_password
:
string
mysql_user
:
string
mysql_database
:
string
mysql_conf
:
string
}
Try it out
## Samples​
brunocURLJavaScriptPHPPython
bruno
```
PATCH https://app.coolify.io/api/v1/databases/{uuid}
Headers
Content-Type: application/json
authorization: Bearer Bearer Token
Body
{
 "name": "string",
 "description": "string",
 "image": "string",
 "is_public": true,
 "public_port": 0,
 "limits_memory": "string",
 "limits_memory_swap": "string",
 "limits_memory_swappiness": 0,
 "limits_memory_reservation": "string",
 "limits_cpus": "string",
 "limits_cpuset": "string",
 "limits_cpu_shares": 0,
 "postgres_user": "string",
 "postgres_password": "string",
 "postgres_db": "string",
 "postgres_initdb_args": "string",
 "postgres_host_auth_method": "string",
 "postgres_conf": "string",
 "clickhouse_admin_user": "string",
 "clickhouse_admin_password": "string",
 "dragonfly_password": "string",
 "redis_password": "string",
 "redis_conf": "string",
 "keydb_password": "string",
 "keydb_conf": "string",
 "mariadb_conf": "string",
 "mariadb_root_password": "string",
 "mariadb_user": "string",
 "mariadb_password": "string",
 "mariadb_database": "string",
 "mongo_conf": "string",
 "mongo_initdb_root_username": "string",
 "mongo_initdb_root_password": "string",
 "mongo_initdb_database": "string",
 "mysql_root_password": "string",
 "mysql_password": "string",
 "mysql_user": "string",
 "mysql_database": "string",
 "mysql_conf": "string"
}
```

cURL
```
curl 'https://app.coolify.io/api/v1/databases/%7Buuid%7D' \
 --request PATCH \
 --header 'Authorization: Bearer Bearer Token' \
 --header 'Content-Type: application/json' \
 --data '{
 "name": "string",
 "description": "string",
 "image": "string",
 "is_public": true,
 "public_port": 0,
 "limits_memory": "string",
 "limits_memory_swap": "string",
 "limits_memory_swappiness": 0,
 "limits_memory_reservation": "string",
 "limits_cpus": "string",
 "limits_cpuset": "string",
 "limits_cpu_shares": 0,
 "postgres_user": "string",
 "postgres_password": "string",
 "postgres_db": "string",
 "postgres_initdb_args": "string",
 "postgres_host_auth_method": "string",
 "postgres_conf": "string",
 "clickhouse_admin_user": "string",
 "clickhouse_admin_password": "string",
 "dragonfly_password": "string",
 "redis_password": "string",
 "redis_conf": "string",
 "keydb_password": "string",
 "keydb_conf": "string",
 "mariadb_conf": "string",
 "mariadb_root_password": "string",
 "mariadb_user": "string",
 "mariadb_password": "string",
 "mariadb_database": "string",
 "mongo_conf": "string",
 "mongo_initdb_root_username": "string",
 "mongo_initdb_root_password": "string",
 "mongo_initdb_database": "string",
 "mysql_root_password": "string",
 "mysql_password": "string",
 "mysql_user": "string",
 "mysql_database": "string",
 "mysql_conf": "string"
}'
```

JavaScript
```
fetch('https://app.coolify.io/api/v1/databases/%7Buuid%7D', {
 method: 'PATCH',
 headers: {
  Authorization: 'Bearer Bearer Token',
  'Content-Type': 'application/json'
 },
 body: JSON.stringify({
  name: 'string',
  description: 'string',
  image: 'string',
  is_public: true,
  public_port: 0,
  limits_memory: 'string',
  limits_memory_swap: 'string',
  limits_memory_swappiness: 0,
  limits_memory_reservation: 'string',
  limits_cpus: 'string',
  limits_cpuset: 'string',
  limits_cpu_shares: 0,
  postgres_user: 'string',
  postgres_password: 'string',
  postgres_db: 'string',
  postgres_initdb_args: 'string',
  postgres_host_auth_method: 'string',
  postgres_conf: 'string',
  clickhouse_admin_user: 'string',
  clickhouse_admin_password: 'string',
  dragonfly_password: 'string',
  redis_password: 'string',
  redis_conf: 'string',
  keydb_password: 'string',
  keydb_conf: 'string',
  mariadb_conf: 'string',
  mariadb_root_password: 'string',
  mariadb_user: 'string',
  mariadb_password: 'string',
  mariadb_database: 'string',
  mongo_conf: 'string',
  mongo_initdb_root_username: 'string',
  mongo_initdb_root_password: 'string',
  mongo_initdb_database: 'string',
  mysql_root_password: 'string',
  mysql_password: 'string',
  mysql_user: 'string',
  mysql_database: 'string',
  mysql_conf: 'string'
 })
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
 CURLOPT_CUSTOMREQUEST => "PATCH",
 CURLOPT_POSTFIELDS => "{\"name\":\"string\",\"description\":\"string\",\"image\":\"string\",\"is_public\":true,\"public_port\":0,\"limits_memory\":\"string\",\"limits_memory_swap\":\"string\",\"limits_memory_swappiness\":0,\"limits_memory_reservation\":\"string\",\"limits_cpus\":\"string\",\"limits_cpuset\":\"string\",\"limits_cpu_shares\":0,\"postgres_user\":\"string\",\"postgres_password\":\"string\",\"postgres_db\":\"string\",\"postgres_initdb_args\":\"string\",\"postgres_host_auth_method\":\"string\",\"postgres_conf\":\"string\",\"clickhouse_admin_user\":\"string\",\"clickhouse_admin_password\":\"string\",\"dragonfly_password\":\"string\",\"redis_password\":\"string\",\"redis_conf\":\"string\",\"keydb_password\":\"string\",\"keydb_conf\":\"string\",\"mariadb_conf\":\"string\",\"mariadb_root_password\":\"string\",\"mariadb_user\":\"string\",\"mariadb_password\":\"string\",\"mariadb_database\":\"string\",\"mongo_conf\":\"string\",\"mongo_initdb_root_username\":\"string\",\"mongo_initdb_root_password\":\"string\",\"mongo_initdb_database\":\"string\",\"mysql_root_password\":\"string\",\"mysql_password\":\"string\",\"mysql_user\":\"string\",\"mysql_database\":\"string\",\"mysql_conf\":\"string\"}",
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
payload = "{\"name\":\"string\",\"description\":\"string\",\"image\":\"string\",\"is_public\":true,\"public_port\":0,\"limits_memory\":\"string\",\"limits_memory_swap\":\"string\",\"limits_memory_swappiness\":0,\"limits_memory_reservation\":\"string\",\"limits_cpus\":\"string\",\"limits_cpuset\":\"string\",\"limits_cpu_shares\":0,\"postgres_user\":\"string\",\"postgres_password\":\"string\",\"postgres_db\":\"string\",\"postgres_initdb_args\":\"string\",\"postgres_host_auth_method\":\"string\",\"postgres_conf\":\"string\",\"clickhouse_admin_user\":\"string\",\"clickhouse_admin_password\":\"string\",\"dragonfly_password\":\"string\",\"redis_password\":\"string\",\"redis_conf\":\"string\",\"keydb_password\":\"string\",\"keydb_conf\":\"string\",\"mariadb_conf\":\"string\",\"mariadb_root_password\":\"string\",\"mariadb_user\":\"string\",\"mariadb_password\":\"string\",\"mariadb_database\":\"string\",\"mongo_conf\":\"string\",\"mongo_initdb_root_username\":\"string\",\"mongo_initdb_root_password\":\"string\",\"mongo_initdb_database\":\"string\",\"mysql_root_password\":\"string\",\"mysql_password\":\"string\",\"mysql_user\":\"string\",\"mysql_database\":\"string\",\"mysql_conf\":\"string\"}"
headers = {
  'Authorization': "Bearer Bearer Token",
  'Content-Type': "application/json"
}
conn.request("PATCH", "/api/v1/databases/%7Buuid%7D", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

Powered by  VitePress OpenAPI 
