# This Python file uses the following encoding: utf-8
from PySide6 import QtUiTools
from PySide6.QtCore import QModelIndex
from PySide6.QtWidgets import QMainWindow, QAbstractItemView
from db import Song
from displaywindow import DisplayWindow
from playlistmanager import PlaylistManager
from filemanager import FileManager

class ControlWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = QtUiTools.QUiLoader().load("controlwindow.ui")
        self.displayWindow = DisplayWindow(self, self.ui.guessTime.value())

        self.playlistManager = PlaylistManager()
        self.fileManager = FileManager(self)
        self.ui.categoriesListView.setModel(self.playlistManager.categoriesModel)
        self.ui.songsInListView.setModel(self.playlistManager.songsInModel)
        self.ui.songsOutListView.setModel(self.playlistManager.songsOutModel)

        self.activeSongView = None
        self.loadedIndex = None

        self.ui.categoriesListView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #set validator for ui.startTimeEdit to only accept int

        #connections
        self.ui.categoriesListView.clicked.connect(self.loadCategory)
        self.ui.categoryCreateButton.released.connect(self.createCategory)
        self.ui.categoryEditButton.released.connect(self.editCategory)
        self.ui.categoryRemoveButton.released.connect(self.removeCategory)
        self.ui.songsInListView.clicked.connect(self.loadSongIn)
        self.ui.songsOutListView.clicked.connect(self.loadSongOut)
        self.ui.addSongsButton.released.connect(self.addSongs)
        self.ui.removeSongButton.released.connect(self.removeSong)
        self.ui.moveSongInButton.released.connect(self.addSongToCategory)
        self.ui.moveSongOutButton.released.connect(self.removeSongFromCategory)
        self.ui.playButton.released.connect(self.play)
        self.ui.stopButton.released.connect(self.stop)
        self.ui.volumeSlider.sliderMoved.connect(self.updateVolume)
        self.ui.guessTime.valueChanged.connect(self.updateGuessTime)

        self.ui.show()


#   ~~~CATEGORIES~~~
    def loadCategory(self, index:QModelIndex):
        if self.loadedIndex:
            self.updateLoadedSong()
        cat = self.playlistManager.setActiveCategory(index)
        if cat:
            self.ui.categoryDescriptionEdit.setText(cat.description)
            self.ui.currentCategoryLabel.setText(f'Current Category: {cat.name}')

    def createCategory(self):
        self.playlistManager.createCategory(self)

    def editCategory(self):
        index = self.ui.categoriesListView.currentIndex()
        if self.playlistManager.editActiveCategory(self):
            self.loadCategory(index)

    def removeCategory(self):
        index = self.ui.categoriesListView.currentIndex()
        if self.playlistManager.removeActiveCategory(self):
            index = self.ui.categoriesListView.currentIndex()
            self.loadCategory(index)

#   ~~~SONG LISTVIEWS~~~
    #Sets the currently selected song in the songIn list view as active, then loads its data
    def loadSongIn(self):
        if self.loadedIndex:
            self.updateLoadedSong()
        self.ui.songsOutListView.clearSelection()
        self.activeSongView = self.ui.songsInListView
        self.loadedIndex = self.activeSongView.currentIndex()
        song = self.playlistManager.setActiveSong(self.loadedIndex, isSongIn=True)
        self.loadSongData(song)

    #Sets the currently selected song in the songOut list view as active, then loads its data
    def loadSongOut(self):
        if self.loadedIndex:
            self.updateLoadedSong()
        self.ui.songsInListView.clearSelection()
        self.activeSongView = self.ui.songsOutListView
        self.loadedIndex = self.activeSongView.currentIndex()
        song = self.playlistManager.setActiveSong(self.loadedIndex, isSongIn=False)
        self.loadSongData(song)

    def loadSongData(self, song):
        if song:
            self.ui.fileNameLabel.setText(song.fileName)
            self.ui.songAnimeEdit.setText(song.anime)
            self.ui.songOpSpinBox.setValue(song.opNum)
            self.ui.songTitleEdit.setText(song.title)
            self.ui.songArtistEdit.setText(song.artist)
            if song.startTime:
                self.ui.songStartTimeEdit.setText(str(song.startTime))
            else:
                self.ui.songStartTimeEdit.clear()

    def updateLoadedSong(self):
        song = Song()
        #Get song data from UI
        song.anime = self.ui.songAnimeEdit.text()
        song.opNum = self.ui.songOpSpinBox.value()
        song.title = self.ui.songTitleEdit.text()
        song.artist = self.ui.songArtistEdit.text()
        if self.ui.songStartTimeEdit.text().isnumeric():
            song.startTime = int(self.ui.songStartTimeEdit.text())
        self.playlistManager.updateActiveSong(song)

        #Clear the song data from UI
        self.ui.songAnimeEdit.clear()
        self.ui.songOpSpinBox.setValue(0)
        self.ui.songTitleEdit.clear()
        self.ui.songArtistEdit.clear()
        self.ui.songStartTimeEdit.clear()
        self.loadedIndex = None

#   ~~~SONGS~~~
    def addSongs(self):
        self.playlistManager.addSongs(self)
        index = self.ui.categoriesListView.currentIndex()
        self.loadCategory(index)

    def removeSong(self):
        if self.playlistManager.removeActiveSong(self):
            self.loadedIndex = None
            self.activeSongView = None

    def addSongToCategory(self):
        if self.activeSongView == self.ui.songsOutListView and self.activeSongView.currentIndex().row() >= 0:
            #Move song from bottom view to top view
            self.playlistManager.addActiveSongToActiveCategory()

            #Need to now update the active song in playlistmanager, and update the song info in the UI
            song = self.playlistManager.setActiveSong(self.activeSongView.currentIndex(), False)
            self.loadSongData(song)

    def removeSongFromCategory(self):
        if self.activeSongView == self.ui.songsInListView and self.activeSongView.currentIndex().row() >= 0:
            self.playlistManager.removeActiveSongFromActiveCategory()
            song = self.playlistManager.setActiveSong(self.activeSongView.currentIndex(), True)
            self.loadSongData(song)

#   ~~~MEDIA PLAYER~~~
    def play(self):
        song = self.playlistManager.activeSong
        filepath = self.fileManager.getFilePath(song.fileName)
        if filepath:
            self.displayWindow.play(filepath, str(song))

    def stop(self):
        self.displayWindow.stop()

    def updateGuessTime(self, i):
        self.displayWindow.setCountdownTime(i)

    def updateVolume(self, position):
        self.displayWindow.setVolume(position)
