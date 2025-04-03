// src/App.tsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MenuBar from './components/MenuBar'; // Menu bar component
import Home from './pages/Home';            // Home page component
import About from './pages/About';          // About page component
import Graph1 from './pages/Graph1';        // World Map Information
import Footer from './pages/Footer';
import './styles/App.css';                // Global styles

const App: React.FC = () => {
  return (
    <Router>
      <div className="app">
        <MenuBar />
        <Routes>
          <Route path="/" element={<><Home /> <Footer /></>} />
          <Route path="/about" element={<About />} />
          <Route path="/Graph1" element={<Graph1 />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
