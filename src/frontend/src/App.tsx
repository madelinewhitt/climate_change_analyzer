// src/App.tsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MenuBar from './components/MenuBar'; // Menu bar component
import Home from './pages/Home';            // Home page component
import Graph1 from './pages/Graph1';        // World Map Information
import Footer from './pages/Footer';        // Footer
import Comparison from './pages/Comparison';
import ClusterComparison from './pages/Clustering';
import Anomalies from './pages/Anomalies';

const App: React.FC = () => {
  return (
    <Router>
      <div className="app">
        <MenuBar />
            <Routes>
              <Route path="/" element={<><Home /></>} />
              <Route path="/Graph1" element={<Graph1 />} />
              <Route path="/Comparison" element={<Comparison />} />
              <Route path="/Clustering" element={<ClusterComparison />} />
              <Route path="/Anomalies" element={<Anomalies/>} />
            </Routes>
        <Footer />
      </div>
    </Router>
  );
};

export default App;