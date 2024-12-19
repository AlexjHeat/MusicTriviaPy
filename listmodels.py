# This Python file uses the following encoding: utf-8
from PySide6.QtCore import Qt, QAbstractItemModel, QAbstractListModel, QModelIndex
from db import Song, Category, Group


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



class TreeNode:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.children = []

    def addChild(self, child):
        self.children.append(child)
        child.parent = self


class SongTreeModel(QAbstractItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.root = TreeNode("I am Root!")

    def getGroupNode(self, id: int) -> TreeNode:
        nodes = self.root.children
        for node in nodes:
            if isinstance(node.data, Group) and node.data.id == id:
                return node
        return None

    def loadData(self, songs: [Song]):
        self.root = TreeNode("I am Root!")
        for song in songs:
            if song.groupId is None:
                self.root.addChild(TreeNode(song, parent=self.root))
            else:
                groupNode = self.getGroupNode(song.groupId)
                if groupNode is None:
                    groupNode = TreeNode(song, parent=self.root)
                    self.root.addChild(groupNode)
                self.root.addChild(TreeNode(song, parent=groupNode))

    def rowCount(self, parent=QModelIndex()):
        if not parent.isValid():
            return len(self.root.children)
        else:
            return len(parent.internalPointer().children)

    def columnCount(self, parent=QModelIndex()):
            return 1

    def data(self, index: QModelIndex, role=Qt.DisplayRole):
        if index.isValid():
            return None

        item = index.internalPointer()
        if role == Qt.DisplayRole:
            return str(item.data)
        if role == Qt.ItemDataRole:
            return item.data

    def index(self, row, column=0, parent=QModelIndex()):
        if not parent.isValid():
            parentItem = self.root
        else:
            parentItem = parent.internalPointer()

        if row < len(parentItem.children):
            childItem = parentItem.children[row]
            return self.createIndex(row, column, childItem)
        else:
            return QModelIndex()


    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent

        if parentItem == self.root:
            return QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

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
