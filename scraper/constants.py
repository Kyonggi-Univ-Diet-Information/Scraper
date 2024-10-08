from dotenv import load_dotenv
import os

load_dotenv()

# AWS S3 Access Keys
access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')