import axios, { Axios } from 'axios';

const token = 'ghu_hrjQKJ62M1zVHnyu5yuHfZ4i00K5Ub2sAWfP';

const api = axios.create({
  baseURL: process.env.REACT_APP_BACKEND_URL || 'http://localhost:8000',
  timeout: 1000,
  headers: { 
    'Authorization': `Bearer ${token}`,
    'X-Custom-Header': 'foobar'
  }
});

export default api;