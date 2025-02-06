from flask import Flask, request, jsonify
from flask_cors import CORS
from dynamic_upload_handler import upload_files
from dynamic_metadata_enrichment import validate_and_enrich
from metadata_extractor import extract_metadata
from catalog_generator import generate_catalog
from report_generator import generate_health_report
from storage_manager import StorageManager
import os
from dotenv import load_dotenv
import boto3

load_dotenv()

app = Flask(__name__)
CORS(app)

# AWS S3 setup
s3 = boto3.client('s3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)
storage_manager = StorageManager(s3)

@app.route('/upload', methods=['POST'])
def upload_handler():
    return upload_files(request)

@app.route('/process-metadata', methods=['POST'])
def process_metadata():
    try:
        files = request.files.getlist('file')
        metadata_list = []

        for file in files:
            metadata = extract_metadata(file)
            enriched_metadata = validate_and_enrich(metadata)
            storage_manager.store_metadata(enriched_metadata)
            metadata_list.append(enriched_metadata)

        return jsonify({'success': True, 'metadata': metadata_list})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generate-catalog', methods=['POST'])
def generate_catalog_handler():
    try:
        metadata_list = request.json['metadata']
        output_format = request.json.get('format', 'csv')
        catalog_file = generate_catalog(metadata_list, output_format)
        return jsonify({'success': True, 'catalog_file': catalog_file})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/generate-report', methods=['POST'])
def generate_report():
    try:
        metadata_list = request.json['metadata']
        report = generate_health_report(metadata_list)
        return jsonify({'success': True, 'report': report})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
