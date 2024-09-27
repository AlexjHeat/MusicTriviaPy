# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'displaywindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLCDNumber, QLabel,
    QLayout, QMainWindow, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet(u"background-color: rgb(54, 82, 172);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.mainDisplay = QStackedWidget(self.centralwidget)
        self.mainDisplay.setObjectName(u"mainDisplay")
        self.video = QWidget()
        self.video.setObjectName(u"video")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video.sizePolicy().hasHeightForWidth())
        self.video.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.video)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.videoLayout = QVBoxLayout()
        self.videoLayout.setSpacing(0)
        self.videoLayout.setObjectName(u"videoLayout")
        self.videoLayout.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_2.addLayout(self.videoLayout)

        self.mainDisplay.addWidget(self.video)
        self.countdown = QWidget()
        self.countdown.setObjectName(u"countdown")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.countdown.sizePolicy().hasHeightForWidth())
        self.countdown.setSizePolicy(sizePolicy1)
        self.countdown.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.countdown)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.countdownLCD = QLCDNumber(self.countdown)
        self.countdownLCD.setObjectName(u"countdownLCD")
        sizePolicy.setHeightForWidth(self.countdownLCD.sizePolicy().hasHeightForWidth())
        self.countdownLCD.setSizePolicy(sizePolicy)
        self.countdownLCD.setMinimumSize(QSize(200, 200))
        self.countdownLCD.setStyleSheet(u"background-color: rgb(133, 162, 253);")
        self.countdownLCD.setDigitCount(2)
        self.countdownLCD.setProperty("intValue", 30)

        self.verticalLayout_3.addWidget(self.countdownLCD)

        self.mainDisplay.addWidget(self.countdown)

        self.gridLayout.addWidget(self.mainDisplay, 1, 1, 1, 1)

        self.bannerRight = QLabel(self.centralwidget)
        self.bannerRight.setObjectName(u"bannerRight")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bannerRight.sizePolicy().hasHeightForWidth())
        self.bannerRight.setSizePolicy(sizePolicy2)
        self.bannerRight.setScaledContents(True)
        self.bannerRight.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.bannerRight, 1, 2, 1, 1)

        self.RoundInfo = QVBoxLayout()
        self.RoundInfo.setSpacing(6)
        self.RoundInfo.setObjectName(u"RoundInfo")
        self.RoundInfo.setContentsMargins(-1, 6, -1, 6)
        self.roundLabel = QLabel(self.centralwidget)
        self.roundLabel.setObjectName(u"roundLabel")
        sizePolicy.setHeightForWidth(self.roundLabel.sizePolicy().hasHeightForWidth())
        self.roundLabel.setSizePolicy(sizePolicy)
        self.roundLabel.setAlignment(Qt.AlignCenter)

        self.RoundInfo.addWidget(self.roundLabel)

        self.songLabel = QLabel(self.centralwidget)
        self.songLabel.setObjectName(u"songLabel")
        sizePolicy.setHeightForWidth(self.songLabel.sizePolicy().hasHeightForWidth())
        self.songLabel.setSizePolicy(sizePolicy)
        self.songLabel.setAlignment(Qt.AlignCenter)

        self.RoundInfo.addWidget(self.songLabel)


        self.gridLayout.addLayout(self.RoundInfo, 0, 0, 1, 3)

        self.bannerLeft = QLabel(self.centralwidget)
        self.bannerLeft.setObjectName(u"bannerLeft")
        sizePolicy2.setHeightForWidth(self.bannerLeft.sizePolicy().hasHeightForWidth())
        self.bannerLeft.setSizePolicy(sizePolicy2)
        self.bannerLeft.setScaledContents(True)
        self.bannerLeft.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.bannerLeft, 1, 0, 1, 1)

        self.bannerCenter = QLabel(self.centralwidget)
        self.bannerCenter.setObjectName(u"bannerCenter")
        sizePolicy.setHeightForWidth(self.bannerCenter.sizePolicy().hasHeightForWidth())
        self.bannerCenter.setSizePolicy(sizePolicy)
        self.bannerCenter.setMinimumSize(QSize(0, 0))
        self.bannerCenter.setTextFormat(Qt.AutoText)
        self.bannerCenter.setScaledContents(True)
        self.bannerCenter.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.bannerCenter.setOpenExternalLinks(False)

        self.gridLayout.addWidget(self.bannerCenter, 2, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainDisplay.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bannerRight.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.roundLabel.setText("")
        self.songLabel.setText("")
        self.bannerLeft.setText(QCoreApplication.translate("MainWindow", u"test", None))
        self.bannerCenter.setText(QCoreApplication.translate("MainWindow", u"test", None))
    # retranslateUi

