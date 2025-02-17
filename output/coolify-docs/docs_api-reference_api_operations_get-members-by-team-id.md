Skip to content
Menu
Return to top
# Members​
GET
/teams/{id}/members
Get members by TeamId.
## Authorizations​
bearerAuth
Go to `Keys & Tokens` / `API tokens` and create a new token. Use the token as the bearer token.
TypeHTTP (bearer)
## Parameters​
### Path Parameters
id*
Team ID
Typeinteger
Required
## Responses​
200400401404
List of members.
Content-Type
application/json
SchemaJSON
JSON
[
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
GET
/teams/{id}/members
## Samples​
Powered by  VitePress OpenAPI 
