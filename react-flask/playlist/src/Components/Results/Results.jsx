import React from 'react'
import "./Results.css"

const Results = ({songs}) => {
    if (songs) {
        return (
            <>
            <div className='results-list'>
                {songs.map((song, id) => {
                    console.log(song)
                    return <div key={id}>{song.id}</div>
                })}
            </div>
            </>
          )
    }
}

export default Results