from typing import List

class Artist:
    def __init__(self, name) -> None:
        self.name = name
    
class Track:
    def __init__(self, title: str, artists: List[Artist]) -> None:
        self.title = title
        self.artists = artists

class Playlist:
    def __init__(self, title: str, tracks: List[Track]) -> None:
        self.title = title
        self.tracks = tracks
    
    def track_count(self) -> int:
        return len(self.tracks)