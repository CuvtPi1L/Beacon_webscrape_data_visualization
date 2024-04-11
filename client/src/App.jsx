import React, { useState, useEffect } from 'react';
import SearchComponent from './Search';
import ResultsComponent from './Results';

function App() {
  const [data, setData] = useState([]);
  const [filteredData, setFilteredData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Fetch data from localhost:5000
    fetch('http://localhost:5000/data')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setData(data);
        setFilteredData(data); // Initialize filteredData with all data
      })
      .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        setError(error.message);
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  const handleSearch = (searchCriteria) => {
    const filtered = data.filter(item =>
      (searchCriteria.parcelId ? item.parcelId.toString() === searchCriteria.parcelId : true) &&
      (searchCriteria.salePrice ? item.salePrice.toString() === searchCriteria.salePrice : true) &&
      (searchCriteria.address ? item.address.toLowerCase().includes(searchCriteria.address.toLowerCase()) : true)
    );
    setFilteredData(filtered);
  };

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div className="App">
      <h1>Real Estate Data Viewer</h1>
      <SearchComponent onSearch={handleSearch} />
      <ResultsComponent data={filteredData} />
    </div>
  );
}

export default App;
