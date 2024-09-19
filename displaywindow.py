# This Python file uses the following encoding: utf-8
from PySide6 import QtUiTools
from PySide6.QtCore import QUrl, QTimer
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from countdown import Countdown

class DisplayWindow:
    def __init__(self, parent, countdownTime):
        super().__init__()
        self.parent = parent
        self.ui = QtUiTools.QUiLoader().load("displaywindow.ui")
        self.ui.show()

        self.mediaPlayer = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.mediaPlayer.setAudioOutput(self.audioOutput)
        self.videoWidget = QVideoWidget()
        self.ui.videoLayout.addWidget(self.videoWidget)
        self.mediaPlayer.setVideoOutput(self.videoWidget)

        self.countdown = Countdown(self.ui.countdownLCD, countdownTime)
        self.countdown.countdownComplete.connect(self.showVideo)
        self.showCountdown()

        self.isSongPlaying = False

    def play(self, filepath, songString):
        self.showCountdown()
        self.ui.songStringLabel.setText(songString)
        self.mediaPlayer.setSource(QUrl.fromLocalFile(filepath))
        self.mediaPlayer.play()
        self.countdown.start()
        self.isSongPlaying = True

    def stop(self):
        self.showCountdown()
        self.mediaPlayer.stop()
        self.countdown.stop()
        self.isSongPlaying = False

    def setCountdownTime(self, time):
        self.countdown.setTime(time, not self.isSongPlaying)

    def showVideo(self):
        self.videoWidget.show()
        self.ui.songStringLabel.show()
        self.ui.countdownLCD.hide()

    def showCountdown(self):
        self.ui.countdownLCD.show()
        self.videoWidget.hide()
        self.ui.songStringLabel.hide()

