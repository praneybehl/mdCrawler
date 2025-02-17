Skip to content
Menu
Return to top
# Environment​
GET
/projects/{uuid}/{environment_name_or_uuid}
Get environment by name or UUID.
## Authorizations​
bearerAuth
Go to `Keys & Tokens` / `API tokens` and create a new token. Use the token as the bearer token.
TypeHTTP (bearer)
## Parameters​
### Path Parameters
uuid*
Project UUID
Typestring
Required
environment_name_or_uuid*
Environment name or UUID
Typestring
Required
## Responses​
200400401404
Environment details
Content-Type
application/json
SchemaJSON
JSON
{
"id": 0,
"name": "string",
"project_id": 0,
"created_at": "string",
"updated_at": "string",
"description": "string"
}
GET
/projects/{uuid}/{environment_name_or_uuid}
## Samples​
Powered by  VitePress OpenAPI 
