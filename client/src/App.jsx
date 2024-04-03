import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [data, setData] = useState([]);
  console.log(data)

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/data'); // Assuming your Flask API endpoint is /api/data
        setData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h1>Property Data</h1>
      <table>
        <thead>
          <tr>
            <th>Parcel ID</th>
            <th>Address</th>
            <th>Sale Price</th>
            <th>Sale Date</th>
            {/* Add more table headers for other columns */}
          </tr>
        </thead>
        <tbody>
          {data.length > 0 ? (
            data.map(item => (
              <tr key={item.ParcelID}>
                <td>{item.ParcelID}</td>
                <td>{item.Address}</td>
                <td>{item.SalePrice}</td>
                <td>{item.SaleDate}</td>
                {/* Add more table cells for other columns */}
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="4">No data available</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default App;
