import React, { useState } from 'react';
import axios from 'axios';

const UploadFiles: React.FC = () => {
    const [selectedFiles, setSelectedFiles] = useState<File[]>([]);
    const [uploadStatus, setUploadStatus] = useState('');

    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        if (e.target.files) {
            setSelectedFiles(Array.from(e.target.files));
        }
    };

    const handleUpload = async () => {
        const formData = new FormData();
        selectedFiles.forEach(file => formData.append('files', file));

        try {
            const response = await axios.post(
                'https://eld84ap8v8.execute-api.us-east-1.amazonaws.com/V1/process-metadata',
                formData
            );
            setUploadStatus('Upload Successful: ' + response.data.body);
        } catch (error) {
            setUploadStatus('Upload Failed: ' + error.message);
        }
    };

    return (
        <div>
            <h2>Upload Audio Files</h2>
            <input type="file" multiple onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload</button>
            <p>{uploadStatus}</p>
        </div>
    );
};

export default UploadFiles;
