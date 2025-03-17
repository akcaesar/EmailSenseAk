import * as React from 'react';
import { useEffect, useState } from 'react';
import axios from 'axios';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

export default function BasicTable() {
  const [rows, setRows] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('https://fuzzy-rotary-phone-jw66v6699q4h54qg-8000.app.github.dev/emails', {
          headers: {
            'Authorization': `Bearer ghu_hrjQKJ62M1zVHnyu5yuHfZ4i00K5Ub2sAWfP`,
          }
        });
        const data = JSON.parse(response.data);
        setRows(data.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>From</TableCell>
            <TableCell>Subject</TableCell>
            <TableCell>Date</TableCell>
            <TableCell>Time</TableCell>
            <TableCell>Body</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.index}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.From}
              </TableCell>
              <TableCell>{row.Subject}</TableCell>
              <TableCell>{new Date(row.Date).toLocaleDateString()}</TableCell>
              <TableCell>{new Date(row.Date).toLocaleTimeString()}</TableCell>
              <TableCell>{row.Body}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}