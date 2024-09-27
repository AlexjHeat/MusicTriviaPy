# This Python file uses the following encoding: utf-8
from PySide6 import QtUiTools
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtGui import QPixmap, QMovie
from countdown import Countdown
from volumemanager import VolumeManager
import time, random

MIN_POST_GUESS_TIME = 20

class DisplayWindow:

    def __init__(self, parent, countdownTime):
        super().__init__()
        self.parent = parent
        self.ui = QtUiTools.QUiLoader().load("displaywindow.ui")
        self.ui.show()

        self.activeSong = None
        self.activeCategory = None
        self.round = 0

        self.videoOutput = QVideoWidget()
        self.videoOutput.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.ui.videoLayout.addWidget(self.videoOutput)
        self.mediaPlayer = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.mediaPlayer.setAudioOutput(self.audioOutput)
        self.mediaPlayer.setVideoOutput(self.videoOutput)

        self.countdown = Countdown(self.ui.countdownLCD, countdownTime)
        self.countdown.countdownComplete.connect(self.reveal)
        self.showCountdown()
        self.volumeManager = VolumeManager(self.audioOutput)

        self.mediaPlayer.mediaStatusChanged.connect(self.updatePosition)

    def loadCategory(self, category):
        if category is None:
            return False

        self.activeCategory = category
        folder = self.activeCategory.folderName
        movie = QMovie(folder + "/center.gif")
        self.ui.bannerCenter.setMovie(movie)
        movie.start()
        self.ui.bannerLeft.setPixmap(QPixmap(folder + "/left.png"))
        self.ui.bannerRight.setPixmap(QPixmap(folder + "/right.png"))

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

    def updatePosition(self, status):
        if status == QMediaPlayer.LoadedMedia:
            if self.activeSong.startTime == 0 or self.activeSong.startTime is None:
                trackLength = int(self.mediaPlayer.duration() / 1000)
                countdownTime = self.countdown.getTime()
                maxStartTime = trackLength - countdownTime - MIN_POST_GUESS_TIME
                if maxStartTime <= 0:
                    self.mediaPlayer.setPosition(0)
                else:
                    self.mediaPlayer.setPosition(random.randint(0,maxStartTime) * 1000)
            elif self.activeSong.startTime > 0:
                self.mediaPlayer.setPosition(self.activeSong.startTime * 1000)

    def getPosition(self):
        if self.mediaPlayer.mediaStatus() == QMediaPlayer.EndOfMedia:
            return False
        else:
            return int(self.mediaPlayer.position() /1000)

    def getTrackLength(self):
        return int(self.mediaPlayer.duration() / 1000)

    def setCountdownTime(self, time):
        self.countdown.setTime(time, not self.mediaPlayer.isPlaying())

    def reveal(self):
        self.showVideo()
        self.volumeManager.enterQuietMode()

    def showVideo(self):
        self.ui.mainDisplay.setCurrentIndex(0)
        #add try catch block in case activeSong is still a None type (AttributeError)
        self.ui.songLabel.setText(self.activeSong.anime)
        if self.round > 0 : self.ui.roundLabel.setText(f'Round {self.round}')

    def showCountdown(self):
        self.ui.mainDisplay.setCurrentIndex(1)
        self.ui.songLabel.setText("")
        if self.round > 0 : self.ui.roundLabel.setText(f'Round {self.round}')

    def setVolume(self, i):
        self.volumeManager.setVolume(i)

    def setRound(self, i):
        self.round = i
        if self.round > 0 : self.ui.roundLabel.setText(f'Round {self.round}')

    def setFullscreen(self, enable):
        if enable:
            self.ui.showFullScreen()
        else:
            self.ui.showNormal()

