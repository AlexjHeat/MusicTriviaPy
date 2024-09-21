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

        self.activeSong = None
        self.round = 0

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


    def play(self, filepath, song):
        self.showCountdown()
        self.activeSong = song
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
        self.ui.countdownLCD.hide()
        #add try catch block in case activeSong is still a None type (AttributeError)
        self.ui.songLabel.setText(self.activeSong.anime)
        if self.round > 0 : self.ui.roundLabel.setText(f'Round {self.round}')

    def showCountdown(self):
        self.ui.countdownLCD.show()
        self.videoWidget.hide()
        self.ui.songLabel.setText("")
        if self.round > 0 : self.ui.roundLabel.setText(f'Round {self.round}')

    def setVolume(self, i):
        self.volumeManager.setVolume(i)

    def setRound(self, i):
        self.round = i
        if self.round > 0 : self.ui.roundLabel.setText(f'Round {self.round}')
