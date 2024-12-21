# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Qt, QModelIndex, QFileInfo
from PySide6.QtWidgets import QDialog, QMessageBox, QFileDialog
import sqlalchemy
from enum import Enum
from db import Session, Song, Category, updateSong, updateCategory
from viewmodels import CategoryListModel, SongTreeModel
from categorydialog import CategoryDialog
from config import DEFAULT_CATEGORY, SONG_PATH
import os

class SongList(Enum):
    NEITHER = 0
    IN = 1
    OUT = 2


class PlaylistManager:
    def __init__(self):
        session = Session()
        self.categoriesModel = CategoryListModel(session.query(Category).all())
        self.songsInModel = SongTreeModel()
        self.songsOutModel = SongTreeModel()

        self.activeCategoryIndex = QModelIndex()
        self.activeSongIndex = QModelIndex()


#   ~~~CATEGORIES~~~
    def setActiveCategory(self, index: QModelIndex):
        if index.isValid() is False:
           self.activeCategoryIndex = QModelIndex()
           return None
        self.activeCategoryIndex = index
        self.activeSongIndex = None

        cat = index.data(role=Qt.EditRole)

        session = Session()
        songs = session.query(Song).filter(Song.categories.any(Category.name == cat.name), Song.missingFile == False).all()
        self.songsInModel.loadData(songs)
        songs = session.query(Song).filter(~Song.categories.any(Category.name == cat.name), Song.missingFile == False).all()
        self.songsOutModel.loadData(songs)
        return cat

    def getActiveCategory(self):
        return self.activeCategoryIndex.data()

    def getCategories(self):
        session = Session()
        return session.query(Category).filter(Category.name != DEFAULT_CATEGORY).all()

    def createCategory(self, parent):
        dialog = CategoryDialog(parent)
        if dialog.exec() == QDialog.Accepted:
            cat = dialog.getCategory()
            session = Session()
            try:
                session.add(cat)
                session.commit()
            except sqlalchemy.exc.IntegrityError:
                QMessageBox.critical(parent, 'Error', f"Category name '{cat.name}' already exists!")
            else:
                session.expunge(cat)
                self.categoriesModel.append(cat)
                return True
        return False


    def editActiveCategory(self, parent):
        #Make sure default category is not being edited
        if self.activeCategory.name == DEFAULT_CATEGORY:
            QMessageBox.warning(parent, 'Warning', "Cannot edit default category!")
            return False

        #Edit active category
        dialog = CategoryDialog(parent)
        category = self.activeCategoryIndex.data(Qt.EditRole)
        dialog.loadInfo(self.activeCategoryIndex.data())
        if dialog.exec() == QDialog.Accepted:
            data = dialog.getCategory()
            try:
                updateCategory(category.id, data)
            except sqlalchemy.exc.IntegrityError:
                QMessageBox.critical(parent, 'Error', "Category name already exists!")
            else:
                if self.categoriesModel.setData(self.activeCategoryIndex, cat):
                    return True
        return False

    def removeActiveCategory(self, parent):
        #Make sure default category is not being edited
        if self.activeCategoryIndex.data().name == DEFAULT_CATEGORY:
            QMessageBox.warning(parent, 'Warning', "Cannot remove default category!")
            return False

        #Make user confirm to prevent accidental loss of data
        warning_msg = QMessageBox.warning(
                        parent,
                        "Warning",
                        f"Do you really want to remove the category: {self.activeCategory.name}",
                        QMessageBox.Ok | QMessageBox.Cancel)
        if warning_msg == QMessageBox.Ok:
            session = Session()
            cat = session.query(Category).filter(Category.id == self.activeCategoryIndex.data().id).one()
            session.delete(cat)
            session.commit()
            self.categoriesModel.removeData(self.activeCategoryIndex)
            return True
        return False

#   ~~~SONGS~~~
    def scanSongFolder(self):
        song_files = [f for f in os.listdir(SONG_PATH) if os.path.isfile(f'{SONG_PATH}/{f}')]
        session = Session()
        song_db = session.query(Song).all()
        default_cat = session.query(Category).filter(Category.name == DEFAULT_CATEGORY).one()

        for song in song_db:
            song.missingFile = True

        for file in song_files:
            found = False
            for song in song_db:
                if file == song.fileName:
                    song.missingFile = False
                    found = True
                    break
            if not found:
                song = Song(fileName=file)
                if default_cat:
                    song.categories.append(default_cat)

                session.add(song)
        session.commit()
        session.close()

    def setActiveSong(self, index:QModelIndex):
        if not index.isValid():
            return None
        self.activeSongIndex = index
        return index.data(Qt.EditRole)


    def updateActiveSong(self, data:Song):
        if self.activeSongIndex is None or self.activeSongIndex.isValid() is False:
            return

        if self.activeSongIndex.data(Qt.WhatsThisRole) == 'group':
            #Call model to update group node's name for all its children
            #Update all children in database
            return

        elif self.activeSongIndex.data(Qt.WhatsThisRole) == 'song':
            activeSong = self.activeSongIndex.data(Qt.EditRole)
            if activeSong is None:
                return
            self.activeSongIndex.model().setSongData(self.activeSongIndex, data)    #updates model
            updateSong(activeSong.id, data)                                         #updates database
            return

    '''
    #This action resets the active song
    def addActiveSongToActiveCategory(self):
        #Get active category and song from database, add song to category
        session = Session()
        cat = session.query(Category).filter(Category.id == self.activeCategory.id).one()
        song = session.query(Song).filter(Song.id == self.activeSong.id).one()
        cat.songs.append(song)
        session.commit()

        #Update change in model
        session.expunge(cat)
        session.expunge(song)
        #self.setActiveCategory(self.activeCategoryIndex)
        #remove song from songsOutModel
        #append song to songsInModel
        self.songsOutModel.removeData(self.activeSongIndex)
        self.songsInModel.append(song)

        #update activeSong info now that it has moved to the songsIn model
        self.activeSong = song
        self.activeSongModel = self.songsInModel
        self.activeSongIndex = self.activeSongModel.index(self.activeSongModel.rowCount()-1)

    def removeActiveSongFromActiveCategory(self):
        #Get active category and song from database, add song to category
        session = Session()
        cat = session.query(Category).filter(Category.id == self.activeCategory.id).one()
        song = session.query(Song).filter(Song.id == self.activeSong.id).one()
        cat.songs.remove(song)
        session.commit()

        #Update change in model
        session.expunge(cat)
        session.expunge(song)
        self.songsInModel.removeData(self.activeSongIndex)
        self.songsOutModel.append(song)

        #update activeSong info now that it has moved to the songsOut model
        self.activeSong = song
        self.activeSongModel = self.songsOutModel
        self.activeSongIndex = self.activeSongModel.index(self.activeSongModel.rowCount()-1)
    '''

