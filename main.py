from yt_music.exporter import Exporter
from ya_music.importer import Importer

import sys

from PyQt5 import QtWidgets
from generated_ui.main_window import Ui_MainWindow

def show_message(title: str, text: str, status):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(status)
    msg.setText(text)
    msg.setWindowTitle(title)
    msg.exec_()

def show_error_message(text: str):
    show_message("Error", text, QtWidgets.QMessageBox.Critical)

def show_success_message(text: str):
    show_message("Success", text, QtWidgets.QMessageBox.Information)

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.convert_button.clicked.connect(self.convert)

    def convert(self):
        lost_count = 0
        lost_percent = 0.0
        try:
            ya_token = self.ui.ya_music_token_line_edit.text()
            yt_music_playlist_url = self.ui.yt_music_playlist_url_line_edit.text()
            yt_exporter = Exporter()
            playlist = yt_exporter.export_playlist(yt_music_playlist_url)

            ya_importer = Importer(ya_token)
            lost_track_ids = ya_importer.import_playlist(playlist)

            lost_count = len(lost_track_ids)
            lost_percent = lost_count * 100 / playlist.track_count()

        except Exception as ex:
            show_error_message(f"Failed to convert playlist.\nReason: {str(ex)}")
            return

        try:
            show_success_message(f"The conversion was completed successfully.")

            self.ui.lost_tracks_count_spin.setValue(lost_count)
            self.ui.lost_tracks_percent_spin.setValue(lost_percent)

            self.ui.lost_tracks_list_widget.clear()
            for track_id in lost_track_ids:
                track = playlist.tracks[track_id]
                title = track.title
                artist = track.artists[0].name
                self.ui.lost_tracks_list_widget.addItem(f"{title} - {artist}")
        
        except Exception as ex:
            show_error_message(f"Error: {str(ex)}")
            return
    
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())