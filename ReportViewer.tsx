import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ReportViewer: React.FC = () => {
    const [report, setReport] = useState<any>(null);

    useEffect(() => {
        const fetchReport = async () => {
            try {
                const response = await axios.get(
                    'https://eld84ap8v8.execute-api.us-east-1.amazonaws.com/V1/generate-report'
                );
                setReport(response.data);
            } catch (error) {
                console.error('Error fetching report:', error);
            }
        };
        fetchReport();
    }, []);

    return (
        <div>
            <h2>Health Report</h2>
            {report ? <pre>{JSON.stringify(report, null, 2)}</pre> : <p>Loading report...</p>}
        </div>
    );
};

export default ReportViewer;
