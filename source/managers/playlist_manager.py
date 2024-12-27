# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Qt, QModelIndex
from PySide6.QtWidgets import QDialog, QMessageBox
import sqlalchemy
from enum import Enum
from source.models import CategoryListModel, SongTreeModel
from source.dialogs.category_dialog import CategoryDialog
from source.dialogs.record_dialog import RecordDialog
from source.db import Song, Category
import source.db_access as db
from config import DEFAULT_CATEGORY, SONG_PATH
import os

class SongList(Enum):
    NEITHER = 0
    IN = 1
    OUT = 2


class PlaylistManager:
    def __init__(self):

        self.categoriesModel = CategoryListModel(db.getCategories())
        self.songsInModel = SongTreeModel()
        self.songsOutModel = SongTreeModel()

        self.activeCategoryIndex = QModelIndex()
        self.activeSongIndex = QModelIndex()


#   ~~~CATEGORIES~~~
    def setActiveCategory(self, index: QModelIndex):
        self.activeCategoryIndex = index
        self.activeSongIndex = None
        cat = self.getActiveCategory()
        if cat:
            self.songsInModel.loadData(db.getSongsInCategory(cat.id))
            self.songsOutModel.loadData(db.getSongsOutOfCategory(cat.id))
            return cat

    def getActiveCategory(self):
        if self.activeCategoryIndex and self.activeCategoryIndex.isValid():
            return self.activeCategoryIndex.data(role=Qt.EditRole)
        return None

    def getActiveCategorySongs(self) -> [Song]:
        cat = self.getActiveCategory()
        if cat:
            return db.getSongsInCategory(cat.id)

    def getCategories(self):
        return db.getCategories()

    def createCategory(self, parent):
        dialog = CategoryDialog(parent)
        if dialog.exec() == QDialog.Accepted:
            cat = dialog.getCategory()
            try:
                db.addCategory(cat)
            except sqlalchemy.exc.IntegrityError:
                QMessageBox.critical(parent, 'Error', f"Category name '{cat.name}' already exists!")
            else:
                self.categoriesModel.append(cat)
                return True
        return False


    def editActiveCategory(self, parent):
        category = self.getActiveCategory()
        if not category:
            return False
        if category.name == DEFAULT_CATEGORY:
            QMessageBox.warning(parent, 'Warning', "Cannot edit default category!")
            return False

        dialog = CategoryDialog(parent)
        dialog.loadInfo(category)
        if dialog.exec() == QDialog.Accepted:
            data = dialog.getCategory()
            try:
                category = db.updateCategory(category.id, data)

            except sqlalchemy.exc.IntegrityError:
                QMessageBox.critical(parent, 'Error', "Category name already exists!")
            else:
                if self.categoriesModel.setData(self.activeCategoryIndex, category):
                    return True
        return False

    def removeActiveCategory(self, parent):
        category = self.getActiveCategory()
        if not category:
            return False
        if category.name == DEFAULT_CATEGORY:
            QMessageBox.warning(parent, 'Warning', "Cannot remove default category!")
            return False

        #Make user confirm to prevent accidental loss of data
        warning_msg = QMessageBox.warning(
                        parent,
                        "Warning",
                        f"Do you really want to remove the category: {self.activeCategoryIndex.data()}",
                        QMessageBox.Ok | QMessageBox.Cancel)
        if warning_msg == QMessageBox.Ok:
            db.deleteCategory(category.id)
            self.categoriesModel.removeData(self.activeCategoryIndex)
            return True
        return False

#   ~~~SONGS~~~
    def scanSongFolder(self):
        song_files = [f for f in os.listdir(SONG_PATH) if os.path.isfile(f'{SONG_PATH}/{f}')]
        db.verifySongFiles(song_files)
        db.addSongsFromFile(song_files)

    def getActiveSong(self):
        if self.activeSongIndex and self.activeSongIndex.isValid() and self.activeSongIndex.data(Qt.WhatsThisRole) == 'song':
            return self.activeSongIndex.data(Qt.EditRole)
        return None

    def getActiveGroup(self):
        if self.activeSongIndex and self.activeSongIndex.isValid() and self.activeSongIndex.data(Qt.WhatsThisRole) == 'group':
            return self.activeSongIndex.data(Qt.EditRole)
        return None

    def setActiveIndex(self, index:QModelIndex):
        if not index.isValid():
            return None
        self.activeSongIndex = index
        return index.data(Qt.EditRole)

    def updateActiveSong(self, data: Song):
        song = self.getActiveSong()
        if song:
            song = db.updateSong(song.id, data)
            self.activeSongIndex.model().setSongData(self.activeSongIndex, song)

    def updateActiveGroup(self, data: str):
        group = self.getActiveGroup()
        if group:
            db.updateGroup(group, data)
            self.activeSongIndex.model().setGroupName(self.activeSongIndex, data)

    def addActiveSongToActiveCategory(self):
        category = self.getActiveCategory()
        song = self.getActiveSong()
        if song is None or category is None:
            return

        db.addSongToCategory(category.id, song.id)
        self.songsOutModel.removeSong(self.activeSongIndex)
        self.songsInModel.addSong(song)
        self.activeSongIndex = None
        return True

    def removeActiveSongFromActiveCategory(self):
        category = self.getActiveCategory()
        song = self.getActiveSong()
        if song is None or category is None:
            return

        db.removeSongFromCategory(category.id, song.id)
        self.songsInModel.removeSong(self.activeSongIndex)
        self.songsOutModel.addSong(song)
        self.activeSongIndex = None
        return True

#   ~~~RECORDS~~~
    def addRecord(self, parent):
        song = self.getActiveSong()
        if song is None:
            return
        dialog = RecordDialog(song, parent)
        if dialog.exec() == QDialog.Accepted:
            record = dialog.getRecord()
            try:
                db.addRecord(record)
            except sqlalchemy.exc.IntegrityError:
                QMessageBox.critical(parent, 'Error', "Something's Fucked!")
            else:
                return True
