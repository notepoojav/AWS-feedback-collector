# AWS-feedback-collector
A serverless AWS application that captures user feedback through an API, processes it with AWS Lambda (Python), stores it securely in DynamoDB, and sends real-time email alerts using Amazon SES. Built with scalability, clean backend logic, and cloud-native architecture in mind.

# Tech Stacks employed 
* AWS Lambda [Python]
* Amazon API Gateway
* Amazon Dynamo DB
* Amazon Simple Email Service
* IAM Roles and Permissions
* AWS Cloudwwatch [to track log lambda events]

# What does the AWS Feedback Collector do?
* Accepts feedback [generalised to a product feedback] via HTTP POST Method.
* Sends to Lambda function.
* Stores the feedback data in DynamoDb.
* Sends feedback email using Amazon SES.

#How to Deploy?
* Create and deploy a Lambda Function. Refer to feedback.py.
* Assign permissions to access DynamoDB and SES.
* Create a POST HTTP API with Resource path: /submitFeedback.
* Integrate with the contructed Lambda function.
* Create DynamoDB Table - feedid (String) as primary key.
* Verify email identity in SES.
* Set up corresponding IAM Roles.


