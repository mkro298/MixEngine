import React from 'react'
import "./Results.css"
import Song from "../Song/Song"

const Results = ({songs}) => {
    if (songs) {
        return (
            <>
            <div className='results-list'>
                {songs.map((song, id) => {
                    return <Song image={song.album.images[0].url} name={song.name} artist={song.artists[0].name} id={song.id}/>
                })}
            </div>
            </>
          )
    }
}

export default Results