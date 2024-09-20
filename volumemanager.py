# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QTimer

class VolumeManager:
    def __init__(self, audioOutput):
        self.audioOutput = audioOutput
        self.volume = 1

        self.softStartTimer = QTimer()
        self.softStartTimer.timeout.connect(self.softStartTimeout)
        self.softStartSpeed = 10

        self.quietModeTimer = QTimer()
        self.quietModeTimer.timeout.connect(self.quietModeTimeout)
        self.quietMode = False
        self.quietModeSpeed = 25
        self.quietModeFactor = 2.5


    def setVolume(self, i):
        self.volume = i/100
        if self.quietMode:
            self.audioOutput.setVolume(self.volume / self.quietModeFactor)
        else:
            self.audioOutput.setVolume(self.volume)

    def softStart(self):
        self.quietMode = False
        self.audioOutput.setVolume(0/100)
        self.softStartTimer.start(self.softStartSpeed)

    def softStartTimeout(self):
        currentVolume = self.audioOutput.volume()
        if currentVolume < self.volume:
            self.audioOutput.setVolume(currentVolume + .01)
        else:
            self.softStartTimer.stop()

    def enterQuietMode(self):
        self.quietMode = True
        self.quietModeTimer.start(self.quietModeSpeed)

    def quietModeTimeout(self):
        currentVolume = self.audioOutput.volume()
        if currentVolume > (self.volume / self.quietModeFactor):
            self.audioOutput.setVolume(currentVolume - .01)
        else:
            self.quietModeTimer.stop()
