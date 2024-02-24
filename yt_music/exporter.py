from models import Playlist
from yt_music.conversion import json_to_playlist
from ytmusicapi import YTMusic

def get_yt_music_playlist_id_from_url(url: str):
    try:
        playlist_token = "list="
        return url.split(playlist_token)[1].split("&")[0]
    except Exception:
        raise RuntimeError("Incorrect youtube music playlist url")
    
class Exporter:
    def __init__(self) -> None:
        self.ytmusic = YTMusic()

    def export_playlist(self, playlist_url: str) -> Playlist:
        playlist_id = get_yt_music_playlist_id_from_url(playlist_url)
        json_playlist = self.ytmusic.get_playlist(playlistId=playlist_id, limit=None)
        return json_to_playlist(json_playlist)
