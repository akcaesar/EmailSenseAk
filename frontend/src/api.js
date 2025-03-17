import axios, { Axios } from 'axios';

// // Create an axios instance with base URL
// const api = axios.create({
//     baseURL: 'https://fuzzy-rotary-phone-jw66v6699q4h54qg-8000.app.github.dev/',
// });

// // Add a request interceptor to include the GitHub token in the headers
// api.interceptors.request.use(config => {
//     const token = 'ghu_hrjQKJ62M1zVHnyu5yuHfZ4i00K5Ub2sAWfP'; // Replace with your actual GitHub token
//     if (token) {
//         config.headers.Authorization = `Bearer ${token}`;
//     }
//     return config;
// }, error => {
//     return Promise.reject(error);
// });

// export default api;


const token = 'ghu_hrjQKJ62M1zVHnyu5yuHfZ4i00K5Ub2sAWfP';

const api = axios.create({
  baseURL: 'https://fuzzy-rotary-phone-jw66v6699q4h54qg-8000.app.github.dev/',
  timeout: 1000,
  headers: { 
    'Authorization': `Bearer ${token}`,
    'X-Custom-Header': 'foobar'
  }
});

export default api;