# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QTimer
from config import SOFT_START_SPEED, QUIET_MODE_SPEED, QUIET_MODE_FACTOR

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
        self.audioOutput.setVolume(0)
        self.softStartTimer.start(10)

    def softStartTimeout(self):
        currentVolume = self.audioOutput.volume()
        if currentVolume < self.volume:
            self.audioOutput.setVolume(currentVolume + (self.volume*10)/SOFT_START_SPEED)
        else:
            self.softStartTimer.stop()

    def enterQuietMode(self):
        self.quietMode = True
        self.quietModeTimer.start(10)

    def quietModeTimeout(self):
        currentVolume = self.audioOutput.volume()
        if currentVolume > (self.volume / QUIET_MODE_FACTOR):
            self.audioOutput.setVolume(currentVolume - ((self.volume/QUIET_MODE_FACTOR)*10)/QUIET_MODE_SPEED)
        else:
            self.quietModeTimer.stop()
