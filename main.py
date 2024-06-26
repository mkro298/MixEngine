import os 
from flask import Flask, session
from dotenv import load_dotenv

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)

client_id =  os.getenv("CLIENT_ID")
client_secert = os.getenv("CLIENT_SECRET")
redirect_url = 'http://localhost:3000/'
scope = 'playlist-read-private, playlist-modify-private'

cache_handler = FlaskSessionCacheHandler(session)
sp_oauth = SpotifyOAuth(
    client_id=client_id, 
    client_secret=client_secert, 
    redirect_uri=redirect_url, 
    scope=scope, 
    cache_handler=cache_handler, 
    show_dialog=True
)

sp = Spotify(auth_manager=sp_oauth)


if __name__ == '__main__':
    app.run(debug=True)

