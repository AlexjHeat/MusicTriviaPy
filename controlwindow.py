# This Python file uses the following encoding: utf-8
from PySide6 import QtUiTools
from PySide6.QtCore import Qt, QModelIndex, QTimer
from PySide6.QtWidgets import QMainWindow, QAbstractItemView, QTreeView, QInputDialog, QLineEdit
from displaywindow import DisplayWindow
from playlistmanager import PlaylistManager
from db import Song, Category
from config import MAX_ROUNDS

class ControlWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = QtUiTools.QUiLoader().load("controlwindow.ui")
        self.displayWindow = DisplayWindow(self, self.ui.guessTime.value())
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
        self.playbackTimer = QTimer()
        self.playbackTimer.timeout.connect(self.updatePlaybackTime)

        #connections
        self.ui.categoriesListView.doubleClicked.connect(self.loadCategoryPlaylist)
        self.ui.categoryCreateButton.released.connect(self.createCategory)
        self.ui.categoryEditButton.released.connect(self.editCategory)
        self.ui.categoryRemoveButton.released.connect(self.removeCategory)

        self.ui.songsInTreeView.clicked.connect(self.loadSong)
        self.ui.songsOutTreeView.clicked.connect(self.loadSong)
        self.ui.scanSongs.triggered.connect(self.scanSongFolder)
        self.ui.moveSongInButton.released.connect(self.addSongToCategory)
        self.ui.moveSongOutButton.released.connect(self.removeSongFromCategory)

        self.ui.playButton.released.connect(self.play)
        self.ui.stopButton.released.connect(self.stop)
        self.ui.volumeSlider.sliderMoved.connect(self.updateVolume)
        self.ui.guessTime.valueChanged.connect(self.updateGuessTime)
        self.ui.nextRoundButton.released.connect(self.nextRound)
        self.ui.prevRoundButton.released.connect(self.prevRound)
        self.ui.menuNewGame.triggered.connect(self.newGame)
        self.ui.menuEndGame.triggered.connect(self.endGame)
        self.ui.menuFullscreen.triggered.connect(self.fullscreen)
        self.ui.menuShowCategories.triggered.connect(self.showCategories)

        self.ui.show()

#   ~~~CATEGORIES~~~
    def loadCategoryPlaylist(self, index:QModelIndex):
        #save currently selected song info before loading new category
        if self.activeSongIndex:
            self.updateActiveSong()
        #load new category information to both Control & Display Window
        cat = self.playlistManager.setActiveCategory(index)
        if cat:
            self.ui.categoryDescriptionEdit.setText(cat.description)
            self.ui.currentCategoryLabel.setText(f'Current Category: {cat.name}')
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
            self.loadCategoryPlaylist(index)

    def addSongToCategory(self):
        pass

    def removeSongFromCategory(self):
        pass


#   ~~~SONG LISTVIEWS~~~
    def loadSong(self, index: QModelIndex):
        self.updateActiveSong()
        if index.model() == self.playlistManager.songsInModel:
            self.ui.songsOutTreeView.clearSelection()
        elif index.model() == self.playlistManager.songsOutModel:
            self.ui.songsInTreeView.clearSelection()

        item = self.playlistManager.setActiveSong(index)
        if item:
            if index.data(Qt.WhatsThisRole) == 'group':
                self.ui.songGroupEdit.setText(item)
                self.ui.fileNameLabel.setText('')
            elif index.data(Qt.WhatsThisRole) == 'song':
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
                #Use stack widget, hide accessing item data from this, do it in playlistmanager
                    #pass back boolean of whetherr its song or group, that's all

    def updateActiveSong(self):
        song = Song()
        song.group = self.ui.songGroupEdit.text()
        song.anime = self.ui.songAnimeEdit.text()
        song.opNum = self.ui.songOpSpinBox.value()
        song.title = self.ui.songTitleEdit.text()
        song.artist = self.ui.songArtistEdit.text()
        if self.ui.songStartTimeEdit.text().isnumeric():
            song.startTime = int(self.ui.songStartTimeEdit.text())
        print(song)
        self.playlistManager.updateActiveSong(song)

        #Clear the song data from UI
        self.ui.songGroupEdit.clear()
        self.ui.songAnimeEdit.clear()
        self.ui.songOpSpinBox.setValue(0)
        self.ui.songTitleEdit.clear()
        self.ui.songArtistEdit.clear()
        self.ui.songStartTimeEdit.clear()
        self.activeSongIndex = None

