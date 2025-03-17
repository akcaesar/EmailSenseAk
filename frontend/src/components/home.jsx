// This file contains the code for the home page of the frontend. It fetches the number of emails from the backend and displays it on the page.
import React, { useEffect, useState } from 'react';
import api from '../api';

const Home = () => {
    const [data, setData] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await api.get('/emails/count');
                setData(response.data);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, []);

    return (
        <div>
            <h1>Connected to backend</h1>
            <p>{data ? JSON.stringify(data.count) : 'Loading...'}</p>
        </div>
    );
};

export default Home;