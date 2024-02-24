from typing import List
from models import Artist, Track

def normalize_title(title: str) -> str:
    return title.translate(str.maketrans('', '', "()."))

def normalize_artist_names(artists: List[Artist]):
    return ' '.join([artist.name for artist in artists])

def get_search_track_query(track: Track) -> str:
    norm_title = normalize_title(track.title)
    norm_artist_names = normalize_artist_names(track.artists)
    
    query = f"{norm_title} - {norm_artist_names}"
    return query 
