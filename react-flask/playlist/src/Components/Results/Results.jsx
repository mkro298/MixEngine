import React, {useState} from 'react'
import "./Results.css"
import Song from "../Song/Song"


const Results = ({songs, setParam}) => {

    if (songs) {
        return (
            <>
            <div className='results-list'>
                {songs.map((song, id) => {
                    return <button onClick={() => setParam(song.id)}>
                        <Song image={song.album.images[0].url} name={song.name} artist={song.artists[0].name} id={song.id}/>
                    </button>
                })}
            </div>
            </>
          )
    }
}

export default Results