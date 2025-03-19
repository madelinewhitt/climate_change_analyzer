// src/pages/Home.tsx
import React from 'react';

const Home: React.FC = () => {
  return (
    <div className="home">
    <div className="center-content">
      <h1>Welcome to PyDisaster</h1>
      <p>The best natural disaster impact analyzer</p>
      <img src="https://www.noaa.gov/sites/default/files/styles/landscape_width_1275/public/2022-03/PHOTO-Climate-Collage-Diagonal-Design-NOAA-Communications-NO-NOAA-Logo.jpg" className="my-image" />
      </div>
    </div>

  );
};

export default Home;
