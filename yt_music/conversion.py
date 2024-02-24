from typing import List

from models import Artist, Playlist, Track

def json_to_artist(artist: dict) -> Artist:
    return Artist(artist["name"])

def json_to_artists(artists: dict) -> List[Artist]:
    return [json_to_artist(artist) for artist in artists]

def json_to_track(track: dict) -> Track:
    return Track(
        title=track["title"], 
        artists=json_to_artists(track["artists"]),
    )

def json_to_playlist(playlist: dict) -> Playlist:
    return Playlist(
        title=playlist["title"],
        tracks=[json_to_track(track) for track in playlist["tracks"]],
    )