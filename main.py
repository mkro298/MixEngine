import os 
from flask import Flask, session, url_for, redirect, request
from dotenv import load_dotenv

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler

from filtering import *

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(64)

client_id =  os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_url = 'http://127.0.0.1:5000/callback'
scope = 'playlist-read-private playlist-modify-private'

cache_handler = FlaskSessionCacheHandler(session)
sp_oauth = SpotifyOAuth(
    client_id=client_id, 
    client_secret=client_secret, 
    redirect_uri=redirect_url, 
    scope=scope, 
    cache_handler=cache_handler, 
    show_dialog=True
)

sp = Spotify(auth_manager=sp_oauth)

@app.route('/')
def home(): 
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    return redirect(url_for('get_playlists'))

@app.route('/callback')
def callback():
    sp_oauth.get_access_token(request.args['code'])
    return redirect(url_for('get_playlists'))

@app.route('/get_playlists')
def get_playlists():
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    user_info = sp.me()
    sp.user_playlist_create(user=user_info['id'], name="play", public=False, description = " ", collaborative=False)
    tracks = get_recs('Anti-Hero', 'Taylor Swift', 20)
    add_songs(tracks=tracks)
    return f"Playlist created for user:{user_info['display_name']}"

def add_songs(tracks):
    user_info = sp.me()
    playlists = sp.user_playlists(user_info['id'])
    pl = list(playlists['items'])[0]
    sp.user_playlist_add_tracks(user=user_info['id'], playlist_id=pl['id'], tracks=tracks)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

