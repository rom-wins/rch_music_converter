from typing import List

import yandex_music
from models import Artist, Playlist, Track

def ya_artist_to_artist(source: yandex_music.Artist):
    return Artist(
        name=source.name,
    )

def ya_artists_to_artists(source: List[yandex_music.Artist]) -> List[Artist]:
    return [ya_artist_to_artist(item) for item in source]

def ya_track_to_track(source: yandex_music.Track) -> Track:
    return Track(
        title=source.title,
        artists=ya_artists_to_artists(source.artists),
    )

def ya_short_tracks_to_tracks(source: List[yandex_music.TrackShort]) -> List[Track]:
    return [ya_track_to_track(item.track) for item in source]

def ya_playlist_to_playlist(source: yandex_music.Playlist) -> Playlist:
    return Playlist(
        title=source.title,
        tracks=ya_short_tracks_to_tracks(source.tracks),
    )