import json
import boto3
import os
from metadata_extractor import extract_metadata
from dynamic_metadata_enrichment import validate_and_enrich

# Initialize S3 client with environment variables
s3 = boto3.client('s3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)
bucket_name = os.getenv('AWS_S3_BUCKET')

def lambda_handler(event, context):
    try:
        # Extract file information from the event
        file_info = event['file_info']
        file_name = file_info['file_name']

        # Simulate file access (for Lambda, adjust this for S3-triggered events if needed)
        metadata = extract_metadata(file_name)
        enriched_metadata = validate_and_enrich(metadata)

        # Store enriched metadata in S3
        store_metadata_in_s3(file_name, enriched_metadata)

        return {
            'statusCode': 200,
            'body': json.dumps(f'Metadata for {file_name} stored successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }

def store_metadata_in_s3(file_name, metadata):
    s3.put_object(
        Bucket=bucket_name,
        Key=f"metadata/{file_name}.json",
        Body=json.dumps(metadata)
    )
