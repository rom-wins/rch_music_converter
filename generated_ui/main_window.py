# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(671, 544)
        MainWindow.setMinimumSize(QtCore.QSize(671, 544))
        MainWindow.setMaximumSize(QtCore.QSize(671, 544))
        MainWindow.setWindowTitle("Convert your music")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.convert_button = QtWidgets.QPushButton(self.centralwidget)
        self.convert_button.setGeometry(QtCore.QRect(84, 120, 485, 27))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.convert_button.setFont(font)
        self.convert_button.setText("Convert youtube music playlist to yandex music playlist")
        self.convert_button.setObjectName("convert_button")
        self.ya_music_token_label = QtWidgets.QLabel(self.centralwidget)
        self.ya_music_token_label.setGeometry(QtCore.QRect(48, 32, 197, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ya_music_token_label.setFont(font)
        self.ya_music_token_label.setText("Yandex music token")
        self.ya_music_token_label.setObjectName("ya_music_token_label")
        self.yt_music_playlist_url_label = QtWidgets.QLabel(self.centralwidget)
        self.yt_music_playlist_url_label.setGeometry(QtCore.QRect(50, 76, 197, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.yt_music_playlist_url_label.setFont(font)
        self.yt_music_playlist_url_label.setText("YT music playlist url")
        self.yt_music_playlist_url_label.setObjectName("yt_music_playlist_url_label")
        self.lost_tracks_count_spin = QtWidgets.QSpinBox(self.centralwidget)
        self.lost_tracks_count_spin.setGeometry(QtCore.QRect(398, 186, 105, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lost_tracks_count_spin.setFont(font)
        self.lost_tracks_count_spin.setAlignment(QtCore.Qt.AlignCenter)
        self.lost_tracks_count_spin.setReadOnly(True)
        self.lost_tracks_count_spin.setMaximum(1000)
        self.lost_tracks_count_spin.setObjectName("lost_tracks_count_spin")
        self.lost_tracks_percent_spin = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lost_tracks_percent_spin.setGeometry(QtCore.QRect(398, 222, 105, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lost_tracks_percent_spin.setFont(font)
        self.lost_tracks_percent_spin.setAlignment(QtCore.Qt.AlignCenter)
        self.lost_tracks_percent_spin.setReadOnly(True)
        self.lost_tracks_percent_spin.setObjectName("lost_tracks_percent_spin")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(116, 182, 55, 16))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.lost_tracks_count_label = QtWidgets.QLabel(self.centralwidget)
        self.lost_tracks_count_label.setGeometry(QtCore.QRect(70, 188, 267, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lost_tracks_count_label.setFont(font)
        self.lost_tracks_count_label.setText("The number of lost tracks")
        self.lost_tracks_count_label.setObjectName("lost_tracks_count_label")
        self.lost_tracks_percent_label = QtWidgets.QLabel(self.centralwidget)
        self.lost_tracks_percent_label.setGeometry(QtCore.QRect(72, 220, 295, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lost_tracks_percent_label.setFont(font)
        self.lost_tracks_percent_label.setText("The percentage of lost tracks")
        self.lost_tracks_percent_label.setObjectName("lost_tracks_percent_label")
        self.ya_music_token_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.ya_music_token_line_edit.setGeometry(QtCore.QRect(256, 34, 375, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ya_music_token_line_edit.setFont(font)
        self.ya_music_token_line_edit.setText("")
        self.ya_music_token_line_edit.setObjectName("ya_music_token_line_edit")
        self.yt_music_playlist_url_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.yt_music_playlist_url_line_edit.setGeometry(QtCore.QRect(256, 76, 375, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.yt_music_playlist_url_line_edit.setFont(font)
        self.yt_music_playlist_url_line_edit.setText("")
        self.yt_music_playlist_url_line_edit.setObjectName("yt_music_playlist_url_line_edit")
        self.lost_tracks_label = QtWidgets.QLabel(self.centralwidget)
        self.lost_tracks_label.setGeometry(QtCore.QRect(294, 276, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lost_tracks_label.setFont(font)
        self.lost_tracks_label.setText("Lost tracks")
        self.lost_tracks_label.setObjectName("lost_tracks_label")
        self.lost_tracks_list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.lost_tracks_list_widget.setGeometry(QtCore.QRect(138, 304, 423, 185))
        self.lost_tracks_list_widget.setObjectName("lost_tracks_list_widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 671, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass
