Skip to content
Menu
Return to top
# Execute Command​
POST
/applications/{uuid}/execute
Execute a command on the application's current container.
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
"command": "string"
}
## Responses​
200400401404
Execute a command on the application's current container.
Content-Type
application/json
SchemaJSON
JSON
{
"message": "Command executed.",
"response": "string"
}
POST
/applications/{uuid}/execute
## Samples​
Powered by  VitePress OpenAPI 
