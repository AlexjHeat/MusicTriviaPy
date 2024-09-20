# This Python file uses the following encoding: utf-8
from PySide6 import QtUiTools
from PySide6.QtCore import QUrl
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
import time
from countdown import Countdown
from volumemanager import VolumeManager

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
        self.countdown.countdownComplete.connect(self.reveal)
        self.showCountdown()

        self.volumeManager = VolumeManager(self.audioOutput)

    def play(self, filepath, songString):
        self.showCountdown()
        self.ui.songStringLabel.setText(songString)

        if self.mediaPlayer.isPlaying():
            self.mediaPlayer.stop()
            time.sleep(0.1)

        self.mediaPlayer.setSource(QUrl.fromLocalFile(filepath))
        self.mediaPlayer.play()
        self.volumeManager.softStart()
        self.countdown.start()

    def stop(self):
        self.showCountdown()
        self.mediaPlayer.stop()
        self.countdown.stop()

    def setCountdownTime(self, time):
        self.countdown.setTime(time, not self.mediaPlayer.isPlaying())

    def reveal(self):
        self.showVideo()
        self.volumeManager.enterQuietMode()

    def showVideo(self):
        self.videoWidget.show()
        self.ui.songStringLabel.show()
        self.ui.countdownLCD.hide()

    def showCountdown(self):
        self.ui.countdownLCD.show()
        self.videoWidget.hide()
        self.ui.songStringLabel.hide()

    def setVolume(self, i):
        self.volumeManager.setVolume(i)
