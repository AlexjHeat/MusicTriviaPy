# This Python file uses the following encoding: utf-8
from PySide6 import QtUiTools
from PySide6.QtCore import QUrl, QFileInfo
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import QMessageBox, QFileDialog

class DisplayWindow:
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = QtUiTools.QUiLoader().load("displaywindow.ui")
        self.ui.show()

        self.mediaPlayer = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.mediaPlayer.setAudioOutput(self.audioOutput)


        #self.videoWidget = QVideoWidget()
        #QMessageBox.warning(self.parent, 'Warning', str(type(self.ui.videoWidget)))
        #self.video = QVideoWidget(self.ui.videoScreen)
        #self.mediaPlayer.setVideoOutput(self.video)
        #self.video = QVideoWidget(self.ui.videoScreen)
        #self.videoWidget.show()

    def play(self, filepath):
        self.mediaPlayer.setSource(QUrl.fromLocalFile(filepath))


        #TESTING
        #test = QVBoxLayout(self.ui.videoScreen)
        self.videoWidget = QVideoWidget()
        #test.addWidget(self.videoWidget)
        self.ui.mainLayout.addWidget(self.videoWidget)
        #self.videoWidget = QVideoWidget(self.ui.videoScreen)
        #self.videoWidget.resize(500, 500)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.play()

