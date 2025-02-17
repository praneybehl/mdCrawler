![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-light.cf7eca76.svg)![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-dark.01246f11.svg)
Search...
`⌘ K`
Feedback
Log In
Sign Up
CLI & API
Vercel REST API
Reference
# Vercel REST API
The Vercel REST API is a REST-styled API that gives full control over the entire Vercel platform.
Table of Contents
Vercel REST API allows developers to interact programmatically with their Vercel account and services using HTTP requests.
With the API, developers can deploy new versions of web applications, manage custom domains, retrieve information about deployments, and manage secrets and environment variables for projects.
The API supports any programming language or framework that can send HTTP requests.
You can use the commands listed below with `curl` by providing your token.
To view all endpoints, and explore code examples, see the reference documentation.
## API Basics
Our API is exposed as an HTTP/1 and HTTP/2 service over SSL. All endpoints live under the URL `https://api.vercel.com` and then generally follow the REST architecture.
### Server Specs
#### HTTP and TLS
The API supports HTTP versions 1, 1.1, and 2, although HTTP/2 is preferred.
TLS versions 1.2 and 1.3 are supported, with resumption.
For more information on TLS support, refer to the SSL Labs report.
### Content Type
All requests must be encoded as JSON with the `Content-Type: application/json` header. If not otherwise specified, responses from the Vercel API, including errors, are encoded exclusively as JSON as well.
### Authentication
Vercel Access Tokens are required to authenticate and use the Vercel API.
index.js
```
 Authorization: Bearer <TOKEN>
```

The `Authorization` header with an access token.
#### Creating an Access Token
Access Tokens can be created and managed from inside your account settings.
![Create a new Access Token.](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1701697368%2Fdocs-assets%2Fstatic%2Fdocs%2Frest-api%2Fcreate-token-light.png&w=1920&q=75)![Create a new Access Token.](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1701697369%2Fdocs-assets%2Fstatic%2Fdocs%2Frest-api%2Fcreate-token-dark.png&w=1920&q=75)Create a new Access Token.
  1. In the upper-right corner of your dashboard, click your profile picture, then select Settings
  2. Select Tokens from the sidebar
  3. Enter a descriptive name for the token
  4. Choose the scope from the list of Teams in the drop-down menu. The scope ensures that only your specified Team(s) can use an Access Token
  5. From the drop-down, select an expiration date for the Token
  6. Click Create Token
  7. Once you've created an Access Token, securely store the value as it will not be shown again.


#### Expiration
Setting an expiration date on an Access Token is highly recommended and is considered one of the standard security practices that helps keep your information secure. You can select from a default list of expiration dates ranging from 1 day to 1 year. You can view the expiration date of your Access Tokens on the tokens page.
#### Accessing Resources Owned by a Team
By default, you can access resources contained within your own user account (personal).
To access resources owned by a team, or create a project for a _specific_ team, you must first find the Team ID.
After you obtained the Team ID, append it as a query string at the end of the API endpoint URL:
index.js
```
https://api.vercel.com/v6/deployments?teamId=[teamID]
```

Replace `[teamID]` with the Team ID you obtained.
You still need to provide an API token through the `Authorization` header.
#### Failed Authentication
If authentication is unsuccessful for a request, the error status code 403 is returned.
### Pagination
When the API response includes an array of records, a pagination object is returned when the total number of records present is greater than the limit per request. The default value of this limit is 20 but it can be changed by passing a value to the query parameter `limit` when the request is made. The maximum possible value of `limit` is 100.
You can then use the pagination object to make additional requests and obtain all the records.
The pagination object is structured as shown in the example below:
pagination-structure
```
{
"pagination": {
"count":20,//Amount of items in the current page.
"next":1555072968396,//Timestamp that must be used to request the next page.
"prev":1555413045188//Timestamp that must be used to request the previous page.
 }
}
```

Pagination object returned with response
In order to obtain the records for the next batch, perform the following actions:
  1. Send a request to the same API endpoint
  2. Include the query parameter `until` with a value equal to the timestamp value of `next` returned in the previous request
  3. Repeat this sequence until the pagination object has a `next` value of `null`


