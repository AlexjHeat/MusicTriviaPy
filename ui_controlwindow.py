# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'controlwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListView, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QSplitter, QStatusBar,
    QTextEdit, QToolButton, QTreeView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1004, 600)
        self.menuNewGame = QAction(MainWindow)
        self.menuNewGame.setObjectName(u"menuNewGame")
        self.menuEndGame = QAction(MainWindow)
        self.menuEndGame.setObjectName(u"menuEndGame")
        self.menuFullscreen = QAction(MainWindow)
        self.menuFullscreen.setObjectName(u"menuFullscreen")
        self.menuFullscreen.setCheckable(True)
        self.menuShowCategories = QAction(MainWindow)
        self.menuShowCategories.setObjectName(u"menuShowCategories")
        self.menuShowCategories.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 60, 253, 448))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.categoriesListView = QListView(self.layoutWidget)
        self.categoriesListView.setObjectName(u"categoriesListView")

        self.verticalLayout.addWidget(self.categoriesListView)

        self.categoryDescriptionEdit = QTextEdit(self.layoutWidget)
        self.categoryDescriptionEdit.setObjectName(u"categoryDescriptionEdit")
        self.categoryDescriptionEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.categoryDescriptionEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.categoryCreateButton = QPushButton(self.layoutWidget)
        self.categoryCreateButton.setObjectName(u"categoryCreateButton")

        self.horizontalLayout.addWidget(self.categoryCreateButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.categoryEditButton = QPushButton(self.layoutWidget)
        self.categoryEditButton.setObjectName(u"categoryEditButton")

        self.horizontalLayout.addWidget(self.categoryEditButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.categoryRemoveButton = QPushButton(self.layoutWidget)
        self.categoryRemoveButton.setObjectName(u"categoryRemoveButton")

        self.horizontalLayout.addWidget(self.categoryRemoveButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(320, 30, 321, 476))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.currentCategoryLabel = QLabel(self.layoutWidget1)
        self.currentCategoryLabel.setObjectName(u"currentCategoryLabel")

        self.verticalLayout_2.addWidget(self.currentCategoryLabel)

        self.songsOutTreeView = QTreeView(self.layoutWidget1)
        self.songsOutTreeView.setObjectName(u"songsOutTreeView")

        self.verticalLayout_2.addWidget(self.songsOutTreeView)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.moveSongInButton = QToolButton(self.layoutWidget1)
        self.moveSongInButton.setObjectName(u"moveSongInButton")
        self.moveSongInButton.setAutoRaise(False)
        self.moveSongInButton.setArrowType(Qt.UpArrow)

        self.horizontalLayout_2.addWidget(self.moveSongInButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.moveSongOutButton = QToolButton(self.layoutWidget1)
        self.moveSongOutButton.setObjectName(u"moveSongOutButton")
        self.moveSongOutButton.setArrowType(Qt.DownArrow)

        self.horizontalLayout_2.addWidget(self.moveSongOutButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.songsInTreeView = QTreeView(self.layoutWidget1)
        self.songsInTreeView.setObjectName(u"songsInTreeView")

        self.verticalLayout_2.addWidget(self.songsInTreeView)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.createGroupBTN = QPushButton(self.layoutWidget1)
        self.createGroupBTN.setObjectName(u"createGroupBTN")

        self.horizontalLayout_10.addWidget(self.createGroupBTN)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_11)

        self.removeGroupBTN = QPushButton(self.layoutWidget1)
        self.removeGroupBTN.setObjectName(u"removeGroupBTN")

        self.horizontalLayout_10.addWidget(self.removeGroupBTN)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_12)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.updateSongsBTN = QPushButton(self.layoutWidget1)
        self.updateSongsBTN.setObjectName(u"updateSongsBTN")

        self.horizontalLayout_3.addWidget(self.updateSongsBTN)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.removeSongButton = QPushButton(self.layoutWidget1)
        self.removeSongButton.setObjectName(u"removeSongButton")

        self.horizontalLayout_3.addWidget(self.removeSongButton)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(700, 50, 257, 481))
        self.verticalLayout_3 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.fileNameLabel = QLabel(self.layoutWidget2)
        self.fileNameLabel.setObjectName(u"fileNameLabel")

        self.verticalLayout_3.addWidget(self.fileNameLabel)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.songAnimeEdit = QLineEdit(self.layoutWidget2)
        self.songAnimeEdit.setObjectName(u"songAnimeEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songAnimeEdit.sizePolicy().hasHeightForWidth())
        self.songAnimeEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.songAnimeEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.songOpSpinBox = QSpinBox(self.layoutWidget2)
        self.songOpSpinBox.setObjectName(u"songOpSpinBox")
        sizePolicy.setHeightForWidth(self.songOpSpinBox.sizePolicy().hasHeightForWidth())
        self.songOpSpinBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.songOpSpinBox)

        self.horizontalSpacer_8 = QSpacerItem(95, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.layoutWidget2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.songTitleEdit = QLineEdit(self.layoutWidget2)
        self.songTitleEdit.setObjectName(u"songTitleEdit")
        sizePolicy.setHeightForWidth(self.songTitleEdit.sizePolicy().hasHeightForWidth())
        self.songTitleEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.songTitleEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.songArtistEdit = QLineEdit(self.layoutWidget2)
        self.songArtistEdit.setObjectName(u"songArtistEdit")
        sizePolicy.setHeightForWidth(self.songArtistEdit.sizePolicy().hasHeightForWidth())
        self.songArtistEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.songArtistEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.layoutWidget2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.songStartTimeEdit = QLineEdit(self.layoutWidget2)
        self.songStartTimeEdit.setObjectName(u"songStartTimeEdit")
        sizePolicy.setHeightForWidth(self.songStartTimeEdit.sizePolicy().hasHeightForWidth())
        self.songStartTimeEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.songStartTimeEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.roundLabel = QLabel(self.layoutWidget2)
        self.roundLabel.setObjectName(u"roundLabel")

        self.verticalLayout_3.addWidget(self.roundLabel)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.guessTime = QSpinBox(self.layoutWidget2)
        self.guessTime.setObjectName(u"guessTime")
        self.guessTime.setMinimum(5)
        self.guessTime.setValue(30)

        self.horizontalLayout_9.addWidget(self.guessTime)

        self.playButton = QPushButton(self.layoutWidget2)
        self.playButton.setObjectName(u"playButton")

        self.horizontalLayout_9.addWidget(self.playButton)

        self.stopButton = QPushButton(self.layoutWidget2)
        self.stopButton.setObjectName(u"stopButton")

        self.horizontalLayout_9.addWidget(self.stopButton)

        self.prevRoundButton = QToolButton(self.layoutWidget2)
        self.prevRoundButton.setObjectName(u"prevRoundButton")
        self.prevRoundButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.prevRoundButton.setArrowType(Qt.LeftArrow)

        self.horizontalLayout_9.addWidget(self.prevRoundButton)

        self.nextRoundButton = QToolButton(self.layoutWidget2)
        self.nextRoundButton.setObjectName(u"nextRoundButton")
        self.nextRoundButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.nextRoundButton.setArrowType(Qt.RightArrow)

        self.horizontalLayout_9.addWidget(self.nextRoundButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.volumeSlider = QSlider(self.layoutWidget2)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setSliderPosition(99)
        self.volumeSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_3.addWidget(self.volumeSlider)

        self.splitter = QSplitter(self.layoutWidget2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.currentPosLabel = QLabel(self.splitter)
        self.currentPosLabel.setObjectName(u"currentPosLabel")
        self.currentPosLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.splitter.addWidget(self.currentPosLabel)
        self.trackDurLabel = QLabel(self.splitter)
        self.trackDurLabel.setObjectName(u"trackDurLabel")
        self.splitter.addWidget(self.trackDurLabel)

        self.verticalLayout_3.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1004, 22))
        self.menuCategory = QMenu(self.menubar)
        self.menuCategory.setObjectName(u"menuCategory")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCategory.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuCategory.addSeparator()
        self.menuCategory.addAction(self.menuNewGame)
        self.menuCategory.addAction(self.menuEndGame)
        self.menuView.addAction(self.menuFullscreen)
        self.menuView.addAction(self.menuShowCategories)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuNewGame.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.menuEndGame.setText(QCoreApplication.translate("MainWindow", u"End Game", None))
        self.menuFullscreen.setText(QCoreApplication.translate("MainWindow", u"Fullscreen", None))
        self.menuShowCategories.setText(QCoreApplication.translate("MainWindow", u"Show Categories", None))
        self.categoryCreateButton.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.categoryEditButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.categoryRemoveButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.currentCategoryLabel.setText(QCoreApplication.translate("MainWindow", u"Current Category:", None))
        self.moveSongInButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.moveSongOutButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.createGroupBTN.setText(QCoreApplication.translate("MainWindow", u"Create Group", None))
        self.removeGroupBTN.setText(QCoreApplication.translate("MainWindow", u"Remove Group", None))
#if QT_CONFIG(tooltip)
        self.updateSongsBTN.setToolTip(QCoreApplication.translate("MainWindow", u"Updates lists to the current contents of the song folder", None))
#endif // QT_CONFIG(tooltip)
        self.updateSongsBTN.setText(QCoreApplication.translate("MainWindow", u"Update Songs", None))
        self.removeSongButton.setText(QCoreApplication.translate("MainWindow", u"Remove Song", None))
        self.fileNameLabel.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Anime", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"OP", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Artist", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Start Time", None))
        self.songStartTimeEdit.setText("")
        self.roundLabel.setText(QCoreApplication.translate("MainWindow", u"No Active Game", None))
#if QT_CONFIG(tooltip)
        self.guessTime.setToolTip(QCoreApplication.translate("MainWindow", u"Guess Time", None))
#endif // QT_CONFIG(tooltip)
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.prevRoundButton.setText("")
        self.nextRoundButton.setText("")
        self.currentPosLabel.setText("")
        self.trackDurLabel.setText("")
        self.menuCategory.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi

