# This Python file uses the following encoding: utf-8
from PySide6 import QtUiTools
from PySide6.QtCore import QUrl, Qt
from PySide6.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QLabel
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtGui import QPixmap, QMovie, QFontDatabase, QFont, QColor
from countdown import Countdown
from volumemanager import VolumeManager
from db import Category
import fontlib
import time, random
from config import MIN_POST_GUESS_TIME, DEFAULT_ROUND_FONT, DEFAULT_ROUND_FONT_SIZE, DEFAULT_ROUND_COLOR, DEFAULT_CLOCK_FONT, DEFAULT_CLOCK_FONT_SIZE, DEFAULT_CLOCK_COLOR, DEFAULT_BACKGROUND_COLOR
MIN_POST_GUESS_TIME = 15


class DisplayWindow:

    def __init__(self, parent, countdownTime):
        super().__init__()
        self.parent = parent
        self.ui = QtUiTools.QUiLoader().load("displaywindow.ui")
        self.displayInfoLabel = QLabel(self.ui.backgroundImageLabel)
        self.displayInfoLabel.setGeometry(610, 10, 710, 220)
        self.displayInfoLabel.setAlignment(Qt.AlignCenter)
        self.displayInfoLabel.setWordWrap(True)
        self.displayInfoLabel.show()
        self.ui.show()

        self.activeSong = None
        self.activeCategory = None
        self.round = 0

        self.videoOutput = QVideoWidget()
        self.videoOutput.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.ui.videoLayout.addWidget(self.videoOutput)
        self.mediaPlayer = QMediaPlayer()
        audioOutput = QAudioOutput()
        self.mediaPlayer.setAudioOutput(audioOutput)
        self.mediaPlayer.setVideoOutput(self.videoOutput)
        self.mediaPlayer.mediaStatusChanged.connect(self.updateStartPosition)

        self.countdown = Countdown(self.ui.countdownLabel, countdownTime)
        self.countdown.countdownComplete.connect(self.reveal)
        self.countdown.countdownTransition.connect(self.transition)
        self.showCountdownPage()
        self.volumeManager = VolumeManager(audioOutput)


    def loadCategory(self, category):
        if category is None:
            return False
        self.activeCategory = category

        #Display label stylesheets
        displayColor = {QColor(category.nameColor).isValid(): category.nameColor}.get(True, DEFAULT_ROUND_COLOR)
        styleSheet = f"color: {displayColor}"
        font = fontlib.getFont(category.nameFont, DEFAULT_ROUND_FONT_SIZE, DEFAULT_ROUND_FONT)
        self.displayInfoLabel.setStyleSheet(styleSheet)
        self.displayInfoLabel.setFont(font)

        #clock label stylesheet
        backgroundColor = {QColor(category.backgroundColor).isValid(): category.backgroundColor}.get(True, DEFAULT_BACKGROUND_COLOR)
        clockColor = {QColor(category.clockColor).isValid(): category.clockColor}.get(True, DEFAULT_CLOCK_COLOR)
        styleSheet = f"background-color: {backgroundColor}; color: {clockColor}"
        font = fontlib.getFont(category.clockFont, DEFAULT_CLOCK_FONT_SIZE, DEFAULT_CLOCK_FONT)
        self.ui.countdownLabel.setStyleSheet(styleSheet)
        self.ui.countdownLabel.setFont(font)

        self.updateDisplayInfo()


#   ~~~MEDIA PLAYER~~~
    def play(self, filepath, song):
        self.showCountdownPage()
        self.activeSong = song
        if self.mediaPlayer.isPlaying():
            self.mediaPlayer.stop()
            time.sleep(0.1)

        self.mediaPlayer.setSource(QUrl.fromLocalFile(filepath))
        self.mediaPlayer.play()
        self.volumeManager.softStart()
        self.countdown.start()

    def stop(self):
        self.showCountdownPage()
        self.mediaPlayer.stop()
        self.mediaPlayer.setSource(QUrl())
        self.countdown.stop()

    def setVolume(self, i):
        self.volumeManager.setVolume(i)

    def updateStartPosition(self, status):
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

    def getCurrentPosition(self):
        if self.mediaPlayer.mediaStatus() != QMediaPlayer.EndOfMedia:
            return int(self.mediaPlayer.position() /1000)

    def getTrackLength(self):
        return int(self.mediaPlayer.duration() / 1000)


#   ~~~COUNTDOWN CLOCK & VIDEO SCREEN STACK~~~
    def setCountdownTime(self, time):
        self.countdown.setTime(time, reset=not self.mediaPlayer.isPlaying())

    def transition(self):
        movie = QMovie("./images/transitionBackground.gif")
        self.ui.backgroundImageLabel.setMovie(movie)
        movie.start()

    def reveal(self):
        self.showVideoPage()
        self.volumeManager.enterQuietMode()

    def showCountdownPage(self):
        self.ui.mainDisplay.setCurrentWidget(self.ui.countdownPage)
        movie = QMovie("./images/countdownBackground.gif")
        self.ui.backgroundImageLabel.setMovie(movie)
        movie.start()
        self.updateDisplayInfo()

    def showVideoPage(self):
        self.ui.mainDisplay.setCurrentWidget(self.ui.videoPage)
        #add try catch block in case activeSong is still a None type (AttributeError)
        movie = QMovie("./images/videoBackground.png")
        self.ui.backgroundImageLabel.setMovie(movie)
        movie.start()
        self.updateDisplayInfo()


#   ~~~DISPLAY~~~
    def setFullscreen(self, enable: bool):
        if enable:
            self.ui.showFullScreen()
        else:
            self.ui.showNormal()

    def setRound(self, i):
        self.round = i
        self.updateDisplayInfo()

    def updateDisplayInfo(self):
        text = ''
        if self.ui.mainDisplay.currentWidget() == self.ui.videoPage:
            if self.activeSong and self.activeSong.anime:
                text = f'\n{self.activeSong.anime}'
        else:
            if self.activeCategory and self.activeCategory.name != 'Default':
                text += self.activeCategory.name
            text += '\n'
            if self.round > 0:
                text += f'Round {str(self.round)}'
        self.displayInfoLabel.setText(text)

    def showCategories(self, enable: bool, categories: [Category]):
        if enable:
            self.ui.mainDisplay.setCurrentIndex(2)
            self.buildCategoryList(categories)
        elif self.mediaPlayer.isPlaying():
            self.ui.mainDisplay.setCurrentIndex(1)
        else:
            self.ui.mainDisplay.setCurrentIndex(0)

    def buildCategoryList(self, categories: [Category]):
        self.vbox = QVBoxLayout()
        self.widget = QWidget()
        for cat in categories:
            label = QLabel(cat.name)
            self.vbox.addWidget(label)
        self.widget.setLayout(self.vbox)
        self.ui.categoryScroll.setWidget(self.widget)










