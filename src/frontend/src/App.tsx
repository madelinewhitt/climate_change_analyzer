// src/App.tsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MenuBar from './components/MenuBar'; // Menu bar component
import Home from './pages/Home';           // Home page component
import About from './pages/About';         // About page component
import './styles/App.css';                // Global styles

const App: React.FC = () => {
  return (
    <Router>
      <div className="app">
        <MenuBar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
