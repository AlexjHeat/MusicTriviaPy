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
    def __init__(self, data, group=False):
        self.data = data
        self.parent = None
        self.children = []
        self.isGroup = group

    def addChild(self, item):
            self.children.append(item)
            item.parent = self

    def removeChild(self, i):
        del self.children[i]

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

    def loadData(self, songs: [Song]):
        self.beginResetModel()
        self.rootItem = TreeNode("I am Root!")
        for song in songs:
            if song.group == None or song.group == '':
                songNode = TreeNode(song, group=False)
                self.rootItem.addChild(songNode)
            else:
                groupNode = self.getGroupNode(song.group)
                if groupNode is None:
                    groupNode = TreeNode(song.group, group=True)
                    self.rootItem.addChild(groupNode)
                songNode = TreeNode(song, group=False)
                groupNode.addChild(songNode)
        self.endResetModel()

    def updateGroup(self):
        pass

    def getGroupNode(self, group: str) -> TreeNode:
        nodes = self.rootItem.children
        for node in nodes:
            if node.isGroup and node.data == group:
                return node
        return None



    def setSongData(self, index: QModelIndex, newData: Song):
        if index.isValid() is False:
            return False
        item = index.internalPointer()
        if item.data.group != newData.group:
            #self.changeGroup(index, newData.group)
            pass
        else:
            item.data = newData
        return True

    def changeGroup(self, index: QModelIndex, row: int, newGroup: str):
        item = index.internalPointer()
        oldGroupNode = self.getGroupNode(item.data.group)
        oldGroupNode.removeChild(index.row())
        if oldGroupNode != self.rootItem and oldGroupNode.childCount() == 0:
            self.rootItem.removeChild(index.parent().row())

        newGroupNode = self.getGroupNode(newGroup)
        if newGroupNode is None:
            newGroupNode = TreeNode(newGroup, group=True)
            self.rootItem.addChild(newGroupNode)
        newGroupNode.addChild(item)

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid() is False:
            return None
        item = index.internalPointer()
        if role == Qt.DisplayRole:
            return str(item.data)
        if role == Qt.EditRole:
            return item.data
        if role == Qt.DecorationRole and item.isGroup:
            return QIcon(QPixmap('.//marcille1'))
        if role == Qt.WhatsThisRole:
            if item.isGroup:
                return 'group'
            else:
                return 'song'

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
