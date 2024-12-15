# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QTimer, QObject, Signal

class Countdown(QObject):
    countdownComplete = Signal()
    countdownWarning = Signal()     #Set to n seconds

    def __init__(self, countdownLCD, time):
        super().__init__()
        self.totalTime = time
        self.display = countdownLCD
        self.resetDisplay()

        self.timer = QTimer()
        self.timer.timeout.connect(self.countdownUpdate)

    def setTime(self, time, reset):
        self.totalTime = time
        if reset:
            self.resetDisplay()

    def getTime(self):
        return self.totalTime

    def start(self):
       self.resetDisplay()
       self.timer.start(1000)

    def stop(self):
        self.resetDisplay()
        self.timer.stop()

    def countdownUpdate(self):
        self.currentTime -= 1
        self.setDisplay(self.currentTime)
        if self.currentTime == 2:
            self.countdownWarning.emit()
        if self.currentTime <= 0:
            self.stop()
            self.countdownComplete.emit()

    def resetDisplay(self):
        self.currentTime = self.totalTime
        self.setDisplay(self.totalTime)


    def setDisplay(self, i):
        self.display.setDigitCount(len(str(i)))
        self.display.display(i)


