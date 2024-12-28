# This Python file uses the following encoding: utf-8
from PySide6 import QtUiTools
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QMovie, QColor
from source.managers.media_manager import MediaManager
from source.managers.countdown_manager import Countdown
from source.db import Category
import source.libraries.font_lib as fontlib
from config import DEFAULT_CATEGORY, DEFAULT_ROUND_FONT, DEFAULT_ROUND_FONT_SIZE, DEFAULT_ROUND_COLOR, DEFAULT_CLOCK_FONT, DEFAULT_CLOCK_FONT_SIZE, DEFAULT_CLOCK_COLOR, DEFAULT_BACKGROUND_COLOR, DEFAULT_COUNTDOWN_TIME


class DisplayWindow:
    def __init__(self, parent, mediaPlayer: MediaManager):
        super().__init__(),
        self.parent = parent
        self.ui = QtUiTools.QUiLoader().load("source\\displaywindow.ui")
        self.displayInfoLabel = QLabel(self.ui.backgroundImageLabel)
        self.displayInfoLabel.setGeometry(610, 10, 710, 220)
        self.displayInfoLabel.setAlignment(Qt.AlignCenter)
        self.displayInfoLabel.setWordWrap(True)
        self.displayInfoLabel.show()
        self.ui.show()

        self.activeSong = None
        self.activeCategory = None
        self.round = 0
        self.alwaysShowVideo = False
        self.backgroundMovie = QMovie()

        self.mediaPlayer = mediaPlayer
        self.mediaPlayer.songBegan.connect(self.songBegan)
        self.mediaPlayer.songEnded.connect(self.songEnded)
        self.ui.videoLayout.addWidget(mediaPlayer.videoOutput)

        self.countdown = Countdown(self.ui.countdownLabel, DEFAULT_COUNTDOWN_TIME)
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
    def songBegan(self, song):
        if song is None:
            return
        self.activeSong = song
        self.updateDisplayInfo()
        if self.alwaysShowVideo is False:
            self.showCountdownPage()
            self.countdown.start()

    def songEnded(self):
        self.activeSong = None
        self.updateDisplayInfo()
        self.countdown.stop()
        if self.alwaysShowVideo is False:
            self.showCountdownPage()


#   ~~~COUNTDOWN CLOCK & VIDEO SCREEN STACK~~~
    def setCountdownTime(self, n):
        self.countdown.setTime(n, reset=not self.mediaPlayer.isPlaying())

    def transition(self):
        self.backgroundMovie.stop()
        self.backgroundMovie = QMovie("./images/transitionBackground.gif")
        self.ui.backgroundImageLabel.setMovie(self.backgroundMovie)
        self.backgroundMovie.start()

    def reveal(self):
        self.showVideoPage()
        self.mediaPlayer.enterQuietMode()

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


#   ~~~ROUNDS~~~
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

#   ~~~DISPLAY~~~
    def updateDisplayInfo(self):
        text = ''
        if self.alwaysShowVideo:
            if self.activeSong:
                if self.activeSong.anime:
                    text = f"{self.activeSong.anime}\n\n"
                if self.activeSong.title:
                    text += f'"{self.activeSong.title}"'
                    if self.activeSong.artist:
                        text += f" by {self.activeSong.artist}"

        elif self.ui.mainDisplay.currentWidget() == self.ui.videoPage:
            if self.activeSong and self.activeSong.anime:
                text = f'\n{self.activeSong.anime}'
        else:
            if self.activeCategory and self.activeCategory.name != DEFAULT_CATEGORY:
                text += self.activeCategory.name
            text += '\n'
            if self.round > 0:
                text += f'Round {str(self.round)}'
        self.displayInfoLabel.setText(text)

    def setAlwaysShowVideo(self, enable):
        self.alwaysShowVideo = enable
        if enable:
            self.showVideoPage()


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











