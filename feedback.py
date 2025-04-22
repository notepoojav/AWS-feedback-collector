import json
import boto3
import uuid
import os

dynamodb = boto3.resource('dynamodb')
ses = boto3.client('ses', region_name='us-east-1')  # Use your SES region

# Set table name as an environment variable for best practice
table = dynamodb.Table(os.environ['FEEDBACK_TABLE'])

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        name = body.get('name')
        email = body.get('email')
        message = body.get('message')

        if not name or not email or not message:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing required fields'})
            }

        feedback_id = str(uuid.uuid4())

        # 1. Store in DynamoDB
        table.put_item(Item={
            'feedid': feedback_id,
            'name': name,
            'email': email,
            'message': message
        })

        # 2. Send Email using SES
        ses.send_email(
            Source='notepooja.v@gmail.com',  # SES verified email
            Destination={'ToAddresses': [email]},
            Message={
                'Subject': {'Data': 'Thank you for your feedback!'},
                'Body': {
                    'Text': {
                        'Data': f'Hi {name},\n\nThanks for your message:\n\n"{message}"\n\nWe appreciate it!'
                    }
                }
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Feedback submitted successfully!'})
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Something went wrong.'})
        }
