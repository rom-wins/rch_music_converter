from enum import Enum
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

class Token(Enum):
    YANDEX_TOKEN = 1

class Data:
    def __init__(self) -> None:
        self.users = {}

    def create_user(self, username: str) -> None:
        if username in self.users.keys():
            return
        self.users[username] = {}

    def save_yandex_token(self, username: str, token: str) -> None:
        self.users[username][Token.YANDEX_TOKEN] = token

    def get_yandex_token(self, username: str) -> str:
        if username is None or len(username) == 0:
            raise RuntimeError("Error: Username could not be empty.")

        if username not in self.users:
            raise RuntimeError("Error: User is not registered.")

        if Token.YANDEX_TOKEN not in self.users[username]:
            raise RuntimeError("Error: User don't add yandex token.")

        return self.users[username][Token.YANDEX_TOKEN]
