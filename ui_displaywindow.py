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
from PySide6.QtWidgets import (QApplication, QLabel, QLayout, QMainWindow,
    QScrollArea, QSizePolicy, QStackedWidget, QVBoxLayout,
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
        self.videoPage = QWidget()
        self.videoPage.setObjectName(u"videoPage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoPage.sizePolicy().hasHeightForWidth())
        self.videoPage.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.videoPage)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.videoLayout = QVBoxLayout()
        self.videoLayout.setSpacing(0)
        self.videoLayout.setObjectName(u"videoLayout")
        self.videoLayout.setSizeConstraint(QLayout.SetMaximumSize)

        self.verticalLayout_2.addLayout(self.videoLayout)

        self.mainDisplay.addWidget(self.videoPage)
        self.countdownPage = QWidget()
        self.countdownPage.setObjectName(u"countdownPage")
        sizePolicy.setHeightForWidth(self.countdownPage.sizePolicy().hasHeightForWidth())
        self.countdownPage.setSizePolicy(sizePolicy)
        self.countdownPage.setMinimumSize(QSize(0, 0))
        self.verticalLayout_3 = QVBoxLayout(self.countdownPage)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.countdownLabel = QLabel(self.countdownPage)
        self.countdownLabel.setObjectName(u"countdownLabel")
        self.countdownLabel.setStyleSheet(u"")
        self.countdownLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.countdownLabel)

        self.mainDisplay.addWidget(self.countdownPage)
        self.categoriesPage = QWidget()
        self.categoriesPage.setObjectName(u"categoriesPage")
        sizePolicy.setHeightForWidth(self.categoriesPage.sizePolicy().hasHeightForWidth())
        self.categoriesPage.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.categoriesPage)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.categoryScroll = QScrollArea(self.categoriesPage)
        self.categoryScroll.setObjectName(u"categoryScroll")
        self.categoryScroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 98, 28))
        self.categoryScroll.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.categoryScroll)

        self.mainDisplay.addWidget(self.categoriesPage)
        self.backgroundImageLabel = QLabel(self.centralwidget)
        self.backgroundImageLabel.setObjectName(u"backgroundImageLabel")
        self.backgroundImageLabel.setGeometry(QRect(0, 0, 1921, 1081))
        self.backgroundImageLabel.setStyleSheet(u"")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainDisplay.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.countdownLabel.setText("")
        self.backgroundImageLabel.setText("")
    # retranslateUi

