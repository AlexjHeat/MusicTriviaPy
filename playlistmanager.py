# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtWidgets import QDialog, QMessageBox
import sqlalchemy
from enum import Enum
from db import Session, Song, Category, updateSong, updateCategory, updateGroup
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
        categories = session.query(Category).filter(Category.name != DEFAULT_CATEGORY).all()
        return categories

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
        category = self.activeCategoryIndex.data(Qt.EditRole)
        if category.name == DEFAULT_CATEGORY:
            QMessageBox.warning(parent, 'Warning', "Cannot edit default category!")
            return False

        #Edit active category
        dialog = CategoryDialog(parent)
        dialog.loadInfo(self.activeCategoryIndex.data(Qt.EditRole))
        if dialog.exec() == QDialog.Accepted:
            data = dialog.getCategory()
            try:
                category = updateCategory(category.id, data)

            except sqlalchemy.exc.IntegrityError:
                QMessageBox.critical(parent, 'Error', "Category name already exists!")
            else:
                if self.categoriesModel.setData(self.activeCategoryIndex, category):
                    return True
        return False

    def removeActiveCategory(self, parent):
        #Make sure default category is not being edited
        if self.activeCategoryIndex.data() == DEFAULT_CATEGORY:
            QMessageBox.warning(parent, 'Warning', "Cannot remove default category!")
            return False

        #Make user confirm to prevent accidental loss of data
        warning_msg = QMessageBox.warning(
                        parent,
                        "Warning",
                        f"Do you really want to remove the category: {self.activeCategoryIndex.data()}",
                        QMessageBox.Ok | QMessageBox.Cancel)
        if warning_msg == QMessageBox.Ok:
            session = Session()
            cat = session.query(Category).filter(Category.id == self.activeCategoryIndex.data(Qt.EditRole).id).one()
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

    def getActiveSong(self):
        if not self.activeSongIndex.isValid() and self.activeSongIndex.data(Qt.WhatsThisRole) != 'song':
            return None
        return self.activeSongIndex.data(Qt.EditRole)

    def setActiveIndex(self, index:QModelIndex):
        if not index.isValid():
            return None
        self.activeSongIndex = index
        return index.data(Qt.EditRole)

    def updateActiveSong(self, data: Song):
        if self.activeSongIndex is None or self.activeSongIndex.data(Qt.WhatsThisRole) != 'song':
            return
        activeSong = self.activeSongIndex.data(Qt.EditRole)
        if activeSong is None:
            return
        song = updateSong(activeSong.id, data)
        self.activeSongIndex.model().setSongData(self.activeSongIndex, song)

    def updateActiveGroup(self, data: str):
        if self.activeSongIndex is None or self.activeSongIndex.data(Qt.WhatsThisRole) != 'group':
            return
        activeGroup = self.activeSongIndex.data(Qt.EditRole)
        if activeGroup is None:
            return
        updateGroup(activeGroup, data)
        self.activeSongIndex.model().setGroupName(self.activeSongIndex, data)

    def addActiveSongToActiveCategory(self):
        if self.activeSongIndex.data(Qt.WhatsThisRole) == 'group':
            return False
        session = Session()
        cat = session.query(Category).filter(Category.id == self.activeCategoryIndex.data(Qt.EditRole).id).one()
        song = session.query(Song).filter(Song.id == self.activeSongIndex.data(Qt.EditRole).id).one()
        cat.songs.append(song)
        session.commit()
        session.close()

        self.songsOutModel.removeSong(self.activeSongIndex)
        self.songsInModel.addSong(song)
        self.activeSongIndex = None
        return True

    def removeActiveSongFromActiveCategory(self):
        if self.activeSongIndex.data(Qt.WhatsThisRole) == 'group':
            return False
        session = Session()
        cat = session.query(Category).filter(Category.id == self.activeCategoryIndex.data(Qt.EditRole).id).one()
        song = session.query(Song).filter(Song.id == self.activeSongIndex.data(Qt.EditRole).id).one()
        cat.songs.remove(song)
        session.commit()
        session.close()

        self.songsInModel.removeSong(self.activeSongIndex)
        self.songsOutModel.addSong(song)
        self.activeSongIndex = None
        return True
