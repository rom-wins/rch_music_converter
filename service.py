from yt_music import exporter as yt_exporter
from ya_music import importer as ya_importer

class ConvertService:

    def __init__(self):
        self.default_yt_exporter = yt_exporter.Exporter()
    
    def convert_youtube_to_yandex(self, yt_url: str, yandex_token: str) -> dict:
        try:
            yt_playlist = self.default_yt_exporter.export_playlist(yt_url)
            importer = ya_importer.Importer(yandex_token)
            losted_track_ids = importer.import_playlist(yt_playlist)

            result = {}
            for track_id in range(len(yt_playlist.tracks)):
                track = yt_playlist.tracks[track_id]
                track_name = f"{track.title}"
                result[track_name] = track_id not in losted_track_ids

            return result

        except Exception as ex:
            raise RuntimeError(
                "Error: could't convert playlist\n"
                f"Reason: {str(ex)}"
            )