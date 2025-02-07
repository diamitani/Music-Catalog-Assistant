import React, { useEffect, useState } from 'react';
import axios from 'axios';

const MetadataViewer: React.FC = () => {
    const [metadata, setMetadata] = useState<any[]>([]);

    useEffect(() => {
        const fetchMetadata = async () => {
            try {
                const response = await axios.get(
                    'https://eld84ap8v8.execute-api.us-east-1.amazonaws.com/V1/get-metadata'
                );
                setMetadata(response.data);
            } catch (error) {
                console.error('Error fetching metadata:', error);
            }
        };
        fetchMetadata();
    }, []);

    return (
        <div>
            <h2>Metadata Viewer</h2>
            <ul>
                {metadata.map((item, index) => (
                    <li key={index}>
                        <strong>{item.file_name}:</strong> {JSON.stringify(item.metadata)}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default MetadataViewer;
