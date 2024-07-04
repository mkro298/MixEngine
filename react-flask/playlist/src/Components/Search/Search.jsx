import React, {useEffect, useState} from 'react'
import "./Search.css"; 
import {FaSearch} from "react-icons/fa"; 

const CLIENT_SECRET = process.env.CLIENT_SECRET;
const CLIENT_ID = process.env.CLIENT_ID; 

const Search = ({setSongs}) => {
    const [input, setInput] = useState(""); 
    const[accessToken, setAccessToken] = useState(""); 

    useEffect(() => {
        //getting the token 
        var authParam = {
            method: 'POST', 
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }, 
            body: 'grant_type=client_credentials&client_id=' + CLIENT_ID + '&client_secret=' + CLIENT_SECRET
        }
        fetch('https://accounts.spotify.com/api/token',authParam).then(result => result.json()).then(data => setAccessToken(data.access_token))
    }, [])

    //search function 
    async function search() {
        console.log("Search for " + input)
        console.log(CLIENT_ID); 
        console.log(CLIENT_SECRET); 
    
        //get top 20 tracks based off searched title 
        var trackParam = {
            method: 'GET', 
            headers: {
                'Content-Type': 'application/json', 
                'Authorization': 'Bearer ' + accessToken
            }
        }
        //need to save spotify ID 
        var tracks = await fetch('https://api.spotify.com/v1/search?q=' + input + '&type=track', trackParam).then(response => response.json()).then(data => {
            if (data.tracks && data.tracks.items) {
                return data.tracks.items
            }
        })
        console.log(tracks)
        setSongs(tracks)

        //display tracks 

    }


    const handleChange = (value) => {
        setInput(value)
        search()
    }

  return (
    <>
    <div className='search-bar'>
        <div className='input-wrapper'>
            <FaSearch id="search-icon" />
            <input placeholder='Type to find song...' v
            alue={input} 
            onChange={(e) => handleChange(e.target.value)}/>
        </div>
    </div>
    </>
  )
}

export default Search