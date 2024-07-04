import React, {useState} from 'react'
import "./Results.css"
import Song from "../Song/Song"


const Results = ({songs}) => {
    const [param, setParam] = useState("")
    const [enlarged, setEnlargedImage] = useState(null); 

    const handleClick = (songID, src) => {
        setEnlargedImage(src);
        setParam(songID); 
    }; 

    const handleOverlayClick = (e) => {
        if (e.target.tagName !== 'IMG') {
            setEnlargedImage(null);
        }
    };

    if (songs) {
        return (
            <>
            <div className='results-list'>
                {songs.map((song, id) => {
                    return <button onClick={() => handleClick(song.id, song.album.images[0].url)}>
                        <Song image={song.album.images[0].url} name={song.name} artist={song.artists[0].name} id={song.id}/>
                    </button>
                })}
            </div>

            {enlarged && (
                <div className='overlay' onClick={handleOverlayClick}>
                <img className='enlarged-image' src={enlarged} alt="Enlarged Art" />
                <button className='spotify-button' onClick={() => window.location.href = `https://mixengine-9e2430800a72.herokuapp.com/?param=${param}`}>
                Make Playlist
                </button>
                </div>
            )}
            </>
          )
    }
}

export default Results