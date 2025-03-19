// src/main.tsx
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';  // Import the App component
import './styles/App.css';  // Import global styles

// Create the root of your React app and render the App component
const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
root.render(
  <React.StrictMode>
    <App />  {/* Render the App component */}
  </React.StrictMode>
);
