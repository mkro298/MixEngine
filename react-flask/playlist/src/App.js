import './App.css';
import React, {useState} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Search, Results } from './Components/index';

function App() {
  const [songs, setSongs] = useState([]); 
  const [param, setParam] = useState(""); 
  return (
    <>
    <div className='app'>
      <div className='search-bar'>
      <Search setSongs={setSongs}/>
      </div>
      <div className='song-results'>
      <Results songs={songs} setParam={setParam}/>
      </div>
    </div>
    </>
  );
}

export default App;
