# This Python file uses the following encoding: utf-8
from PySide6 import QtUiTools
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget

class DisplayWindow:
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = QtUiTools.QUiLoader().load("displaywindow.ui")
        self.ui.show()

        self.mediaPlayer = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.mediaPlayer.setAudioOutput(self.audioOutput)
        self.videoWidget = QVideoWidget()
        self.ui.verticalLayout.addWidget(self.videoWidget)
        self.mediaPlayer.setVideoOutput(self.videoWidget)

    def play(self, filepath):
        self.mediaPlayer.setSource(QUrl.fromLocalFile(filepath))
        self.mediaPlayer.play()

    def stop(self):
        self.mediaPlayer.stop()

