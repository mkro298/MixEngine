import React from 'react'
import "./Song.css"

const Song = ({image, name, artist, id}) => {
  return (
    <div className='result'>
        <img src={image}></img>
        <div className='blurb'>
            <p>{name}</p>
            <p>{artist}</p>
        </div>
    </div>
  )
}

export default Song