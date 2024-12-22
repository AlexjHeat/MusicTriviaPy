# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QObject, QUrl, QTimer, Signal
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from volumemanager import VolumeManager
from db import Song
from config import SONG_PATH, MIN_POST_GUESS_TIME, DEFAULT_COUNTDOWN_TIME
import time, random

class MediaPlayer(QObject):
    playbackUpdate = Signal(int, int)
    songBegan = Signal(Song)
    songEnded = Signal()

    def __init__(self):
        super().__init__()

        self.mediaPlayer = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.videoOutput = QVideoWidget()

        self.mediaPlayer.setAudioOutput(self.audioOutput)
        self.mediaPlayer.setVideoOutput(self.videoOutput)
        self.volumeManager = VolumeManager(self.audioOutput)
        self.mediaPlayer.mediaStatusChanged.connect(self.mediaStatusChanged)

        self.activeSong = None
        self.countdownTime = DEFAULT_COUNTDOWN_TIME
        self.playlist = [Song]
        self.continuousMode = False

        self.playbackTimer = QTimer()
        self.playbackTimer.timeout.connect(self.playbackTimeout)

    def play(self, song: Song):
        self.activeSong = song
        if song is None:
            return
        if self.mediaPlayer.isPlaying():
            self.mediaPlayer.stop()
            time.sleep(0.1)
        self.mediaPlayer.setSource(QUrl.fromLocalFile(f"{SONG_PATH}//{song.fileName}"))
        self.mediaPlayer.play()
        self.songBegan.emit(song)
        self.playbackTimer.start(1000)
        self.volumeManager.softStart()

    def stop(self):
        self.mediaPlayer.stop()
        self.playbackTimer.stop()
        self.songEnded.emit()
        #self.mediaPlayer.setSource(QUrl(''))   #Crashes program now, not sure why...

    def isPlaying(self) -> bool:
        return self.mediaPlayer.isPlaying()

    def setCountdownTime(self, n: int):
        self.countdownTime = n

    def mediaStatusChanged(self, status: QMediaPlayer.MediaStatus):
        if status == QMediaPlayer.LoadedMedia:
            self.updateStartPosition(status)
        if status == QMediaPlayer.EndOfMedia:
            self.stop()
            if self.continuousMode:
                self.play(random.choice(self.playlist))

    def setContinuousMode(self, enable: bool):
        self.continuousMode = enable

    def setPlaylist(self, songs: [Song]):
        self.playlist = songs
        if self.continuousMode and not self.isPlaying():
            self.play(random.choice(self.playlist))

#   ~~~POSITION~~~
    def updateStartPosition(self, status: QMediaPlayer.MediaStatus):
        if self.continuousMode:
            pass
        elif self.activeSong.startTime and self.activeSong.startTime > 0:
            self.mediaPlayer.setPosition(self.activeSong.startTime * 1000)
        else:
            trackLength = int(self.mediaPlayer.duration() / 1000)
            maxStartTime = trackLength - self.countdownTime - MIN_POST_GUESS_TIME
            if maxStartTime <= 0:
                self.mediaPlayer.setPosition(0)
            else:
                self.mediaPlayer.setPosition(random.randint(0, maxStartTime) * 1000)

    def playbackTimeout(self):
        if self.mediaPlayer.mediaStatus() != QMediaPlayer.EndOfMedia:
            currentPos = int(self.mediaPlayer.position() /1000)
        else:
            currentPos = 0
        trackLen = int(self.mediaPlayer.duration() / 1000)
        self.playbackUpdate.emit(currentPos, trackLen)

#   ~~~VOLUME~~~
    def setVolume(self, n: int):
        self.volumeManager.setVolume(n)

    def enterQuietMode(self):
        if not self.continuousMode:
            self.volumeManager.enterQuietMode()
