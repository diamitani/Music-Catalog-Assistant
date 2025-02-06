import os
from werkzeug.utils import secure_filename
import boto3
from flask import jsonify

def upload_files(request):
    s3 = boto3.client('s3')
    bucket_name = os.getenv('AWS_S3_BUCKET')
    
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    files = request.files.getlist('file')
    responses = []

    for file in files:
        filename = secure_filename(file.filename)
        if not is_valid_format(filename):
            return jsonify({'error': f"Invalid format for file {filename}"}), 400
        
        try:
            s3.upload_fileobj(file, bucket_name, f"uploads/{filename}")
            responses.append({'file': filename, 'status': 'uploaded successfully'})
        except Exception as e:
            responses.append({'file': filename, 'status': f'upload failed: {str(e)}'})

    return jsonify({'uploads': responses})

def is_valid_format(filename):
    allowed_formats = {'mp3', 'wav', 'flac', 'aiff', 'aac'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_formats