This is an example of applying this sequence with `Node.js` to save all the projects in your personal account to a `json` file:
pagination-example.js
```
constaxios=require('axios');
constfs=require('fs');
constvercelToken='yourtokenvalue'; //Replace with your token
constapiEndPt='https://api.vercel.com/v9/projects';
let config = {
 method:'get',
 url: apiEndPt,
 headers: {
  Authorization:'Bearer '+ vercelToken,
 },
};
let results = [];
(functionloop() {
axios(config)
.then(function (response) {
results.push(...response.data.projects);
if (response.data.pagination.next !==null) {
config.url =`${apiEndPt}?until=${response.data.pagination.next}`;
loop();
   } else {
//you can use the final results object and for example save it to a json file
fs.writeFileSync('projects.json',JSON.stringify(results));
   }
  })
.catch(function (error) {
console.log(error);
  });
})();
```

Save all the Projects in your Vercel personal account to `projects.json`
### Errors
All API endpoints contain a `code` and `message` within the error responses, though some API endpoints extend the `error` object to contain other information. Each endpoint that does this will be documented in their appropriate section.
While we recommend that you write error messages that fit your needs and provide your users with the best experience, our `message` fields are designed to be neutral, not contain sensitive information, and can be safely passed down to user interfaces.
error-response
```
{
"error": {
"code":"forbidden",
"message":"Not authorized"
 }
}
```

An example of an unauthorized request error.
### Rate Limits
We limit the number of calls you can make over a certain period of time. Rate limits vary and are specified by the following header in all responses:
Header| Description  
---|---  
`X-RateLimit-Limit`| The maximum number of requests that the consumer is permitted to make.  
`X-RateLimit-Remaining`| The number of requests remaining in the current rate limit window.  
`X-RateLimit-Reset`| The time at which the current rate limit window resets in UTC epoch seconds.  
When the rate limit is exceeded, an error is returned with the status "429 Too Many Requests":
error-response
```
{
"error": {
"code":"too_many_requests",
"message":"Rate limit exceeded"
 }
}
```

