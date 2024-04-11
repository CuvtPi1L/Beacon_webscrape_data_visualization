import React from 'react';

function ResultsComponent({ data }) {
  return (
    <div>
      {data.length > 0 ? (
        <ul>
          {data.map((item, index) => (
            <li key={index}>
              {item.address} - Parcel ID: {item.parcelId}, Sale Price: {item.salePrice}
            </li>
          ))}
        </ul>
      ) : (
        <p>No results found.</p>
      )}
    </div>
  );
}

export default ResultsComponent;
