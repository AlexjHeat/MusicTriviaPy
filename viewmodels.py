# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Qt, QAbstractItemModel, QAbstractListModel, QModelIndex
from PySide6.QtGui import QStandardItemModel, QPixmap, QIcon
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



class TreeNode():
    def __init__(self, data, parent=None, group=False):
        self.data = data
        self.parent = parent
        self.children = []
        self.isGroup = group

    def addChild(self, item):
            self.children.append(item)

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
    def __init__(self, parent=None):
        super().__init__(parent)
        self.rootItem = TreeNode("I am Root!")

    def getGroupNode(self, group: str) -> TreeNode:
        nodes = self.rootItem.children
        for node in nodes:
            if node.isGroup and node.data == group:
                return node
        return None

    def loadData(self, songs: [Song]):
        self.rootItem = TreeNode("I am Root!")
        for song in songs:
            if song.group == None or song.group == '':
                songNode = TreeNode(song, parent=self.rootItem, group=False)
                self.rootItem.addChild(songNode)
            else:
                groupNode = self.getGroupNode(song.group)
                if groupNode is None:
                    groupNode = TreeNode(song, parent=self.rootItem, group=True)
                    self.rootItem.addChild(groupNode)
                songNode = TreeNode(song, parent=groupNode, group=False)
                self.rootItem.addChild(songNode)

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
        if role == Qt.ItemDataRole:
            return item.data
        if role == Qt.DecorationRole and item.isGroup:
            return QIcon(QPixmap('.//marcille1'))

    def index(self, row, column=1, parent=QModelIndex()):
        if parent.isValid():
            parentItem = parent.internalPointer()
        else:
            parentItem = self.rootItem

        if row < len(parentItem.children):

            childItem = parentItem.children[row]
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()

    def parent(self, index: QModelIndex):
        if index.isValid() is False:
            return QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent

        if parentItem == self.rootItem or parentItem == None:
            return QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def append(self, data, group=False):
        self.rootItem.addChild(TreeNode(data, parent=self.rootItem, group=True))


    '''
    def setData(self, index:QModelIndex, song:Song, role=Qt.EditRole):
        if index.isValid():
            self.songs[index.row()] = song
            return True
        return False

    def removeData(self, index:QModelIndex):
        self.beginRemoveRows(QModelIndex(), index.row(), index.row())
        del self.songs[index.row()]
        self.endRemoveRows()
    '''


    '''
    def append(self, song):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.songs.append(song)
        self.endInsertRows()
    '''
