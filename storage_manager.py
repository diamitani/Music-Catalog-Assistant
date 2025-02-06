import boto3
import os
import json

class StorageManager:
    def __init__(self, s3_client):
        self.s3 = s3_client
        self.bucket_name = os.getenv('AWS_S3_BUCKET')

    def store_metadata(self, metadata):
        file_path = f"metadata/{metadata.get('title', 'unknown')}.json"
        self.s3.put_object(Bucket=self.bucket_name, Key=file_path, Body=json.dumps(metadata))
