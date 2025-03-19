// import React, { useEffect, useState } from 'react';

// const Home = () => {
//     const [data, setData] = useState(null);

//     useEffect(() => {
//         const fetchData = async () => {
//             try {
//                 const response = await fetch('https://fuzzy-rotary-phone-jw66v6699q4h54qg-8000.app.github.dev/emails/count', {
//                     // headers: {
//                     //     'Authorization': `Bearer ghu_hrjQKJ62M1zVHnyu5yuHfZ4i00K5Ub2sAWfP`,
//                     // }
//                 });
//                 const result = await response.json();
//                 setData(result);
//             } catch (error) {
//                 console.error(error);
//             }
//         };

//         fetchData();
//     }, []);

//     return (
//         <div>
//             <h1>Home Page</h1>
//             <p>{data ? JSON.stringify(data) : 'Loading...'}</p>
//         </div>
//     );
// };

// export default Home;

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