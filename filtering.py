import numpy as np
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler


df1 = pd.read_csv("/Users/monishakrothapalli/Documents/GitHub/playlistGen/spotify_data.csv")

def section_data(genre):
    sampled = df1[df1['genre'] == genre]
    features = ['popularity', 'valence', 'energy', 'danceability', 'loudness']
    df2 = sampled[features]
    scaler = StandardScaler()
    df2  = scaler.fit_transform(df2)
    sim_matrix = cosine_similarity(df2)
    return sim_matrix, sampled 

def get_indices(genre):
    _, sampled = section_data(genre)
    indices = {song: i for i, song in enumerate(sampled['track_name'])}
    return indices; 

def get_genre(song, artist):
    genre = df1.loc[(df1['track_name'] == song) & (df1['artist_name'] == artist), 'genre'].values[0]
    return genre 

def get_recs(song, aritst, length):
    genre = get_genre(song, aritst)

    cosine_sim, sampled = section_data(genre)
    indices = get_indices(genre)

    if song not in indices:
        raise ValueError("Song '{song}' not found.")
    
    index = indices[song]

    sim_scores = list(enumerate(cosine_sim[index]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[0:length]

    song_index = [i[0] for i in sim_scores]

    return sampled['track_name'].iloc[song_index]

def main():
    tracks = get_recs('Anti-Hero', 'Taylor Swift', 20)
    for song in tracks:
        print(song)

if __name__ == "__main__":
    main()