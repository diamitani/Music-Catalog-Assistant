import { NextApiRequest, NextApiResponse } from 'next';
import axios from 'axios';

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
    if (req.method === 'POST') {
        try {
            const { message } = req.body;
            const apiResponse = await axios.post(
                'https://eld84ap8v8.execute-api.us-east-1.amazonaws.com/V1/process-metadata',
                { message }
            );
            res.status(200).json(apiResponse.data);
        } catch (error) {
            res.status(500).json({ error: 'Failed to process request' });
        }
    } else {
        res.status(405).json({ message: 'Method Not Allowed' });
    }
}
