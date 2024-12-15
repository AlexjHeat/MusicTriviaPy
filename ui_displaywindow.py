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
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLabel, QLayout,
    QMainWindow, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-image: url(:/images/default/background.png)")
        self.mainDisplay = QStackedWidget(self.centralwidget)
        self.mainDisplay.setObjectName(u"mainDisplay")
        self.mainDisplay.setGeometry(QRect(372, 240, 1181, 621))
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
        self.countdownLCD.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.countdownLCD.sizePolicy().hasHeightForWidth())
        self.countdownLCD.setSizePolicy(sizePolicy2)
        self.countdownLCD.setMinimumSize(QSize(200, 200))
        self.countdownLCD.setStyleSheet(u"background-color: rgb(133, 162, 253);")
        self.countdownLCD.setDigitCount(2)
        self.countdownLCD.setProperty("intValue", 30)

        self.verticalLayout_3.addWidget(self.countdownLCD)

        self.mainDisplay.addWidget(self.countdown)
        self.backgroundImageLabel = QLabel(self.centralwidget)
        self.backgroundImageLabel.setObjectName(u"backgroundImageLabel")
        self.backgroundImageLabel.setGeometry(QRect(0, 0, 1921, 1081))
        self.backgroundImageLabel.setStyleSheet(u"")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(620, 0, 661, 241))
        self.RoundInfo = QVBoxLayout(self.widget)
        self.RoundInfo.setSpacing(6)
        self.RoundInfo.setObjectName(u"RoundInfo")
        self.RoundInfo.setContentsMargins(0, 6, 0, 6)
        self.roundLabel = QLabel(self.widget)
        self.roundLabel.setObjectName(u"roundLabel")
        sizePolicy.setHeightForWidth(self.roundLabel.sizePolicy().hasHeightForWidth())
        self.roundLabel.setSizePolicy(sizePolicy)
        self.roundLabel.setStyleSheet(u"font: 700 48pt \"Segoe UI\";\n"
"color: #C0BBFE;")
        self.roundLabel.setAlignment(Qt.AlignCenter)

        self.RoundInfo.addWidget(self.roundLabel)

        self.songLabel = QLabel(self.widget)
        self.songLabel.setObjectName(u"songLabel")
        sizePolicy.setHeightForWidth(self.songLabel.sizePolicy().hasHeightForWidth())
        self.songLabel.setSizePolicy(sizePolicy)
        self.songLabel.setStyleSheet(u"font: 700 36pt \"Segoe UI\";\n"
"color: #C0BBFE;")
        self.songLabel.setAlignment(Qt.AlignCenter)

        self.RoundInfo.addWidget(self.songLabel)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainDisplay.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.backgroundImageLabel.setText("")
        self.roundLabel.setText("")
        self.songLabel.setText("")
    # retranslateUi

