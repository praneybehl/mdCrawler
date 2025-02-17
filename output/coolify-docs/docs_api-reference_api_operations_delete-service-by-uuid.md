Skip to content
Menu
Return to top
# Delete​
DELETE
/services/{uuid}
Delete service by UUID.
## Authorizations​
bearerAuth
Go to `Keys & Tokens` / `API tokens` and create a new token. Use the token as the bearer token.
TypeHTTP (bearer)
## Parameters​
### Path Parameters
uuid*
Service UUID
Typestring
Required
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
Delete a service by UUID
Content-Type
application/json
SchemaJSON
JSON
{
"message": "Service deletion request queued."
}
DELETE
/services/{uuid}
## Samples​
Powered by  VitePress OpenAPI 
