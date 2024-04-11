import React, { useState } from 'react';

function SearchComponent({ onSearch }) {
  const [searchCriteria, setSearchCriteria] = useState({
    parcelId: '',
    salePrice: '',
    address: '',
  });

  const handleChange = (e) => {
    setSearchCriteria({ ...searchCriteria, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch(searchCriteria);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="parcelId"
        placeholder="Parcel ID"
        value={searchCriteria.parcelId}
        onChange={handleChange}
      />
      <input
        type="text"
        name="salePrice"
        placeholder="Sale Price"
        value={searchCriteria.salePrice}
        onChange={handleChange}
      />
      <input
        type="text"
        name="address"
        placeholder="Address"
        value={searchCriteria.address}
        onChange={handleChange}
      />
      <button type="submit">Search</button>
    </form>
  );
}

export default SearchComponent;
