# This Python file uses the following encoding: utf-8
from PySide6 import QtUiTools
from PySide6.QtCore import QUrl, QTimer
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget

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

        self.countdownTime = countdownTime
        self.ui.countdownLCD.display(self.countdownTime)
        self.countdownTimer = QTimer()
        self.countdownTimer.timeout.connect(self.countdownUpdate)

        self.showCountdown()

    def play(self, filepath):
        self.mediaPlayer.setSource(QUrl.fromLocalFile(filepath))
        self.mediaPlayer.play()

        self.showCountdown()
        self.countdown = self.countdownTime
        self.ui.countdownLCD.display(self.countdown)
        self.countdownTimer.start(1000)

    def stop(self):
        self.mediaPlayer.stop()

        self.countdown = self.countdownTime
        self.ui.countdownLCD.display(self.countdown)
        self.showCountdown()
        self.countdownTimer.stop()

    def setCountdownTime(self, time):
        self.countdownTime = time
        self.ui.countdownLCD.display(self.countdownTime)

    def countdownUpdate(self):
        self.countdown -= 1
        self.ui.countdownLCD.display(self.countdown)
        if self.countdown <= 0:
            self.countdownTimer.stop()
            self.showVideo()


    def showVideo(self):
        self.videoWidget.show()
        self.ui.countdownLCD.hide()

    def showCountdown(self):
        self.ui.countdownLCD.show()
        self.videoWidget.hide()
