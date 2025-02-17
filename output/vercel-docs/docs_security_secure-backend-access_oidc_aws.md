# Your Privacy
This site uses tracking technologies. You may opt in or opt out of the use of these technologies.
DenyAccept all
Consent Settings
Privacy Policy
Your Privacy
This site uses tracking technologies. You may opt in or opt out of the use of these technologies.
Marketing
Off
Marketing cookies and services are used to deliver personalized advertisements, promotions, and offers. These technologies enable targeted advertising and marketing campaigns by collecting information about users' interests, preferences, and online activities. 
Analytics
Off
Analytics cookies and services are used for collecting statistical information about how visitors interact with a website. These technologies provide insights into website usage, visitor behavior, and site performance to understand and improve the site and enhance user experience.
Functional
Off
Functional cookies and services are used to offer enhanced and personalized functionalities. These technologies provide additional features and improved user experiences, such as remembering your language preferences, font sizes, region selections, and customized layouts. Opting out of these cookies may render certain services or functionality of the website unavailable.
Essential
On
Essential cookies and services are used to enable core website features, such as ensuring the security of the website. 
SaveDenyAccept all
Privacy Policy
![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-light.cf7eca76.svg)![vercel-logotype Logo](https://vercel.com/vc-ap-vercel-docs/_next/static/media/vercel-logotype-dark.01246f11.svg)
Search...
`⌘ K`
Feedback
Log In
Sign Up
Security
Secure Backend Access
OpenID Connect Federation
Connect to Amazon Web Services (AWS)
How-to
# Connect to Amazon Web Services (AWS)
Learn how to configure your AWS account to trust Vercel's OpenID Connect (OIDC) Identity Provider (IdP).
Table of Contents
Secure backend access with OIDC federation is available on all plans
To understand how AWS supports OIDC, and for a detailed user guide on creating an OIDC identity provider with AWS, consult the AWS OIDC documentation.
## Configure your AWS account
  1. ### Create an OIDC identity provider
    1. Navigate to the AWS Console
    2. Navigate to IAM then Identity Providers
    3. Select Add Provider
    4. Select OpenID Connect from the provider type
    5. Enter the Provider URL, the URL will depend on the issuer mode setting: 
       * Team: `https://oidc.vercel.com/[TEAM_SLUG]`, replacing `[TEAM_SLUG]` with the path from your Vercel team URL
       * Global: `https://oidc.vercel.com`
    6. Enter `https://vercel.com/[TEAM_SLUG]` in the Audience field, replacing `[TEAM_SLUG]` with the path from your Vercel team URL
    7. Select Add Provider
![](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1718267924%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Faws-create-id-provider.png&w=1080&q=75)![](https://vercel.com/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fv1718267924%2Fdocs-assets%2Fstatic%2Fdocs%2Fconcepts%2Foidc-tokens%2Faws-create-id-provider.png&w=1080&q=75)
  2. ### Create an IAM role
To use AWS OIDC Federation you must have an IAM role. IAM roles require a "trust relationship" (also known as a "trust policy") that describes which "Principal(s)" are allowed to assume the role under certain "Condition(s)".
Here is an example of a trust policy using the Team issuer mode:
trust-policy.json
```
{
"Version":"2012-10-17",
"Statement": [
  {
"Effect":"Allow",
"Principal": {
"Federated":"arn:aws:iam::[YOUR AWS ACCOUNT ID]:oidc-provider/oidc.vercel.com/[TEAM_SLUG]"
   },
"Action":"sts:AssumeRoleWithWebIdentity",
"Condition": {
"StringEquals": {
"oidc.vercel.com/[TEAM_SLUG]:sub":"owner:[TEAM SLUG]:project:[PROJECT NAME]:environment:production",
"oidc.vercel.com/[TEAM_SLUG]:aud":"https://vercel.com/[TEAM SLUG]"
    }
   }
  }
 ]
}
```

The above policy's conditions are quite strict. It requires the `aud` sub `sub` claims to match exactly, but it's possible to configure less strict trust policies conditions:
trust-policy.json
```
{
"Version":"2012-10-17",
"Statement": [
  {
"Effect":"Allow",
"Principal": {
"Federated":"arn:aws:iam::[YOUR AWS ACCOUNT ID]:oidc-provider/oidc.vercel.com/[TEAM_SLUG]"
   },
"Action":"sts:AssumeRoleWithWebIdentity",
"Condition": {
"StringEquals": {
"oidc.vercel.com/[TEAM_SLUG]:aud":"https://vercel.com/[TEAM SLUG]"
    },
"StringLike": {
"oidc.vercel.com/[TEAM_SLUG]:sub": [
"owner:[TEAM SLUG]:project:*:environment:preview",
"owner:[TEAM SLUG]:project:*:environment:production"
     ]
    }
   }
  }
 ]
}
```

This policy allows any project matched by the `*` that are targeted to `preview` and `production` but not `development`.
  3. ### Define the role ARN as environment variable
Once you have created the role, copy the role's ARN and declare it as an environment variable in your Vercel project with key name `AWS_ROLE_ARN`.
.env.local
```
AWS_ROLE_ARN=arn:aws:iam::accountid:user/username
```

You are now ready to connect to your AWS resource in your project's code. Review the examples below.


## Examples
In the following examples, you create a Vercel function in the Vercel project where you have defined the OIDC role ARN environment variable. The function will connect to a specific resource in your AWS backend using OIDC and perform a specific action using the AWS SDK.
### List objects in an AWS S3 bucket
Install the following packages:
pnpmyarnnpm
```
pnpm i @aws-sdk/client-s3 @vercel/functions
```

In the API route for the function, use the AWS SDK for JavaScript to list objects in an S3 bucket with the following code:
/api/aws-s3/route.ts
```
import*as S3 from'@aws-sdk/client-s3';
import { awsCredentialsProvider } from'@vercel/functions/oidc';
constAWS_REGION=process.env.AWS_REGION!;
constAWS_ROLE_ARN=process.env.AWS_ROLE_ARN!;
constS3_BUCKET_NAME=process.env.S3_BUCKET_NAME!;
// Initialize the S3 Client
consts3client=newS3.S3Client({
 region:AWS_REGION,
// Use the Vercel AWS SDK credentials provider
 credentials:awsCredentialsProvider({
  roleArn:AWS_ROLE_ARN,
 }),
});
exportasyncfunctionGET() {
constresult=awaits3client.send(
newS3.ListObjectsV2Command({
   Bucket:S3_BUCKET_NAME,
  }),
 );
returnresult?.Contents?.map((object) =>object.Key) ?? [];
}
```

Vercel sends the OIDC token to the SDK using the `awsCredentialsProvider` function from `@vercel/functions`.
### Query an AWS RDS instance
Install the following packages:
pnpmyarnnpm
```
pnpm i @aws-sdk/rds-signer @vercel/functions pg
```

In the API route for the function, use the AWS SDK for JavaScript to perform a database `SELECT` query from an AWS RDS instance with the following code:
/api/aws-rds/route.ts
```
import { awsCredentialsProvider } from'@vercel/functions/oidc';
import { Signer } from'@aws-sdk/rds-signer';
import { Pool } from'pg';
constRDS_PORT=parseInt(process.env.RDS_PORT!);
constRDS_HOSTNAME=process.env.RDS_HOSTNAME!;
constRDS_DATABASE=process.env.RDS_DATABASE!;
constRDS_USERNAME=process.env.RDS_USERNAME!;
constRDS_CA_PEM=process.env.RDS_CA_PEM!;
constAWS_REGION=process.env.AWS_REGION!;
constAWS_ROLE_ARN=process.env.AWS_ROLE_ARN!;
// Initialize the RDS Signer
constsigner=newSigner({
// Use the Vercel AWS SDK credentials provider
 credentials:awsCredentialsProvider({
  roleArn:AWS_ROLE_ARN,
 }),
 region:AWS_REGION,
 port:RDS_PORT,
 hostname:RDS_HOSTNAME,
 username:RDS_USERNAME,
});
// Initialize the Postgres Pool
constpool=newPool({
 password:signer.getAuthToken,
 user:RDS_USERNAME,
 host:RDS_HOSTNAME,
 database:RDS_DATABASE,
 port:RDS_PORT,
});
// Export the route handler
exportasyncfunctionGET() {
try {
constclient=awaitpool.connect();
const { rows } =awaitclient.query('SELECT * FROM my_table');
returnResponse.json(rows);
 } finally {
client.release();
 }
}
```

Last updated on October 23, 2024
Previous
OpenID Connect Federation
Next
Connect to Google Cloud Platform (GCP)
Was this helpful?
supported.
Send
AskAsk v0
Connect to Amazon Web Services (AWS)AskAsk v0
