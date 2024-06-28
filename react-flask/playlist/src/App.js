import './App.css';
import React from 'react';
import axios from 'axios';

function App() {
  const param = 'Anti-Hero';
  return (
    <>
    <a href={`http://127.0.0.1:5000/?param=${param}`}>sign into spotify</a>
    </>
  );
}

export default App;
