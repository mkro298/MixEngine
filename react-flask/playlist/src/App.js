import './App.css';
import React, {useState} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Search, Results } from './Components/index';

function App() {
  const [songs, setSongs] = useState([]); 
  const param = 'Anti-Hero';
  return (
    <>
    <div className='app'>
    <Search setSongs={setSongs}/>
    <Results songs={songs} />
    <a href={`http://127.0.0.1:5000/?param=${param}`}>sign into spotify</a>
    </div>
    </>
  );
}

export default App;
