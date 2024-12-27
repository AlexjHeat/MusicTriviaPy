# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QTimer, QObject, Signal
from config import TRANSITION_TIME

class Countdown(QObject):
    countdownComplete = Signal()
    countdownTransition = Signal()

    def __init__(self, countdownLabel, time):
        super().__init__()
        self.totalTime = time
        self.clock = countdownLabel
        self.resetClock()

        self.timer = QTimer()
        self.timer.timeout.connect(self.countdownUpdate)

    def setTime(self, time, reset):
        self.totalTime = time
        if reset:
            self.resetClock()

    def getTime(self):
        return self.totalTime

    def start(self):
       self.resetClock()
       self.timer.start(1000)

    def stop(self):
        self.resetClock()
        self.timer.stop()

    def countdownUpdate(self):
        self.currentTime -= 1
        self.clock.setText(str(self.currentTime))
        if self.currentTime == TRANSITION_TIME:
            self.countdownTransition.emit()
        if self.currentTime <= 0:
            self.stop()
            self.countdownComplete.emit()

    def resetClock(self):
        self.currentTime = self.totalTime
        self.clock.setText(str(self.totalTime))


