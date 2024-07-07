import numpy as np
import pandas as pd 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

url = "https://media.githubusercontent.com/media/mkro298/MixEngine/main/spotify_data.csv"
columns = ['track_name', 'artist_name', 'track_id', 'genre', 'valence', 'energy', 'danceability', 'loudness', 'instrumentalness']
df1 = pd.read_csv(url, usecols=columns)
df1 = df1.drop_duplicates()


def get_matrix(genre):
    sampled = df1[df1['genre'] == genre]
    features = ['valence', 'energy', 'danceability', 'loudness', 'instrumentalness']
    df2 = sampled[features]
    scaler = StandardScaler()
    df2  = scaler.fit_transform(df2)
    sim_matrix = cosine_similarity(df2)
    return sim_matrix, sampled 

def get_genre(song, artist):
    genre = df1.loc[(df1['track_name'] == song) & (df1['artist_name'] == artist), 'genre'].values[0]
    return genre 

def check_in_database(song, artist):
    return not df1[(df1['track_name'] == song) & (df1['artist_name'] == artist)].empty

def get_recs(song, artist, length, id = None, genre=None, new_song_features=None):
    global df1
    if new_song_features:
        if (not(check_in_database(song, artist))):
            new_song_data = {
                'track_name': song,
                'artist_name': artist,
                'genre': genre,  
                'track_id': id
            }
            new_song_data.update(new_song_features[0])
            new_song_df = pd.DataFrame([new_song_data])
            df1 = pd.concat([df1, new_song_df], ignore_index=True)
            
    genre = get_genre(song, artist)
    cosine_sim, sampled = get_matrix(genre)
    indices = {song: i for i, song in enumerate(sampled['track_name'])}

    if song not in indices:
        raise ValueError("Song '{song}' not found.")
    
    index = indices[song]

    sim_scores = list(enumerate(cosine_sim[index]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[0:length]

    song_index = [i[0] for i in sim_scores]

    return sampled['track_id'].iloc[song_index]
