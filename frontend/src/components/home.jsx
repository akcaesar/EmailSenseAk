
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
            <h1>Home Page</h1>
            <p>{data ? JSON.stringify(data) : 'Loading...'}</p>
        </div>
    );
};

export default Home;