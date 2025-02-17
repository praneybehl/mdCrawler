Skip to content
Menu
On this page
# AWS S3 ​
## TLDR ​
  1. Create a bucket in AWS Console
  2. Create a custom policy in AWS Console with the following permissions:


json```
{
 "Version": "2012-10-17",
 "Statement": [
  {
   "Effect": "Allow",
   "Action": [
    "s3:ListBucket",
    "s3:GetObject",
    "s3:DeleteObject",
    "s3:GetObjectAcl",
    "s3:PutObjectAcl",
    "s3:PutObject"
   ],
   "Resource": [
    // rewrite your-bucket-name with your bucket name
    "arn:aws:s3:::your-bucket-name",
    "arn:aws:s3:::your-bucket-name/*"
   ]
  }
 ]
}
```

  1. Create an IAM user in AWS Console & attach the policy from the previous step.
  2. Go to User settings & create an `Access Key` in AWS Console.
  3. Add the `Access Key` and `Secret Key` in Coolify when you create a new S3 source.
Tip
You need to use the S3 HTTP endpoint without the bucket name, for example,`https://s3.eu-central-1.amazonaws.com`.


# Detailed steps ​
### Create a bucket ​
  1. Create a bucket in AWS Console Go to AWS Console and create a new bucket.
![](https://coolify.io/docs/images/aws-s3/1-bucket.webp)
  2. Name your bucket.


![](https://coolify.io/docs/images/aws-s3/2-bucket.webp)
### Create a new policy ​
  1. Create a new policy. Go to AWS Console and create a new policy.
![](https://coolify.io/docs/images/aws-s3/1-policy.webp)
  2. Name & configure your policy. Add the following JSON permissions to your policy (replace `your-bucket-name` with your bucket name):
json```
{
 "Version": "2012-10-17",
 "Statement": [
  {
   "Effect": "Allow",
   "Action": [
    "s3:ListBucket",
    "s3:GetObject",
    "s3:DeleteObject",
    "s3:GetObjectAcl",
    "s3:PutObjectAcl",
    "s3:PutObject"
   ],
   "Resource": [
    "arn:aws:s3:::your-bucket-name",
    "arn:aws:s3:::your-bucket-name/*"
   ]
  }
 ]
}
```

![](https://coolify.io/docs/images/aws-s3/2-policy.webp)
![](https://coolify.io/docs/images/aws-s3/3-policy.webp)


### Create a new IAM user ​
  1. Create a new IAM User. Go to AWS Console and create a new user.
![](https://coolify.io/docs/images/aws-s3/1-iam.webp)
  2. Name your user.
![](https://coolify.io/docs/images/aws-s3/2-iam.webp)
  3. Attach the policy created in the previous step.
![](https://coolify.io/docs/images/aws-s3/3-iam.webp)
  4. Go to your user settings.
![](https://coolify.io/docs/images/aws-s3/4-iam.webp)
  5. Create a new `Access Key`.
![](https://coolify.io/docs/images/aws-s3/5-iam.webp)
  6. Set `Other` as use-case.
![](https://coolify.io/docs/images/aws-s3/6-iam.webp)
  7. Copy the `Access Key` & `Secret Access Key`. You will need it to configure this S3 storage in Coolify.
![](https://coolify.io/docs/images/aws-s3/7-iam.webp)


### Configure S3 in Coolify ​
  1. Add new S3 Storage. Go to your Coolify instance and create a new S3 storage.
![](https://coolify.io/docs/images/aws-s3/1-coolify.webp)
  2. Add the details. Make sure you use the S3 HTTP endpoint without the bucket name. For example,`https://s3.eu-central-1.amazonaws.com`.
![](https://coolify.io/docs/images/aws-s3/2-coolify.webp)


Well done!
