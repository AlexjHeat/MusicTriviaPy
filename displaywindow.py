# This Python file uses the following encoding: utf-8
from PySide6 import QtUiTools
from PySide6.QtCore import QUrl, Qt
from PySide6.QtWidgets import QWidget, QSizePolicy, QVBoxLayout, QLabel
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtGui import QMovie, QColor
from countdown import Countdown
from volumemanager import VolumeManager
from db import Category, Song
import fontlib
import time, random
from config import MIN_POST_GUESS_TIME, DEFAULT_ROUND_FONT, DEFAULT_ROUND_FONT_SIZE, DEFAULT_ROUND_COLOR, DEFAULT_CLOCK_FONT, DEFAULT_CLOCK_FONT_SIZE, DEFAULT_CLOCK_COLOR, DEFAULT_BACKGROUND_COLOR, SONG_PATH


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
        self.mediaPlayerMode = False
        self.backgroundMovie = QMovie()

        audioOutput = QAudioOutput()
        videoOutput = QVideoWidget()
        videoOutput.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.volumeManager = VolumeManager(audioOutput)
        self.ui.videoLayout.addWidget(videoOutput)

        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer.setAudioOutput(audioOutput)
        self.mediaPlayer.setVideoOutput(videoOutput)
        self.mediaPlayer.mediaStatusChanged.connect(self.mediaStatusChanged)

        self.countdown = Countdown(self.ui.countdownLabel, countdownTime)
        self.countdown.countdownComplete.connect(self.reveal)
        self.countdown.countdownTransition.connect(self.transition)
        self.showCountdownPage()


    def loadCategory(self, category: Category):
        if category is None:
            return False
        self.activeCategory = category
        self.updateDisplayInfo()

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

#   ~~~MEDIA PLAYER~~~
    def play(self, song: Song):
        if song is None:
            return
        self.activeSong = song
        if self.mediaPlayer.isPlaying():
            self.mediaPlayer.stop()
            time.sleep(0.1)
        self.mediaPlayer.setSource(QUrl.fromLocalFile(f"{SONG_PATH}//{song.fileName}"))
        self.mediaPlayer.play()
        self.volumeManager.softStart()
        if not self.mediaPlayerMode:
            self.showCountdownPage()
            self.countdown.start()
        else:
            self.updateDisplayInfo()

    def stop(self):
        self.mediaPlayer.stop()
        #self.mediaPlayer.setSource(QUrl(''))   #Crashes program now, not sure why...
        self.countdown.stop()
        if not self.mediaPlayerMode:
            self.showCountdownPage()

    def setMediaPlayerMode(self, enable: bool):
        self.mediaPlayerMode = enable
        self.showVideoPage() if enable else self.showCountdownPage()

    def mediaStatusChanged(self, status: QMediaPlayer.MediaStatus):
        if status == QMediaPlayer.LoadedMedia:
            self.updateStartPosition(status)

    def updateStartPosition(self, status):
            if self.activeSong.startTime and self.activeSong.startTime > 0:
                self.mediaPlayer.setPosition(self.activeSong.startTime * 1000)
            else:
                trackLength = int(self.mediaPlayer.duration() / 1000)
                countdownTime = self.countdown.getTime()
                maxStartTime = trackLength - countdownTime - MIN_POST_GUESS_TIME
                if maxStartTime <= 0:
                    self.mediaPlayer.setPosition(0)
                else:
                    self.mediaPlayer.setPosition(random.randint(0,maxStartTime) * 1000)

    def setVolume(self, i):
        self.volumeManager.setVolume(i)

    def getCurrentPosition(self):
        if self.mediaPlayer.mediaStatus() != QMediaPlayer.EndOfMedia:
            return int(self.mediaPlayer.position() /1000)

    def getTrackLength(self):
        return int(self.mediaPlayer.duration() / 1000)


#   ~~~COUNTDOWN CLOCK & VIDEO SCREEN STACK~~~
    def setCountdownTime(self, time):
        self.countdown.setTime(time, reset=not self.mediaPlayer.isPlaying())

    def transition(self):
        self.backgroundMovie.stop()
        self.backgroundMovie = QMovie("./images/transitionBackground.gif")
        self.ui.backgroundImageLabel.setMovie(self.backgroundMovie)
        self.backgroundMovie.start()

    def reveal(self):
        self.showVideoPage()
        self.volumeManager.enterQuietMode()

    def showCountdownPage(self):
        self.ui.mainDisplay.setCurrentWidget(self.ui.countdownPage)
        self.backgroundMovie.stop()
        self.backgroundMovie = QMovie("./images/countdownBackground.gif")
        self.ui.backgroundImageLabel.setMovie(self.backgroundMovie)
        self.backgroundMovie.start()
        self.updateDisplayInfo()

    def showVideoPage(self):
        self.ui.mainDisplay.setCurrentWidget(self.ui.videoPage)
        self.backgroundMovie.stop()
        self.backgroundMovie = QMovie("./images/videoBackground.png")
        self.ui.backgroundImageLabel.setMovie(self.backgroundMovie)
        self.backgroundMovie.start()
        self.updateDisplayInfo()


#   ~~~DISPLAY~~~
    def setFullscreen(self, enable: bool):
        if enable:
            self.ui.showFullScreen()
        else:
            self.ui.showNormal()

    def setRound(self, i: int):
        self.round = i
        self.updateDisplayInfo()

    def adjustRound(self, i: int) -> int:
        self.round += i
        if self.round < 0:
            self.round = 0
        self.updateDisplayInfo()
        return self.round

    def updateDisplayInfo(self):
        text = ''
        if self.mediaPlayerMode:
            if self.activeSong:
                if self.activeSong.anime:
                    text = f"{self.activeSong.anime}\n"
                    if self.activeSong.opNum > 0:
                        text += f"OP {self.activeSong.opNum}"
                if self.activeSong.opNum > 0:
                    text += " - "
                if self.activeSong.title:
                    text += f"{self.activeSong.title}"

        elif self.ui.mainDisplay.currentWidget() == self.ui.videoPage:
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
            self.ui.mainDisplay.setCurrentWidget(self.ui.categoriesPage)
            self.buildCategoryList(categories)
        elif self.mediaPlayer.isPlaying():
            self.ui.mainDisplay.setCurrentWidget(self.ui.videoPage)
        else:
            self.ui.mainDisplay.setCurrentWidget(self.ui.countdownPage)

    def buildCategoryList(self, categories: [Category]):
        self.vbox = QVBoxLayout()
        widget = QWidget()
        for cat in categories:
            label = QLabel(cat.name)
            displayColor = {QColor(cat.nameColor).isValid(): cat.nameColor}.get(True, DEFAULT_ROUND_COLOR)
            styleSheet = f"background-color: {DEFAULT_BACKGROUND_COLOR}; color: {displayColor}"
            font = fontlib.getFont(cat.nameFont, DEFAULT_ROUND_FONT_SIZE, DEFAULT_ROUND_FONT)
            label.setStyleSheet(styleSheet)
            label.setFont(font)
            label.setAlignment(Qt.AlignCenter)
            self.vbox.addWidget(label)
        widget.setLayout(self.vbox)
        self.ui.categoryScroll.setWidget(widget)











