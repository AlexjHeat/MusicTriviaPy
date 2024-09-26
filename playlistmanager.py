# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Qt, QModelIndex, QFileInfo
from PySide6.QtWidgets import QDialog, QMessageBox, QFileDialog
import sqlalchemy
from enum import Enum
from db import Session, Song, Category, Directory
from listmodels import CategoryListModel, SongListModel
from categorydialog import CategoryDialog
from config import defaultCategory as default
#from sqlalchemy import select

class SongList(Enum):
    NEITHER = 0
    IN = 1
    OUT = 2


class PlaylistManager:
    def __init__(self):
        session = Session()
        self.categoriesModel = CategoryListModel(session.query(Category).all())
        self.songsInModel = SongListModel()
        self.songsOutModel = SongListModel()

        self.activeCategory = None
        self.activeCategoryIndex = None
        self.activeSong = None
        self.activeSongIndex = None
        self.activeSongModel = None


    def setActiveCategory(self, index:QModelIndex):
        if not index.isValid():
           self.activeCategoryIndex = None
           self.activeCategory = None
           return None
        self.activeCategoryIndex = index
        self.activeCategory = self.categoriesModel.data(index, Qt.ItemDataRole)

        #load songs belonging to the active category to model

        session = Session()
        songs = session.query(Song).filter(Song.categories.any(Category.name == self.activeCategory.name)).all()
        self.songsInModel.loadData(songs)

        #load songs NOT belonging to the active category to model
        songs = session.query(Song).filter(~Song.categories.any(Category.id == self.activeCategory.id)).all()
        self.songsOutModel.loadData(songs)

        #no active song now
        self.activeSong = None
        self.activeSongIndex = None
        self.activeSongModel = None

        return self.activeCategory

    def getActiveCategory(self):
        return self.activeCategory

    def getDefaultCategory(self):
        session = Session()
        return session.query(Category).filter(Category.name == default).one()

    def createCategory(self, parent):
        dialog = CategoryDialog(parent)
        if dialog.exec() == QDialog.Accepted:
            cat = dialog.getCategory()
            session = Session()
            try:
                session.add(cat)
                session.commit()
            except sqlalchemy.exc.IntegrityError:
                QMessageBox.critical(parent, 'Error', "Category name already exists!")
            else:
                session.expunge(cat)
                self.categoriesModel.append(cat)
                return True
        return False

    def editActiveCategory(self, parent):
        #Make sure default category is not being edited
        if self.activeCategory.name == default:
            QMessageBox.warning(parent, 'Warning', "Cannot edit default category!")
            return False

        #Edit active category
        dialog = CategoryDialog(parent)
        dialog.loadInfo(self.activeCategory)
        if dialog.exec() == QDialog.Accepted:
            data = dialog.getCategory()
            session = Session()
            try:
                cat = session.query(Category).filter(Category.name == self.activeCategory.name).one()
                cat.name = data.name
                cat.description = data.description
                session.commit()
            except sqlalchemy.exc.IntegrityError:
                QMessageBox.critical(parent, 'Error', "Category name already exists!")
            else:
                session.expunge(cat)
                self.activeCategory = cat
                if self.categoriesModel.setData(self.activeCategoryIndex, cat):
                    return True
        return False

    def removeActiveCategory(self, parent):
        #Make sure default category is not being edited
        if self.activeCategory.name == default:
            QMessageBox.warning(parent, 'Warning', "Cannot edit default category!")
            return False

        #Make user confirm to prevent accidental loss of data
        warning_msg = QMessageBox.warning(
                        parent,
                        "Warning",
                        f"Do you really want to remove the category: {self.activeCategory.name}",
                        QMessageBox.Ok | QMessageBox.Cancel)
        if warning_msg == QMessageBox.Ok:
            session = Session()
            cat = session.query(Category).filter(Category.id == self.activeCategory.id).one()
            session.delete(cat)
            session.commit()
            self.categoriesModel.removeData(self.activeCategoryIndex)
            return True
        return False

    def setActiveSong(self, index:QModelIndex, isSongIn:bool):
        if not index.isValid():
            return None
        if isSongIn:
            self.activeSongModel = self.songsInModel
        else:
            self.activeSongModel = self.songsOutModel
        self.activeSong = self.activeSongModel.data(index, Qt.ItemDataRole)
        self.activeSongIndex = index
        return self.activeSong

    def updateActiveSong(self, data:Song):
        #Update song in database
        if self.activeSong == None:
            return False
        session = Session()
        song = session.query(Song).filter(Song.id == self.activeSong.id).one()
        song.anime = data.anime
        song.opNum = data.opNum
        song.title = data.title
        song.artist = data.artist
        song.startTime = data.startTime
        session.commit()

        #update song in model
        session.expunge(song)
        self.activeSongModel.setData(self.activeSongIndex, song)
        self.activeSong = song
        return True

    def addSongs(self, parent):
        files, filter = QFileDialog().getOpenFileNames(parent, "Select song files to add", ".", "multimedia(*.wav *.mp3 *.mp4 *.m4a *.flac)")
        #Check if file already exists in playlist, then add default category to each song if a default category is set
        session = Session()
        default_cat = session.query(Category).filter(Category.name == default).one()
        pathChecked = False
        for file in files:
            file = QFileInfo(file)

            #Add song to database, if file name does not already exist
            name = file.fileName()
            if session.query(Song).filter(Song.fileName == name).scalar() == None:
                song = Song(fileName=name)
                session.add(song)
                if default_cat:
                    song.categories.append(default_cat)

            #Add file path to database, if it does not already exist
            if pathChecked == False:
                dir = file.absolutePath() + "\\"
                if session.query(Directory).filter(Directory.dir == dir).scalar() == None:
                    directory = Directory(dir=dir)
                    session.add(directory)
                pathChecked = True
        session.commit()

    def removeActiveSong(self, parent):
        #Make user confirm to prevent accidental loss of data
        warning_msg = QMessageBox.warning(
                        parent,
                        "Warning",
                        f"Do you really want to remove the song: {str(self.activeSong)}",
                        QMessageBox.Ok | QMessageBox.Cancel)
        if warning_msg == QMessageBox.Ok:
            session = Session()
            #remove from database
            song = session.query(Song).filter(Song.id == self.activeSong.id).one()
            session.delete(song)
            session.commit()
            session.expunge(song)

            #remove from model
            self.activeSongModel.removeData(self.activeSongIndex)
            self.activeSong = None
            self.activeSongIndex = None
            self.activeSongModel = None
            return True
        return False

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
