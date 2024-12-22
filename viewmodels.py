# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Qt, QAbstractItemModel, QAbstractListModel, QModelIndex
from PySide6.QtGui import QPixmap, QIcon
from db import Song, Category


class CategoryListModel(QAbstractListModel):
    def __init__(self, categories = []):
        super().__init__()
        self.categories = categories

    def rowCount(self, parent=QModelIndex()):
        return len(self.categories)

    def setData(self, index:QModelIndex, cat:Category, role=Qt.EditRole):
        if index.isValid():
            self.categories[index.row()] = cat
            return True
        return False

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return self.categories[index.row()].name
            if role == Qt.EditRole:
                return self.categories[index.row()]
        return None

    def removeData(self, index:QModelIndex):
        self.beginRemoveRows(QModelIndex(), index.row(), index.row())
        del self.categories[index.row()]
        self.endRemoveRows()

    def append(self, category):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.categories.append(category)
        self.endInsertRows()


class TreeNode():
    def __init__(self, data, parent=None, group=False):
        self.data = data
        self.parent = parent
        self.children = []
        self.isGroup = group

    def addChild(self, item):
            self.children.append(item)
            #item.parent = self

    def removeChild(self, i):
        self.children.pop(i)

    def child(self, row):
        return self.children[row]

    def childCount(self):
        return len(self.children)

    def columnCount(self):
        return len(self.data)

    def data(self, column=1):
        return self.data

    def parent(self):
        return self.parent

    def row(self):
        if self.parent:
            return self.parent.children.index(self)
        return 0


class SongTreeModel(QAbstractItemModel):
    def __init__(self, songs:[Song]=[], parent=None):
        super().__init__(parent)
        self.loadData(songs)

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def rowCount(self, parent=QModelIndex()):
        if parent.isValid():
            return len(parent.internalPointer().children)
        else:
            return len(self.rootItem.children)

    def columnCount(self, parent=QModelIndex()):
        return 1

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid() is False:
            return None
        item = index.internalPointer()
        if role == Qt.DisplayRole:
            return str(item.data)
        if role == Qt.EditRole:
            return item.data
        if role == Qt.WhatsThisRole:
            if item.isGroup:
                return 'group'
            else:
                return 'song'

    def index(self, row, column=1, parent=QModelIndex()) -> QModelIndex:
        if parent.isValid():
            parentItem = parent.internalPointer()
        else:
            parentItem = self.rootItem

        if row < len(parentItem.children):
            childItem = parentItem.children[row]
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

    def parent(self, index: QModelIndex) -> QModelIndex:
        if index.isValid() is False:
            return QModelIndex()
        childItem = index.internalPointer()
        parentItem = childItem.parent

        if parentItem == None or parentItem == self.rootItem:
            return QModelIndex()
        else:
            return self.createIndex(parentItem.row(), 0, parentItem)

    def loadData(self, songs: [Song]):
        self.beginResetModel()
        self.rootItem = TreeNode("I am Root!")
        for song in songs:
            groupItem = self.getGroupItem(song.group)
            songItem = TreeNode(song, parent=groupItem, group=False)
            groupItem.addChild(songItem)
        self.endResetModel()

    def getGroupItem(self, group: str) -> TreeNode:
        if group is None or group == "":
            return self.rootItem
        items = self.rootItem.children
        for item in items:
            if item.isGroup and item.data == group:
                return item

        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        item = TreeNode(group, parent=self.rootItem, group=True)
        self.rootItem.addChild(item)
        self.endInsertRows()
        return item

    def deleteIfChildless(self, index: QModelIndex):
        if index.isValid() is False:
            return
        item = index.internalPointer()
        if item.childCount() <= 0:
            self.beginRemoveRows(index.parent(), index.row(), index.row())
            self.rootItem.removeChild(index.row())
            self.endRemoveRows()

    def changeGroup(self, songIndex: QModelIndex, group: str):
        #Remove from old group
        item = songIndex.internalPointer()
        self.beginRemoveRows(songIndex.parent(), songIndex.row(), songIndex.row())
        oldGroupItem = self.getGroupItem(item.data.group)
        oldGroupItem.removeChild(songIndex.row())
        self.endRemoveRows()
        self.deleteIfChildless(songIndex.parent())

        #Add to new group
        newGroupItem = self.getGroupItem(group)
        if newGroupItem == self.rootItem:
            newGroupIndex = QModelIndex()
        else:
            newGroupIndex = self.index(self.rootItem.childCount(), 0, QModelIndex())
        self.beginInsertRows(newGroupIndex, self.rowCount(), self.rowCount())
        newGroupItem.addChild(item)
        item.parent = newGroupItem
        self.endInsertRows()

    def setSongData(self, index: QModelIndex, newData: Song):
        if index.isValid() is False:
            return False
        item = index.internalPointer()
        if item.data.group != newData.group:
            self.changeGroup(index, newData.group)
        item.data = newData
        return True    

    def setGroupName(self, index: QModelIndex, name: str):
        if index.isValid() is False:
            return False
        groupItem = index.internalPointer()
        groupItem.data = name
        for songItem in groupItem.children:
            songItem.data.group = name
        return True

    def addSong(self, song: Song, group=False):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        groupItem = self.getGroupItem(song.group)
        songItem = TreeNode(song, parent=groupItem, group=False)
        groupItem.addChild(songItem)
        self.endInsertRows()

    def removeSong(self, index:QModelIndex):
        parentIndex = index.parent()
        if parentIndex.isValid():
            parentItem = parentIndex.internalPointer()
        else:
            parentItem = self.rootItem
        self.beginRemoveRows(parentIndex, index.row(), index.row())
        parentItem.removeChild(index.row())
        self.endRemoveRows()
        if parentItem != self.rootItem:
            self.deleteIfChildless(parentIndex)