An example of a rate limit exceeded error.
You can find the complete list of rate limits in the limits documentation.
### Versioning
All endpoints and examples are designated with a specific version. Versions vary per endpoint and are not global.
The response shape of a certain endpoint is not guaranteed to be fixed over time. In particular, we might add new keys to responses without bumping a version endpoint, which will be noted in the changelog.
To ensure the security and correctness of your application, make sure to only read the keys from the response that your application needs. Don't proxy entire responses to third-parties without validation.
Old versions of each endpoint are supported for as long as possible. When we intend to deprecate, we will notify users in the changelog section.
Endpoint versions follow the base URL and come before the endpoint. For example:
version-endpoint
```
https://api.vercel.com/v6/deployments`
```

Using version `6` of the deployments endpoint.
### Types
The following is a list of the types of data used within the Vercel API:
Name| Definition| Example  
---|---|---  
ID| A unique value used to identify resources.| `"V0fra8eEgQwEpFhYG2vTzC3K"`  
String| A string is a sequence of characters used to represent text.| `"value"`  
Integer| An integer is a number without decimals.| `1234`  
Float| A float is a number with decimals.| `12.34`  
Map| A data structure with a list of values assigned to a unique key.| `{ "key": "value" }`  
List| A data structure with only a list of values separated by a comma.| `["value", 1234, 12.34]`  
Enum| An Enum is a String with only a few possible valid values.| `A | B`  
Date| An Integer representing a date in milliseconds since the UNIX epoch.| `1540095775941`  
IsoDate| A String representing a date in the 8601 format.| `YYYY-MM-DDTHH:mm:ssZ`  
Boolean| A Boolean is a type of two possible values representing true or false.| `true`  
Checks are tests and assertions that run after each deployment has been built. They are powered by Integrations, which allow you to connect any third-party service of your choice with Vercel. Learn more about Checks for deployments.
### Status and conclusion
Please update the Check `status` to `running` once you have begun performing the respective action within your service. Updating the Check with a `conclusion` will automatically set the Check `status` to `completed`.
Based on the `conclusion`, a deployment may fail:
Conclusion| `blocking` equals to true  
---|---  
cancelled| Yes  
failed| Yes  
neutral| No  
succeeded| No  
skipped| No  
### Output
The output of a check can contain arbitrary data, or can contain Web Vitals and a Virtual Experience Score.
To include Web Vitals and a Virtual Experience Score, the following can be passed to `output` under a `metrics` field:
Key| Type| Description  
---|---|---  
TBT| Map| The Total Blocking Time, as measured by the Check  
LCP| Map| The Largest Contentful Paint, as measured by the Check  
FCP| Map| The First Contentful Paint, as measured by the Check  
CLS| Map| The Cumulative Layout Shift, as measured by the Check  
virtualExperienceScore| Map| The overall Virtual Experience Score measured by the Check  
Each of these has the following properties:
Key| Type| Description  
---|---|---  
value| Float| The value measured for the particular metric, in milliseconds. For virtualExperienceScore this value is the percentage between 0 and 1  
previousValue| Float| A previous value for comparison purposes.  
source| Enum| `web-vitals`  
Log Drains allow you to collect logs from your deployments. To enable Log Drains, you must provide a destination URL to send the logs to.
We send logs to destination URLs over `HTTPS`, `HTTP`, `TLS`, or `TCP` every time logs are generated.
### Format and Transport
We support 3 types of Log Drains:
  * JSON
  * NDJSON
  * Syslog


For more information, review Format and Transport.
### JSON drains
When you choose the `json` type, the URL receives a HTTPS or HTTP POST request with a JSON array on the `POST` body.
If the response of the request returns an HTTP `statusCode` with a value of `-1`, that means there was no response returned and the lambda crashed. In the same response, if the value of `proxy.statusCode` is returned with `-1`, that means the revalidation occurred in the background.
The logs are buffered and submitted as batches with the following formats:
json-drains
```
[
 {
"id": <identifier>,
"message": <text>,
"timestamp": <timestamp>,
"type": <"stdout" or "stderr">,
"source": <"build","static", "external", or "lambda">,
"projectId": <identifier of project>,
"deploymentId": <identifier of deployment>,
"buildId": <identifier of build>,
"host": <hostname>,
"entrypoint": <entrypoint>
 },
 {
"id": <identifier>,
"message": <text>,
"timestamp": <timestamp>,
"requestId": <identifier of request>,
"statusCode": <HTTP status code of request>,
"source": <"build","static", "external", or "lambda">,
"projectId": <identifier of project>,
"deploymentId": <identifier of deployment>,
"executionRegion": <region where the request is executed>,
"buildId": <identifier of build only on build logs>,
"destination": <origin of external content only on external logs>,
"host": <hostname>,
"path": <path>,
"level": <"error","warning", or "info">,
"proxy": {
"timestamp": <timestamp of proxy request>,
"method": <method of request>,
"scheme": <protocol of request>,
"host": <hostname>,
"path": <path of proxy request>,
"userAgent": <user agent>,
"referer": <referer>,
"statusCode": <HTTP status code of proxy request>,
"clientIp": <client IP>,
"region": <region request is processed>,
"cacheId": <original request id when request is served from cache>,
"errorCode": <error code happened on proxy request>,
  }
 }
]
```

The requests are posted with an `x-vercel-signature` header which contains a hash signature you can use to validate the request body. See the Securing your Log Drains section to learn how to verify requests.
### NDJSON Drains
When you choose the `ndjson` type, the URL receives a HTTPS or HTTP POST request with JSON objects delimited by newline (`\\n`) on the `POST` body. See ndjson.org for more information on the structure.
Each request receives HTTP headers including `x-vercel-signature`.
The following are two example `POST` bodies:
ndjson-drains
```
{
"id":"1573817187330377061717300000",
"message":"done",
"timestamp":1573817187330,
"type":"stdout",
"source":"build",
"projectId":"abcdefgdufoJxB6b9b1fEqr1jUtFkyavUURbnDCFCnZxgs",
"deploymentId":"dpl_233NRGRjVZX1caZrXWtz5g1TAksD",
"buildId":"bld_cotnkcr76",
"host":"*.vercel.app",
"entrypoint":"api/index.js"
}
```

ndjson-drains
```
{
"id":"1573817250283254651097202070",
"message":"START RequestId: 643af4e3-975a-4cc7-9e7a-1eda11539d90 Version: $LATEST\\n2019-11-15T11:27:30.721Z\\t643af4e3-975a-4cc7-9e7a-1eda11539d90\\tINFO\\thello\\nEND RequestId: 643af4e3-975a-4cc7-9e7a-1eda11539d90\\nREPORT RequestId: 643af4e3-975a-4cc7-9e7a-1eda11539d90\\tDuration: 16.76 ms\\tBilled Duration: 100 ms\\tMemory Size: 1024 MB\\tMax Memory Used: 78 MB\\tInit Duration: 186.49 ms\\t\\n",
"timestamp":1573817250283,
"source":"lambda",
"requestId":"894xj-1573817250172-7847d20a4939",
"statusCode":200,
"proxy": {
"timestamp":1573817250172,
"path":"/api",
"userAgent": [
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"
  ],
"referer":"*.vercel.app",
"method":"GET",
"scheme":"https",
"host":"*.vercel.app",
"statusCode":200,
"clientIp":"120.75.16.101",
"region":"sfo1"
 },
"projectId":"abcdefgdufoJxB6b9b1fEqr1jUtFkyavUURbnDCFCnZxgs",
"deploymentId":"dpl_233NRGRjVZX1caZrXWtz5g1TAksD",
"host":"*.vercel.app",
"path":"api/index.js"
}
```

### Syslog Drain
When you choose the `syslog` type, the URL is connected with TLS or TCP. Log Drain messages are formatted according to RFC5424 framed using octet counting defined in RFC6587.
Syslog messages resemble the following:
syslog-drains
```
425<142>12019-11-15T11:42:22.562Z*.vercel.app now proxy - [proxy@54735 requestId="q8k4w-1573818142562-9adfb40ce9d4" statusCode="200" method="GET" path="/api" userAgent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36" referer="*.vercel.app" clientIp="120.75.16.101" region="sfo1" signature="b847f4dd531d0b41094fb4b38fd62bde0b0e29a5"]587<150>12019-11-15T11:42:22.833Z*.vercel.app now lambda - [lambda@54735 requestId="q8k4w-1573818142562-9adfb40ce9d4" statusCode="200" path="api/index.js" signature="0900101157dac2a2e555524c2f8d61229b15307d"] BOMSTART RequestId: ec00309f-4514-4128-8b8a-9a0e74900283 Version: $LATEST
2019-11-15T11:42:23.176Z\\tec00309f-4514-4128-8b8a-9a0e74900283\\tINFO\\thello
END RequestId: ec00309f-4514-4128-8b8a-9a0e74900283
REPORT RequestId: ec00309f-4514-4128-8b8a-9a0e74900283\\tDuration:20.08 ms\\tBilled Duration:100 ms Memory Size:1024MB\\tMax Memory Used:77MB\\tInit Duration:157.97 ms
```

Similar to JSON and NDJSON drains, a syslog message contains a hash signature for verifying messages on the `signature` key of structured data. On syslog drains, the signature is computed using an OAuth2 secret and the `MSG` section of the syslog format.
### Securing your Log Drains
All drains support transport-level encryption using `HTTPS` or `TLS` protocols, and we strongly recommend using them on production and use others only for development and testing.
When your server starts receiving payloads, it could be a third party sending log messages to your server if they know the URL. Therefore, it is recommended to use HTTP Basic Authentication, or verify messages are sent from Vercel using an OAuth2 secret and hash signature.
For example, if you have a basic HTTP server subscribing to Log Drains, the payload can be validated like so:
server.js
```
consthttp=require('http');
constcrypto=require('crypto');
http
.createServer((req, res) => {
var body ='';
req.on('data',function (chunk) {
   body += chunk;
  });
req.on('end',function () {
if (!verifySignature(req, body)) {
res.statusCode =403;
res.end("signature didn't match");
return;
   }
res.end('ok');
  });
 })
.listen(3000);
functionverifySignature(req, body) {
constsignature= crypto
.createHmac('sha1',process.env.OAUTH2_SECRET)
.update(body)
.digest('hex');
return signature ===req.headers['x-vercel-signature'];
}
```

You can compute the signature using an HMAC hexdigest from the `secret` token of the OAuth2 app and request body, then compare it with the value of the `x-vercel-signature` header to validate the payload.
## Next steps
### Endpoints
Learn about the available endpoints, their parameters and responses with examples.
### Errors
Learn about the different kinds of errors you may encounter when using the Rest API.
### Interfaces
Learn about the shared interfaces referenced across multiple endpoints.
### Integrations
Learn how to use the REST API to build your Integrations and work with Redirect URLs.
Last updated on July 16, 2024
Previous
whoami
Next
Endpoints
Was this helpful?
supported.
Send
AskAsk v0
Vercel REST APIAskAsk v0