#   ~~~SONGS~~~
    def scanSongFolder(self):
        self.playlistManager.scanSongFolder()
        self.loadCategoryPlaylist(self.ui.categoriesListView.currentIndex())
    '''
    def removeSong(self):
        if self.playlistManager.removeActiveSong(self):
            self.activeSongIndex = None
            self.activeSongView = None

    def addSongToCategory(self):
        if self.activeSongView == self.ui.songsOutListView and self.activeSongView.currentIndex().row() >= 0:
            #Move song from bottom view to top view
            self.playlistManager.addActiveSongToActiveCategory()

            #Update the active song in playlistmanager, and update the song info in the UI
            song = self.playlistManager.setActiveSong(self.activeSongView.currentIndex(), False)
            self.loadSongData(song)

    def removeSongFromCategory(self):
        if self.activeSongView == self.ui.songsInListView and self.activeSongView.currentIndex().row() >= 0:
            self.playlistManager.removeActiveSongFromActiveCategory()
            song = self.playlistManager.setActiveSong(self.activeSongView.currentIndex(), True)
            self.loadSongData(song)
        '''
#   ~~~MEDIA PLAYER~~~
    def play(self):
        song = self.playlistManager.activeSong
        filepath = self.fileManager.getFilePath(song.fileName)
        if filepath:
            self.displayWindow.play(filepath, song)
            self.playbackTimer.start(1000)

    def stop(self):
        self.displayWindow.stop()
        self.playbackTimer.stop()
        self.ui.currentPosLabel.setText('0:00')
        self.ui.trackDurLabel.setText('/ 0:00')

    def updateGuessTime(self, i):
        self.displayWindow.setCountdownTime(i)

    def updateVolume(self, position):
        self.displayWindow.setVolume(position)

    def updatePlaybackTime(self):
        currentPos = self.displayWindow.getCurrentPosition()
        trackLength = self.displayWindow.getTrackLength()
        if currentPos is None:
            self.playbackTimer.stop()
            self.stop()
        self.ui.currentPosLabel.setText(f'{int(currentPos/60)}:{int((currentPos%60)/10)}{(currentPos%60)%10}')
        self.ui.trackDurLabel.setText(f'/ {int(trackLength/60)}:{int((trackLength%60)/10)}{(trackLength%60)%10}')

#   ~~~GAME~~~
    def newGame(self):
        self.round = 1
        self.ui.roundLabel.setText(f'Round {self.round}')
        self.displayWindow.setRound(self.round)
        self.stop()

    def endGame(self):
        self.round = 0
        self.ui.roundLabel.setText('No Active Game')
        self.displayWindow.setRound(self.round)
        self.stop()

    def prevRound(self):
        if self.round > 0:
            self.round -= 1
            if self.round == 0:
                self.ui.roundLabel.setText('No Active Game')
            else:
                self.ui.roundLabel.setText(f'Round {self.round}')
        self.displayWindow.setRound(self.round)
            #self.stop()

    def nextRound(self):
        if self.round < MAX_ROUNDS:
            self.round += 1
            self.ui.roundLabel.setText(f'Round {self.round}')
            self.displayWindow.setRound(self.round)
            #self.stop()

#   ~~~DISPLAY~~~
    def fullscreen(self):
        self.displayWindow.setFullscreen(self.ui.menuFullscreen.isChecked())

    def showCategories(self):
        categories = self.playlistManager.getCategories()
        self.displayWindow.showCategories(self.ui.menuShowCategories.isChecked(), categories)

