# This Python file uses the following encoding: utf-8
from PySide6 import QtUiTools
from PySide6.QtCore import Qt, QModelIndex, QTimer
from PySide6.QtWidgets import QMainWindow, QAbstractItemView
from PySide6.QtGui import QIcon, QPixmap
from mediaplayer import MediaPlayer
from displaywindow import DisplayWindow
from playlistmanager import PlaylistManager
from functools import partial
from db import Song, getCategorySongs
from config import RESET_ICON_PATH, DEFAULT_COUNTDOWN_TIME

class ControlWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = QtUiTools.QUiLoader().load("controlwindow.ui")
        self.mediaPlayer = MediaPlayer()
        self.mediaPlayer.playbackUpdate.connect(self.updatePlaybackTime)
        self.displayWindow = DisplayWindow(self, self.mediaPlayer)
        self.playlistManager = PlaylistManager()

        self.activeSongView = None
        self.activeSongIndex = None
        self.ui.categoriesListView.setModel(self.playlistManager.categoriesModel)
        self.ui.songsInTreeView.setModel(self.playlistManager.songsInModel)
        self.ui.songsOutTreeView.setModel(self.playlistManager.songsOutModel)
        self.ui.categoriesListView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.categoriesListView.setCurrentIndex(self.ui.categoriesListView.model().index(0,0))
        self.loadCategoryPlaylist(self.ui.categoriesListView.currentIndex())

        self.round = 0
        self.ui.round_reset_button.setIcon(QIcon(QPixmap(RESET_ICON_PATH)))
        self.ui.guessTime.setValue(DEFAULT_COUNTDOWN_TIME)

        #connections
        self.ui.categoriesListView.doubleClicked.connect(self.loadCategoryPlaylist)
        self.ui.categoryCreateButton.released.connect(self.createCategory)
        self.ui.categoryEditButton.released.connect(self.editCategory)
        self.ui.categoryRemoveButton.released.connect(self.removeCategory)

        self.ui.songsInTreeView.clicked.connect(self.loadSong)
        self.ui.songsOutTreeView.clicked.connect(self.loadSong)
        self.ui.scan_songs.triggered.connect(self.scanSongFolder)
        self.ui.remove_missing_songs.triggered.connect(self.removeMissingSongs)
        self.ui.moveSongInButton.released.connect(self.addSongToCategory)
        self.ui.moveSongOutButton.released.connect(self.removeSongFromCategory)

        self.ui.round_reset_button.released.connect(self.resetRound)
        self.ui.nextRoundButton.released.connect(partial(self.adjustRound, 1))
        self.ui.prevRoundButton.released.connect(partial(self.adjustRound, -1))

        self.ui.playButton.released.connect(self.play)
        self.ui.stopButton.released.connect(self.stop)
        self.ui.volumeSlider.sliderMoved.connect(self.updateVolume)
        self.ui.guessTime.valueChanged.connect(self.updateGuessTime)

        self.ui.menuFullscreen.triggered.connect(self.fullscreen)
        self.ui.menuShowCategories.triggered.connect(self.showCategories)
        self.ui.always_show_video.triggered.connect(self.alwaysShowVideo)
        self.ui.continuous_mode.triggered.connect(self.continuousMode)

        self.ui.show()

#   ~~~CATEGORIES~~~
    def loadCategoryPlaylist(self, index:QModelIndex):
        if self.activeSongIndex:
            self.updateActiveSong()
        cat = self.playlistManager.setActiveCategory(index)
        if cat:
            self.ui.category_description_label.setText(cat.description)
            self.ui.current_category_label.setText(f'Current Category: {cat.name}')
            self.displayWindow.loadCategory(cat)

    def createCategory(self):
        self.playlistManager.createCategory(self)

    def editCategory(self):
        if self.playlistManager.editActiveCategory(self):
            self.loadCategoryPlaylist(self.ui.categoriesListView.currentIndex())

    def removeCategory(self):
        if self.playlistManager.removeActiveCategory(self):
            self.ui.categoriesListView.setCurrentIndex(self.ui.categoriesListView.model().index(0,0))
            self.loadCategoryPlaylist(self.ui.categoriesListView.currentIndex())

