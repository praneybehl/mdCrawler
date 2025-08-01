API Records
###  CRUD actions 
**List/Search records**
Returns a paginated records list, supporting sorting and filtering.
Depending on the collection's `listRule` value, the access to this action may or may not have been restricted.
_You could find individual generated records API documentation in the "Dashboard > Collections > API Preview"._
JavaScript
Dart
`import PocketBase from 'pocketbase'; const pb = new PocketBase('http://127.0.0.1:8090'); ... // fetch a paginated records list const resultList = await pb.collection('posts').getList(1, 50, { filter: 'created >= "2022-01-01 00:00:00" && someField1 != someField2', }); // you can also fetch all records at once via getFullList const records = await pb.collection('posts').getFullList({ sort: '-created', }); // or fetch only the first record that matches the specified filter const record = await pb.collection('posts').getFirstListItem('someField="test"', { expand: 'relField1,relField2.subRelField', });`
`import 'package:pocketbase/pocketbase.dart'; final pb = PocketBase('http://127.0.0.1:8090'); ... // fetch a paginated records list final resultList = await pb.collection('posts').getList(  page: 1,  perPage: 50,  filter: 'created >= "2022-01-01 00:00:00" && someField1 != someField2', ); // you can also fetch all records at once via getFullList final records = await pb.collection('posts').getFullList(sort: '-created'); // or fetch only the first record that matches the specified filter final record = await pb.collection('posts').getFirstListItem( 'someField="test"',  expand: 'relField1,relField2.subRelField', );`
###### API details
**GET**
/api/collections/`collectionIdOrName`/records
Path parameters
Param | Type | Description  
---|---|---  
collectionIdOrName | String | ID or name of the records' collection.  
Query parameters
Param | Type | Description  
---|---|---  
page | Number | The page (aka. offset) of the paginated list (_default to 1_).  
perPage | Number | The max returned records per page (_default to 30_).  
sort | String | Specify the _ORDER BY_ fields. Add `-` / `+` (default) in front of the attribute for DESC / ASC order, eg.: `// DESC by created and ASC by id ?sort=-created,id` **Supported record sort fields:** `@random`, `@rowid`, `id`, **and any other collection field**.  
filter | String | Filter expression to filter/search the returned records list (in addition to the collection's `listRule`), e.g.: `?filter=(title~'abc' && created>'2022-01-01')` **Supported record filter fields:** `id`, **+ any field from the collection schema**. The syntax basically follows the format `OPERAND OPERATOR OPERAND`, where:
  * `OPERAND` - could be any field literal, string (single or double quoted), number, null, true, false
  * `OPERATOR` - is one of: 
    * `=` Equal
    * `!=` NOT equal
    * `>` Greater than
    * `>=` Greater than or equal
    * `<` Less than
    * `<=` Less than or equal
    * `~` Like/Contains (if not specified auto wraps the right string OPERAND in a "%" for wildcard match)
    * `!~` NOT Like/Contains (if not specified auto wraps the right string OPERAND in a "%" for wildcard match)
    * `?=` _Any/At least one of_ Equal
    * `?!=` _Any/At least one of_ NOT equal
    * `?>` _Any/At least one of_ Greater than
    * `?>=` _Any/At least one of_ Greater than or equal
    * `?<` _Any/At least one of_ Less than
    * `?<=` _Any/At least one of_ Less than or equal
    * `?~` _Any/At least one of_ Like/Contains (if not specified auto wraps the right string OPERAND in a "%" for wildcard match)
    * `?!~` _Any/At least one of_ NOT Like/Contains (if not specified auto wraps the right string OPERAND in a "%" for wildcard match)

To group and combine several expressions you can use parenthesis `(...)`, `&&` (AND) and `||` (OR) tokens. Single line comments are also supported: `// Example comment`.  
expand | String | Auto expand record relations. Ex.: `?expand=relField1,relField2.subRelField` Supports up to 6-levels depth nested relations expansion. The expanded relations will be appended to the record under the `expand` property (e.g. `"expand": {"relField1": {...}, ...}`). Only the relations to which the request user has permissions to **view** will be expanded.  
fields | String | Comma separated string of the fields to return in the JSON response _(by default returns all fields)_. Ex.: `?fields=*,expand.relField.name` `*` targets all keys from the specific depth level. In addition, the following field modifiers are also supported:
  * `:excerpt(maxLength, withEllipsis?)` Returns a short plain text version of the field string value. Ex.: `?fields=*,description:excerpt(200,true)`

  
skipTotal | Boolean | If it is set the total counts query will be skipped and the response fields `totalItems` and `totalPages` will have `-1` value. This could drastically speed up the search queries when the total counters are not needed or cursor based pagination is used. For optimization purposes, it is set by default for the `getFirstListItem()` and `getFullList()` SDKs methods.  
Responses
200 400 403 
`{ "page": 1, "perPage": 100, "totalItems": 2, "totalPages": 1, "items": [ { "id": "ae40239d2bc4477", "collectionId": "a98f514eb05f454", "collectionName": "posts", "updated": "2022-06-25 11:03:50.052", "created": "2022-06-25 11:03:35.163", "title": "test1" }, { "id": "d08dfc4f4d84419", "collectionId": "a98f514eb05f454", "collectionName": "posts", "updated": "2022-06-25 11:03:45.876", "created": "2022-06-25 11:03:45.876", "title": "test2" } ] }`
`{ "status": 400, "message": "Something went wrong while processing your request. Invalid filter.", "data": {} }`
`{ "status": 403, "message": "Only superusers can filter by '@collection.*'", "data": {} }`
**View record**
Returns a single collection record by its ID.
Depending on the collection's `viewRule` value, the access to this action may or may not have been restricted.
_You could find individual generated records API documentation in the "Dashboard > Collections > API Preview"._
JavaScript
Dart
`import PocketBase from 'pocketbase'; const pb = new PocketBase('http://127.0.0.1:8090'); ... const record1 = await pb.collection('posts').getOne('RECORD_ID', { expand: 'relField1,relField2.subRelField', });`
`import 'package:pocketbase/pocketbase.dart'; final pb = PocketBase('http://127.0.0.1:8090'); ... final record1 = await pb.collection('posts').getOne('RECORD_ID',  expand: 'relField1,relField2.subRelField', );`
###### API details
**GET**
/api/collections/`collectionIdOrName`/records/`recordId`
Path parameters
Param | Type | Description  
---|---|---  
collectionIdOrName | String | ID or name of the record's collection.  
recordId | String | ID of the record to view.  
Query parameters
Param | Type | Description  
---|---|---  
expand | String | Auto expand record relations. Ex.: `?expand=relField1,relField2.subRelField` Supports up to 6-levels depth nested relations expansion. The expanded relations will be appended to the record under the `expand` property (e.g. `"expand": {"relField1": {...}, ...}`). Only the relations to which the request user has permissions to **view** will be expanded.  
fields | String | Comma separated string of the fields to return in the JSON response _(by default returns all fields)_. Ex.: `?fields=*,expand.relField.name` `*` targets all keys from the specific depth level. In addition, the following field modifiers are also supported:
  * `:excerpt(maxLength, withEllipsis?)` Returns a short plain text version of the field string value. Ex.: `?fields=*,description:excerpt(200,true)`

  
Responses
200 403 404 
`{ "id": "ae40239d2bc4477", "collectionId": "a98f514eb05f454", "collectionName": "posts", "updated": "2022-06-25 11:03:50.052", "created": "2022-06-25 11:03:35.163", "title": "test1" }`
`{ "status": 403, "message": "Only superusers can perform this action.", "data": {} }`
`{ "status": 404, "message": "The requested resource wasn't found.", "data": {} }`
**Create record**
Creates a new collection _Record_.
Depending on the collection's `createRule` value, the access to this action may or may not have been restricted.
_You could find individual generated records API documentation from the Dashboard._
JavaScript
Dart
`import PocketBase from 'pocketbase'; const pb = new PocketBase('http://127.0.0.1:8090'); ... const record = await pb.collection('demo').create({ title: 'Lorem ipsum', });`
`import 'package:pocketbase/pocketbase.dart'; final pb = PocketBase('http://127.0.0.1:8090'); ... final record = await pb.collection('demo').create(body: { 'title': 'Lorem ipsum', });`
###### API details
**POST**
/api/collections/`collectionIdOrName`/records
Path parameters
Param | Type | Description  
---|---|---  
collectionIdOrName | String | ID or name of the record's collection.  
Body Parameters
Param | Type | Description  
---|---|---  
Optional id | String | **15 characters string** to store as record ID. If not set, it will be auto generated.  
Schema fields  
**Any field from the collection's schema.**  
Additional auth record fields  
Required password | String | Auth record password.  
Required passwordConfirm | String | Auth record password confirmation.  
Body parameters could be sent as _JSON_ or _multipart/form-data_. File upload is supported only through _multipart/form-data_.
Query parameters
Param | Type | Description  
---|---|---  
expand | String | Auto expand record relations. Ex.: `?expand=relField1,relField2.subRelField` Supports up to 6-levels depth nested relations expansion. The expanded relations will be appended to the record under the `expand` property (e.g. `"expand": {"relField1": {...}, ...}`). Only the relations to which the request user has permissions to **view** will be expanded.  
fields | String | Comma separated string of the fields to return in the JSON response _(by default returns all fields)_. Ex.: `?fields=*,expand.relField.name` `*` targets all keys from the specific depth level. In addition, the following field modifiers are also supported:
  * `:excerpt(maxLength, withEllipsis?)` Returns a short plain text version of the field string value. Ex.: `?fields=*,description:excerpt(200,true)`

  
Responses
200 400 403 404 
`{ "collectionId": "a98f514eb05f454", "collectionName": "demo", "id": "ae40239d2bc4477", "updated": "2022-06-25 11:03:50.052", "created": "2022-06-25 11:03:35.163", "title": "Lorem ipsum" }`
`{ "status": 400, "message": "Failed to create record.", "data": { "title": { "code": "validation_required", "message": "Missing required value." } } }`
`{ "status": 403, "message": "Only superusers can perform this action.", "data": {} }`
`{ "status": 404, "message": "The requested resource wasn't found. Missing collection context.", "data": {} }`
**Update record**
Updates an existing collection _Record_.
Depending on the collection's `updateRule` value, the access to this action may or may not have been restricted.
_You could find individual generated records API documentation from the Dashboard._
JavaScript
Dart
`import PocketBase from 'pocketbase'; const pb = new PocketBase('http://127.0.0.1:8090'); ... const record = await pb.collection('demo').update('YOUR_RECORD_ID', { title: 'Lorem ipsum', });`
`import 'package:pocketbase/pocketbase.dart'; final pb = PocketBase('http://127.0.0.1:8090'); ... final record = await pb.collection('demo').update('YOUR_RECORD_ID', body: { 'title': 'Lorem ipsum', });`
###### API details
**PATCH**
/api/collections/`collectionIdOrName`/records/`recordId`
Path parameters
Param | Type | Description  
---|---|---  
collectionIdOrName | String | ID or name of the record's collection.  
recordId | String | ID of the record to update.  
Body Parameters
Param | Type | Description  
---|---|---  
Schema fields  
**Any field from the collection's schema.**  
Additional auth record fields  
Optional oldPassword | String | Old auth record password. This field is required only when changing the record password. Superusers and auth records with "Manage" access can skip this field.  
Optional password | String | New auth record password.  
Optional passwordConfirm | String | New auth record password confirmation.  
Body parameters could be sent as _JSON_ or _multipart/form-data_. File upload is supported only through _multipart/form-data_.
Query parameters
Param | Type | Description  
---|---|---  
expand | String | Auto expand record relations. Ex.: `?expand=relField1,relField2.subRelField` Supports up to 6-levels depth nested relations expansion. The expanded relations will be appended to the record under the `expand` property (e.g. `"expand": {"relField1": {...}, ...}`). Only the relations to which the request user has permissions to **view** will be expanded.  
fields | String | Comma separated string of the fields to return in the JSON response _(by default returns all fields)_. Ex.: `?fields=*,expand.relField.name` `*` targets all keys from the specific depth level. In addition, the following field modifiers are also supported:
  * `:excerpt(maxLength, withEllipsis?)` Returns a short plain text version of the field string value. Ex.: `?fields=*,description:excerpt(200,true)`

  
Responses
200 400 403 404 
`{ "collectionId": "a98f514eb05f454", "collectionName": "demo", "id": "ae40239d2bc4477", "updated": "2022-06-25 11:03:50.052", "created": "2022-06-25 11:03:35.163", "title": "Lorem ipsum" }`
`{ "status": 400, "message": "Failed to create record.", "data": { "title": { "code": "validation_required", "message": "Missing required value." } } }`
`{ "status": 403, "message": "Only superusers can perform this action.", "data": {} }`
`{ "status": 404, "message": "The requested resource wasn't found. Missing collection context.", "data": {} }`
**Delete record**
Deletes a single collection _Record_ by its ID.
Depending on the collection's `deleteRule` value, the access to this action may or may not have been restricted.
_You could find individual generated records API documentation from the Dashboard._
JavaScript
Dart
`import PocketBase from 'pocketbase'; const pb = new PocketBase('http://127.0.0.1:8090'); ... await pb.collection('demo').delete('YOUR_RECORD_ID');`
`import 'package:pocketbase/pocketbase.dart'; final pb = PocketBase('http://127.0.0.1:8090'); ... await pb.collection('demo').delete('YOUR_RECORD_ID');`
###### API details
**DELETE**
/api/collections/`collectionIdOrName`/records/`recordId`
Path parameters
Param | Type | Description  
---|---|---  
collectionIdOrName | String | ID or name of the record's collection.  
recordId | String | ID of the record to delete.  
Responses
204 400 403 404 
`null`
`{ "status": 400, "message": "Failed to delete record. Make sure that the record is not part of a required relation reference.", "data": {} }`
`{ "status": 403, "message": "Only superusers can perform this action.", "data": {} }`
`{ "status": 404, "message": "The requested resource wasn't found.", "data": {} }`
**Batch create/update/upsert/delete records**
Batch and transactional create/update/upsert/delete of multiple records in a single request.
The batch Web API need to be explicitly enabled and configured from the _Dashboard > Settings > Application_.
Because this endpoint process the requests in a single read&write transaction, other queries could queue up and it could degrade the performance of your application if not used with proper care and configuration (couple recommendations: prefer using the smallest possible max processing time limit, avoid large file uploads over slow S3 networks, restrict the body size limit to something smaller, etc.).
JavaScript
Dart
`import PocketBase from 'pocketbase'; const pb = new PocketBase('http://127.0.0.1:8090'); ... const batch = pb.createBatch(); batch.collection('example1').create({ ... }); batch.collection('example2').update('RECORD_ID', { ... }); batch.collection('example3').delete('RECORD_ID'); batch.collection('example4').upsert({ ... }); const result = await batch.send();`
`import 'package:pocketbase/pocketbase.dart'; final pb = PocketBase('http://127.0.0.1:8090'); ... final batch = pb.createBatch(); batch.collection('example1').create(body: { ... }); batch.collection('example2').update('RECORD_ID', body: { ... }); batch.collection('example3').delete('RECORD_ID'); batch.collection('example4').upsert(body: { ... }); final result = await batch.send();`
###### API details
**POST**
/api/batch
Body Parameters
Body parameters could be sent as _application/json_ or _multipart/form-data_. File upload is supported only via _multipart/form-data_ (see below for more details).
Param | Description  
---|---  
Required requests | Array<Request> - List of the requests to process. The supported batch request actions are:
  * record create - `POST /api/collections/{collection}/records`
  * record update - `PATCH /api/collections/{collection}/records/{id}`
  * record upsert - `PUT /api/collections/{collection}/records` (the body must have `id` field)
  * record delete - `DELETE /api/collections/{collection}/records/{id}`

Each batch Request element have the following properties:
  * `url path` _(could include query parameters)_
  * `method` _(GET, POST, PUT, PATCH, DELETE)_
  * `headers` _(custom per-request`Authorization` header is not supported at the moment, aka. all batch requests have the same auth state)_
  * `body`

**NB!** When the batch request is send as `multipart/form-data`, the regular batch action fields are expected to be submitted as serialized json under the `@jsonPayload` field and file keys need to follow the pattern `requests.N.fileField` or `requests[N].fileField` _(this is usually handled transparently by the SDKs when their specific object notation is used)_. If you don't use the SDKs or prefer manually to construct the `FormData` body, then it could look something like: `const formData = new FormData(); formData.append("@jsonPayload", JSON.stringify({ requests: [ { method: "POST", url: "/api/collections/example/records?expand=user", body: { title: "test1" }, }, { method: "PATCH", url: "/api/collections/example/records/RECORD_ID", body: { title: "test2" }, }, { method: "DELETE", url: "/api/collections/example/records/RECORD_ID", }, ] })) // file for the first request formData.append("requests.0.document", new File(...)) // file for the second request formData.append("requests.1.document", new File(...))`  
Responses
200 400 403 
`[ { "status": 200, "body": { "collectionId": "a98f514eb05f454", "collectionName": "demo", "id": "ae40239d2bc4477", "updated": "2022-06-25 11:03:50.052", "created": "2022-06-25 11:03:35.163", "title": "test1", "document": "file_a98f51.txt" } }, { "status": 200, "body": { "collectionId": "a98f514eb05f454", "collectionName": "demo", "id": "31y1gc447bc9602", "updated": "2022-06-25 11:03:50.052", "created": "2022-06-25 11:03:35.163", "title": "test2", "document": "file_f514eb0.txt" } }, ]`
`{ "status": 400, "message": "Batch transaction failed.", "data": { "requests": { "1": { "code": "batch_request_failed", "message": "Batch request failed.", "response": { "status": 400, "message": "Failed to create record.", "data": { "title": { "code": "validation_min_text_constraint", "message": "Must be at least 3 character(s).", "params": { "min": 3 } } } } } } } }`
`{ "status": 403, "message": "Batch requests are not allowed.", "data": {} }`
###  Auth record actions 
**List auth methods**
Returns a public list with the allowed collection authentication methods.
JavaScript
Dart
`import PocketBase from 'pocketbase'; const pb = new PocketBase('http://127.0.0.1:8090'); ... const result = await pb.collection('users').listAuthMethods();`
`import 'package:pocketbase/pocketbase.dart'; final pb = PocketBase('http://127.0.0.1:8090'); ... final result = await pb.collection('users').listAuthMethods();`
###### API details
**GET**
/api/collections/`collectionIdOrName`/auth-methods
Path parameters
Param | Type | Description  
---|---|---  
collectionIdOrName | String | ID or name of the auth collection.  
Query parameters
Param | Type | Description  
---|---|---  
fields | String | Comma separated string of the fields to return in the JSON response _(by default returns all fields)_. Ex.: `?fields=*,expand.relField.name` `*` targets all keys from the specific depth level. In addition, the following field modifiers are also supported:
  * `:excerpt(maxLength, withEllipsis?)` Returns a short plain text version of the field string value. Ex.: `?fields=*,description:excerpt(200,true)`

  
Responses
200 
`{ "password": { "enabled": true, "identityFields": ["email"] }, "oauth2": { "enabled": true, "providers": [ { "name": "github", "displayName": "GitHub", "state": "nT7SLxzXKAVMeRQJtxSYj9kvnJAvGk", "authURL": "https://github.com/login/oauth/authorize?client_id=test&code_challenge=fcf8WAhNI6uCLJYgJubLyWXHvfs8xghoLe3zksBvxjE&code_challenge_method=S256&response_type=code&scope=read%3Auser+user%3Aemail&state=nT7SLxzXKAVMeRQJtxSYj9kvnJAvGk&redirect_uri=", "codeVerifier": "PwBG5OKR2IyQ7siLrrcgWHFwLLLAeUrz7PS1nY4AneG", "codeChallenge": "fcf8WAhNI6uCLJYgJubLyWXHvfs8xghoLe3zksBvxjE", "codeChallengeMethod": "S256" } ] }, "mfa": { "enabled": false, "duration": 0 }, "otp": { "enabled": false, "duration": 0 } }`
**Auth with password**
Authenticate a single auth record by combination of a password and a unique identity field (e.g. email).
JavaScript
Dart
`import PocketBase from 'pocketbase'; const pb = new PocketBase('http://127.0.0.1:8090'); ... const authData = await pb.collection('users').authWithPassword( 'YOUR_USERNAME_OR_EMAIL', 'YOUR_PASSWORD', ); // after the above you can also access the auth data from the authStore console.log(pb.authStore.isValid); console.log(pb.authStore.token); console.log(pb.authStore.record.id); // "logout" the last authenticated record pb.authStore.clear();`
`import 'package:pocketbase/pocketbase.dart'; final pb = PocketBase('http://127.0.0.1:8090'); ... final authData = await pb.collection('users').authWithPassword( 'YOUR_USERNAME_OR_EMAIL', 'YOUR_PASSWORD', ); // after the above you can also access the auth data from the authStore print(pb.authStore.isValid); print(pb.authStore.token); print(pb.authStore.record.id); // "logout" the last authenticated record pb.authStore.clear();`
###### API details
**POST**
/api/collections/`collectionIdOrName`/auth-with-password
Path parameters
Param | Type | Description  
---|---|---  
collectionIdOrName | String | ID or name of the auth collection.  
Body Parameters
Param | Type | Description  
---|---|---  
Required identity | String | Auth record username or email address.  
Required password | String | Auth record password.  
Optional identityField | String | A specific identity field to use (by default fallbacks to the first matching one).  
Body parameters could be sent as _JSON_ or _multipart/form-data_.
Query parameters
Param | Type | Description  
---|---|---  
expand | String | Auto expand record relations. Ex.: `?expand=relField1,relField2.subRelField` Supports up to 6-levels depth nested relations expansion. The expanded relations will be appended to the record under the `expand` property (e.g. `"expand": {"relField1": {...}, ...}`). Only the relations to which the request user has permissions to **view** will be expanded.  
fields | String | Comma separated string of the fields to return in the JSON response _(by default returns all fields)_. Ex.: `?fields=*,record.expand.relField.name` `*` targets all keys from the specific depth level. In addition, the following field modifiers are also supported:
  * `:excerpt(maxLength, withEllipsis?)` Returns a short plain text version of the field string value. Ex.: `?fields=*,record.description:excerpt(200,true)`

  
Responses
200 400 
`{ "token": "eyJhbGciOiJIUzI1NiJ9.eyJpZCI6IjRxMXhsY2xtZmxva3UzMyIsInR5cGUiOiJhdXRoUmVjb3JkIiwiY29sbGVjdGlvbklkIjoiX3BiX3VzZXJzX2F1dGhfIiwiZXhwIjoyMjA4OTg1MjYxfQ.UwD8JvkbQtXpymT09d7J6fdA0aP9g4FJ1GPh_ggEkzc", "record": { "id": "8171022dc95a4ed", "collectionId": "d2972397d45614e", "collectionName": "users", "created": "2022-06-24 06:24:18.434Z", "updated": "2022-06-24 06:24:18.889Z", "username": "test@example.com", "email": "test@example.com", "verified": false, "emailVisibility": true, "someCustomField": "example 123" } }`
`{ "status": 400, "message": "An error occurred while submitting the form.", "data": { "password": { "code": "validation_required", "message": "Missing required value." } } }`
**Auth with OAuth2**
Authenticate with an OAuth2 provider and returns a new auth token and record data.
This action usually should be called right after the provider login page redirect.
You could also check the OAuth2 web integration example.
JavaScript
Dart
`import PocketBase from 'pocketbase'; const pb = new PocketBase('http://127.0.0.1:8090'); ... const authData = await pb.collection('users').authWithOAuth2Code( 'google', 'CODE', 'VERIFIER', 'REDIRECT_URL', // optional data that will be used for the new account on OAuth2 sign-up { 'name': 'test', }, ); // after the above you can also access the auth data from the authStore console.log(pb.authStore.isValid); console.log(pb.authStore.token); console.log(pb.authStore.record.id); // "logout" the last authenticated record pb.authStore.clear();`
`import 'package:pocketbase/pocketbase.dart'; final pb = PocketBase('http://127.0.0.1:8090'); ... final authData = await pb.collection('users').authWithOAuth2Code( 'google', 'CODE', 'VERIFIER', 'REDIRECT_URL', // optional data that will be used for the new account on OAuth2 sign-up  createData: { 'name': 'test', }, ); // after the above you can also access the auth data from the authStore print(pb.authStore.isValid); print(pb.authStore.token); print(pb.authStore.record.id); // "logout" the last authenticated record pb.authStore.clear();`
###### API details
**POST**
/api/collections/`collectionIdOrName`/auth-with-oauth2
Path parameters
Param | Type | Description  
---|---|---  
collectionIdOrName | String | ID or name of the auth collection.  
Body Parameters
Param | Type | Description  
---|---|---  
Required provider | String | The name of the OAuth2 client provider (e.g. "google").  
Required code | String | The authorization code returned from the initial request.  
Required codeVerifier | String | The code verifier sent with the initial request as part of the code_challenge.  
Required redirectUrl | String | The redirect url sent with the initial request.  
Optional createData | Object | Optional data that will be used when creating the auth record on OAuth2 sign-up. The created auth record must comply with the same requirements and validations in the regular **create** action. _The data can only be in`json` , aka. `multipart/form-data` and files upload currently are not supported during OAuth2 sign-ups._  
Body parameters could be sent as _JSON_ or _multipart/form-data_.
Query parameters
Param | Type | Description  
---|---|---  
expand | String | Auto expand record relations. Ex.: `?expand=relField1,relField2.subRelField` Supports up to 6-levels depth nested relations expansion. The expanded relations will be appended to the record under the `expand` property (e.g. `"expand": {"relField1": {...}, ...}`). Only the relations to which the request user has permissions to **view** will be expanded.  
fields | String | Comma separated string of the fields to return in the JSON response _(by default returns all fields)_. Ex.: `?fields=*,record.expand.relField.name` `*` targets all keys from the specific depth level. In addition, the following field modifiers are also supported:
  * `:excerpt(maxLength, withEllipsis?)` Returns a short plain text version of the field string value. Ex.: `?fields=*,record.description:excerpt(200,true)`

  
Responses
200 400 
`{ "token": "eyJhbGciOiJIUzI1NiJ9.eyJpZCI6IjRxMXhsY2xtZmxva3UzMyIsInR5cGUiOiJhdXRoUmVjb3JkIiwiY29sbGVjdGlvbklkIjoiX3BiX3VzZXJzX2F1dGhfIiwiZXhwIjoyMjA4OTg1MjYxfQ.UwD8JvkbQtXpymT09d7J6fdA0aP9g4FJ1GPh_ggEkzc", "record": { "id": "8171022dc95a4ed", "collectionId": "d2972397d45614e", "collectionName": "users", "created": "2022-06-24 06:24:18.434Z", "updated": "2022-06-24 06:24:18.889Z", "username": "test@example.com", "email": "test@example.com", "verified": true, "emailVisibility": false, "someCustomField": "example 123" }, "meta": { "id": "abc123", "name": "John Doe", "username": "john.doe", "email": "test@example.com", "isNew": false, "avatarURL": "https://example.com/avatar.png", "rawUser": {...}, "accessToken": "...", "refreshToken": "...", "expiry": "..." } }`
`{ "status": 400, "message": "An error occurred while submitting the form.", "data": { "provider": { "code": "validation_required", "message": "Missing required value." } } }`
**Auth with OTP**
Authenticate a single auth record with an one-time password (OTP).
Note that when requesting an OTP we return an `otpId` even if a user with the provided email doesn't exist as a very basic enumeration protection.
JavaScript
Dart
`import PocketBase from 'pocketbase'; const pb = new PocketBase('http://127.0.0.1:8090'); ... // send OTP email to the provided auth record const req = await pb.collection('users').requestOTP('test@example.com'); // ... show a screen/popup to enter the password from the email ... // authenticate with the requested OTP id and the email password const authData = await pb.collection('users').authWithOTP(req.otpId, "YOUR_OTP"); // after the above you can also access the auth data from the authStore console.log(pb.authStore.isValid); console.log(pb.authStore.token); console.log(pb.authStore.record.id); // "logout" pb.authStore.clear();`
`import 'package:pocketbase/pocketbase.dart'; final pb = PocketBase('http://127.0.0.1:8090'); ... // send OTP email to the provided auth record final req = await pb.collection('users').requestOTP('test@example.com'); // ... show a screen/popup to enter the password from the email ... // authenticate with the requested OTP id and the email password final authData = await pb.collection('users').authWithOTP(req.otpId, "YOUR_OTP"); // after the above you can also access the auth data from the authStore print(pb.authStore.isValid); print(pb.authStore.token); print(pb.authStore.record.id); // "logout" pb.authStore.clear();`
###### API details
OTP Request
OTP Auth
**POST**
/api/collections/`collectionIdOrName`/request-otp
Path parameters
Param | Type | Description  
---|---|---  
collectionIdOrName | String | ID or name of the auth collection.  
Body Parameters
Param | Type | Description  
---|---|---  
Required email | String | The auth record email address to send the OTP request (if exists).  
Responses
200 400 429 
`{ "otpId": "7Ch3QSvxlGEeWTs" }`
`{ "status": 400, "message": "An error occurred while validating the submitted data.", "data": { "email": { "code": "validation_is_email", "message": "Must be a valid email address." } } }`
`{ "status": 429, "message": "You've send too many OTP requests, please try again later.", "data": {} }`
**POST**
/api/collections/`collectionIdOrName`/auth-with-otp
Path parameters
Param | Type | Description  
---|---|---  
collectionIdOrName | String | ID or name of the auth collection.  
Body Parameters
Param | Type | Description  
---|---|---  
Required otpId | String | The id of the OTP request.  
Required password | String | The one-time password.  
Query parameters
Param | Type | Description  
---|---|---  
expand | String | Auto expand record relations. Ex.: `?expand=relField1,relField2.subRelField` Supports up to 6-levels depth nested relations expansion. The expanded relations will be appended to the record under the `expand` property (e.g. `"expand": {"relField1": {...}, ...}`). Only the relations to which the request user has permissions to **view** will be expanded.  
fields | String | Comma separated string of the fields to return in the JSON response _(by default returns all fields)_. Ex.: `?fields=*,record.expand.relField.name` `*` targets all keys from the specific depth level. In addition, the following field modifiers are also supported:
  * `:excerpt(maxLength, withEllipsis?)` Returns a short plain text version of the field string value. Ex.: `?fields=*,record.description:excerpt(200,true)`

  
Responses
200 400 
`{ "token": "eyJhbGciOiJIUzI1NiJ9.eyJpZCI6IjRxMXhsY2xtZmxva3UzMyIsInR5cGUiOiJhdXRoUmVjb3JkIiwiY29sbGVjdGlvbklkIjoiX3BiX3VzZXJzX2F1dGhfIiwiZXhwIjoyMjA4OTg1MjYxfQ.UwD8JvkbQtXpymT09d7J6fdA0aP9g4FJ1GPh_ggEkzc", "record": { "id": "8171022dc95a4ed", "collectionId": "d2972397d45614e", "collectionName": "users", "created": "2022-06-24 06:24:18.434Z", "updated": "2022-06-24 06:24:18.889Z", "username": "test@example.com", "email": "test@example.com", "verified": false, "emailVisibility": true, "someCustomField": "example 123" } }`
`{ "status": 400, "message": "Failed to authenticate.", "data": { "otpId": { "code": "validation_required", "message": "Missing required value." } } }`
**Auth refresh**
Returns a new auth response (token and user data) for already authenticated auth record.
_This method is usually called by users on page/screen reload to ensure that the previously stored data in`pb.authStore` is still valid and up-to-date._
JavaScript
Dart
`import PocketBase from 'pocketbase'; const pb = new PocketBase('http://127.0.0.1:8090'); ... const authData = await pb.collection('users').authRefresh(); // after the above you can also access the refreshed auth data from the authStore console.log(pb.authStore.isValid); console.log(pb.authStore.token); console.log(pb.authStore.record.id);`
`import 'package:pocketbase/pocketbase.dart'; final pb = PocketBase('http://127.0.0.1:8090'); ... final authData = await pb.collection('users').authRefresh(); // after the above you can also access the refreshed auth data from the authStore print(pb.authStore.isValid); print(pb.authStore.token); print(pb.authStore.record.id);`
###### API details
**POST**
/api/collections/`collectionIdOrName`/auth-refresh
Requires `Authorization:TOKEN`
Path parameters
Param | Type | Description  
---|---|---  
collectionIdOrName | String | ID or name of the auth collection.  
Query parameters
Param | Type | Description  
---|---|---  
expand | String | Auto expand record relations. Ex.: `?expand=relField1,relField2.subRelField` Supports up to 6-levels depth nested relations expansion. The expanded relations will be appended to the record under the `expand` property (e.g. `"expand": {"relField1": {...}, ...}`). Only the relations to which the request user has permissions to **view** will be expanded.  
fields | String | Comma separated string of the fields to return in the JSON response _(by default returns all fields)_. Ex.: `?fields=*,record.expand.relField.name` `*` targets all keys from the specific depth level. In addition, the following field modifiers are also supported:
  * `:excerpt(maxLength, withEllipsis?)` Returns a short plain text version of the field string value. Ex.: `?fields=*,record.description:excerpt(200,true)`

  
Responses
200 401 403 404 
`{ "token": "eyJhbGciOiJIUzI1NiJ9.eyJpZCI6IjRxMXhsY2xtZmxva3UzMyIsInR5cGUiOiJhdXRoUmVjb3JkIiwiY29sbGVjdGlvbklkIjoiX3BiX3VzZXJzX2F1dGhfIiwiZXhwIjoyMjA4OTg1MjYxfQ.UwD8JvkbQtXpymT09d7J6fdA0aP9g4FJ1GPh_ggEkzc", "record": { "id": "8171022dc95a4ed", "collectionId": "d2972397d45614e", "collectionName": "users", "created": "2022-06-24 06:24:18.434Z", "updated": "2022-06-24 06:24:18.889Z", "username": "test@example.com", "email": "test@example.com", "verified": false, "emailVisibility": true, "someCustomField": "example 123" } }`
`{ "status": 401, "message": "The request requires valid record authorization token to be set.", "data": {} }`
`{ "status": 403, "message": "The authorized record model is not allowed to perform this action.", "data": {} }`
`{ "status": 404, "message": "Missing auth record context.", "data": {} }`
**Verification**
Sends auth record email verification request.
JavaScript
Dart
`import PocketBase from 'pocketbase'; const pb = new PocketBase('http://127.0.0.1:8090'); ... await pb.collection('users').requestVerification('test@example.com'); // --- // (optional) in your custom confirmation page: // --- await pb.collection('users').confirmVerification('VERIFICATION_TOKEN');`
`import 'package:pocketbase/pocketbase.dart'; final pb = PocketBase('http://127.0.0.1:8090'); ... await pb.collection('users').requestVerification('test@example.com'); // --- // (optional) in your custom confirmation page: // --- await pb.collection('users').confirmVerification('VERIFICATION_TOKEN');`
###### API details
Request verification
Confirm verification
**POST**
/api/collections/`collectionIdOrName`/request-verification
Body Parameters
Param | Type | Description  
---|---|---  
Required email | String | The auth record email address to send the verification request (if exists).  
Responses
204 400 
`null`
`{ "status": 400, "message": "An error occurred while validating the submitted data.", "data": { "email": { "code": "validation_required", "message": "Missing required value." } } }`
**POST**
/api/collections/`collectionIdOrName`/confirm-verification
Body Parameters
Param | Type | Description  
---|---|---  
Required token | String | The token from the verification request email.  
Responses
204 400 
`null`
`{ "status": 400, "message": "An error occurred while validating the submitted data.", "data": { "token": { "code": "validation_required", "message": "Missing required value." } } }`
**Password reset**
Sends auth record password reset email request.
On successful password reset all previously issued auth tokens for the specific record will be automatically invalidated.
JavaScript
Dart
`import PocketBase from 'pocketbase'; const pb = new PocketBase('http://127.0.0.1:8090'); ... await pb.collection('users').requestPasswordReset('test@example.com'); // --- // (optional) in your custom confirmation page: // --- // note: after this call all previously issued auth tokens are invalidated await pb.collection('users').confirmPasswordReset( 'RESET_TOKEN', 'NEW_PASSWORD', 'NEW_PASSWORD_CONFIRM', );`
`import 'package:pocketbase/pocketbase.dart'; final pb = PocketBase('http://127.0.0.1:8090'); ... await pb.collection('users').requestPasswordReset('test@example.com'); // --- // (optional) in your custom confirmation page: // --- // note: after this call all previously issued auth tokens are invalidated await pb.collection('users').confirmPasswordReset( 'RESET_TOKEN', 'NEW_PASSWORD', 'NEW_PASSWORD_CONFIRM', );`
###### API details
Request password reset
Confirm password reset
**POST**
/api/collections/`collectionIdOrName`/request-password-reset
Body Parameters
Param | Type | Description  
---|---|---  
Required email | String | The auth record email address to send the password reset request (if exists).  
Responses
204 400 
`null`
`{ "status": 400, "message": "An error occurred while validating the submitted data.", "data": { "email": { "code": "validation_required", "message": "Missing required value." } } }`
**POST**
/api/collections/`collectionIdOrName`/confirm-password-reset
Body Parameters
Param | Type | Description  
---|---|---  
Required token | String | The token from the password reset request email.  
Required password | String | The new password to set.  
Required passwordConfirm | String | The new password confirmation.  
Responses
204 400 
`null`
`{ "status": 400, "message": "An error occurred while validating the submitted data.", "data": { "token": { "code": "validation_required", "message": "Missing required value." } } }`
**Email change**
Sends auth record email change request.
On successful email change all previously issued auth tokens for the specific record will be automatically invalidated.
JavaScript
Dart
`import PocketBase from 'pocketbase'; const pb = new PocketBase('http://127.0.0.1:8090'); ... await pb.collection('users').authWithPassword('test@example.com', '1234567890'); await pb.collection('users').requestEmailChange('new@example.com'); // --- // (optional) in your custom confirmation page: // --- // note: after this call all previously issued auth tokens are invalidated await pb.collection('users').confirmEmailChange('EMAIL_CHANGE_TOKEN', 'YOUR_PASSWORD');`
`import 'package:pocketbase/pocketbase.dart'; final pb = PocketBase('http://127.0.0.1:8090'); ... await pb.collection('users').authWithPassword('test@example.com', '1234567890'); await pb.collection('users').requestEmailChange('new@example.com'); ... // --- // (optional) in your custom confirmation page: // --- // note: after this call all previously issued auth tokens are invalidated await pb.collection('users').confirmEmailChange('EMAIL_CHANGE_TOKEN', 'YOUR_PASSWORD');`
###### API details
Request email change
Confirm email change
**POST**
/api/collections/`collectionIdOrName`/request-email-change
Requires `Authorization:TOKEN`
Body Parameters
Param | Type | Description  
---|---|---  
Required newEmail | String | The new email address to send the change email request.  
Responses
204 400 401 403 
`null`
`{ "status": 400, "message": "An error occurred while validating the submitted data.", "data": { "newEmail": { "code": "validation_required", "message": "Missing required value." } } }`
`{ "status": 401, "message": "The request requires valid record authorization token to be set.", "data": {} }`
`{ "status": 403, "message": "The authorized record model is not allowed to perform this action.", "data": {} }`
**POST**
/api/collections/`collectionIdOrName`/confirm-email-change
Body Parameters
Param | Type | Description  
---|---|---  
Required token | String | The token from the change email request email.  
Required password | String | The account password to confirm the email change.  
Responses
204 400 
`null`
`{ "status": 400, "message": "An error occurred while validating the submitted data.", "data": { "token": { "code": "validation_required", "message": "Missing required value." } } }`
**Impersonate**
Impersonate allows you to authenticate as a different user by generating a **nonrefreshable** auth token.
Only superusers can perform this action.
JavaScript
Dart
`import PocketBase from 'pocketbase'; const pb = new PocketBase('http://127.0.0.1:8090'); ... // authenticate as superuser await pb.collection("_superusers").authWithPassword("test@example.com", "1234567890"); // impersonate // (the custom token duration is optional and must be in seconds) const impersonateClient = pb.collection("users").impersonate("USER_RECORD_ID", 3600) // log the impersonate token and user data console.log(impersonateClient.authStore.token); console.log(impersonateClient.authStore.record); // send requests as the impersonated user impersonateClient.collection("example").getFullList();`
`import 'package:pocketbase/pocketbase.dart'; final pb = PocketBase('http://127.0.0.1:8090'); ... // authenticate as superuser await pb.collection("_superusers").authWithPassword("test@example.com", "1234567890"); // impersonate // (the custom token duration is optional and must be in seconds) final impersonateClient = pb.collection("users").impersonate("USER_RECORD_ID", 3600) // log the impersonate token and user data print(impersonateClient.authStore.token); print(impersonateClient.authStore.record); // send requests as the impersonated user impersonateClient.collection("example").getFullList();`
###### API details
**POST**
/api/collections/`collectionIdOrName`/impersonate/`id`
Requires `Authorization:TOKEN`
Path parameters
Param | Type | Description  
---|---|---  
collectionIdOrName | String | ID or name of the auth collection.  
id | String | ID of the auth record to impersonate.  
Body Parameters
Param | Type | Description  
---|---|---  
Optional duration | Number | Optional custom JWT duration for the `exp` claim (in seconds). If not set or 0, it fallbacks to the default collection auth token duration option.  
Body parameters could be sent as _JSON_ or _multipart/form-data_.
Query parameters
Param | Type | Description  
---|---|---  
expand | String | Auto expand record relations. Ex.: `?expand=relField1,relField2.subRelField` Supports up to 6-levels depth nested relations expansion. The expanded relations will be appended to the record under the `expand` property (e.g. `"expand": {"relField1": {...}, ...}`). Only the relations to which the request user has permissions to **view** will be expanded.  
fields | String | Comma separated string of the fields to return in the JSON response _(by default returns all fields)_. Ex.: `?fields=*,record.expand.relField.name` `*` targets all keys from the specific depth level. In addition, the following field modifiers are also supported:
  * `:excerpt(maxLength, withEllipsis?)` Returns a short plain text version of the field string value. Ex.: `?fields=*,record.description:excerpt(200,true)`

  
Responses
200 400 401 403 404 
`{ "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb2xsZWN0aW9uSWQiOiJfcGJjX2MwcHdrZXNjcXMiLCJleHAiOjE3MzAzNjgxMTUsImlkIjoicXkwMmMxdDBueDBvanFuIiwicmVmcmVzaGFibGUiOmZhbHNlLCJ0eXBlIjoiYXV0aCJ9.1JOaE54TyPdDLf0mb0T6roIYeh8Y1HfJvDlYZADMN4U", "record": { "id": "8171022dc95a4ed", "collectionId": "d2972397d45614e", "collectionName": "users", "created": "2022-06-24 06:24:18.434Z", "updated": "2022-06-24 06:24:18.889Z", "username": "test@example.com", "email": "test@example.com", "verified": false, "emailVisibility": true, "someCustomField": "example 123" } }`
`{ "status": 400, "message": "The request requires valid record authorization token to be set.", "data": { "duration": { "code": "validation_min_greater_equal_than_required", "message": "Must be no less than 0." } } }`
`{ "status": 401, "message": "An error occurred while validating the submitted data.", "data": {} }`
`{ "status": 403, "message": "The authorized record model is not allowed to perform this action.", "data": {} }`
`{ "status": 404, "message": "The requested resource wasn't found.", "data": {} }`
Next: API Realtime
