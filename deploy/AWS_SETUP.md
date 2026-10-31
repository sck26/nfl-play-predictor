# AWS deployment guide

Review the latest [AWS Free Tier](https://aws.amazon.com/free/) terms before creating services. Enable MFA, monitor billing, and do not share credentials. A parent or guardian may need to help with age, payment, and account requirements.

## 1. Lambda API
1. In the [AWS Lambda Console](https://console.aws.amazon.com/lambda/), create a Python function using a least-privilege execution role.
2. Copy `lambda_api/app.py` into the code editor's `lambda_function.py`; set the handler to `lambda_function.handler`. Alternatively, zip `app.py` at the ZIP root and use `app.handler`.
3. Deploy and test with:
```json
{"requestContext":{"http":{"method":"GET"}},"queryStringParameters":{"down":"3","distance":"8"}}
```
4. To use the browser demo, enable a Lambda Function URL with authorization type `NONE` and configure CORS for `GET`, `OPTIONS`, and `content-type`. This exposes a public API. Monitor usage and costs.
5. Test `https://YOUR_FUNCTION_URL/?down=3&distance=8`.

## 2. Connect the website
Set `const API_URL='https://YOUR_FUNCTION_URL/';` inside `site/index.html`. Test that the response comes from AWS Lambda rather than the browser fallback.

## 3. S3 hosting
1. Create a dedicated S3 bucket and upload only `site/index.html`, named `index.html`.
2. Enable Static website hosting and specify `index.html` as the index document.
3. To make the website public, follow the [official Amazon S3 static website tutorial](https://docs.aws.amazon.com/AmazonS3/latest/userguide/HostingWebsiteOnS3Setup.html). Restrict any public-read policy to this specific bucket's objects. Do not upload credentials or private information.
4. Open the website endpoint from bucket Properties.

S3 website endpoints are HTTP-only. For HTTPS and a private bucket, consider AWS Amplify Hosting or CloudFront with origin access control; check additional costs.

## 4. Verify / clean up
Test the page and the Lambda API separately, then together. Configure usage monitoring and remove unneeded services. AWS Budgets alerts are not a hard spending cap.

This project is not considered AWS-deployed until you actually complete the above steps.
