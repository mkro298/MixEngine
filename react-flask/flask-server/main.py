import os
from flask import Flask, session, url_for, redirect, request
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler

from filtering import *

load_dotenv()

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = os.urandom(64)

client_id =  os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_url = 'https://flaskengine-156a7f257487.herokuapp.com/callback'
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

@cross_origin
@app.route('/', methods=['GET'])
def home(): 
    param = request.args.get('param')
    if param:
        session['param'] = param 
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    
    stored_param = session.get('param')
    return get_playlists(stored_param)
     

@app.route('/callback')
def callback():
    sp_oauth.get_access_token(request.args['code'])
    stored_param = session.get('param')
    return get_playlists(stored_param)
    

def get_playlists(param):
    if not sp_oauth.validate_token(cache_handler.get_cached_token()):
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)
    user_info = sp.me()
    track = sp.track(track_id=param)
    audio_features = sp.audio_features(param)

    if ('genres' in track['artists'][0]):
        genre = track['artists'][0]['genres'][0]
    else:
        genre = 'pop'
    
    tracks = get_recs(track['name'], track['artists'][0]['name'], 20, param, genre, audio_features)

    name = track['name']
    playlist_name = f"Songs Based on {name}"
    sp.user_playlist_create(user=user_info['id'], name=playlist_name, public=False, description = " ", collaborative=False)
    add_songs(tracks=tracks)
    return f"Playlist created for user {user_info['display_name']} has now been added to your profile"

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
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

