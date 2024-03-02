from typing import Optional

import yandex_music
from models import Playlist, Track
from ya_music.queries import get_search_track_query

class Importer:

    def __init__(self, token: str) -> None:
        self.client = yandex_music.Client(token=token).init()

    def _create_playlist(self, title: str) -> Optional[yandex_music.Playlist]:
        try:
            return self.client.users_playlists_create(title)
        except Exception as ex:
            raise RuntimeError(f"Could't create playlist. Error: {ex}")

    @staticmethod
    def parse_track(track: yandex_music.Track) -> tuple:
        try:
            return track.id, track.albums[0].id
        except Exception as ex:
            raise RuntimeError(f"Could't parse track. Error: {ex}")
        
    def _search_track(self, track: Track) -> yandex_music.Track:
        try:
            query = get_search_track_query(track)
            result = self.client.search(query, type_="all")
            
            if result.best and result.best.type == "track":
                return result.best.result
            
            if result.tracks and result.tracks.total:
                return result.tracks.results[0]
            
        except Exception as ex:
            raise RuntimeError(f"Could't search track. Error: {ex}")

    def import_playlist(self, playlist: Playlist) -> yandex_music.Playlist:
        ya_playlist = self._create_playlist(playlist.title)
        
        lost_track_ids = []
        for track_id in range(len(playlist.tracks)):
            try:
                track = playlist.tracks[track_id]
                result = self._search_track(track)
                track_id, album_id = Importer.parse_track(result)
                ya_playlist.insert_track(track_id, album_id)
                ya_playlist.revision += 1

            except Exception:
                lost_track_ids.append(track_id)
                continue

        return lost_track_ids
