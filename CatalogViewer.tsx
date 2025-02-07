import React, { useEffect, useState } from 'react';
import axios from 'axios';

const CatalogViewer: React.FC = () => {
    const [catalog, setCatalog] = useState<string[]>([]);

    useEffect(() => {
        const fetchCatalog = async () => {
            try {
                const response = await axios.get(
                    'https://eld84ap8v8.execute-api.us-east-1.amazonaws.com/V1/generate-catalog'
                );
                setCatalog(response.data);
            } catch (error) {
                console.error('Error fetching catalog:', error);
            }
        };
        fetchCatalog();
    }, []);

    return (
        <div>
            <h2>Generated Catalog</h2>
            <ul>
                {catalog.map((entry, index) => (
                    <li key={index}>{entry}</li>
                ))}
            </ul>
        </div>
    );
};

export default CatalogViewer;
