import React, { useEffect, useState } from 'react';
import api from '../api';

const Emails = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await api.get('/emails');
                setData(response.data);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, []);

    return (
        <div>
            <h2>These are the emails</h2>
            <p>{data ? JSON.stringify(data) : 'Loading...'}</p>
        </div>
    );
};

export default Emails;