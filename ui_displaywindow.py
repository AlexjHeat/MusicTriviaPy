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
from PySide6.QtWidgets import (QApplication, QLCDNumber, QLabel, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1141, 685)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(110, 40, 931, 501))
        self.videoLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.videoLayout.setObjectName(u"videoLayout")
        self.videoLayout.setContentsMargins(0, 0, 0, 0)
        self.countdownLCD = QLCDNumber(self.centralwidget)
        self.countdownLCD.setObjectName(u"countdownLCD")
        self.countdownLCD.setGeometry(QRect(110, 40, 931, 501))
        self.countdownLCD.setDigitCount(2)
        self.countdownLCD.setProperty("intValue", 30)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(370, 0, 411, 40))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.roundLabel = QLabel(self.widget)
        self.roundLabel.setObjectName(u"roundLabel")
        self.roundLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.roundLabel)

        self.songLabel = QLabel(self.widget)
        self.songLabel.setObjectName(u"songLabel")
        self.songLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.songLabel)

        MainWindow.setCentralWidget(self.centralwidget)
        self.countdownLCD.raise_()
        self.verticalLayoutWidget.raise_()
        self.songLabel.raise_()
        self.roundLabel.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1141, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.roundLabel.setText("")
        self.songLabel.setText("")
    # retranslateUi

