import boto3

Bucket='data-transfers'
Key='directory-one'
client = boto3.client('s3')

response = client.put_object(
        Bucket='data-transfers',
        Body='',
        Key='directory-one/'
        )