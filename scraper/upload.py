import constants
import boto3
import requests

OBJECT_NAME_TO_UPLOAD = 'output.csv'

s3_client = boto3.client(
    's3',
    aws_access_key_id = constants.access_key,
    aws_secret_access_key = constants.secret_access_key,
    region_name = 'us-east-1'
)

response = s3_client.generate_presigned_post(
    Bucket = 'dorm-menu',
    Key = OBJECT_NAME_TO_UPLOAD,
    ExpiresIn = 60
)

files = {'file' : open(OBJECT_NAME_TO_UPLOAD, 'rb')}
r = requests.post(response['url'], data=response['fields'], files=files)
print(f"Status Code: {r.status_code}")
print(f"Response Text: {r.text}")