#   ~~~SONG LISTVIEWS~~~
    def loadSong(self, index: QModelIndex):
        self.updateActiveSong()
        if index.model() == self.playlistManager.songsInModel:
            self.ui.songsOutTreeView.clearSelection()
        elif index.model() == self.playlistManager.songsOutModel:
            self.ui.songsInTreeView.clearSelection()

        song = self.playlistManager.setActiveIndex(index)
        if index.data(Qt.WhatsThisRole) == 'group':
            self.loadGroupToUI(song)
        elif index.data(Qt.WhatsThisRole) == 'song':
            self.loadSongToUI(song)

    def updateActiveSong(self):
        if self.ui.song_group_info_display.currentWidget() == self.ui.groupInfoPage:
            self.playlistManager.updateActiveGroup(self.ui.group_name_edit.text())
        elif self.ui.song_group_info_display.currentWidget() == self.ui.songInfoPage:
            song = self.getSongFromUI()
            self.playlistManager.updateActiveSong(song)
        self.clearSongAndGroupInfoUI()

    def addSongToCategory(self):
        currentIndex = self.ui.songsOutTreeView.currentIndex()
        if currentIndex.isValid():
            self.playlistManager.addActiveSongToActiveCategory()
            index = self.ui.songsOutTreeView.currentIndex()
            self.playlistManager.setActiveIndex(index)

    def removeSongFromCategory(self):
        index = self.ui.songsInTreeView.currentIndex()
        if index.isValid():
            self.playlistManager.removeActiveSongFromActiveCategory()
            index = self.ui.songsInTreeView.currentIndex()
            self.playlistManager.setActiveIndex(index)

    def scanSongFolder(self):
        self.playlistManager.scanSongFolder()
        self.loadCategoryPlaylist(self.ui.categoriesListView.currentIndex())

    def removeMissingSongs(self):
        pass

#   ~~~MEDIA PLAYER~~~
    def continuousMode(self):
        checked = self.ui.continuous_mode.isChecked()
        self.mediaPlayer.setContinuousMode(checked)
        if checked:
            songs = self.playlistManager.getActiveCategorySongs()
            self.mediaPlayer.setPlaylist(songs)

    def play(self):
        song = self.playlistManager.getActiveSong()
        if song:
            self.mediaPlayer.play(song)

    def stop(self):
        if self.mediaPlayer.isPlaying() and self.ui.autoIncrementRounds_checkbox.isChecked():
            self.adjustRound(1)
        self.mediaPlayer.stop()
        self.ui.current_position_label.setText('0:00 / 0:00')

    def updateGuessTime(self, i):
        self.displayWindow.setCountdownTime(i)

    def updateVolume(self, position):
        self.mediaPlayer.setVolume(position)

    def updatePlaybackTime(self, currentPos: int, trackLen: int):
            currentPositionStr = f'{int(currentPos/60)}:{int((currentPos%60)/10)}{(currentPos%60)%10}'
            trackDurationStr = f'{int(trackLen/60)}:{int((trackLen%60)/10)}{(trackLen%60)%10}'
            self.ui.current_position_label.setText(f'{currentPositionStr} / {trackDurationStr}')


#   ~~~ROUNDS~~~
    def resetRound(self):
        self.ui.roundLabel.setText('')
        self.displayWindow.setRound(0)

    def adjustRound(self, n: int):
        round = self.displayWindow.adjustRound(n)
        self.ui.roundLabel.setText(f'Round {round}')

#   ~~~UI~~~
    def loadSongToUI(self, item: Song):
        self.ui.song_group_info_display.setCurrentWidget(self.ui.songInfoPage)
        self.ui.fileNameLabel.setText(item.fileName)
        self.ui.songGroupEdit.setText(item.group)
        self.ui.songAnimeEdit.setText(item.anime)
        self.ui.songOpSpinBox.setValue(item.opNum)
        self.ui.songTitleEdit.setText(item.title)
        self.ui.songArtistEdit.setText(item.artist)
        if item.startTime:
            self.ui.songStartTimeEdit.setText(str(item.startTime))
        else:
            self.ui.songStartTimeEdit.clear()

    def loadGroupToUI(self, item: str):
        self.ui.song_group_info_display.setCurrentWidget(self.ui.groupInfoPage)
        self.ui.group_name_edit.setText(item)

    def getSongFromUI(self):
        song = Song()
        song.group = self.ui.songGroupEdit.text()
        song.anime = self.ui.songAnimeEdit.text()
        song.opNum = self.ui.songOpSpinBox.value()
        song.title = self.ui.songTitleEdit.text()
        song.artist = self.ui.songArtistEdit.text()
        if self.ui.songStartTimeEdit.text().isnumeric():
            song.startTime = int(self.ui.songStartTimeEdit.text())
        return song

    def clearSongAndGroupInfoUI(self):
        self.ui.group_name_edit.setText('')
        self.ui.songGroupEdit.setText('')
        self.ui.songAnimeEdit.setText('')
        self.ui.songOpSpinBox.setValue(0)
        self.ui.songTitleEdit.setText('')
        self.ui.songArtistEdit.setText('')
        self.ui.songStartTimeEdit.setText('')

#   ~~~DISPLAY~~~
    def fullscreen(self):
        self.displayWindow.setFullscreen(self.ui.menuFullscreen.isChecked())

    def showCategories(self):
        categories = self.playlistManager.getCategories()
        self.displayWindow.showCategories(self.ui.menuShowCategories.isChecked(), categories)

    def alwaysShowVideo(self):
        self.displayWindow.setAlwaysShowVideo(self.ui.always_show_video.isChecked())





