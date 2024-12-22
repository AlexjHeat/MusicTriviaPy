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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QSplitter, QStackedWidget, QStatusBar, QToolButton,
    QTreeView, QVBoxLayout, QWidget)

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
        self.scan_songs = QAction(MainWindow)
        self.scan_songs.setObjectName(u"scan_songs")
        self.media_player_mode = QAction(MainWindow)
        self.media_player_mode.setObjectName(u"media_player_mode")
        self.media_player_mode.setCheckable(True)
        self.remove_missing_songs = QAction(MainWindow)
        self.remove_missing_songs.setObjectName(u"remove_missing_songs")
        self.continuous_mode = QAction(MainWindow)
        self.continuous_mode.setObjectName(u"continuous_mode")
        self.continuous_mode.setCheckable(True)
        self.always_show_video = QAction(MainWindow)
        self.always_show_video.setObjectName(u"always_show_video")
        self.always_show_video.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 60, 253, 371))
        self.category_layout = QVBoxLayout(self.layoutWidget)
        self.category_layout.setObjectName(u"category_layout")
        self.category_layout.setContentsMargins(0, 0, 0, 0)
        self.categoriesListView = QListView(self.layoutWidget)
        self.categoriesListView.setObjectName(u"categoriesListView")

        self.category_layout.addWidget(self.categoriesListView)

        self.category_description_label = QLabel(self.layoutWidget)
        self.category_description_label.setObjectName(u"category_description_label")

        self.category_layout.addWidget(self.category_description_label)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.category_layout.addItem(self.verticalSpacer_4)

        self.category_button_layout = QHBoxLayout()
        self.category_button_layout.setObjectName(u"category_button_layout")
        self.categoryCreateButton = QPushButton(self.layoutWidget)
        self.categoryCreateButton.setObjectName(u"categoryCreateButton")

        self.category_button_layout.addWidget(self.categoryCreateButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.category_button_layout.addItem(self.horizontalSpacer)

        self.categoryEditButton = QPushButton(self.layoutWidget)
        self.categoryEditButton.setObjectName(u"categoryEditButton")

        self.category_button_layout.addWidget(self.categoryEditButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.category_button_layout.addItem(self.horizontalSpacer_2)

        self.categoryRemoveButton = QPushButton(self.layoutWidget)
        self.categoryRemoveButton.setObjectName(u"categoryRemoveButton")

        self.category_button_layout.addWidget(self.categoryRemoveButton)


        self.category_layout.addLayout(self.category_button_layout)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(320, 30, 321, 476))
        self.treeview_layout = QVBoxLayout(self.layoutWidget1)
        self.treeview_layout.setObjectName(u"treeview_layout")
        self.treeview_layout.setContentsMargins(0, 0, 0, 0)
        self.current_category_label = QLabel(self.layoutWidget1)
        self.current_category_label.setObjectName(u"current_category_label")

        self.treeview_layout.addWidget(self.current_category_label)

        self.songsInTreeView = QTreeView(self.layoutWidget1)
        self.songsInTreeView.setObjectName(u"songsInTreeView")
        self.songsInTreeView.setDragEnabled(False)
        self.songsInTreeView.setDragDropMode(QAbstractItemView.DragDrop)
        self.songsInTreeView.setUniformRowHeights(False)
        self.songsInTreeView.setSortingEnabled(True)
        self.songsInTreeView.setHeaderHidden(True)

        self.treeview_layout.addWidget(self.songsInTreeView)

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


        self.treeview_layout.addLayout(self.horizontalLayout_2)

        self.songsOutTreeView = QTreeView(self.layoutWidget1)
        self.songsOutTreeView.setObjectName(u"songsOutTreeView")
        self.songsOutTreeView.setDragEnabled(True)
        self.songsOutTreeView.setDragDropMode(QAbstractItemView.DragDrop)
        self.songsOutTreeView.setSortingEnabled(True)
        self.songsOutTreeView.setHeaderHidden(True)

        self.treeview_layout.addWidget(self.songsOutTreeView)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(700, 50, 257, 421))
        self.song_layout = QVBoxLayout(self.layoutWidget2)
        self.song_layout.setObjectName(u"song_layout")
        self.song_layout.setContentsMargins(0, 0, 0, 0)
        self.song_group_info_display = QStackedWidget(self.layoutWidget2)
        self.song_group_info_display.setObjectName(u"song_group_info_display")
        self.songInfoPage = QWidget()
        self.songInfoPage.setObjectName(u"songInfoPage")
        self.verticalLayout_2 = QVBoxLayout(self.songInfoPage)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.fileNameLabel = QLabel(self.songInfoPage)
        self.fileNameLabel.setObjectName(u"fileNameLabel")

        self.verticalLayout.addWidget(self.fileNameLabel)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_6 = QLabel(self.songInfoPage)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_11.addWidget(self.label_6)

        self.songGroupEdit = QLineEdit(self.songInfoPage)
        self.songGroupEdit.setObjectName(u"songGroupEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songGroupEdit.sizePolicy().hasHeightForWidth())
        self.songGroupEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.songGroupEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.songInfoPage)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.songAnimeEdit = QLineEdit(self.songInfoPage)
        self.songAnimeEdit.setObjectName(u"songAnimeEdit")
        sizePolicy.setHeightForWidth(self.songAnimeEdit.sizePolicy().hasHeightForWidth())
        self.songAnimeEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.songAnimeEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.songInfoPage)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_7.addWidget(self.label_5)

        self.songOpSpinBox = QSpinBox(self.songInfoPage)
        self.songOpSpinBox.setObjectName(u"songOpSpinBox")
        sizePolicy.setHeightForWidth(self.songOpSpinBox.sizePolicy().hasHeightForWidth())
        self.songOpSpinBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.songOpSpinBox)

        self.horizontalSpacer_8 = QSpacerItem(95, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.songInfoPage)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.songTitleEdit = QLineEdit(self.songInfoPage)
        self.songTitleEdit.setObjectName(u"songTitleEdit")
        sizePolicy.setHeightForWidth(self.songTitleEdit.sizePolicy().hasHeightForWidth())
        self.songTitleEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.songTitleEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.songInfoPage)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.songArtistEdit = QLineEdit(self.songInfoPage)
        self.songArtistEdit.setObjectName(u"songArtistEdit")
        sizePolicy.setHeightForWidth(self.songArtistEdit.sizePolicy().hasHeightForWidth())
        self.songArtistEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.songArtistEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_4 = QLabel(self.songInfoPage)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_8.addWidget(self.label_4)

        self.songStartTimeEdit = QLineEdit(self.songInfoPage)
        self.songStartTimeEdit.setObjectName(u"songStartTimeEdit")
        sizePolicy.setHeightForWidth(self.songStartTimeEdit.sizePolicy().hasHeightForWidth())
        self.songStartTimeEdit.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.songStartTimeEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.song_group_info_display.addWidget(self.songInfoPage)
        self.groupInfoPage = QWidget()
        self.groupInfoPage.setObjectName(u"groupInfoPage")
        self.verticalLayout_3 = QVBoxLayout(self.groupInfoPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.empty_label = QLabel(self.groupInfoPage)
        self.empty_label.setObjectName(u"empty_label")

        self.verticalLayout_3.addWidget(self.empty_label)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_7 = QLabel(self.groupInfoPage)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_12.addWidget(self.label_7)

        self.group_name_edit = QLineEdit(self.groupInfoPage)
        self.group_name_edit.setObjectName(u"group_name_edit")
        sizePolicy.setHeightForWidth(self.group_name_edit.sizePolicy().hasHeightForWidth())
        self.group_name_edit.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.group_name_edit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.song_group_info_display.addWidget(self.groupInfoPage)

        self.song_layout.addWidget(self.song_group_info_display)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.song_layout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.prevRoundButton = QToolButton(self.layoutWidget2)
        self.prevRoundButton.setObjectName(u"prevRoundButton")
        self.prevRoundButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.prevRoundButton.setArrowType(Qt.LeftArrow)

        self.horizontalLayout.addWidget(self.prevRoundButton)

        self.round_reset_button = QToolButton(self.layoutWidget2)
        self.round_reset_button.setObjectName(u"round_reset_button")

        self.horizontalLayout.addWidget(self.round_reset_button)

        self.nextRoundButton = QToolButton(self.layoutWidget2)
        self.nextRoundButton.setObjectName(u"nextRoundButton")
        self.nextRoundButton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.nextRoundButton.setArrowType(Qt.RightArrow)

        self.horizontalLayout.addWidget(self.nextRoundButton)

        self.roundLabel = QLabel(self.layoutWidget2)
        self.roundLabel.setObjectName(u"roundLabel")

        self.horizontalLayout.addWidget(self.roundLabel)


        self.song_layout.addLayout(self.horizontalLayout)

        self.autoIncrementRounds_checkbox = QCheckBox(self.layoutWidget2)
        self.autoIncrementRounds_checkbox.setObjectName(u"autoIncrementRounds_checkbox")

        self.song_layout.addWidget(self.autoIncrementRounds_checkbox)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.song_layout.addItem(self.verticalSpacer_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.playButton = QPushButton(self.layoutWidget2)
        self.playButton.setObjectName(u"playButton")

        self.horizontalLayout_9.addWidget(self.playButton)

        self.stopButton = QPushButton(self.layoutWidget2)
        self.stopButton.setObjectName(u"stopButton")

        self.horizontalLayout_9.addWidget(self.stopButton)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)

        self.guessTime = QSpinBox(self.layoutWidget2)
        self.guessTime.setObjectName(u"guessTime")
        self.guessTime.setMinimum(5)
        self.guessTime.setValue(30)

        self.horizontalLayout_9.addWidget(self.guessTime)


        self.song_layout.addLayout(self.horizontalLayout_9)

        self.volumeSlider = QSlider(self.layoutWidget2)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setSliderPosition(99)
        self.volumeSlider.setOrientation(Qt.Horizontal)

        self.song_layout.addWidget(self.volumeSlider)

        self.splitter = QSplitter(self.layoutWidget2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.current_position_label = QLabel(self.splitter)
        self.current_position_label.setObjectName(u"current_position_label")
        self.splitter.addWidget(self.current_position_label)

        self.song_layout.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1004, 22))
        self.menuSongFiles = QMenu(self.menubar)
        self.menuSongFiles.setObjectName(u"menuSongFiles")
        self.menuOptions = QMenu(self.menubar)
        self.menuOptions.setObjectName(u"menuOptions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSongFiles.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menuSongFiles.addSeparator()
        self.menuSongFiles.addAction(self.scan_songs)
        self.menuSongFiles.addAction(self.remove_missing_songs)
        self.menuOptions.addAction(self.menuFullscreen)
        self.menuOptions.addAction(self.menuShowCategories)
        self.menuOptions.addAction(self.continuous_mode)
        self.menuOptions.addAction(self.always_show_video)

        self.retranslateUi(MainWindow)

        self.song_group_info_display.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuNewGame.setText(QCoreApplication.translate("MainWindow", u"New Game", None))
        self.menuEndGame.setText(QCoreApplication.translate("MainWindow", u"End Game", None))
        self.menuFullscreen.setText(QCoreApplication.translate("MainWindow", u"Fullscreen", None))
        self.menuShowCategories.setText(QCoreApplication.translate("MainWindow", u"Show Categories", None))
        self.scan_songs.setText(QCoreApplication.translate("MainWindow", u"Scan Song Folder", None))
        self.media_player_mode.setText(QCoreApplication.translate("MainWindow", u"Continuous Mode", None))
        self.remove_missing_songs.setText(QCoreApplication.translate("MainWindow", u"Remove Missing Songs", None))
        self.continuous_mode.setText(QCoreApplication.translate("MainWindow", u"Continuous Mode", None))
        self.always_show_video.setText(QCoreApplication.translate("MainWindow", u"Always Show Video", None))
        self.category_description_label.setText("")
        self.categoryCreateButton.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.categoryEditButton.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.categoryRemoveButton.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.current_category_label.setText(QCoreApplication.translate("MainWindow", u"Current Category:", None))
        self.moveSongInButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.moveSongOutButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.fileNameLabel.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Anime", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"OP", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Artist", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Start Time", None))
        self.songStartTimeEdit.setText("")
        self.empty_label.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Group", None))
        self.prevRoundButton.setText("")
        self.round_reset_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.nextRoundButton.setText("")
        self.roundLabel.setText(QCoreApplication.translate("MainWindow", u"Round 0", None))
        self.autoIncrementRounds_checkbox.setText(QCoreApplication.translate("MainWindow", u"Auto-Increment rounds", None))
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
#if QT_CONFIG(tooltip)
        self.guessTime.setToolTip(QCoreApplication.translate("MainWindow", u"Guess Time", None))
#endif // QT_CONFIG(tooltip)
        self.current_position_label.setText("")
        self.menuSongFiles.setTitle(QCoreApplication.translate("MainWindow", u"Song Files", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

