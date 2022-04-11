import os

from spotify import SpotifyClient

#Browse through Spotify for random songs and create a list

def start_program():
    spotify_token = input('Please enter your Spotify Token: ')
    spotify_client = SpotifyClient(spotify_token)
    random_songs = spotify_client.get_random_tracks()
    songs_ids = [song['id'] for song in random_songs]

#Add this list to library

    added_to_library = spotify_client.add_songs_to_library(songs_ids)
    if added_to_library:
        for song in random_songs:
            print(f"Added {song['name']} to the library")

if __name__ == '__main__':
    start_program()