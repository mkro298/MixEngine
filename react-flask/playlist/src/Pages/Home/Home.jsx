import React, {useState} from 'react'
import { Search, Results } from '../../Components/index.js';
import "./Home.css"

const Home = () => {
    const [songs, setSongs] = useState([]); 
    const [param, setParam] = useState(""); 
    return (
      <>
      <div className='app'>
        <div className='search-bar'>
          <h5>Search to find a song you like then click on the Make Playlist button to add a playlist based on your chosen song to your Spotify dashboard</h5>
        <Search setSongs={setSongs}/>
        </div>
        <div className='song-results'>
        <Results songs={songs} setParam={setParam}/>
        </div>
      </div>
      </>
    );
}

export default Home