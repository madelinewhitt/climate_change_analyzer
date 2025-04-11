import React from 'react';

const Home: React.FC = () => {
  return (
    <div className="home flex justify-center items-center min-h-screen w-full relative bg-cover bg-center" style={{ backgroundImage: 'url(../assets/nikolas-noonan-fQM8cbGY6iQ-unsplash.jpg)' }}>
      <div className="content-overlay relative z-10 text-center text-white p-8">
        <h1 className="text-5xl font-bold">Welcome to PyDisaster</h1>
        <p className="text-xl mt-4">The best natural disaster impact analyzer</p>
      </div>
      <div className="absolute inset-0 bg-black opacity-50"></div>
    </div>
  );
};

export default Home;
