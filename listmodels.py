# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex
from db import Song, Category


class CategoryListModel(QAbstractListModel):
    def __init__(self, categories = []):
        super().__init__()
        self.categories = categories

    def rowCount(self, parent=QModelIndex()):
        return len(self.categories)

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return self.categories[index.row()].name
            if role == Qt.ItemDataRole:
                return self.categories[index.row()]
        return None

    def setData(self, index:QModelIndex, cat:Category, role=Qt.EditRole):
        if index.isValid():
            self.categories[index.row()] = cat
            return True
        return False

    def removeData(self, index:QModelIndex):
        self.beginRemoveRows(QModelIndex(), index.row(), index.row())
        del self.categories[index.row()]
        self.endRemoveRows()

    def append(self, category):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.categories.append(category)
        self.endInsertRows()


class SongListModel(QAbstractListModel):
    def __init__(self, parent=None):
        super(SongListModel, self).__init__(parent)
        self.songs = []

    def rowCount(self, parent=QModelIndex()):
        return len(self.songs)

    def data(self, index:QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self.songs[index.row()])
            if role == Qt.ItemDataRole:
                return self.songs[index.row()]
        return None

    def setData(self, index:QModelIndex, song:Song, role=Qt.EditRole):
        if index.isValid():
            self.songs[index.row()] = song
            return True
        return False

    def removeData(self, index:QModelIndex):
        self.beginRemoveRows(QModelIndex(), index.row(), index.row())
        del self.songs[index.row()]
        self.endRemoveRows()

    def loadData(self, data:[Song]):
        self.beginResetModel()
        self.songs.clear()
        self.endResetModel()

        self.beginInsertRows(QModelIndex(), 0, len(data))
        for song in data:
            self.songs.append(song)
        self.endInsertRows()

    def append(self, song):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.songs.append(song)
        self.endInsertRows()



