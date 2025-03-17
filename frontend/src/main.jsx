import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import Home from './components/home.jsx'
import Emails from './components/Emails.jsx'
import BasicTable from './layouts/Table.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BasicTable />
  </StrictMode>,
)
