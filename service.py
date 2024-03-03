from yt_music import exporter as yt_exporter
from ya_music import importer as ya_importer

class ConvertService:

    def __init__(self):
        self.default_yt_exporter = yt_exporter.Exporter()
    
    def convert_youtube_to_yandex(self, yt_url: str, yandex_token: str):
        try:
            yt_playlist = self.default_yt_exporter.export_playlist(yt_url)
            ya_importer.Importer(yandex_token).import_playlist(yt_playlist)
        except Exception as ex:
            raise RuntimeError(
                "Error: could't convert playlist\n"
                f"Reason: {str(ex)}"
            )