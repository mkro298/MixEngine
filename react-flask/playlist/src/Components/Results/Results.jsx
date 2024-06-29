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
                <a href={`http://127.0.0.1:5000/?param=${param}`}>sign into spotify</a>
                </div>
            )}
            </>
          )
    }
}

export default Results